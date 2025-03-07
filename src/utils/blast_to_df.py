import logging
import pandas as pd


# for pytest
# qseq	sseq	differences
# AACGCC	AACGCG	6:G->C
# AA-GCC	AACGCG	3:C->-, 6:G->C
# AACGCC	AA-GCG	3:-->C, 5:G->C

def get_differences(qseq, sseq):
    """
    Compare two sequences and return a formatted string 
    describing differences in position and values.

    Args:
        qseq (str): Query sequence.
        sseq (str): Subject/reference sequence.

    Returns:
        str: Differences in format "position:ref->query".
    """

    differences = []
    sseq_clean = sseq.replace("-", "")

    s_index = 0
    for q, s in zip(qseq, sseq):
        if q != s:
            differences.append(f"{s_index+1}:{s}->{q}")

            # doesn't increment position of reference if there's an insertion
            if s != "-":
                s_index += 1
        else:
            # sanity check
            if sseq_clean[s_index] != s:
                logging.fatal("The reference does not match itself!")
                exit()
            s_index += 1
    
    return ", ".join(differences)


def blast_to_df(file):
    """
    Read a BLAST output file and annotate sequence differences.

    Args:
        file (str): Path to the BLAST tab-delimited file.

    Returns:
        pd.DataFrame: DataFrame with BLAST results and sequence differences.
    """

    column_names = [
        "qaccver", 
        "saccver", 
        "pident", 
        "length", 
        "mismatch", 
        "gapopen", 
        "qstart", 
        "qend", 
        "sstart", 
        "send", 
        "evalue", 
        "bitscore", 
        "qseq", 
        "sseq"
    ]

    df = pd.read_csv(file, sep="\t", comment="#", header=None, names=column_names)

    df["differences"] = df.apply(lambda row: get_differences(row["qseq"], row["sseq"]), axis=1)

    return df