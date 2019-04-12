# Master NoSQL databases

## Elasticsearch queries

### Simple queries

Simple queries can be done directly using the URL to match text in specific fields, or avoid text in specific fields (need to use `%20` instead of spaces to avoid errors):

~~~
http://localhost:9200/movies2/_search?q=fields.actors:Harrison+Ford%20AND%20fields.plot:Jones
~~~

Naturally, this can also be done using `curl` instead of the browser, e.g. :

~~~shell
curl 'http://localhost:9200/movies2/_search?q=fields.actors:Harrison+Ford%20AND%20fields.plot:Jones' | python -m json.tool | less
~~~


<br>


### More advanced queries

* More complex Elasticsearch queries can be written in a **JSON format** and sent using `curl`.

Request body:

~~~json
{
    "query":{
        "match":{
            "fields.title":"Star Wars"
        }
    }
}
~~~

Request sending:

~~~shell
curl -XGET -H "Content-Type: application/json" 'localhost:9200/movies2/movie/_search?pretty' -d @query1
~~~


* Requests can also use other operations than simple matching of text values, such as using a range of values, or filtering the results.

~~~json
{
    "query": {
        "bool":{
            "must": {"match": {"fields.directors": "J.J. Abrams"}},
            "should": {"range": {"fields.rating": {"gte": 5}}},
            "filter": {"range": {"fields.release_date":
                { "from": "2010-01-01", "to": "2015-12-31"}}}
}}}
~~~


<br>


### Aggregates

* Aggregates can be computed using the `aggs` key instead of the `query` key. The following query computes a count of movies for each year (also outputs the documents taken as input of the aggregate):

~~~json
{
    "aggs": {
        "nb_per_year": {
            "terms": {"field": "fields.year"}
        }
    }
}
~~~

* Queries and aggregates can be chained in the following way:

~~~json
{
    "query": {
        "match_phrase": {"fields.directors": "George Lucas"}
    },
    "aggs": {
        "average_rating": {
            "avg": {"field": "field.rating"}
        },
        "average_rank": {
            "avg": {"field": "fields.rank"}
        }
    }
}
~~~