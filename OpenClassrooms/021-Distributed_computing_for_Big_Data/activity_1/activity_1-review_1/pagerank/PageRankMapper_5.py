#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys

# on spilt le contenu pour le trier par valeur
for line in sys.stdin:
    line = line.strip() 
    
    i, value = line.split("\t")
    value = float(value)
    
    print("%f\t%s" % (value, i))
