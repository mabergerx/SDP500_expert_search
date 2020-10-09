from Functions.distance_functions import calculate_distances_from_query_to_fos
from Functions.loaders import authors

import ast

def retrieve_author_tags(author_id):
    """
    Retrieve the author's tags given their author id.
    
    Parameters:
    author_id (string or int)
    
    Returns:
    a list of author's tags
    """
    try:
        return ast.literal_eval(authors[authors.id == author_id].tags.values[0])
    except:
        return {}

def check_if_author_relevant(author_id, query):
    """
    Check whether the author is relevant to the search query based on their tags.
    
    Parameters:
    author_id (string or int)
    query (string): The search query used to retrieve this particular author
    
    Returns:
    boolean based on the presence of the query in the author's tags; 
    string if the author is not in the dataset or has no tags
    """
    query = query.lower()
    tags = [t['t'].lower() for t in retrieve_author_tags(author_id)]

    if tags:
        if query in tags:
            return True
        else:
            return False
    else:
        return "Not in the dataset or no tags present!"

def check_if_author_relevant_approximate(author_id, query, similarity_threshold=0.7, tfidf=False):
    """
    Check whether the author is relevant to the search query based on their tags
    using the approximate similarity-based strategy.
    
    Parameters:
    author_id (string or int)
    query (string): The search query used to retrieve this particular author
    similarity_threshold (float): The approximate topic query similarity threshold
    tfidf (boolean): Whether the tf-idf embeddings are used for retrieval instead of SBERT.
    
    Returns:
    boolean based on the presence of a tag in the author's tag list 
    that is sifficiently similar to the query
    """
    query = query.lower()
    tags = [t['t'].lower() for t in retrieve_author_tags(author_id)]
    if tfidf:
        distances = calculate_distances_from_query_to_fos(query, tags, tfidf_clf)
    else:
        distances = calculate_distances_from_query_to_fos(query, tags)
    similar = [d for d in distances if d[1] > similarity_threshold]\
    
    if similar:
        return True
    else:
        return False
