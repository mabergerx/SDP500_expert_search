# Effective Distributed Representations for Academic Expert Search

This repository contains (partial) code that was used in conducting research for the "Effective Distributed Representations for Academic Expert Search" paper to appear at the [SDP 2020 workshop @ EMNLP 20202](https://ornlcda.github.io/SDProc/) by Mark Berger, Jakub Zavrel and Paul Groth.


## Disclaimer

The SDP 2020 paper was written and submitted as a result of the MSc thesis project by Mark Berger. Due to their specificity to the scope of the conducted thesis project, some parts of the processes referenced in the paper are not verbosely presented in this repository, such as the explicit code for the creation and population of the FAISS indexes, and the experiments we performed before arriving at the baseline BERT and GloVe embeddings. However, with the provided datasets and the populated and ready-to-go FAISS indexes, the presented thought process in the notebooks, and the final expert search API, we believe future visitors will be able to re-use our data and ideas to conduct new research.

## Structure

The repository is structured in the following way:

The **Notebooks** directory contains Jupyter notebooks concerning our work process around preparing and embedding the papers and obtaining author metadata. Moreover, the Jupyter notebook at **Notebooks/Embedding_and_retrieval/Ranking_complete.ipynb** can be considered as the main logic of the produced expert search system and contains most of the processes explained in the paper. This file, however, can better be accessed and read through the **ExpertSearchAPI/API/Functions/re_ranking.py** file, where each function is documented and explained.

The **Utility** directory contains fully documented Python scripts containing the data preprocessing, data alignment, custom embedding, and evaluation functions.
Users wanting to have a good starting point to re-use our ideas should look at this directory for clearly documented methodologies we used. Note however that the file **ExpertSearchAPI/API/Functions/re_ranking.py** contains all of the voting model, data fusion and actual retrieval logic that we used in our research and our final system, and is also a very good overview of our work and a good starting point.



## Data

The accompanying datasets are published and can be accessed at https://doi.org/10.5281/zenodo.4075181. 


## Citing this code & using this data

Please cite the following paper when using this code:
```
**TO APPEAR HERE SOON AFTER THE PUBLICATION**
```


Please cite the following when using the data:

```
@misc{berger2020data,
  doi = {10.5281/ZENODO.4075166},
  url = {https://zenodo.org/record/4075166},
  author = {Berger,  Mark},
  title = {Datasets for Effective Distributed Representations for Academic Expert Search},
  publisher = {Zenodo},
  year = {2020},
  copyright = {Creative Commons Attribution 4.0 International}
}
```
