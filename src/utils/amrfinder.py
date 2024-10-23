import subprocess
import logging

def run_amrfinder(args):
    """Run amrfinder."""

    # TODO : put fasta file in tmp directory 

    logging.info(f"Running AMRFinder on {args.fasta}")

    command = [
        "amrfinder",
        "--nucleotide", args.fasta,
        "--threads", str(args.threads),
        "--output", f"{args.outdir}/amrfinder.txt",
        "--nucleotide_output", f"{args.outdir}/amrfinder.fasta",
        #"--nucleotide_flank5_output", f"{args.outdir}/amrfinder_flanked.fasta",
        #"--nucleotide_flank5_size", str(0),
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

        logging.info("AMRFinder completed successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error running AMRFinder: {e}")
        logging.error(f"Command output:\n{e.stdout}")
        logging.error(f"Command error output:\n{e.stderr}")

    return f"{args.outdir}/amrfinder.fasta"
