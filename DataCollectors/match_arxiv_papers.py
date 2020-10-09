# ============================================================================

# These functions were used to match the arXiv set to the full OAG set. Used
# to create a subset of OAG with relevant CS papers.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import orjson
import pickle
import json
import gc


with open("titles_dirt", "r") as tf: 
    all_arxiv_titles = tf.readlines()
    all_arxiv_titles = set([" ".join(t.replace("\n", "").split()) for t in all_arxiv_titles]) 


def load(line):
    try:
        return orjson.loads(line)
    except:
        return None


TOTAL_COUNTER = 0


with open('../0.json', 'rb') as fin:
    lines = fin.readlines()

json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('0_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 0.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 0.")
del rel_lines
del json_lines
del lines
gc.collect()


with open('../1.json', 'rb') as fin:
    lines = fin.readlines()

json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('1_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 1.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 1.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../2.json', 'rb') as fin:
    lines = fin.readlines()

json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('2_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 2.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 2.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../3.json', 'rb') as fin:
    lines = fin.readlines()

json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('3_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 3.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 3.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../4.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('4_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 4.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 4.")
del rel_lines
del json_lines
del lines
gc.collect()


with open('../5.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('5_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 5.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 5.")
del rel_lines
del json_lines
del lines
gc.collect()



with open('../6.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('6_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 6.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 6.")
del rel_lines
del json_lines
del lines
gc.collect()


with open('../7.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('7_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 7.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 7.")
del rel_lines
del json_lines
del lines
gc.collect()


with open('../8.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('8_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 8.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 8.")
del rel_lines
del json_lines
del lines
gc.collect()


with open('../9.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('9_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 9.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 9.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../10.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('10_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 10.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 10.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../11.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('11_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 11.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 11.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../12.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('12_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 12.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 12.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../13.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('13_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 13.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 13.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../14.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('14_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 14.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 14.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../15.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('15_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 15.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 15.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../16.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('16_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 16.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 16.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../17.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('17_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 17.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 17.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../18.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('18_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 18.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 18.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../19.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('19_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 19.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 19.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../20.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('20_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 20.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 20.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../21.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('21_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 21.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 21.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../22.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('22_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 22.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 22.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../23.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('23_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 23.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 23.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../24.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('24_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 24.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 24.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../25.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('25_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 25.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 25.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../26.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('26_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 26.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 26.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../27.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('27_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 27.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 27.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../28.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('28_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 28.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 28.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../29.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('29_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 29.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 29.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../30.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('30_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 30.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 30.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../31.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('31_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 31.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 31.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../32.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('32_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 32.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 32.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../33.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('33_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 33.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 33.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../34.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('34_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 34.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 34.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../35.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('35_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 35.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 35.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../36.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('36_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 36.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 36.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../37.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('37_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 37.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 37.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../38.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('38_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 38.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 38.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../39.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('39_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 39.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 39.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../40.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('40_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 40.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 40.")
del rel_lines
del json_lines
del lines
gc.collect()

with open('../41.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["title"] in all_arxiv_titles]

with open('41_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Found", len(rel_lines), "relevant papers in 41.")
TOTAL_COUNTER += len(rel_lines)
print("Done with 41.")
del rel_lines
del json_lines
del lines
gc.collect()

print("Done all files!")
print("Found", TOTAL_COUNTER, "arXiv matches.")