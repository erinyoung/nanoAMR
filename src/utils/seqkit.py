import subprocess
import logging

def run_seqkit(args, tmp):
    """Run seqkit on nanopore reads to convert them to fasta."""

    # TODO : put fasta file in tmp directory 
    logging.info(f"Running SeqKit on {args.reads}")
    
    command = [
        "seqkit",
        "fq2fa",
        args.reads,
        "--threads", str(args.threads),
        #"--out-file", f"{tmp}/nanopore.fasta",
        "--out-file", f"{args.outdir}/nanopore.fasta",
    ]
    
    logging.debug(f"Running command: {' '.join(command)}")

    try:
        result = subprocess.run(
            command, 
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )

        logging.debug(f"Command output:\n{result.stdout}")
            
        if result.stderr:
            logging.error(f"Command error output:\n{result.stderr}")

        logging.info("SeqKit completed successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error running SeqKit: {e}")
        logging.error(f"Command output:\n{e.stdout}")
        logging.error(f"Command error output:\n{e.stderr}")

    #return f"{tmp}/nanopore.fasta"

    return f"{args.outdir}/nanopore.fasta"
