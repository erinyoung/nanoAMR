import logging
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


def extract_mutations(differences):

    """
    Extract type of difference from a string of differences.

    Args:
        differences (str): A space-separated string of differences in the format "position:ref->query".

    Returns:
        list: A list of mutations positions.
    """
    mutations = [diff.split(":")[1] for diff in differences.split()]

    logging.debug(f"Identified list of positions {mutations}")

    return mutations


def graph_differences(args, input_df):

    """
    Generate bar graph and save data for mutations observed in genes.

    Args:
        input_df (pd.DataFrame): DataFrame containing 'unique_name' and 'differences' columns.
    """
    logging.info("Creating graphs for each gene")

    # TODO: get total reads

    for _, row in input_df.iterrows():
        name = row["unique_name"]
        logging.info(f"Creating graphs for {name}")

        mutations = extract_mutations(row["differences"])
        counter = Counter(mutations)
        gene_df = pd.DataFrame(counter.items(), columns = ["mutation", "count"])

        # TODO: counts of one side of the graph percent on the other side of the graph with n=number of reads with that gene

        plt.scatter(gene_df["mutation"], gene_df["count"])

        plt.xlabel(f"position in {name}")
        plt.ylabel("count")
        plt.title(f"Basepair differences in {name}")
        plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
        plt.savefig(f"{args.outdir}/{name}.png", bbox_inches="tight")

        gene_df.to_csv(f"{args.outdir}/{name}_df.csv", index=False)


    