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

def main():
    """Main function to run the script."""
    args = parse_args()

    logging.basicConfig(format='%(asctime)s - %(message)s',
        datefmt = '%y-%b-%d %H:%M:%S',
        level=args.loglevel.upper())

    logging.info(f'Reference fasta :\t{args.fasta}')
    logging.info(f'Nanopore reads :\t{args.reads}')
    check_versions()
    exit
    logging.info(f'Num threads :\t{str(args.threads)}')
    if args.gene:
        logging.info(f'Regex str :\t{args.gene}')
    logging.info(f'Result dir :\t{args.outdir}')

    if os.path.exists(args.outdir):
        logging.fatal("FATAL: outdir directory already exists")
        sys.exit(1)
    else:
        os.mkdir(args.outdir)

    with tempfile.TemporaryDirectory(dir = args.outdir) as temp_dir:
        pre_amr_fasta = run_amrfinder(args)
        amr_fasta = reformat_fasta_header(args, pre_amr_fasta) 
        nanopore_fasta = run_seqkit(args, temp_dir)
        blast_results = run_blast(args, nanopore_fasta, amr_fasta)
        # TODO :
        # convert blast output to pandas df
        # current header : qaccver saccver pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq
        # for each oxagene_node: , get the length and position of each difference



if __name__ == "__main__":
    main()