import sys
from pyspark import SparkContext

# The SparkContext handles global parameters, and the reading of files
sc = SparkContext()

# Create a Resilient Distributed Dataset (RDD) from the lines of the file
# This is subject to lazy evaluation, i.e. it is not evaluated 
# (only building the execution graph) until an action occurs
lines = sc.textFile(sys.argv[1])

# A bunch of transformations (lazy) : RDD -> RDD
words = lines.flatMap(lambda line: line.split(' '))
words_with_1 = words.map(lambda word: (word, 1))
word_counts = words_with_1.reduceByKey(lambda count1, count2: count1 + count2)

# Collecting the results is an action (triggers evaluation) : RDD -> list
# This is also added to the execution graph (which is a DAG)
result = word_counts.collect()

for (word, count) in result:
    print(word, count)