import subprocess
import logging

def run_seqkit(args, temp_dir):
    """
    Run SeqKit on nanopore reads to convert them to FASTA format.

    Args:
        args: Command-line arguments containing `reads` and `threads`.
        temp_dir (str): Path to the temporary directory for output.

    Returns:
        str: Path to the output FASTA file.
    """

    logging.info(f"Running SeqKit on {args.reads}")
    
    command = [
        "seqkit",
        "fq2fa",
        args.reads,
        "--threads", str(args.threads),
        "--out-file", f"{temp_dir}/nanopore.fasta",
    ]
    
    logging.debug(f"Running command: {" ".join(command)}")

    try:
        result = subprocess.run(
            command, 
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )

        logging.debug(f"Command output:\n{result.stdout.decode()}")

        if result.stderr:
            logging.error(f"Command error output:\n{result.stderr.decode()}")

        logging.info("SeqKit completed successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error running SeqKit: {e}")
        logging.error(f"Command output:\n{e.stdout.decode()}")
        logging.error(f"Command error output:\n{e.stderr.decode()}")
    

    return f"{temp_dir}/nanopore.fasta"
