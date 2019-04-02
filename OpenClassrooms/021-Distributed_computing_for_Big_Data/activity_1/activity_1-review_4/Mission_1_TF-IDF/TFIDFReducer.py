#! /usr/bin/env python2

from __future__ import division
import sys

lastword = None
lastwordcount = None
lastwordperdoc = None
tf_idf = {}
df_t = 1
line_bis=[]

for line in sys.stdin:

    # Supprimer les espaces
    line = line.strip()
    line_bis.append(line)

    # split de la lignes
    word_filename,wordcount_wordperdoc = line.split()
    word,filename = word_filename.split('|')
    wordcount,wordperdoc = wordcount_wordperdoc.split('|')
        
    if lastword != word:
        # Initialisation du df_t 
        if lastword is not None:
            tf_idf[lastword] = str((int(lastwordcount) / int(lastwordperdoc)) * (2 / df_t))
        df_t = 1
        lastword = word
        lastwordcount = wordcount
        lastwordperdoc = wordperdoc
    
    else:
        df_t += 1
    
tf_idf[lastword] = str((int(wordcount) / int(wordperdoc)) * (2 / df_t))

# Reconstitution de la liste initiale en ajoutant le tf idf
for line in line_bis:
    
    word_filename,wordcount_wordperdoc = line.split()
    word,filename = word_filename.split('|')
    
	#Sortie avec (filename|word,count)
    print "%s|%s\t%s" % (word, filename, tf_idf.get(word))
