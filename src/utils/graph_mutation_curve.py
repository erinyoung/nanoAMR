import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from src.utils.group_differences import generate_unique_name

def graph_mutation_curve(args, df):
    """
    Generates and saves histograms showing the distribution of mismatches and indels
    in blast results for each unique gene.

    Args:
        args: The command-line arguments, which should include an 'outdir' attribute
              to specify the output directory for saving plots.
        df: A pandas DataFrame containing the blast results. The DataFrame must have
            at least the following columns: 'saccver', 'mismatch', and 'gapopen'.

    The function generates a histogram plot for each unique gene based on the
    'unique_name' derived from 'saccver'. The plot shows the distribution of
    mismatches ('mismatch') and indels ('gapopen'), and saves the plot as a PNG file.
    """

    logging.info("Grouping blast results by gene")

    df["unique_name"] = df["saccver"].apply(lambda x: generate_unique_name(x, df))

    unique_names = df['unique_name'].unique()

    for name in unique_names:
        # Create a new dataframe for each unique_name
        df_name = df[df['unique_name'] == name]
        
        bin_max = max(df['mismatch'].max(), df['gapopen'].max())
        bin_range = np.linspace(0, bin_max, 11)

        # Create the plot
        sns.histplot(data=df_name, x='mismatch', bins=bin_range, color="#E69F00", label="mismatches")
        sns.histplot(data=df_name, x='gapopen',  bins=bin_range, color="#56B4E9", label="indels")

        # Customize the plot
        plt.title(f'Artifact Distribution for {name}')
        plt.xlabel('Number of Artifacts in Read')
        plt.ylabel('Number of Reads')
        plt.legend(title='Artifact type', loc='upper right', fontsize=10)

        # Save the plot as a PNG file
        plt.savefig(f"{args.outdir}/{name}_artifact_distribution.png")

        plt.close()