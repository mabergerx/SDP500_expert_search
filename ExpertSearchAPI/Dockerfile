FROM mesosphere/aws-cli:latest as Downloader
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION=eu-central-1

RUN aws s3 cp --recursive s3://expert-search/Data/ /Data

FROM frolvlad/alpine-miniconda3

COPY ./API /API
COPY requirements.txt /
RUN conda install faiss-cpu -c pytorch
RUN pip install -r /requirements.txt

EXPOSE 80
COPY --from=Downloader /Data /API/Data

#CMD ["cd", "API"]
WORKDIR "/API"
CMD ["uvicorn", "main:expertsearch_app", "--host", "0.0.0.0", "--port", "80"]

#CMD cd API && uvicorn main:expertsearch_app --port 80 --host 0.0.0.0