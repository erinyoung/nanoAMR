import subprocess
import logging

def reformat_fasta_header(args, fasta):
    """Fix amr fasta."""

    logging.info("Adjusting AMRFinder fasta file")

    # TODO : put this in tmp directory
    # TODO : add gene regex

    with open(fasta, 'r') as infile, open(f"{args.outdir}/amr.fasta", 'w') as outfile:
        for line in infile:
            line = line.strip() 
            
            if line.startswith('>'):
                gene = line.split()[2]
                node = f"{line.split()[0].replace(">","")}"
                logging.debug(f"{gene} found on {node}")
                outfile.write(f">{gene}_node:{node}\n")
            else:
                outfile.write(f"{line}\n")

    logging.info("Adjusted AMRFinder fasta file headers")

    return f"{args.outdir}/amr.fasta"