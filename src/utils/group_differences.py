import logging
import pandas as pd

def generate_unique_name(base_name, df):
    """
    Generate a unique name by checking for duplicates in the given DataFrame.

    Args:
        base_name (str): The base name to modify if duplicates exist.
        df (pd.DataFrame): DataFrame containing a 'unique_name' column.

    Returns:
        str: A unique name.
    """

    parsed_name = base_name.split("_node:NODE")[0]

    # Check if the base_name already exists in the dataframe
    if "unique_name" in df.keys():
        existing_names = df["unique_name"].tolist()
    else:
        existing_names = []

    if parsed_name not in existing_names:
        return parsed_name
    else:
        # If the name exists, append an incremental number
        count = 1
        new_name = f"{parsed_name}_{count}"
        while new_name in existing_names:
            count += 1
            new_name = f"{parsed_name}_{count}"
        return new_name

def group_differences(blast_df):
    """
    Group differences by 'saccver' and assign unique names.

    Args:
        blast_df (pd.DataFrame): DataFrame containing 'saccver' and 'differences' columns.

    Returns:
        pd.DataFrame: A DataFrame with grouped differences and unique names.
    """

    logging.info("Grouping blast results by gene")
    df = blast_df.groupby("saccver")["differences"].apply(lambda x: " ".join(x)).reset_index()

    df["unique_name"] = df["saccver"].apply(lambda x: generate_unique_name(x, df))

    df['num_reads']   = df['saccver'].apply(lambda x: blast_df["saccver"].value_counts().get(x, 0))

    return df