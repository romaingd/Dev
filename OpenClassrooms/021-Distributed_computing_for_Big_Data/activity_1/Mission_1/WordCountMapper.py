#! /usr/bin/env python3

import sys
import re
import os

for line in sys.stdin:
    # Get filename to set (word, filename) as a key
    filename = os.environ["map_input_file"]

    # Remove beginning and end whitespaces
    line = line.strip()
    # To lower case
    line = line.lower()
    # Remove punctuation and numbers
    line = re.sub(r'[\d.,?"\'\'\/#!$%\^&\*;:{}=\-_`~()]', ' ', line)

    words = line.split()
    # Remove words with less than 3 letters
    words_lengths = list(map(len, words))
    words = [words[i] for i, x in enumerate(words_lengths) if x >= 3]
    # Remove stop words
    with open('stopwords_en.txt', 'r') as f:
        stop_words = [word for line in f for word in line.split()]

    words = [word for word in words if word not in stop_words]

    for word in words:
        key = word + '\t' + filename
        print('%s\t%d' % (key, 1))
