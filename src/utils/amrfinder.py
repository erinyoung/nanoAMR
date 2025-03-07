import subprocess
import logging

def run_amrfinder(args, temp_dir):
    """
    Run AMRFinder with the given arguments.

    Args:
        args: Command-line arguments containing fasta, threads, and output directory.
        temp_dir (str): Path to the temporary directory for intermediate files.

    Returns:
        str: Path to the generated AMRFinder nucleotide output file.
    """

    logging.info(f"Running AMRFinder on {args.fasta}")

    command = [
        "amrfinder",
        "--nucleotide", args.fasta,
        "--threads", str(args.threads),
        "--output", f"{args.outdir}/amrfinder.txt",
        "--nucleotide_output", f"{temp_dir}/amrfinder.fasta",
        #"--nucleotide_flank5_output", f"{temp_dir}/amrfinder_flanked.fasta",
        #"--nucleotide_flank5_size", str(0),
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

        logging.info("AMRFinder completed successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error running AMRFinder: {e}")
        logging.error(f"Command output:\n{e.stdout.decode() if e.stdout else "No output"}")
        logging.error(f"Command error output:\n{e.stderr.decode() if e.stderr else "No error output"}")


    return f"{temp_dir}/amrfinder.fasta"
