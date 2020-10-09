import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

def load_relevant_index(type="separate_sbert"):
    """
    Load a populated FAISS index with paper embeddings.

    Parameters:
    type (string): The type of the paper embeddings index to load
    
    Returns:
    index (obj): A loaded FAISS index object
    """
    index = None
    if type == "separate_sbert":
        index = faiss.read_index("Data/mapped_indeces/separate_embeddings_faiss.index")
    elif type == "merged_sbert":
        index = faiss.read_index("Data/mapped_indeces/merged_embeddings_faiss.index")
    elif type == "retro_merged_sbert":
        index = faiss.read_index("Data/mapped_indeces/retro_merged_embeddings_faiss.index")
    elif type == "retro_separate_sbert":
        index = faiss.read_index("Data/mapped_indeces/retro_separate_embeddings_faiss.index")
    elif type == "tfidf_svd":
        index = faiss.read_index("Data/mapped_indeces/tfidf_embeddings_faiss.index")

    return index


def load_data_and_authors(data_path="Data/data_with_title_embeddings.pkl",
                          authors_path="Data/authors_with_wikidata.csv"):
    """
    Load the authors and papers metadata. 
    This data is used to enrich retrieved results with useful information. 
    
    Parameters:
    data_path (string): Path to the papers CSV file
    authors_path (string): Path to the authors CSV file
    
    Returns:
    data (dataframe): A Pandas dataframe with papers data
    authors (dataframe): A Pandas dataframe with authors data
    """
    data = pd.read_pickle(data_path)
    data.drop(63376, inplace=True)
    authors = pd.read_csv(authors_path)
    authors.drop("Unnamed: 0", inplace=True, axis=1)
    return data, authors


def load_embedder(sbert_model='roberta-base-nli-stsb-mean-tokens'):
    """
    Load the Sentence-BERT embedder model. Note: this will load the model
    file from the internet if it is not detected in the system.
    
    Parameters:
    sbert_model (string): Specification of the SBERT model type.
    
    Returns:
    embedder (obj): A loaded Sentence-BERT model.
    """
    embedder = SentenceTransformer(sbert_model)
    return embedder


# Load all the data and models at API startup.
data_and_authors = load_data_and_authors()
data = data_and_authors[0]
authors = data_and_authors[1]
embedder = load_embedder()

