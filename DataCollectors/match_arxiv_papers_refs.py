# ============================================================================

# These functions were used to match the arXiv set to the full OAG set. Used
# to create a subset of OAG with relevant CS papers. This version also collected
# the references of the relevant papers.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import pandas as pd
import json
import os
import gc
import pickle
import orjson

all_paper_files = [fil for fil in os.listdir() if "json" in fil]

# with open("../authors/all_sample_ids.pkl", "rb") as f:
#     rel_ids = pickle.load(f)

def parse_one_file(file):
    try:
        return orjson.loads(file.decode('utf-8'))
    except AttributeError:
        return orjson.loads(file)

references = []

for pf in all_paper_files:
    with open(pf, "rb") as bigfile:
        print('Started on file ', pf)
        lines = bigfile.readlines()
        jl = parse_one_file(lines[0])
        for j in jl:
             try:
                 references.extend(j["references"])
                 references.extend(j["id"])
             except:
                 continue
        print("Done with", pf)


print("Done processing all the papers, saving to pickle now...")
references = set(references)
print("Unique ID's collected: ", len(references))

with open('all_arxiv_matched_ids_with_refs.pkl', 'wb') as handle:
    pickle.dump(all_ids, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("All done.")