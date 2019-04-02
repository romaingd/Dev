#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys
import math

lastword = None
documents = []
word_list = {}
document_list_per_doc = dict()
docid = ""

for line in sys.stdin:
    line = line.strip()

    words, counts = line.split("\t", 1)
    word, docid = words.split()
    wordcount, wordcount_per_doc = counts.split()

    wordcount = int(wordcount)
    wordcount_per_doc = int(wordcount_per_doc)

    if docid not in documents:
        documents.append(docid)

    tf_t_d = wordcount / wordcount_per_doc

    if lastword is None:
        lastword = word

    if word != lastword:
        word_list[lastword] = document_list_per_doc
        document_list_per_doc = {}
        lastword = word
    document_list_per_doc[docid] = tf_t_d

N = len(documents)

for word, document_list_per_doc in word_list.items():
    for docid, tf_t_d in document_list_per_doc.items():
        tf_idf = tf_t_d * math.log10(N / len(document_list_per_doc))
        print("%s %s\t%f" % (word, docid, tf_idf))
