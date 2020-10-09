import math
from collections import defaultdict
from Functions.loaders import authors
from Functions.field_retrieval import get_authors_by_id, retrieve_pub_count_by_id, retrieve_authorname_by_authorid, \
    retrieve_cit_count_by_id, get_abstract_by_id, get_fos_by_id, get_title_by_id, get_year_by_id
from Functions.relevancy_checkers import check_if_author_relevant, check_if_author_relevant_approximate
from Functions.faiss_index_operations import get_most_similar_ids
from Functions.retrieve_author_affiliation import get_author_affiliation_infos, get_author_wikidata
import time
from more_itertools import unique_everseen

# ================================================
# This is the most important file in the codebase.
# All the final retrieval logic is happening here.
# ================================================

# AVERAGE_N_PUBS = authors.n_pubs.mean()

def create_score_author_dict(query, retrieved_paper_ids, retrieved_distances, strategy="uniform", normalized=False,
                             average_pub_count=58,
                             normalization_alpha=1, extra_normalization_term=10):
    """
    Create a dictionary where each author gets a score in relation to the query. 
    The author ranking is assembled through a document-centric voting model process: 
    first, for each top retrieved paper, its score is assigned to each of the paper 
    authors following one of the data fusion strategies. Next, all the scores per author
    are aggregated into a mapping of authors to scores. Finally, a combination function (expCombSUM) 
    is applied to all author scores. These scores are returned per author in combination with the papers 
    that contributed to that score (for explainibility sake).
    
    Parameters:
    query (string): The search query
    retrieved_paper_ids (list): The papers that were retrieved from the FAISS index as 
    nearest neighbours for the query
    retrieved_distances (list): The distances from the query for each paper that were retrieved 
    from the FAISS index as nearest neighbours for the query
    strategy (string): The data fusion strategy used for assigning author score per paper
    normalized (bool): Whether normalization should be applied to the scores, boosting less prolific
    authors and "punishing" highly prolific authors
    average_pub_count (int): Average publication count for the authors in our dataset. Used for normalization
    normalization_alpha (int or float): The inverse strength of normalization (higher alpha means less normalization)
    extra_normalization_term (int): Extra normalization damping term, further reduces normalization effect
    
    
    Returns:
    authorship_scores (dict): A mapping between authors and their calculated score in relation to the query.
    """
    def expCombSUM(list_of_scores):
        return sum([math.exp(score) for score in list_of_scores])

    def normalize_score(score, l_pro, average_l=average_pub_count, alpha=normalization_alpha):
        normalized_score = score * math.log(1 + alpha * (average_l / (l_pro + extra_normalization_term)), 2)
        return normalized_score

    scores_per_author = defaultdict(list)
    reasons_per_author = defaultdict(list)
    for pi, score in zip(retrieved_paper_ids, retrieved_distances):
        # Prune only for author that exist in our data.
        authors = [item["id"] for item in get_authors_by_id(str(pi)) if
                   check_if_author_relevant(int(item["id"]), query) != 'Not in the dataset or no tags present!']
        if authors:
            if strategy == "uniform":
                score_per_author = score / len(authors)
                for author in authors:
                    if normalized:
                        pub_count = retrieve_pub_count_by_id(int(author))
                        normalized_score = normalize_score(score_per_author, pub_count)
                        scores_per_author[author].append(normalized_score)
                    else:
                        scores_per_author[author].append(score_per_author)
                    reasons_per_author[author].append({"paper": pi, "score": score})
            elif strategy == "binary":
                score_per_author = score
                for author in authors:
                    if normalized:
                        pub_count = retrieve_pub_count_by_id(int(author))
                        normalized_score = normalize_score(score_per_author, pub_count)
                        scores_per_author[author].append(normalized_score)
                    else:
                        scores_per_author[author].append(score_per_author)
                    reasons_per_author[author].append({"paper": pi, "score": score})
            elif strategy == "descending":
                decay_factor = 1
                for author in authors:
                    if normalized:
                        score_d = score * decay_factor
                        pub_count = retrieve_pub_count_by_id(int(author))
                        normalized_score = normalize_score(score_d, pub_count)
                        scores_per_author[author].append(normalized_score)
                        decay_factor -= 0.2
                    else:
                        scores_per_author[author].append(score * decay_factor)
                        decay_factor -= 0.2
                    reasons_per_author[author].append({"paper": pi, "score": score})
            elif strategy == "parabolic":
                #  TODO: here we did not yet write the normalization code because we do not run it for this config.
                decay_factor = 0.8
                scores_per_author[authors[0]].append(score)
                scores_per_author[authors[-1]].append(score)
                reasons_per_author[authors[0]].append({"paper": pi, "score": score})
                reasons_per_author[authors[-1]].append({"paper": pi, "score": score})
                for author in authors[1:-1]:
                    scores_per_author[author].append(score * decay_factor)
                    decay_factor -= 0.2
                    reasons_per_author[author] = {"paper": pi, "score": score}
                    reasons_per_author[author].append({"paper": pi, "score": score})
        else:
            continue

    authorship_scores = {k: {"score": expCombSUM(v),
                             "reasons": reasons_per_author[k]} for k, v in scores_per_author.items()}

    return authorship_scores


