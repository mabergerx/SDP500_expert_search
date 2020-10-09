# ==========================================================================

# These functions are used for embedding the papers. Both embedding strategies
# introduced in the thesis are present here: the merged and the separate
# strategies.
#
# (c) Mark Berger

# ==========================================================================

import ast
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd


embedder = SentenceTransformer('roberta-base-nli-stsb-mean-tokens')

# code to embed all the titles
def create_title_embeddings(df, model=embedder):
    """
    Embed all the paper titles.
    
    :param df: The papers dataframe.
    :param model: The embedder model (Sentence-BERT)
    
    :return df: Papers dataframe with an added column 
    that contains title embeddings
    """
    title_embeddings = model.encode(df.cleaned_title)
    df["title_embedding"] = title_embeddings
    return df


def calculate_average_abstract_embedding(emb_list):
    """
    Calculate the average of a list of abstract sentence
    embeddings.
    
    :param emb_list: List of sentence embeddings.
    
    :return The average embedding.
    """
    return np.mean(emb_list, axis=0)


def create_abstract_sentence_embeddings(df, model=embedder):
    """
    Embed a flat list of all abstract sentences all at once using batch embedding.
    
    :param df: The papers dataframe.
    :param model: The embedder model (Sentence-BERT)
    
    :return flat_sentence_embeddings: A flat list of all sentence embeddings.
    """
    def create_literal_arrays(array_repr):
        corrected = " ".join(
            array_repr.replace("\n", "").replace("      dtype=float32),", "").replace("array(", "").replace(
                ",      dtype=float32)", "").split())
        return ast.literal_eval(corrected)

    if "abstract_sentence_embeddings" in df.columns:
        df["abstract_sentence_embeddings"] = df.abstract_sentence_embeddings.apply(
            lambda x: create_literal_arrays(x))
        print("Converted existing column to arrays!")
    else:
        flat_sentence_list = [s for sublist in df.abstract_sentences for s in sublist]
        flat_sentence_embeddings = model.encode(flat_sentence_list)
        return flat_sentence_embeddings


def calculate_all_average_abstract_embeddings(abstract_embedding_batches):
    """
    Calculate average abstract embedding for each abstract.
    
    :param abstract_embedding_batches: Batches of abstract sentence embeddings.
    
    :return A list of abstract embeddings.
    """
    return [calculate_average_abstract_embedding(el) for el in abstract_embedding_batches]


def create_merged_sbert_embeddings(title_embeddings, abstract_embedding_batches):
    """
    Calculate paper embeddings following the merge strategy (described in paper).
    
    :param title_embeddings: A list of title embeddings.
    :param abstract_embedding_batches: Batches of abstract sentence embeddings.
    
    :return merged_embeddings: A list of paper embeddings following the merge strategy
    """
    merged_embeddings = []

    for title_embedding, batch in zip(title_embeddings, abstract_embedding_batches):
        batch.append(title_embedding.tolist())
        mean = np.mean(batch, axis=0)
        merged_embeddings.append(mean)

    return merged_embeddings


def create_separate_sbert_embeddings(title_embeddings, average_abstract_embeddings):
    """
    Calculate paper embeddings following the separate strategy (described in paper).
    
    :param title_embeddings: A list of title embeddings.
    :param abstract_embedding_batches: Batches of abstract sentence embeddings.
    
    :return merged_embeddings: A list of paper embeddings following the separate strategy
    """
    separate_embeddings = []

    for title_embedding, avg_embedding in zip(title_embeddings, average_abstract_embeddings):
        mean = np.mean([avg_embedding, title_embedding], axis=0)
        separate_embeddings.append(mean)

    return separate_embeddings


def get_average_sentences_embedding(sentences, model=embedder):
    """
    Calculate average embedding for a list of sentences.
    
    :param sentences: A list of sentences.
    :param model: The embedder model (Sentence-BERT)
    
    :return The average embedding.
    """
    embeddings = model.encode(sentences)
    return np.mean(embeddings, axis=0)


def calculate_average_sbert_embeddings_abstract_and_title(data, strategy="merge"):
    """
    A convinience function combining both embedding stratgies into a single function.
    
    :param data: The papers dataframe
    :param strategy: The embedding strategy to employ.
    
    :return embeddings: The calculated paper embeddings following the chosen strategy.
    """
    title_embeddings = data.title_embeddings
    abstract_embedding_batches = data.abstract_embedding_batches
    average_abstract_embeddings = data.average_abstract_embeddings

    if strategy == "merge":
         embeddings = create_merged_sbert_embeddings(title_embeddings, abstract_embedding_batches)
    elif strategy == "separate":
        embeddings = create_separate_sbert_embeddings(title_embeddings, average_abstract_embeddings)
    else:
        print("No or wrong strategy is used! Using the 'merge' strategy instead.")
        embeddings = create_merged_sbert_embeddings(title_embeddings, abstract_embedding_batches)

    return embeddings
