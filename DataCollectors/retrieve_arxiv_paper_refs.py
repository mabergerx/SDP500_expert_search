# ============================================================================

# These functions were used to retrieve the references of the relevant CS
# papers matched with the arXiv set.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================


import os
import gc
import pickle
import orjson

all_paper_files = [fil for fil in os.listdir() if "txt" in fil]

all_ids = set()

with open("arxiv_matching/all_arxiv_matched_ids_with_refs.pkl", "rb") as f:
    rel_ids = pickle.load(f)


def parse_one_line(line):
    try:
        return orjson.loads(line.decode('utf-8'))
    except AttributeError:
        return orjson.loads(line)


def process_one_line(line):
    dct = parse_one_line(line)
    if dct["id"] in rel_ids:
        if "references" in dct and "indexed_abstract" in dct and "fos" in dct and "id" in dct:
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
        del lines
        gc.collect() #Garbage collector


def process_all_files():
    for paper_path in all_paper_files:
        process_file(paper_path)


process_all_files()
print("Done processing all the papers, saving to pickle now...")
all_ids.update(rel_ids)
print("Unique ID's collected: ", len(all_ids))

with open('all_ids_with_collabs_and_refs_sample.pkl', 'wb') as handle:
    pickle.dump(all_ids, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("All done.")