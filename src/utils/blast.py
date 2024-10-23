import logging
import subprocess

def run_blast(args, query_file, subject_file):
    """Using AMR genes fasta file on nanopore reads."""
    logging.info("Running blast with AMR genes as subject and nanopore reads as query")

    try:
        # note: -num_threads is ignored when using subject

        fmt = "6 std qseq sseq"

        command = [
            "blastn",
            "-query", query_file,
            "-subject", subject_file,
            "-outfmt", '6 std qseq sseq',
            "-out", f"{args.outdir}/blast.txt",
            "-evalue", "1e-25", 
        ]
        
        logging.debug(f"Running BLAST search with command: {' '.join(command)}")
        
        # Run the blast command
        subprocess.run(command, check=True)
        logging.info("BLAST search completed successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error running BLAST: {e}")
        raise

    return f"{args.outdir}/blast.txt"