# ==========================================================================

# These functions are used for evaluation of the proposed retrieval systems.
# The binary evaluation metrics are:
#               Mean Reciprocal Rank (MRR)
#               Mean Average Precision (MAP)
#               Precision @ N (P@N)
# The gain-based evaluation metric is:
#               Normalized Discounted Cumulative Gain (nDCG)
#
# (c) Mark Berger

# ==========================================================================

import numpy as np
import math


def mean_reciprocal_rank(results):
    """
    Calculate the Mean Reciprocal Rank. The reciprocal rank of a query response
    is the multiplicative inverse of the rank of the first correct answer.

    :param results: Multiple rankings produced by the system for different queries,
    aggregated together.
    :return mrr: The mean reciprocal rank of the system.
    """
    partial_ranks = []

    for result in results:
        sortd = sorted(result.items(), key=lambda item: item[1]['rank'])

        for s in sortd:
            if s[1]['relevancy'] == True:
                # We had to do rank from 1 on instead of 0 on because of the 1 / rank formula.
                partial_ranks.append(1 / (s[1]['rank'] + 1))
                break

    mrr = np.around(np.mean(partial_ranks), decimals=3)

    return mrr


def mean_average_precision(results):
    """
    Calculate the Mean Average Precision. The average precision of a query
    is the mean of the precision scores after each relevant document is retrieved
    (at each position).

    :param results: Multiple rankings produced by the system for different queries,
    aggregated together.
    :return mrr: The mean average precision of the system.
    """
    average_precision_scores = []

    for result in results:
        sortd = sorted(result.items(), key=lambda item: item[1]['rank'])

        average_precison_partials_list = []
        current_sublist_size = 0
        relevant_found = 0

        for s in sortd:
            if s[1]['relevancy'] == True:
                current_sublist_size += 1
                relevant_found += 1
                average_precision_partial = relevant_found / current_sublist_size
                average_precison_partials_list.append(average_precision_partial)
            else:
                current_sublist_size += 1

        average_precision = np.sum(average_precison_partials_list) / len(sortd)
        average_precision_scores.append(average_precision)

    mapr = np.around(np.mean(average_precision_scores), decimals=3)

    return mapr


def mean_precision_at_n(results, n=5):
    """
    Calculate Precision@N. Mean precision @ N corresponds to the number of
    relevant results among the top N documents.

    :param results: Multiple rankings produced by the system for different queries,
    aggregated together.
    :return mrr: The precision @ N of the system.
    """
    average_precision_scores = []

    for result in results:

        sortd = sorted(result.items(), key=lambda item: item[1]['rank'])

        correct = 0

        for s in sortd[:n]:
            if s[1]['relevancy'] == True:
                correct += 1

        average_precision_scores.append(correct / n)

    mpan = np.around(np.mean(average_precision_scores), decimals=3)

    return mpan


def ideal_dcg(query, rankings, n=10):
    """
    Calculate the ideal DCG for a query at N.
    The premise of DCG is that highly relevant documents appearing lower
    in a search result list should be penalized as the graded relevance value is reduced
    logarithmically proportional to the position of the result. This function calculates
    what the ideal DCG would be for a given query.

    :param query: The search query.
    :param rankings: A pre-calculated dictionary of queries with relevance labels (available on request).
    :param n: The position through which to calculate the DCG.
    :return idcg: The ideal DCG through N for a given query.
    """
    ranking = rankings[query.lower()][:n]
    idcg = sum([r["label"]/math.log((i+1)+1) for i, r in enumerate(ranking)])
    return idcg


def actual_dcg(result, query, author_rankings, n=10):
    """
    Calculate the actual DCG for a query at N.
    The premise of DCG is that highly relevant documents appearing lower
    in a search result list should be penalized as the graded relevance value is reduced
    logarithmically proportional to the position of the result. This function calculates
    what the actual DCG is for a given query.

    :param query: The search query.
    :param result: The result produced by the retrieval system.
    :param author_rankings: A pre-calculated dictionary of authors rankings with relevance labels (available on request).
    :param n: The position through which to calculate the DCG.
    :return dcg: The actual DCG through N for a given query.
    """
    sortd = sorted(result.items(), key=lambda item: item[1]['rank'])[:n]
    labels = []
    for author_id, v in sortd:
        if query.lower() in author_rankings[author_id]:
            label = author_rankings[author_id][query.lower()]
            labels.append(label)
        else:
            labels.append(0)

    dcg = sum([l / math.log((i + 1) + 1) for i, l in enumerate(labels)])

    return dcg


def normalized_discounted_cumulative_gain(query, result, rankings, author_rankings, n=10):
    """
    Calculate the normalized DCG for a query at N, to standardize the DCG calculation among
    queries with different result lengths.
    The premise of DCG is that highly relevant documents appearing lower
    in a search result list should be penalized as the graded relevance value is reduced
    logarithmically proportional to the position of the result. This function calculates
    what the normalized DCG would be for a given query.

    :param query: The search query.
    :param result: The result produced by the retrieval system.
    :param rankings: A pre-calculated dictionary of queries with relevance labels (available on request).
    :param author_rankings: A pre-calculated dictionary of authors rankings with relevance labels (available on request).
    :param n: The position through which to calculate the DCG.
    :return dcg: The actual DCG through N for a given query.
    """
    query = query.lower()
    idcg = ideal_dcg(query, rankings, n)
    dcg = actual_dcg(result, query, author_rankings, n)
    return dcg/idcg


def average_normalized_discounted_cumulative_gain(queries, results, rankings, author_rankings, n=10):
    """
    Calculate the average normalized DCG for a set of queries at N.
    The premise of DCG is that highly relevant documents appearing lower
    in a search result list should be penalized as the graded relevance value is reduced
    logarithmically proportional to the position of the result. This function calculates
    what the normalized DCG would be for a given query.

    :param queries: The search queries.
    :param results: The results produced by the retrieval system for the set of test queries.
    :param rankings: A pre-calculated dictionary of queries with relevance labels (available on request).
    :param author_rankings: A pre-calculated dictionary of authors rankings with relevance labels (available on request).
    :param n: The position through which to calculate the DCG.
    :return dcg: The actual DCG through N for a given query.
    """
    scores = []
    for q, r in zip(queries, results):
        score = normalized_discounted_cumulative_gain(q, r, rankings, author_rankings, n)
        scores.append(score)
    return f"{np.around(np.mean(scores), decimals=2)}"