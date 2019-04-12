# Master NoSQL databases

## Discover Elasticsearch

### Introduction

Elasticsearch is a NoSQL database with a specific ability of indexing text-oriented documents. Intuitively, **Elasticsearch behaves like a search engine able to store a large amount of documents** and to interrogate them in real-time. The query language also offers interesting opportunities, e.g. computing statistics in real-time.


<br>


### The search engine Lucene

Like all search engines, Lucene is based on **Information Retrieval**, but it has two more properties: it is heavily parametrizable, and it lies at the core of Elasticsearch. How do those work together? Each Elasicsearch query will be transmitted to Lucene instances, which will return results based on **relevance**, i.e. proximity of each document to the request (using a mix of tf-idf and cosine distance). By default, the search will be performed on the entire documents, however it can be refined by targeting specific fields.


<br>


### Elasticsearch: a distributed text search engine

![Elasticsearch architecture](pictures/elasticsearch_lucene.png)

Elasticsearch's architecture is distributed over multiple servers, each of which being a Lucene engine in charge of managing a fraction of the documents, extracting words from the document and preparing word columns. Thus **Elasticsearch is a column-oriented NoSQL database**, where one word makes one column of documents with the weight (~tf-idf) as value.