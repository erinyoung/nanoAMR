import subprocess
import logging

def reformat_fasta_header(args, temp_dir, fasta):
    """
    Adjust the headers of an AMRFinder FASTA file.

    Args:
        args: Command-line arguments.
        temp_dir (str): Path to the temporary directory for output.
        fasta (str): Path to the input FASTA file.

    Returns:
        str: Path to the reformatted FASTA file.
    """

    logging.info("Adjusting AMRFinder fasta file")

    # TODO : add gene regex

    with open(fasta, "r") as infile, open(f"{temp_dir}/amr.fasta", "w") as outfile:
        for line in infile:
            line = line.strip() 
            
            if line.startswith(">"):
                gene = line.split()[2]
                node = f"{line.split()[0].replace(">","")}"
                logging.debug(f"{gene} found on {node}")
                outfile.write(f">{gene}_node:{node}\n")
            else:
                outfile.write(f"{line}\n")

    logging.info("Adjusted AMRFinder fasta file headers")

    return f"{temp_dir}/amr.fasta"