import logging

def num_reads(fasta):
    """Count the number of '>' characters in a FASTA file."""
    with open(fasta, "r") as file:
        num_reads = file.read().count(">")

    logging.debug(f"There are {num_reads} in the sample")
    return int(num_reads)