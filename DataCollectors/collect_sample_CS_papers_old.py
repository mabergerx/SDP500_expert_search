# ============================================================================

# These functions were used to collect the initial sample CS papers.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import pandas as pd
import os
import gc
import orjson
import pickle

all_paper_files = [fil for fil in os.listdir() if "txt" in fil]
# all_paper_files = ["mag_papers_31.txt", "mag_papers_32.txt"]

with open("all_ids_with_collabs_and_refs_sample.pkl", "rb") as f:
    all_ids = pickle.load(f)


relevant_rows = []


def parse_one_line(line):
    try:
        return orjson.loads(line.decode('utf-8'))
    except AttributeError:
        return orjson.loads(line)


def prune_one_line(line):
    dct = parse_one_line(line)
    if dct["id"] in all_ids:
        if "references" in dct and "indexed_abstract" in dct and "authors" in dct and "fos" in dct:
            if dct["fos"] and dct["authors"] and dct["indexed_abstract"] and dct["references"] and dct["title"]:
                relevant_keys = ["authors", "fos", "id", "indexed_abstract", "n_citation", "references", "title", "year"]
                new_dct = {relevant_key: dct[relevant_key] for relevant_key in relevant_keys if relevant_key in dct}
                relevant_rows.append(new_dct)
                del new_dct
                gc.collect()


def process_file(file_path):
    with open(file_path, "rb") as bigfile:
        print('Started on file ', file_path)
        lines = bigfile.readlines()
        print("Read the lines...")
        [prune_one_line(l) for l in lines]
        print("Processed all lines in the file...")
        print("The amount of collected rows is now:", len(relevant_rows))
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
print("Done processing all the papers, saving to CSV now...")
print("Unique rows collected: ", len(relevant_rows))

pd.DataFrame(relevant_rows).to_csv("all_relevant_CS_papers.csv")

print("All done.")