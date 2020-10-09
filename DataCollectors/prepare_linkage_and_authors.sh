#!/bin/bash

wget https://academicgraphv2.blob.core.windows.net/oag/linkage/paper_linking_pairs.zip
unzip paper_linking_pairs.zip -d data/paper_linking_pairs
rm paper_linking_pairs.zip
gsutil cp -r data/paper_linking_pairs gs://noobs-ml/sem-search/paper_linking_pairs
rm -r data/paper_linking_pairs
wget https://academicgraphv2.blob.core.windows.net/oag/linkage/author_linking_pairs.zip
unzip author_linking_pairs.zip -d data/author_linking_pairs
rm author_linking_pairs.zip
gsutil cp -r data/author_linking_pairs gs://noobs-ml/sem-search/author_linking_pairs
rm -r data/author_linking_pairs

wget https://academicgraphv2.blob.core.windows.net/oag/mag/author/mag_authors_0.zip
unzip mag_authors_0.zip -d data/mag_authors_0
rm mag_authors_0.zip
gsutil cp -r data/mag_authors_0 gs://noobs-ml/sem-search/mag_authors_0
rm -r data/mag_authors_0
wget https://academicgraphv2.blob.core.windows.net/oag/mag/author/mag_authors_1.zip
unzip mag_authors_1.zip -d data/mag_authors_1
rm mag_authors_1.zip
gsutil cp -r data/mag_authors_1 gs://noobs-ml/sem-search/mag_authors_1
rm -r data/mag_authors_1
wget https://academicgraphv2.blob.core.windows.net/oag/mag/author/mag_authors_2.zip
unzip mag_authors_2.zip -d data/mag_authors_2
rm mag_authors_2.zip
gsutil cp -r data/mag_authors_2 gs://noobs-ml/sem-search/mag_authors_2
rm -r data/mag_authors_2

wget https://academicgraphv2.blob.core.windows.net/oag/aminer/author/aminer_authors_0.zip
unzip aminer_authors_0.zip -d data/aminer_authors_0
rm aminer_authors_0.zip
gsutil cp -r data/aminer_authors_0 gs://noobs-ml/sem-search/aminer_authors_0
rm -r data/aminer_authors_0
wget https://academicgraphv2.blob.core.windows.net/oag/aminer/author/aminer_authors_1.zip
unzip aminer_authors_1.zip -d data/aminer_authors_1
rm aminer_authors_1.zip
gsutil cp -r data/aminer_authors_1 gs://noobs-ml/sem-search/aminer_authors_1
rm -r data/aminer_authors_1
wget https://academicgraphv2.blob.core.windows.net/oag/aminer/author/aminer_authors_2.zip
unzip aminer_authors_2.zip -d data/aminer_authors_2
rm aminer_authors_2.zip
gsutil cp -r data/aminer_authors_2 gs://noobs-ml/sem-search/aminer_authors_2
rm -r data/aminer_authors_2
wget https://academicgraphv2.blob.core.windows.net/oag/aminer/author/aminer_authors_3.zip
unzip aminer_authors_3.zip -d data/aminer_authors_3
rm aminer_authors_3.zip
gsutil cp -r data/aminer_authors_3 gs://noobs-ml/sem-search/aminer_authors_3
rm -r data/aminer_authors_3