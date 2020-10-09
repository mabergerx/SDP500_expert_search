from Functions.relevancy_checkers import check_if_author_relevant_approximate, check_if_author_relevant
from Functions.field_retrieval import get_first_author_by_id
from Functions.faiss_index_operations import retrieve_results, retrieve_results_average
from more_itertools import unique_everseen

def get_author_ranking_exact(query, index, k=10, tfidf=False):
    """
    (OBSOLETE) Create a dictionary with author id's mapped to their exact relevancy and their ranking
    in regard to the query.

    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of authors to retrieve
    tfidf (boolean): Whether the tf-idf embeddings are used for retrieval instead of SBERT.

    Returns:
    ranking (dict): Mapping from authors to their query relevancy and rank.

    """
    query = query.lower()
    results = retrieve_results(query, index, k, tfidf=tfidf)
    candidate_papers = results[0]

    # We remove duplicate authors for now, while preserving order (their highest position)
    authors = list(unique_everseen([get_first_author_by_id(str(rid))["id"] for rid in candidate_papers]))
    relevancies = [check_if_author_relevant(int(a), query) for a in authors]

    ranking = {}

    for rank, (author, relevancy) in enumerate(zip(authors, relevancies)):
        if author not in ranking.keys():
            ranking[author] = {"relevancy": relevancy, "rank": rank}
        else:
            continue

    return ranking


def get_author_ranking_approximate(query, index, k=10, similarity_threshold=0.7, tfidf=False):
    """
    (OBSOLETE) Create a dictionary with author id's mapped to their approximate relevancy
     and their ranking in regard to the query.

    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of authors to retrieve
    similarity_threshold (float): The approximate topic query similarity threshold
    tfidf (boolean): Whether the tf-idf embeddings are used for retrieval instead of SBERT.

    Returns:
    ranking (dict): Mapping from authors to their query relevancy and rank.
    """
    query = query.lower()
    results = retrieve_results(query, index, k, tfidf=tfidf)

    candidate_papers = results[0]
    # We remove duplicate authors for now, while preserving order (their highest position)
    authors = list(unique_everseen([get_first_author_by_id(str(rid))["id"] for rid in candidate_papers]))
    relevancies = [check_if_author_relevant_approximate(int(a), query, similarity_threshold, tfidf=tfidf) for a in
                   authors]

    ranking = {}

    for rank, (author, relevancy) in enumerate(zip(authors, relevancies)):
        if author not in ranking.keys():
            ranking[author] = {"relevancy": relevancy, "rank": rank}
        else:
            continue

    return ranking


def get_author_ranking_average_exact(query, index, k=10, tfidf=False):
    """
    (OBSOLETE) Create a dictionary with author id's mapped to their exact relevancy and their ranking
    in regard to the query. This uses the average paper representations per author.

    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of authors to retrieve
    tfidf (boolean): Whether the tf-idf embeddings are used for retrieval instead of SBERT.

    Returns:
    ranking (dict): Mapping from authors to their query relevancy and rank.
    """
    query = query.lower()
    results = retrieve_results_average(query, index, k, tfidf=tfidf)
    candidate_authors = list(unique_everseen(results[0]))

    # We remove duplicate authors for now, while preserving order (their highest position)
    # authors = list(unique_everseen([get_first_author_by_id(str(rid))["id"] for rid in candidate_papers]))
    relevancies = [check_if_author_relevant(int(a), query) for a in candidate_authors]

    ranking = {}

    for rank, (author, relevancy) in enumerate(zip(candidate_authors, relevancies)):
        if author not in ranking.keys():
            ranking[author] = {"relevancy": relevancy, "rank": rank}
        else:
            continue

    return ranking


def get_author_ranking_average_approximate(query, index, k=10, similarity_threshold=0.7, tfidf=False):
    """
    (OBSOLETE) Create a dictionary with author id's mapped to their approximate relevancy and their ranking
    in regard to the query. This uses the average paper representations per author.

    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of authors to retrieve
    similarity_threshold (float): The approximate topic query similarity threshold
    tfidf (boolean): Whether the tf-idf embeddings are used for retrieval instead of SBERT.

    Returns:
    ranking (dict): Mapping from authors to their query relevancy and rank.
    """
    query = query.lower()
    results = retrieve_results_average(query, index, k, tfidf=tfidf)

    candidate_authors = list(unique_everseen(results[0]))
    # We remove duplicate authors for now, while preserving order (their highest position)
    # authors = list(unique_everseen([get_first_author_by_id(str(rid))["id"] for rid in candidate_papers]))
    relevancies = [check_if_author_relevant_approximate(int(a), query, similarity_threshold, tfidf=tfidf) for a in
                   candidate_authors]

    ranking = {}

    for rank, (author, relevancy) in enumerate(zip(candidate_authors, relevancies)):
        if author not in ranking.keys():
            ranking[author] = {"relevancy": relevancy, "rank": rank}
        else:
            continue

    return ranking
