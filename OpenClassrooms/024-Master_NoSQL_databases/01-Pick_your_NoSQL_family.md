# Master NoSQL databases

## Pick your NoSQL family

### What is NoSQL

* From *non-SQL* to **Not Only SQL**
* Relax some contraints of relational databases for better **horizontal scaling**, **availability** and **simplicity of design**
* Lower level query language
* More flexible schemes


<br>


### Key-value

![Key-value scheme](pictures/nosql_key_value.png)

* Acts like a huge **distributed hash table**
* The **key** uniquely identifies the data point
* The **value** can contain anything. This means **no scheme, no structure, no query language**.
* Only CRUD operations
* Appropriate to read/manipulate specific values knowing the keys
* Examples: *Redis, Memcached, Azure Cosmos DB, SimpleDB*
* Applications: *real-time fraud detection, IoT, e-commerce, cache management, quick transactions, log files, chat*


<br>


### Column-oriented

![Column-oriented scheme](pictures/nosql_column_oriented.png)

* Instead of storing in lines (1 data point = 1 line), **store in columns and distribute the attributes**
* Very efficient to perform statistics and aggregates, and generally huge analytical computations: **there's no more need to process useless information (the other columns)**, which can dramatically increase the speed of computation.
* Much less efficient than key-value solutions to manipulate specific data points
* Examples: *BigTable, HBase, Spark SQL, ElasticSearch*
* Applications: *statistics, large scale reporting*


<br>


### Document-oriented

![Document-oriented scheme](pictures/nosql_document_oriented.png)

* The data is stored in **documents that are indexed using a key-value principle**. Documents store information using fields and complex structures (types, lists, nesting).
* While in relational databases every record in a table has the same sequence of fields, **documents in a collection may have fields that are completely different**.
* The database also offers a query system to **retrieve documents based on their contents**.
* Examples: *MongoDB, CouchBase, DynamoDB, Cassandra*
* Applications: *content management, complex events collection, user history management on social networks*


<br>


### Graph

![Graph scheme](pictures/nosql_graph.png)

* The data is stored in a graph: **nodes, edges, node properties, edge properties**
* Requests are specific to the graph framework: path algorithms, propagation, aggregation, recommandation.
* Data distribution across a cluster is not trivial
* Very efficient to address correlations between elements, and more generally when the underlying data can be modeled using a graph
* Examples: *Neo4j, OrientDB, FlockDB*
* Applications: *social networks, infrastructure networks, social web*