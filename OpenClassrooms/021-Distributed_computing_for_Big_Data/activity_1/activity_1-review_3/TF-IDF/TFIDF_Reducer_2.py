#! /usr/bin/env python3
# coding: utf-8

import sys

lastdoc = None

for line in sys.stdin:
    line = line.strip()

    # recuperer la cle et la valeur et conversion de la valeur en int
    doc_id, word, count = line.split("\t")
    count = int(count)

    if lastdoc is None:
        lastword = word
        lastdoc = doc_id
        wclist = []
        wordperdoc = 0

    if doc_id == lastdoc:
        wordperdoc += count
        wclist.append([word, count]) # sauvegarde des valeurs word et count pour chaque entree
    else:
        for row in wclist:
            print("%s\t%s\t%d\t%d" % (row[0], lastdoc, row[1], wordperdoc))
        wordperdoc = count
        lastword = word
        lastdoc = doc_id
        wclist = [[word, count]]
        
if lastdoc is not None:
    for row in wclist:
        print("%s\t%s\t%d\t%d" % (row[0], lastdoc, row[1], wordperdoc))
