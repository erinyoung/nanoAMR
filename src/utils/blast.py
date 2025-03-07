import logging
import subprocess

def run_blast(out_dir, query_file, subject_file):
    """
    Run BLAST with AMR genes as the subject and nanopore reads as the query.

    Args:
        out_dir (str): Output directory for BLAST results.
        query_file (str): Path to the query FASTA file (nanopore reads).
        subject_file (str): Path to the subject FASTA file (AMR genes).

    Returns:
        str: Path to the generated BLAST output file.
    """
    logging.info("Running blast with AMR genes as subject and nanopore reads as query")

    try:
        # note: -num_threads is ignored when using subject

        #fmt = "6 std qseq sseq"

        command = [
            "blastn",
            "-query", query_file,
            "-subject", subject_file,
            "-outfmt", "6 std qseq sseq",
            "-out", f"{out_dir}/blast.txt",
            "-evalue", "1e-25", 
        ]
        
        logging.debug(f"Running BLAST search with command: {" ".join(command)}")
        
        # Run the blast command
        # current header : qaccver saccver pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq
        subprocess.run(command, check=True)
        logging.info("BLAST search completed successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error running BLAST: {e}")
        raise

    return f"{out_dir}/blast.txt"