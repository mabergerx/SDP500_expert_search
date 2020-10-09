from Functions.loaders import authors, data
from Functions.relevancy_checkers import check_if_author_relevant, check_if_author_relevant_approximate
import pprint


def retrieve_author_by_id(author_id):
    """
    Retrieve author information by author id.
    authors is the Pandas dataframe with author metadata.

    Parameters:
    author_id (string or int)

    Returns:
    a dataframe row corresponding to the particular author
    """
    return authors[authors.id == int(author_id)]


def get_abstract_by_id(id_):
    """
    Retrieve paper abstract by paper id.
    data is the Pandas dataframe with paper metadata.

    Parameters:
    id_ (string)

    Returns:
    abstract (string)
    """
    return data[data.id == id_].abstract.values[0]


def get_fos_by_id(id_):
    """
    Retrieve paper tags by paper id.
    data is the Pandas dataframe with paper metadata.

    Parameters:
    id_ (string)

    Returns:
    tags (string)
    """
    return data[data.id == id_].fos.values[0]


def get_title_by_id(id_):
    """
    Retrieve paper title by paper id.
    data is the Pandas dataframe with paper metadata.

    Parameters:
    id_ (string)

    Returns:
    title (string)
    """
    return data[data.id == id_].title.values[0]


def get_year_by_id(id_):
    """
    Retrieve paper publication year by paper id.
    data is the Pandas dataframe with paper metadata.

    Parameters:
    id_ (string)

    Returns:
    year (int)
    """
    return data[data.id == id_].year.values[0]


def get_authors_by_id(id_):
    """
    Retrieve paper authors by paper id.
    data is the Pandas dataframe with paper metadata.

    Parameters:
    id_ (string)

    Returns:
    authors (list): A list of author dicts containing their names, ids and (optionally) affiliations
    """
    try:
        return data[data.id == id_].authors.values[0]
    except:
        return []


def get_first_author_by_id(id_):
    """
    Retrieve paper first author by paper id.
    data is the Pandas dataframe with paper metadata.

    Parameters:
    id_ (string)

    Returns:
    author (dict): A single author dictionary containing author metadata
    """
    authors = get_authors_by_id(id_)
    return authors[0]


def retrieve_authorname_by_authorid(author_id):
    """
    Retrieve author's name by author id.
    authors is the Pandas dataframe with author metadata.

    Parameters:
    author_id (string or int)

    Returns:
    abstract (string)
    """
    return authors[authors.id == int(author_id)].name.values[0]


def retrieve_pub_count_by_id(author_id):
    """
    Retrieve author publication count by author id.
    authors is the Pandas dataframe with paper metadata.

    Parameters:
    author_id (string or int)

    Returns:
    pubcount (string)
    """
    return authors[authors.id == int(author_id)].n_pubs.values[0]


def retrieve_cit_count_by_id(author_id):
    """
    Retrieve author citation count by author id.
    authors is the Pandas dataframe with paper metadata.

    Parameters:
    author_id (string)

    Returns:
    citation_count (string)
    """
    return authors[authors.id == int(author_id)].n_citation.values[0]


def retrieve_average_citation_count(author_id):
    pass


def get_information_by_id(id_, query, tfidf=False):
    """
    Print various paper information given a paper id, including relevancy of the paper
    to the query.

    Parameters:
    id_ (string): A paper id
    query (string): The search query used to retrieve this particular paper
    tfidf (bool): Whether the tf-idf embeddings are used for retrieval instead of SBERT.

    Returns:
    - (just prints)
    """
    pprint(f"Title: {get_title_by_id(id_)}")
    print("===")
    pprint(f"Abstract: {get_abstract_by_id(id_)}")
    print("===")
    pprint(f"Tags: {get_fos_by_id(id_)}")
    print("===")
    authors = get_authors_by_id(id_)
    pprint(f"Authors: {authors}")
    first_author = authors[0]
    print("===")
    pprint(f"First author {first_author['name']} relevant: {check_if_author_relevant(int(first_author['id']), query)}")
    print("===")
    pprint(
        f"Approximately relevant: {check_if_author_relevant_approximate(int(first_author['id']), query, tfidf=tfidf)}")


def get_information_by_author_id(aid, query, tfidf=False):
    """
    Print various author information given an author id, including relevancy of the author
    to the query.

    Parameters:
    aid (string): An author id
    query (string): The search query used to retrieve this particular author
    tfidf (bool): Whether the tf-idf embeddings are used for retrieval instead of SBERT.

    Returns:
    - (just prints)
    """
    pprint(f"Name: {retrieve_authorname_by_authorid(aid)}")
    print("===")
    pprint(f"Number of publications: {retrieve_pub_count_by_id(aid)}")
    print("===")
    pprint(f"Number of citations: {retrieve_cit_count_by_id(aid)}")
    print("===")
    pprint(f"Exactly relevant: {check_if_author_relevant(int(aid), query)}")
    print("===")
    pprint(f"Approximately relevant: {check_if_author_relevant_approximate(int(aid), query, tfidf=tfidf)}")
