# Answer required:
# The most frequent 15-letter word in the Iliad is 'many-fountained' 

import re
import pyspark
import sys

from pyspark import SparkContext
from pyspark.sql import Row
from pyspark.sql.functions import desc


sc = SparkContext()
spark = pyspark.sql.session.SparkSession(sc)

def star(f):
    return lambda args: f(*args)



def load_text(text_path):
    to_delete_pattern = r'^[,.;:?!"\-\']*|[,.;:?!"\-\']*$'
    vocabulary = sc.textFile(text_path)\
                   .flatMap(lambda lines: lines.lower().split(" "))\
                   .map(lambda word: re.sub(to_delete_pattern, '', word))\
                   .filter(lambda word: not re.search(r'@|/', word))\
                   .filter(lambda word: word is not None and len(word) > 0)\
                   .persist()   # To avoid repetition for multiple actions

    word_count = vocabulary.count()

    word_len_freq = vocabulary.map(lambda word: (word, 1))\
                              .reduceByKey(lambda count1, count2: count1 + count2)\
                              .map(star(lambda word, count: Row(word=word, length=len(word), freq=count / float(word_count))))
    
    word_df = spark.createDataFrame(word_len_freq)
    return(word_df)


def main():
    word_df = load_text(sys.argv[1])

    # Find longest word
    longest_word = word_df.orderBy(desc('length')).first()
    print('Longest word:', longest_word.word)

    # Find most frequent 4-letter word
    most_frequent_4l = word_df.filter(word_df.length == 4).orderBy(desc('freq')).first()
    print('Most frequent 4-letter word:', most_frequent_4l.word)

    # Find most frequent 15-letter word
    # In the Iliad, this is 'many-fountained'
    most_frequent_15l = word_df.filter(word_df.length == 15).orderBy(desc('freq')).first()
    print('Most frequent 15-letter word:', most_frequent_15l.word)


if __name__ == '__main__':
    main()