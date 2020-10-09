import pandas as pd
import json
import os
import gc

all_paper_files = [fil for fil in os.listdir() if "txt" in fil]

paper_dfs = []


def parse_one_line(line):
    try:
        yield json.loads(line.decode('utf-8'))
    except AttributeError:
        yield json.loads(line)


def prune_one_line(line):
    dct = parse_one_line(line)
    if "references" in dct and "indexed_abstract" in dct and "authors" in dct and "fos" in dct and "id" in dct:
        if dct["fos"] and dct["authors"] and dct["indexed_abstract"] and dct["references"] and dct["title"]:
            relevant_keys = ["authors", "fos", "id", "indexed_abstract", "n_citation", "references", "title", "year"]
            new_dct = {relevant_key: dct[relevant_key] for relevant_key in relevant_keys if relevant_key in dct}
            yield new_dct
        else:
            yield {}
    else:
        yield {}


def prune_and_store(file_path):
    with open(file_path, "rb") as bigfile:
        print('Started on file ', file_path)
        lines = bigfile.readlines()
        print("Read the lines...")
        parsed = [prune_one_line(l) for l in lines]
        proper_parsed = [p for p in parsed if p != {}]
        print("Parsed into JSON...")
        df = pd.DataFrame(proper_parsed)
        print("DF head looks like this:")
        print(df.head(2))
        paper_dfs.append(df)
        print("Dataframe done and appended!")
        print("Deleting the file now to free up space: ", file_path)
        os.remove(file_path)
        print("------")
#         df.dropna(subset=["authors"], inplace=True)
#         df_final = df[["title", "year", "references", "abstract", "id", "authors", "doi", "fos", "keywords"]]
#         df_final.to_pickle(f"{file_path.replace('.txt', '.pkl')}")
        del df
        del proper_parsed
        del parsed
        del lines
        gc.collect() #Garbage collector

def load_all_mag_papers():
    for paper_path in all_paper_files:
        prune_and_store(paper_path)

load_all_mag_papers()
print("Done loading all the papers, concatenating and saving to pickle now...")

pd.concat(paper_dfs).to_pickle("all_papers_new.pkl")

print("All done.")