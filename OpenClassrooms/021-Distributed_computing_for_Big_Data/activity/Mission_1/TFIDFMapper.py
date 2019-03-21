#! /usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    word, filename, wordcount, wordperdoc = line.split()
    wordcount = float(wordcount)
    wordperdoc = float(wordperdoc)

    tf = wordcount / wordperdoc

    key = word
    value = filename + '\t' + str(tf)
    print('%s\t%s' % (key, value))