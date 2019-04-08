# Master NoSQL databases

## Choose your NoSQL database

### Criteria

* **Cost** - examine professional versions to see the associated services - the infrastructure cost should not vary too much
* **Consistency** of the data - depending on the application and the need for up-to-date data
* **Availability** of the data - depending on the application and the need for low latency (when updating, not inserting)
* **Query language** - expressivity, training cost and online support
* **Functionalities** - depending on the application and the precise needs (e.g. data mining, real-time, graphs, etc)


<br>


### Specify your needs

Use a **multicriteria matrix** to evaluate the solutions regarding your needs and the various criteria. Give each criterion a weight (based on your needs), so that all weights sum to the number of criteria (e.g. 5). Evaluate the solutions with respect to each criterion and your needs, but regardless of the weights. Find the final note of each solution by taking the weighted sum. Pick the best solution, enjoy.


<br>


### Check DB-Engines

[DB-Engines](https://db-engines.com/en/ranking_trend) gives a ranking of many databases' popularity level (based e.g. on StackOverflow), as well as a lot of characteristics for each. Remember that giving up on a very good solution with no online presence, to adopt a good solution that is very popular, may be a wise choice for the sake of development and debugging.

*MongoDB* is very popular among developers, thanks to its powerful language and its easy integration into any application managing documents or objects.

*Cassandra* remains popular, but stagnating - its SQL-inspired language is tempting, but the associated constraints can be disappointing. Cassandra is still a very good solution in terms of elasticity, latency and basic functionalities.

*Redis* is a trendy solution, able to manage real-time cache, and renowned for its simplicity.

*ElasticSearch* is also a trendy solution, able to manage huge volumes of documents, and used a lot for real-time visualization and text analysis.