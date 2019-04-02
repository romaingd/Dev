#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys

# on spilt le contenu pour le trier par valeur
for line in sys.stdin:
    line = line.strip() 
    
    value, i = line.split("\t")
    value = float(value)
    
    print("%s\t%f" % (i, value))
