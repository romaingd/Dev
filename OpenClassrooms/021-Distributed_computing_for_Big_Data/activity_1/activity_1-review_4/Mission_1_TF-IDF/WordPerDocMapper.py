#! /usr/bin/env python2

import sys

for line in sys.stdin:

    # Supprimer les espaces
    line = line.strip()

    # recuperer les mots
    word,filename_count = line.split('|')
    
	#Identifier le filename
    filename, count = filename_count.split()
    
	#Sortie avec (filename|word,count)
    print "%s|%s\t%s" % (filename, word, count)

        
        