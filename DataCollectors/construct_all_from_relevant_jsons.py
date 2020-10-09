# ============================================================================

# These functions were used to reconstruct the full filtered data subset from
# separate relevant entries stored in separate JSON files.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import pandas as pd
import os
import orjson

all_paper_files = [fil for fil in os.listdir("references_and_matches") if "json" in fil]

def parse_one_file(file):
    try:
        return orjson.loads(file.decode('utf-8'))
    except AttributeError:
        return orjson.loads(file)

rel_dfs = []

for pf in all_paper_files:
    with open("references_and_matches/"+pf, "rb") as bigfile:
        print('Started on file ', pf)
        lines = bigfile.readlines()
        jl = parse_one_file(lines[0])
        rel_dfs.append(pd.read_json(jl))
        print("Done with", pf)

full_df = pd.concat([rel_dfs])
full_df.to_pickle("all_arxiv_papers_with_references.pkl")

