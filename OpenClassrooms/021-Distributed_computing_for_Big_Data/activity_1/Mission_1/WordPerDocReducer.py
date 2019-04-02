#! /usr/bin/env python3

import sys

last_filename = None
wordperdoc = 0
file_words_and_counts = []

for line in sys.stdin:
    line = line.strip()

    filename, word, count = line.split()
    count = int(count)

    if last_filename is None:
        last_filename = filename

    if filename == last_filename:
        wordperdoc += count
        file_words_and_counts.append((word, count))

    else:
        for w, c in file_words_and_counts:
            key = w + '\t' + last_filename
            value = str(c) + '\t' + str(wordperdoc)
            print('%s\t%s' % (key, value))
        last_filename = filename
        wordperdoc = count
        file_words_and_counts = [(word, count)]


if last_filename is not None:
    for w, c in file_words_and_counts:
        key = w + '\t' + last_filename
        value = str(c) + '\t' + str(wordperdoc)
        print('%s\t%s' % (key, value))