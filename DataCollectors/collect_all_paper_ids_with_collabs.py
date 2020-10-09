# ============================================================================

# These functions were used to collect relevant paper IDS and their collabs
# for one of our initial subset generation strategies.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================


import json
import os
import gc
import pickle

all_paper_files = [fil for fil in os.listdir() if "txt" in fil]

all_ids = set()

with open("../hundred_authors_pubs_with_collabs.pkl", "rb") as f:
    rel_ids = pickle.load(f)


def parse_one_line(line):
    try:
        return json.loads(line.decode('utf-8'))
    except AttributeError:
        return json.loads(line)


def process_one_line(line):
    dct = parse_one_line(line)
    if dct["id"] in rel_ids:
        if "references" in dct and "indexed_abstract" in dct and "authors" in dct and "fos" in dct and "id" in dct:
            if dct["fos"] and dct["authors"] and dct["indexed_abstract"] and dct["references"] and dct["title"]:
                refs = dct["references"][:10]
                all_ids.update(refs)


def process_file(file_path):
    with open(file_path, "rb") as bigfile:
        print('Started on file ', file_path)
        lines = bigfile.readlines()
        print("Read the lines...")
        [process_one_line(l) for l in lines]
        print("Processed all lines in the file...")
        print("------")
#         df.dropna(subset=["authors"], inplace=True)
#         df_final = df[["title", "year", "references", "abstract", "id", "authors", "doi", "fos", "keywords"]]
#         df_final.to_pickle(f"{file_path.replace('.txt', '.pkl')}")
        del lines
        gc.collect() #Garbage collector


def process_all_files():
    for paper_path in all_paper_files:
        process_file(paper_path)


process_all_files()
print("Done processing all the papers, saving to pickle now...")
all_ids.update(rel_ids)
print("Unique ID's collected: ", len(all_ids))

with open('all_ids_with_collabs_and_refs.pkl', 'wb') as handle:
    pickle.dump(all_ids, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("All done.")