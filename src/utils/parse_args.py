import argparse

def parse_args():
    """Set up the command-line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="nanoamr = finding AMR genes in Oxford Nanopore reads."
    )
    
    parser.add_argument(
        "-r", "--reads", 
        required=True,
        type=str,
        help="Path to the input nanopore reads in fastq.gz format."
    )

    parser.add_argument(
        "-f", "--fasta", 
        required=True,
        type=str,
        help="Path to the reference fasta file."
    )

    parser.add_argument(
        "-o", "--outdir", 
        default="nanoamr",
        type=str,
        help="Path for output files. Default is \"nanoamr\"."
    )
    
    parser.add_argument(
        "-t", "--threads", 
        type=int, 
        default=3, 
        help="Number of threads to use. Default is 3."
    )
    
    parser.add_argument(
        "-g", "--gene", 
        default="",
        type=str,
        help="String used for regex to limit results to subset of genes (examples: bla for all beta-lactamases or KPC for KPCs)."
    )

    parser.add_argument('-log', '--loglevel',
        required = False,
        type = str,
        help = 'Logging level',
        default = 'INFO'
        )

    parser.add_argument('-v', '--version',
        help='Print version and exit',
        action = 'version'
        )

    return parser.parse_args()