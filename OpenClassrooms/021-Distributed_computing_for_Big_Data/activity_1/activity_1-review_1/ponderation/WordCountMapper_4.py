#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys

# on spilt le contenu pour le trier par valeur
for line in sys.stdin:
    line = line.strip() 
    
    words, value = line.split("\t", 1)
    word, docid = words.split()
    value = float(value)
    
    print("%f\t%s\t%s" % (value, word, docid))