def produce_authors_ranking(authorship_scores):
    """
    Sorts the author-to-score mapping and produces a final author ranking.
    
    Parameters:
    authorship_scores (dict): An unsorted mapping produced by create_score_author_dict()
    
    Returns:
    sortd (list): A list of (author, {score, reasons}) tuples, descendingly sorted by score. 
    """
    sortd = [(k, v) for k, v in sorted(authorship_scores.items(), key=lambda item: item[1]['score'], reverse=True)]
    return sortd


def get_author_ranking_exact_v2(query, index, k=10, tfidf=False, strategy="uniform",
                                normalized=False, norm_alpha=100, extra_term=10):
    """
    Produces an author ranking given a query and adds relevancy flag to the author
    based on the exact topic evaluation criteria. Used for evaluating the system.
    
    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of authors to retrieve
    tfidf (bool): Whether the tf-idf embeddings are used for retrieval instead of SBERT.
    strategy (string): The data fusion strategy used for assigning author score per paper
    normalized (bool): Whether normalization should be applied to the scores, boosting less prolific
    authors and "punishing" highly prolific authors
    norm_alpha (int or float): The inverse strength of normalization (higher alpha means less normalization)
    extra_term (int): Extra normalization damping term, further reduces normalization effect
    
    Returns:
    ranking (dict): A mapping of authors to their retrieved rank and their 
    relevancy in relation to the query
    """
    if tfidf:
        i, d = get_most_similar_ids(query.lower(), index, 100, tfidf_clf)
    else:
        i, d = get_most_similar_ids(query.lower(), index, 100)

    author_score_dict = create_score_author_dict(query, i, d, strategy,
                                                 normalized=normalized, normalization_alpha=norm_alpha,
                                                 extra_normalization_term=extra_term)

    top_n = produce_authors_ranking(author_score_dict)[:k]

    relevancies = [check_if_author_relevant(int(aid), query) for aid, _ in top_n]

    ranking = {}

    for rank, (author, relevancy) in enumerate(zip([a[0] for a in top_n], relevancies)):
        if author not in ranking.keys():
            ranking[author] = {"relevancy": relevancy, "rank": rank}
        else:
            continue

    return ranking


def get_author_ranking_approximate_v2(query, index, k=10, similarity_threshold=0.7, tfidf=False, strategy="uniform",
                                      normalized=False, norm_alpha=100, extra_term=10):
    """
    Produces an author ranking given a query and adds relevancy flag to the author
    based on the approximate topic evaluation criteria. Used for evaluating the system.
    
    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of authors to retrieve
    similarity_threshold (float): The approximate topic query similarity threshold
    tfidf (bool): Whether the tf-idf embeddings are used for retrieval instead of SBERT.
    strategy (string): The data fusion strategy used for assigning author score per paper
    normalized (bool): Whether normalization should be applied to the scores, boosting less prolific
    authors and "punishing" highly prolific authors
    norm_alpha (int or float): The inverse strength of normalization (higher alpha means less normalization)
    extra_term (int): Extra normalization damping term, further reduces normalization effect
    
    Returns:
    ranking (dict): A mapping of authors to their retrieved rank and their 
    relevancy in relation to the query
    """
    if tfidf:
        i, d = get_most_similar_ids(query.lower(), index, 100, tfidf_clf)
    else:
        i, d = get_most_similar_ids(query.lower(), index, 100)

    author_score_dict = create_score_author_dict(query, i, d, strategy,
                                                 normalized=normalized, normalization_alpha=norm_alpha,
                                                 extra_normalization_term=extra_term)

    top_n = produce_authors_ranking(author_score_dict)[:k]

    relevancies = [check_if_author_relevant_approximate(int(aid), query, similarity_threshold, tfidf=tfidf) for aid, _
                   in top_n]

    ranking = {}

    for rank, (author, relevancy) in enumerate(zip([a[0] for a in top_n], relevancies)):
        if author not in ranking.keys():
            ranking[author] = {"relevancy": relevancy, "rank": rank}
        else:
            continue

    return ranking


