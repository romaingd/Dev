import sys
from pyspark import SparkContext

# The SparkContext handles global parameters, and the reading of files
sc = SparkContext()

# Create a Resilient Distributed Dataset (RDD) from the lines of the file
# This is subject to lazy evaluation, i.e. it is not evaluated 
# (only building the execution graph) until an action occurs
lines = sc.textFile(sys.argv[1])

# Transformations (lazy)
all_words = lines.flatMap(lambda line: line.split(' '))
different_words = all_words.distinct()

# Persistence allows stores a RDD in cache the first time it is evaluated.
# Without persistence, the two actions below would recompute the same RDD twice
different_words.persist()

# Actions
different_words_count = different_words.count()
first_10_words = different_words.takeOrdered(10)