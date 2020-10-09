from Functions.loaders import embedder
import scipy

def calculate_distances_from_query_to_fos(query, fos_tags, tfidf_classifier=None):
    """
    Calculates the cosine distances between the query and all the author tags.
    Used in approximate relevancy calculation.

    Parameters:
    query (string): The search query
    fos_tags (list of strings): The list of author tags
    tfidf_classifier (obj): Instance of the sklearn LSI classifier

    Returns:
    tag_distance (list of tuples): Tags and their corresponding cosine distance to the query.
    """
    if tfidf_classifier:
        fos_tag_embeddings = tfidf_classifier.transform(fos_tags)
        query_emb = tfidf_classifier.transform([query])[0]
    else:
        fos_tag_embeddings = embedder.encode(fos_tags)
        query_emb = embedder.encode([query])[0]

    distances = [ 1- scipy.spatial.distance.cdist([query_emb], [fos_tag_embedding], 'cosine')[0][0] for fos_tag_embedding in fos_tag_embeddings]

    return [(ft, d) for ft, d in zip(fos_tags, distances)]


def dist2sim(d):
    """
    Converts cosine distance into cosine similarity.

    Parameters:
    d (int): Cosine distance.

    Returns:
    sim (list of tuples): Cosine similarity.
    """
    return 1 - d / 2