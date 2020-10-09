from Functions.loaders import load_relevant_index
from Functions.re_ranking import retrieve_authors

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

expertsearch_app = FastAPI()

expertsearch_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

index = load_relevant_index("separate_sbert")
print(f"Loaded the Faiss index with a total of {index.ntotal} embeddings!")
# query = "cluster analysis"
# print(retrieve_authors(query, index))


#ENDPOINT 1: USERS ARTIST (TOP + RELATED)
@expertsearch_app.get("/authors/get_authors")
async def get_authors_endpoint(query: str, n_of_authors: int = 10):
    return {"authors": retrieve_authors(query, index, k=n_of_authors)}