import logging
import pandas as pd
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt

def extract_positions(differences):

    """
    Extract numerical positions from a string of differences.

    Args:
        differences (str): A space-separated string of differences in the format "position:ref->query".

    Returns:
        list: A list of integer positions.
    """
    positions = [int(diff.split(":")[0]) for diff in differences.split()]

    logging.debug(f"Identified list of positions {positions}")

    return positions


def graph_differences(args, group_df, total_reads):

    """
    Generate scatter plots and save data for base pair differences in genes.

    Args:
        input_df (pd.DataFrame): DataFrame containing 'unique_name' and 'differences' columns.
    """
    logging.info("Creating graphs for each gene")

    for _, row in group_df.iterrows():
        name = row["unique_name"]
        logging.info(f"Creating graphs for {name}")

        positions = extract_positions(row["differences"])
        num_reads = row['num_reads']

        counter = Counter(positions)
        gene_df = pd.DataFrame(counter.items(), columns = ["position", "count"])

        gene_df["perc"] = gene_df["count"] / num_reads * 100

        sns.scatterplot(x='position', y='count', data=gene_df, color='black', s=10)

        plt.xlabel(f"Position in {name}")
        plt.ylabel("Raw count of reads")
        plt.title(f"Basepair differences in {name}")
        plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
        plt.savefig(f"{args.outdir}/{name}_counts.png", bbox_inches="tight")

        plt.close()

        sns.scatterplot(x='position', y='perc', data=gene_df, color='black', s=10)

        plt.xlabel(f"Position in {name}")
        plt.ylabel("Percentage of reads")
        plt.title(f"Basepair differences in {name}")
        plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
        plt.savefig(f"{args.outdir}/{name}_perc.png", bbox_inches="tight")

        plt.close()

        gene_df.to_csv(f"{args.outdir}/{name}_df.csv", index=False)


    