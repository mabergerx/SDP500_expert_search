from Functions.loaders import embedder
from Functions.field_retrieval import get_authors_by_id
from Functions.relevancy_checkers import check_if_author_relevant
from Functions.distance_functions import dist2sim

from sklearn.preprocessing import normalize
import numpy as np
import time

def get_most_similar_ids(query, index, k=10, tfidf_classifier=None):
    """
    Given a query, return most similar papers from the specified FAISS index.

    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of papers to retrieve
    tfidf_classifier (obj): Instance of the sklearn LSI classifier

    Returns:
    idxs (list): retrieved paper ids
    dists (list): cosine distances from the retrieved papers to the query
    """
    # First, embed the query, normalize the vector and convert to float32

    if tfidf_classifier:
        query_emb = tfidf_classifier.transform([query])[0]
        normalized_query = np.float32([query_emb])[0]
    else:
        query_emb = embedder.encode([query])[0]
        normalized_query = np.float32(normalize([query_emb])[0])

    assert type(normalized_query[0]).__name__ == 'float32'

    #Next, run the index search

    dists, idxs = index.search(np.array([normalized_query]), k)

    return idxs[0], dist2sim(dists[0])

def retrieve_results(query, index, k=10, verbose=False, tfidf=False):
    """
    (NOT USED) Given a query, return most similar papers from the specified FAISS index.
    Also prunes the resulting papers by filtering out papers whose authors do not have tags.

    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of papers to retrieve
    verbose (bool): Whether to output the debugging information or not
    tfidf (bool): Whether the tf-idf embeddings are used for retrieval instead of SBERT.

    Returns:
    pruned (list): pruned list of most similar papers to the query
    """
    initial_retrieval = k*5
    s = time.time()
    if tfidf:
        most_similar_raw = get_most_similar_ids(query, index, initial_retrieval, tfidf_clf)
    else:
        most_similar_raw = get_most_similar_ids(query, index, initial_retrieval)
        print("MSR:", most_similar_raw)
    s1 = time.time()
    pruned = prune_results_for_authors_wo_tags(most_similar_raw, query, k)
    s2 = time.time()
    if verbose:
        print(f"Full search execution time: {time.time() - s} seconds")
        print(f"from which {s1-s} s. in the search and {s2 - s1} s. in the pruning.")
        print("===")
        print("Pruned IDS, sorted by similarity:")
        print(pruned[0])
        print('Similarity scores:')
        print(pruned[1])
    return pruned

def retrieve_results_average(query, index, k=10, verbose=False, tfidf=False):
    """
    (NOT USED) Given a query, return most similar papers from the specified FAISS index.
    Also prunes the resulting papers by filtering out papers whose authors do not have tags.
    This uses the average paper representations per author.

    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of papers to retrieve
    verbose (bool): Whether to output the debugging information or not
    tfidf (bool): Whether the tf-idf embeddings are used for retrieval instead of SBERT.

    Returns:
    pruned (list): pruned list of most similar papers to the query
    """
    initial_retrieval = k*5
    s = time.time()
    if tfidf:
        most_similar_raw = get_most_similar_ids(query, index, initial_retrieval, tfidf_clf)
    else:
        most_similar_raw = get_most_similar_ids(query, index, initial_retrieval)
    s1 = time.time()
    pruned = prune_results_for_authors_wo_tags_average(most_similar_raw, query, k)
    s2 = time.time()
    if verbose:
        print(f"Full search execution time: {time.time() - s} seconds")
        print(f"from which {s1-s} s. in the search and {s2 - s1} s. in the pruning.")
        print("===")
        print("Pruned author IDS, sorted by similarity:")
        print(pruned[0])
        print('Similarity scores:')
        print(pruned[1])
    return pruned


def prune_results_for_authors_wo_tags(results, query, how_many=10):
    """
    (NOT USED) Prunes the retrieved papers by filtering out all the papers whose authors
    either don't have tags in our dataset or just not in our dataset at all. This is needed
    to be able to perform evaluation.

    Parameters:
    query (string): The search query
    results (tuple): The retrieved papers and their distances
    how_many (int): The amount of papers we want to return

    Returns:
    pruned list of most similar papers to the query and the corresponding cosine distances
    """
    ids = results[0]
    distances = results[1]

    relevant_ids = []
    relevant_distances = []
    # For now, I check if the first author is not in the set, I throw the paper away, because I now
    # only look at first author for evaluation. But later if I have another strategy for retrieving author per paper
    # we can change this logic back to "all authors not in the set".
    for rid, rd in zip(ids, distances):
        authors = [a["id"] for a in get_authors_by_id(str(rid))]
        relevancy = [check_if_author_relevant(int(a), query) for a in authors]
        if relevancy[0] != 'Not in the dataset or no tags present!':
            relevant_ids.append(rid)
            relevant_distances.append(rd)

    return relevant_ids[:how_many], relevant_distances[:how_many]


def prune_results_for_authors_wo_tags_average(results, query, how_many=10):
    """
    (NOT USED) Prunes the retrieved papers by filtering out all the papers whose authors
    either don't have tags in our dataset or just not in our dataset at all. This is needed
    to be able to perform evaluation. This uses the average paper representations per author.

    Parameters:
    query (string): The search query
    results (tuple): The retrieved papers and their distances
    how_many (int): The amount of papers we want to return

    Returns:
    pruned list of most similar papers to the query and the corresponding cosine distances
    """
    ids = results[0]
    distances = results[1]

    relevant_ids = []
    relevant_distances = []
    for aid, ad in zip(ids, distances):
        relevancy = check_if_author_relevant(int(aid), query)

        if relevancy != 'Not in the dataset or no tags present!':
            relevant_ids.append(aid)
            relevant_distances.append(ad)

    return relevant_ids[:how_many], relevant_distances[:how_many]