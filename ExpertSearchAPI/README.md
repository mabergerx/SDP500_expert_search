# ExpertSearchAPI
This repository presents the API that allows searching for expert authors given a query, based on MSc Thesis research performed at the University of Amsterdam Information Systems program and the SDP 2020 workshop paper "Effective Distributed Representations for Academic Expert Search" resulting from this research. This system has been developed in collaboration with [Zeta Alpha Vector](https://www.zeta-alpha.com), an Amsterdam based Deep Learning Enterprise Search R&D Lab.


## What is this repository?
In this repository, we only expose the API side of the system. Algorithms and the main research code involved in creating this system is not included in this repository and will be made available separately. The paper embeddings, the paper metadata, and the author metadata that are needed for the APi to work are also not included here due to their size. This data is available at https://doi.org/10.5281/zenodo.4075181.

This repository contains a Dockerfile for easy deployment. The Docker image downloads the data from the Zeta Alpha S3 expert-search bucket and assumes AWS credentials are set as environment variables. The API is built using [FastAPI](https://fastapi.tiangolo.com/) which uses [uvicorn](https://www.uvicorn.org/) as the underlying ASGI server.


## Data for the system
This system uses the [Open Academic Graph Data](https://www.openacademic.ai/oag/). Various multiple filtering criteria and sampling was applied to arrive at the CS/AI only related paper dataset of around 130.000 papers (the process is described thoroughly in my Thesis) and 68.000 authors. The paper representations are made available via populated [FAISS](https://github.com/facebookresearch/faiss) indeces. The author and paper metadata are made available via CSV files, as well as the populated and ready-to-go FAISS index files.


## Brief system introduction
The designed expert retieval system retrieves experts by using a document-centric voting model. The documents in question are the academic papers and the experts are authors of the papers.


The papers are represented via variously aggregated sentence embeddings which are produced using [Sentence-BERT](https://github.com/UKPLab/sentence-transformers). When the user enters a query, the query is first cast into a vector representation and afterwards, the system performs nearest neighbour vector search through the papers within a FAISS index to find papers that are most similar to the query. Once the top papers are retrieved, a voting process is performed on those papers to produce an author ranking, which is first enriched by various author metadata and then returned to the user.

## Running the API
Using [Docker](https://www.docker.com/), setting up this API is quite easy. 

1) Clone this repository and cd into it:

   `git clone https://github.com/mabergerx/ExpertSearchAPI.git && cd ExpertSearchAPI`

2) Build the Docker image and tag it (it can take a while because the data is being downloaded to the image from AWS and installing [torch](https://pytorch.org/):  
   
   `docker build -t expertapi .`
  
4) Once the image is built, run the container while exposing the defined port (default port 80). This, once again may take some time because the container has to download the Sentence-BERT model checkpoint and also load the FAISS index:

   `docker run -p 80:80 expertapi`
   
5) Now, browse to http://0.0.0.0/docs#/ to access the Swagger documentation for the API. There, you can try out the endpoints and get the corresponding `curl` statements. 


## Example usage

The API exposes 1 endpoint which allows users to submit a query to the system and the number of experts they would like to retrieve. 

- **Endpoint 1:** /authors/get_authors

  **Query parameters:** 
  
  *query*: The search query. 
  
  *n_of_authors*: Number of experts to retrieve. *Default = 10*  

This endpoint will return the following data format:

```
{
  "authors": [
    {
      "name": "Yann LeCun",
      "nPublications": 289,
      "nCitations": 45433,
      "country": "United States",
      "id": "2053214915",
      "magProfile": "https://academic.microsoft.com/author/2053214915",
      "rank": 0,
      "affiliation": {
        "gridPage": "http://www.grid.ac/institutes/grid.137628.9",
        "city": "New York",
        "country": "United States",
        "name": "New York University",
        "homepage": "http://www.nyu.edu/",
        "additionalWebsite": "http://en.wikipedia.org/wiki/New_York_University"
      },
      "wikidata": {
        "wikidataId": "Q3571662",
        "googleScholarLink": "https://scholar.google.com/citations?user=WLN3QrAAAAAJ",
        "occupations": [
          "computer scientist",
          "artificial intelligence researcher",
          "software engineer",
          "electrical engineer"
        ],
        "personalWebsites": "http://yann.lecun.com",
        "allEmployers": [
          "Collège de France",
          "Facebook, Inc.",
          "New York University",
          "Bell Labs"
        ],
        "educatedAt": [
          "ESIEE Paris",
          "University of Toronto",
          "University of Paris VI: Pierre-and-Marie-Curie University"
        ],
        "receivedAwards": [
          "honorary doctor of the École polytechnique fédérale de Lausanne",
          "PAMI Distinguished Researcher Award",
          "Turing Award",
          "Harold Pender Award",
          "AAAI Fellow"
        ],
        "alive": true
      },
      "paperReasons": [
        {
          "paper": {
            "id": "2015861736",
            "title": "Convolutional networks and applications in vision",
            "year": 2010,
            "tags": [
              "Pooling",
              "Visualization",
              "Artificial neural network",
              "Unsupervised learning",
              "Feature extraction",
              "Architecture",
              "Computer science",
              "Machine learning",
              "Mobile robot",
              "Artificial intelligence",
              "Visual perception"
            ],
            "magPage": "https://academic.microsoft.com/paper/2015861736",
            "semanticScholarPage": "https://api.semanticscholar.org/MAG:2015861736"
          },
          "score": 0.6725553274154663
        },
        {
          "paper": {
            "id": "2413904250",
            "title": "Very Deep Convolutional Networks for Natural Language Processing.",
            "year": 2016,
            "tags": [
              "Machine learning",
              "Pooling",
              "Artificial intelligence",
              "Natural language processing",
              "Architecture",
              "Computer science",
              "Deep learning",
              "Convolutional neural network",
              "Recurrent neural network",
              "Text processing"
            ],
            "magPage": "https://academic.microsoft.com/paper/2413904250",
            "semanticScholarPage": "https://api.semanticscholar.org/MAG:2413904250"
          },
          "score": 0.6263455748558044
        },
        {
          "paper": {
            "id": "2198724430",
            "title": "Very deep multilingual convolutional neural networks for LVCSR",
            "year": 2016,
            "tags": [
              "Word error rate",
              "Artificial intelligence",
              "Network architecture",
              "Pooling",
              "Natural language processing",
              "Machine learning",
              "Pattern recognition",
              "Artificial neural network",
              "Deep learning",
              "Computer science",
              "Vocabulary",
              "Convolutional neural network",
              "Architecture"
            ],
            "magPage": "https://academic.microsoft.com/paper/2198724430",
            "semanticScholarPage": "https://api.semanticscholar.org/MAG:2198724430"
          },
          "score": 0.6140035390853882
        },
        {
          "paper": {
            "id": "2116456623",
            "title": "Convolutional neural networks applied to house numbers digit classification",
            "year": 2012,
            "tags": [
              "Machine learning",
              "Feature learning",
              "Feature (computer vision)",
              "Feature extraction",
              "Deep learning",
              "Architecture",
              "Artificial neural network",
              "Convolutional neural network",
              "Neocognitron",
              "Computer science",
              "Artificial intelligence",
              "Pattern recognition"
            ],
            "magPage": "https://academic.microsoft.com/paper/2116456623",
            "semanticScholarPage": "https://api.semanticscholar.org/MAG:2116456623"
          },
          "score": 0.5944952368736267
        }
      ]
    }
  ]
}
```

