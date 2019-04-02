# Setup input (fake JSON - must contain one real JSON per line)
# wget https://s3-eu-west-1.amazonaws.com/course.oc-static.com/courses/4297166/agents.json


import pyspark

sc = pyspark.SparkContext()

# In Spark Shell, a SparkSession is already available as 'spark'
spark = pyspark.sql.session.SparkSession()

# Read the input file into a DataFrame
# DataFrames can store structured data in a distributed fashion
agents = spark.read.json("input/agents.json")
# The data format is automatically inferred, but the data is not loaded yet
print(agents)

# We can filter the DataFrame, like SQL WHERE conditions
french_agents = agents.filter(agents.country_name == "France")
# `filter` is a transformation, hence subject to lazy evaluation
print(french_agents)
# Real evaluation requires an action
print(french_agents.count())
# Taking the first element is also an action
agent = french_agents.first()

# Individual elements of a DataFrame have a Row type
print(agent)
# Column values are accessible as attributes
print(agent.country_name, agent.id)

# The DataFrame API is designed as an Object-Relational Mapping
# We can hence chain the SQL requests, and the following lines are equivalent
print(
    agents.filter(agents.country_name == "France") \
          .filter(agents.latitude < 0) \
          .count()
)
print(
    agents.filter((agents.country_name == "France")
                  & (agents.latitude < 0)) \
          .count()
)

# DataFrame visualization using `show` is also an action
agents.limit(5).show()

# Pure SQL is also available, after creating a view of a DataFrame
agents.createTempView("agents_table")
# This should work, just need to configure Hive
spark.sql("SELECT * FROM agents_table ORDER BY id DESC LIMIT 10").show()

# DataFrame can also be stored in cache using persistence
agents.persist()

# DataFrames can easily be converted to RDD
agents.rdd.filter(lambda row: row.country_name == "France").count()
# ... and conversely, for a structured RDD (composed of Row objects)
from pyspark.sql import Row
rdd = sc.parallelize([Row(name="Alice"), Row(name="Bob")])
people = spark.createDataFrame(rdd)