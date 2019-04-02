#! /usr/bin/env python3
# coding: utf-8

import sys
total = 0
lastword = None

for line in sys.stdin:
    line = line.strip()

    # recuperer la cle et la valeur et conversion de la valeur en int
    word, doc_id, count = line.split("\t")
    count = int(count)

    # passage au mot suivant (plusieurs cles possibles pour une même exécution de programme)
    if lastword is None:
        lastword = word
        lastdoc = doc_id

    if word == lastword and doc_id == lastdoc:
        total += count
    else:
        print("%s\t%s\t%d" % (lastword, lastdoc, total))
        total = count
        lastword = word
        lastdoc = doc_id
        
if lastword is not None:
    print("%s\t%s\t%d" % (lastword, lastdoc, total))
