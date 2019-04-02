#!/usr/bin/env python3

import sys

#
# Ce filtre trie la sortie TFIDF_Reducer.py
#


# lecture de la totalite des donnes en entree
lines = [l.strip() for l in sys.stdin.readlines() ]

# suprime les lignes vides
lines = [ l for l in lines if len(l) > 0] 

# construit une liste (value, line) avec comme valuer le TF-IDF
pairs  = [ ( float(l.split("\t")[1]), l.strip() ) for l in lines]

# sortie de la liste triee
for _,line in sorted(pairs, reverse=True):
    print(line)


