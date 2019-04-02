#!/usr/bin/env python3

# minimal import because of eval used later
from sys import stdin

# Preparation des accumulateurs.
# La memoire est supposee etre suffisante pour ce contenu car le nombre de
# mots du vocabulaire est de l'ordre de 100,000 (sauf vocab technique)
wordsperdoc = {}
words = {}

### Partie 1: accumulation du compte de mots
for line in stdin:
    # decoupage des lignes de la forme "(word, doc_id)\tn"
    keystr, n = line.strip().split("\t")

    # extraction des mots
    word, doc_id = eval(keystr)

    # mise a jour: nombre de mots pour ce document
    n = int(n)
    if not doc_id in wordsperdoc:
        wordsperdoc[doc_id] = 0
    wordsperdoc[doc_id] += n

    # mise a jour: nombre d'occurences du mot dans ce document
    # key utilise explicitement un tuple pour rester homogene sur le reste
    # de la chaine
    key = (word, doc_id)
    if not key in words:
        words[key] = 0
    words[(word, doc_id)] += n

### Partie 2: output des paires (key, value)
for key, wordcount in words.items():
    (word, doc_id) = key
    print("%s\t%s" % ((word, doc_id), (wordcount, wordsperdoc[doc_id])))


