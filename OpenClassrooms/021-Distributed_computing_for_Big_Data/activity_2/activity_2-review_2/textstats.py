#! /usr/bin/env python3

# to run this program, launch the following command in spark app's root directory:
# ./spark-2.4.0-bin-hadoop2.7/bin/spark-submit ./textstats.py ./iliad.mb.txt
# Most frequent 15-letter word: many-fountained

import re
from sys import argv

from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql import Row
sc = SparkContext('local')
spark = SparkSession(sc)

def load_text(text_path):
    # Regex : remove ,.;:?!"-' at begining and end of each word
    regWord = re.compile(r"^[,.;:?!\"\-']*?([a-z\-]+?)[,.;:?!\"\-']*?$")
    
    # Regex : remove @ and /
    regChars = re.compile(r"[@\/]")
    
    words = sc.textFile(text_path) \
        .flatMap(lambda lines: lines.lower().split()) \
        .map(lambda word: re.sub(regWord, r'\1', word)) \
        .filter(lambda word: word is not None and len(word) > 0) \
        .filter(lambda word: re.search(regChars, word) is None)

    row = Row("word")
    df = words.map(row).toDF()
    
    return df

def most_frequent_word_of_n_chars(words, n):
    return spark.sql("SELECT word AS w, COUNT(word) AS c FROM words_table WHERE length(word) = " + str(n) + " GROUP BY w ORDER BY c DESC LIMIT 1")

# dataframe:
words = load_text(argv[1])
words.createTempView("words_table")

# 1st request
longest = spark.sql("SELECT word as w, length(word) as l FROM words_table ORDER BY l DESC LIMIT 1")

if longest.count() > 0:
    print('Longest word: ' + longest.first()['w'])

# 2nd request
words4 = most_frequent_word_of_n_chars(words, 4)

if words4.count() > 0:
    print('Most frequent 4-letter word: ' + words4.first()['w'])

# 3rd request
words15 = most_frequent_word_of_n_chars(words, 15)

if words15.count() > 0:
    print('Most frequent 15-letter word: ' + words15.first()['w'])
    # Most frequent 15-letter word: many-fountained