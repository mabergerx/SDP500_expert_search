# ============================================================================

# These functions were used to extract all the paper tags for IDCG pre-calc.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import orjson
import pickle
import json
from collections import defaultdict
import gc
import pandas as pd

def load(line):
    try:
        return orjson.loads(line)
    except:
        return None

all_tags_per_author = defaultdict(list)

author_ids_set = set(pd.read_csv("../authors/arxiv_authors_127k_data_v2.csv").id.values)

with open("all_pub_ids_for_eval.pickle", "rb") as f:
    all_ids = pickle.load(f)

with open('0.json', 'rb') as fin:
    lines = fin.readlines()

json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

# with open('0_relevant.json', 'w') as outfile:
#     json.dump(rel_lines, outfile)
for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 0.")


with open('1.json', 'rb') as fin:
    lines = fin.readlines()

json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 1.")

with open('2.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 2.")

with open('3.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 3.")

with open('4.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 4.")


with open('5.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 5.")



with open('6.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 6.")



with open('7.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 7.")



with open('8.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 8.")


with open('9.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 9.")


with open('10.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 10.")


with open('11.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 11.")


with open('12.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 12.")

with open('13.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 13.")


with open('14.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 14.")

with open('15.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 15.")

with open('16.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 16.")


with open('17.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 17.")

with open('18.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 18.")

with open('19.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 19.")

with open('20.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 20.")

with open('21.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 21.")

with open('22.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 22.")


with open('23.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 23.")


with open('24.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 24.")


with open('25.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 25.")


with open('26.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 26.")


with open('27.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 27.")


with open('28.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 28.")


with open('29.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 29.")


with open('30.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 30.")


with open('31.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 31.")


with open('32.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 32.")


with open('33.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 33.")


with open('34.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 34.")


with open('35.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 35.")


with open('36.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 36.")


with open('37.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 37.")


with open('38.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 38.")


with open('39.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))

print("Done with 39.")


with open('40.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()
print("Authors found up till now:", len(all_tags_per_author))
print("Done with 40.")


with open('41.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]
for rl in rel_lines:
    try:
        author_ids = [a["id"] for a in rl["authors"] if int(a["id"]) in author_ids_set]
    except:
        continue
    try:
        for ai in author_ids:
            citations = rl["n_citation"] + 1 # Smoothing factor
            fos = [f['name'] for f in rl['fos']]
            fos_with_citations = [(f, citations) for f in fos]
            all_tags_per_author[ai].extend(fos_with_citations)
    except:
        continue

del json_lines
del rel_lines
del lines
gc.collect()

print("Authors found up till now:", len(all_tags_per_author))
print("Done with 41.")

print("Writing to pickle now...")

with open('tags_for_ndcg_with_citations.pickle', 'wb') as handle:
    pickle.dump(all_tags_per_author, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Done all files!")
