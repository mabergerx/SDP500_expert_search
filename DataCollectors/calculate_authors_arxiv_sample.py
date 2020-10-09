# ============================================================================

# These functions were used to calculate arXiv dataset statistics.
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

all_paper_files = [fil for fil in os.listdir("actual_matches") if "json" in fil]

# with open("../authors/all_sample_ids.pkl", "rb") as f:
#     rel_ids = pickle.load(f)

def parse_one_file(file):
    try:
        return orjson.loads(file.decode('utf-8'))
    except AttributeError:
        return orjson.loads(file)

authors = []

for pf in all_paper_files:
    with open(pf, "rb") as bigfile:
        print('Started on file ', pf)
        lines = bigfile.readlines()
        jl = parse_one_file(lines[0])
        for j in jl:
             try:
                 authors.extend([a["id"] for a in j["authors"]])
             except:
                 continue
        print("Done with", pf)


print("Done processing all the papers, saving to pickle now...")
authors = set(authors)
print("Unique ID's collected: ", len(authors))

with open('all_arxiv_matched_author_ids.pkl', 'wb') as handle:
    pickle.dump(authors, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("All done.")