def retrieve_authors(query, index, k=10, strategy="binary", normalized=False, norm_alpha=100, extra_term=10):
    """
    Produces an author ranking given a query and adds various metadata about the authors.
    This is the main retrieval method of the system. Each author's affiliation is looked up
    from their MAG entry at ma-graph.org, and additional author information is looked up
    through exact name look-up on WikiData. The final, enriched ranking of authors is 
    returned through the API endpoint.
    
    Parameters:
    query (string): The search query
    index (obj): The loaded FAISS index populated by paper embeddings
    k (int): The amount of authors to retrieve
    strategy (string): The data fusion strategy used for assigning author score per paper
    normalized (bool): Whether normalization should be applied to the scores, boosting less prolific
    authors and "punishing" highly prolific authors
    norm_alpha (int or float): The inverse strength of normalization (higher alpha means less normalization)
    extra_term (int): Extra normalization damping term, further reduces normalization effect
    
    Returns:
    enriched_top_n (list): A list of k most relevant authors to the query, where each author is contained within a dictionary
    which was enriched with various additional metadata.
    """
    
    s = time.time()
    if k*10 < 100:
        amount_papers_to_retrieve = 100
    else:
        amount_papers_to_retrieve = k*10

    print("Searching in:", amount_papers_to_retrieve, "papers")

    i, d = get_most_similar_ids(query.lower(), index, amount_papers_to_retrieve)

    # print(time.time() - s, "seconds spend in the FAISS search.")
    # s1 = time.time()
    # print("i:", i)
    # print("d", d)
    author_score_dict = create_score_author_dict(query, i, d, strategy,
                                                 normalized=normalized, normalization_alpha=norm_alpha,
                                                 extra_normalization_term=extra_term)

    # print(time.time() - s1, "seconds spend doing the voting model / data fusion and creating the author to score dict.")
    # s2 = time.time()
    # print("author_score_dict:", author_score_dict)
    top_n = produce_authors_ranking(author_score_dict)[:k]
    # print(time.time() - s2, "seconds spend sorting the author scores.")
    # s3 = time.time()

    def enrich_author_info(aid, extra_info, index):

        def parse_reasons(reasons):

            reasons = list(unique_everseen(reasons))

            return [{'paper': {"id": str(item["paper"]),
                               "title": get_title_by_id(str(item['paper'])),
                               "year": int(get_year_by_id(str(item['paper']))),
                               # "abstract": get_abstract_by_id(str(item['paper'])),
                               "tags": [t["name"] for t in get_fos_by_id(str(item['paper']))],
                               "magPage": f"https://academic.microsoft.com/paper/{item['paper']}",
                               "semanticScholarPage": f"https://api.semanticscholar.org/MAG:{item['paper']}"}, 'score': float(item['score'])} for item in reasons]


        def parse_wikidata(wd):
            cleaned = {}
            if wd == {}:
                return cleaned
            else:
                if wd["wikidata_id"]:
                    cleaned["wikidataId"] = wd["wikidata_id"]
                if wd['google_scholar_link']:
                    cleaned["googleScholarLink"] = wd["google_scholar_link"]
                if wd['occupations'] != ['']:
                    cleaned["occupations"] = list(set(wd["occupations"]))
                if wd['personal_websites']:
                    cleaned["personalWebsites"] = wd["personal_websites"]
                if wd['employers'] != ['']:
                    cleaned["allEmployers"] = list(set(wd["employers"]))
                if wd['educated_at'] != ['']:
                    cleaned['educatedAt'] = list(set(wd["educated_at"]))
                if wd['age']:
                    cleaned["age"] = wd["age"]
                if wd['notable_works'] != ['']:
                    cleaned["notableWorks"] = list(set(wd["notable_works"]))
                if wd['awards']:
                    cleaned["receivedAwards"] = list(set(wd['awards']))
                if wd['academic_degree']:
                    cleaned['academicDegree'] = wd['academic_degree']
                if wd['alive']:
                    cleaned['alive'] = wd['alive']
            return cleaned

        name = retrieve_authorname_by_authorid(aid)
        n_pubs = retrieve_pub_count_by_id(aid)
        n_cits = retrieve_cit_count_by_id(aid)
        affiliation_info = get_author_affiliation_infos(aid)
        wikidata = parse_wikidata(get_author_wikidata(aid))
        reasons = parse_reasons(extra_info['reasons'])
        try:
            country = affiliation_info["country"]
        except KeyError:
            country = "Unknown"
        mag_profile_link = f"https://academic.microsoft.com/author/{aid}"
        return {"name": name, "nPublications": int(n_pubs),
                "nCitations": int(n_cits), "country": country, "id": aid, "magProfile": mag_profile_link,
                "rank": index, "affiliation": affiliation_info, "wikidata": wikidata, "paperReasons": reasons}

    enriched_top_n = [enrich_author_info(aid, extra_info, index) for index, (aid, extra_info) in enumerate(top_n)]

    # print(time.time() - s3, "seconds spend enriching the retrieved authors with extra info.")

    return enriched_top_n

