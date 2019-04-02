#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys

# on spilt le contenu pour le trier par valeur
for line in sys.stdin:
    line = line.strip() 
    
    value, word, docid = line.split("\t")
    value = float(value)
    
    print("%s\t%s\t%f" % (word, docid, value))
