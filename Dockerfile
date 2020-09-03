FROM python:3.8-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install libgraphviz-dev graphviz --assume-yes

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


ADD . /polls
WORKDIR /polls
RUN pip install -e .