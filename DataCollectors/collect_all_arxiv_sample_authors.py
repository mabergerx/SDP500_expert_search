# ============================================================================

# These functions were used to collect all the authors for the arXiv sample.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import pandas as pd
import numpy as np

# Read all the ids
all_ids = np.load("all_relevant_author_ids.npy")
print("Read all ids. Sample:", all_ids[:5])
all_ids_set = set(all_ids)

all_data = pd.read_csv("all_authors.csv")
print("Read all author data in memory!")


def extract_relevant_authors(df=all_data):
    return df[df["id"].isin(all_ids_set)]

print("Started extracting...")
extract_relevant_authors().to_csv("arxiv_authors.csv", index=False)
print("Done extracting and saved to CSV!")