# import requests
# import rdflib
import pandas as pd
from Functions.loaders import authors
import ast


# =================================================================
# Commendted code here is not deleted on purpose because
# it allows looking up affiliation info for new authors by making
# an API call to the MAG graph instead of looking it up 
# directly from our data. In case new authors get added to the data.
# =================================================================


def load_grid_data(grid_path="Data/grid.csv"):
    """
    Load the GRID affiliation data.
    
    Parameters:
    grid_path (string): Path to the GRID data file.
    
    Returns:
    Pandas dataframe with the GRID data.
    """
    return pd.read_csv(grid_path)


# grid = load_grid_data()
# print(grid.head())
#
# def get_authors_affiliation_link(author_id):
#     try:
#         r = requests.get(f'http://ma-graph.org/entity/{author_id}')
#         graph = rdflib.Graph()
#         graph.parse(data=r.text)
#         for s, p, o in graph:
#             if "memberOf" in p:
#                 return o.toPython()
#     except:
#         return "Unknown"
#
#
# def get_affiliation_info(affiliation_link, grid_data=grid):
#     r_aff = requests.get(affiliation_link)
#     graph = rdflib.Graph()
#     graph.parse(data=r_aff.text)
#     infos = {}
#     for s, p, o in graph:
#         if "name" in p:
#             infos["name"] = o.toPython()
#         elif "homepage" in p:
#             infos["homepage"] = o.toPython()
#         elif "seeAlso" in p:
#             infos["additionalWebsite"] = o.toPython()
#         elif "grid" in p:
#             infos["gridPage"] = o.toPython()
#             grid_id = o.toPython().split("/")[-1]
#             infos["city"] = grid_data[grid_data.ID == grid_id]["City"].values[0]
#             infos["country"] = grid_data[grid_data.ID == grid_id]["Country"].values[0]
#
#     return infos
#
#
# def get_author_affiliation_infos(author_id):
#     link = get_authors_affiliation_link(author_id)
#     if link != "Unknown":
#         return get_affiliation_info(link)
#     else:
#         return {}


def get_author_affiliation_infos(author_id):
    """
    Retrieve author's affiliation info based on author's id.
    
    Parameters:
    author_id (string or int)
    
    Returns:
    A dictionary with the author's affiliation info.
    """
    info = authors[authors.id == int(author_id)]["info"].values[0]
    return ast.literal_eval(info)


def get_author_wikidata(author_id):
    """
    Retrieve author's wikidata info based on author's id.
    
    Parameters:
    author_id (string or int)
    
    Returns:
    A dictionary with the author's wikidata info.
    """
    wikidata = authors[authors.id == int(author_id)]["wikidata"].values[0]
    return ast.literal_eval(wikidata)
