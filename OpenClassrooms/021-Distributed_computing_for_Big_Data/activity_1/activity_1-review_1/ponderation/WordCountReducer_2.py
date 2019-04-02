#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys
import re

total = 0
words = []
documents = {}

for line in sys.stdin:
    line = line.strip()

    key, count = line.split("\t", 1)
    word, document = key.split()
    if document not in documents.keys():
        documents[document] = 0
    
    documents[document] += int(count)
    words.append((word, document, count))

for word, document, count in words:
    print("%s %s\t%d %d" % (word, document, int(count), int(documents[document])))
