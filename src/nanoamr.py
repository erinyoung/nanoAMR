import tempfile
import logging
import os
import sys

from src.utils.parse_args import parse_args
from src.utils.amrfinder import run_amrfinder
from src.utils.seqkit import run_seqkit
from src.utils.blast import run_blast
from src.utils.reformat_fasta_header import reformat_fasta_header
from src.utils.check_versions import check_versions
from src.utils.blast_to_df import blast_to_df
from src.utils.group_differences import group_differences
from src.utils.graph_differences import graph_differences
from src.utils.num_reads import num_reads
from src.utils.graph_mutation_curve import graph_mutation_curve

def main():
    """Main function to run the script."""
    args = parse_args()

    logging.basicConfig(format="%(asctime)s - %(message)s",
        datefmt = "%y-%b-%d %H:%M:%S",
        level=args.loglevel.upper())

    logging.info(f"Reference fasta :\t{args.fasta}")
    logging.info(f"Nanopore reads :\t{args.reads}")
    check_versions()

    logging.info(f"Num threads :\t{str(args.threads)}")
    if args.gene:
        logging.info(f"Regex str :\t{args.gene}")
    logging.info(f"Result dir :\t{args.outdir}")

    if os.path.exists(args.outdir):
        logging.fatal("FATAL: outdir directory already exists")
        sys.exit(1)
    else:
        os.mkdir(args.outdir)

    with tempfile.TemporaryDirectory(dir = args.outdir) as temp_dir:
        pre_amr_fasta = run_amrfinder(args, temp_dir)
        amr_fasta = reformat_fasta_header(args, temp_dir, pre_amr_fasta) 
        nanopore_fasta = run_seqkit(args, temp_dir)
        total_reads = num_reads(nanopore_fasta)
        blast_results = run_blast(args.outdir, nanopore_fasta, amr_fasta)
        blast_df = blast_to_df(blast_results)
        group_df = group_differences(blast_df)
        graph_differences(args, group_df, total_reads)
        graph_mutation_curve(args, blast_df)

if __name__ == "__main__":
    main()