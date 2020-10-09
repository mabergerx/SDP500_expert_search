# ============================================================================

# These functions were used to calculate arXiv author set statistics.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================


import os
import orjson
import scipy.stats

all_paper_files = [fil for fil in os.listdir("actual_matches") if "json" in fil]

# with open("../authors/all_sample_ids.pkl", "rb") as f:
#     rel_ids = pickle.load(f)

def parse_one_file(file):
    try:
        return orjson.loads(file.decode('utf-8'))
    except AttributeError:
        return orjson.loads(file)

authors = {}

for pf in all_paper_files:
    with open("actual_matches/"+pf, "rb") as bigfile:
        print('Started on file ', pf)
        lines = bigfile.readlines()
        jl = parse_one_file(lines[0])
        for j in jl:
             try:
                for a in j["authors"]:
                    if a["id"] in authors.keys():
                        authors[a["id"]] += 1
                    else:
                        authors[a["id"]] = 1
             except:
                 continue
        print("Done with", pf)

counts = authors.values()

print(scipy.stats.describe(list(counts)))
print("Between 4 and 999:", len([c for c in counts if c>4 and c<1000]))
print("10 or more:", len([c for c in counts if c>9]))
print("20 or more:", len([c for c in counts if c>19]))
print("50 or more:", len([c for c in counts if c>50]))
print("100 or more:", len([c for c in counts if c>100]))