#! /usr/bin/env python3
# coding: utf-8

import sys
from math import log10

lastword = None
N = 2 # nombre de documents de la collection (en dur...)

def compute_TFIDF(wc, wpd, doccount):
    return float(wc) / wpd *  log10( float(N) / doccount)

for line in sys.stdin:

    # recuperer la cle et la valeur et conversion de la valeur en int
    word, doc_id, wc, wpd = line.strip().split("\t")

    if lastword is None:
        lastword = word
        doccount = 0
        rows = []

    if word == lastword:
        doccount += 1
        rows.append([doc_id, int(wc), int(wpd)])
    else:
        for row in rows:
            print("%s\t%s\t%f" % (lastword, row[0], compute_TFIDF(row[1], row[2], doccount)))
        
        doccount = 1
        rows = [[doc_id, int(wc), int(wpd)]]
        lastword = word
        lastdoc = doc_id
        
if lastword is not None:
    for row in rows:
        print("%s\t%s\t%f" % (lastword, row[0], compute_TFIDF(row[1], row[2], doccount)))
