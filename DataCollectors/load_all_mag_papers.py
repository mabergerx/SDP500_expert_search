import pandas as pd
import json
import dask
import dask.dataframe as dd

def read_single_pickle(pickle_path):
    try:
        return pd.read_pickle(pickle_path)
    except:
        return None

def load_paper_pickle_batch(starting_index=0, end_index=5):
    frames = [
       pd.read_pickle(f"paper_pickles/pickles/mag_papers_{i}.pkl") for i in range(starting_index, end_index+1)
    ]
    one_frame = pd.concat([f for f in frames if f])
    return one_frame

def load_all_mag_papers():
    start_i = 0
    end_i = 40
    batches = []
    while end_i < 200:
        print(f"Started loading batch between {start_i} and {end_i}")
        try:
            one_batch = load_paper_pickle_batch(start_i, end_i)
            batches.append(one_batch)
            del one_batch
            print(f"Done batch between {start_i} and {end_i}")
            start_i += 40
            end_i += 40
        except:
            pass

    return pd.concat(batches).reset_index(drop=True)

all_papers = load_all_mag_papers()
all_papers.to_csv("all_papers.csv")