# ============================================================================

# These functions were used to load all the MAG authors into separate files.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import pandas as pd
import json
import os

author_dfs = []

def parse_one_line(line):
    return json.loads(line)


def prune_and_store(file_path):
    with open(file_path, "rb") as bigfile:
        lines = bigfile.readlines()
        parsed = [parse_one_line(l) for l in lines]
        proper_parsed = [p for p in parsed if "pubs" in p and "name" in p and "id" in p]
        df = pd.DataFrame(proper_parsed)
        cols = list(df.columns[df.columns.isin(["h_index", "id", "name", "n_citation", "n_pubs", "pubs", "tags"])])
        df_final = df[cols]
        author_dfs.append(df_final)


def load_all_authors():
    for i in range(0, 3):
        fils = os.listdir()
        for f in fils:
            prune_and_store("mag_authors_"+i)
        print("Loaded all the authors from dir " + str(i))


load_all_authors()

pd.concat([f for f in author_dfs if f]).to_csv("all_authors.csv")