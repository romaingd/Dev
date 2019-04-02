#! /usr/bin/env python2

import sys

lastfilename = None
wordperdoc = 0
files = []
files_count = []
line_bis=[]

for line in sys.stdin:

    # Supprimer les espaces
    line = line.strip()
    line_bis.append(line)
    # recuperer les filename et wordcount
    filenameword, count = line.split()
    filename, word = filenameword.split('|')
    count = int(count)

    if lastfilename is None:
        lastfilename = filename
    
    if filename == lastfilename:
        wordperdoc += count
    
    else:
        # On garde en memoire le fichier precedent et son wordperdoc
        files_count.append(wordperdoc)
        files.append(lastfilename)
        
        wordperdoc = count
        lastfilename = filename


files_count.append(wordperdoc)
files.append(lastfilename)

# Reconstitution de la liste initiale en ajoutant le wordperdoc
i = 0
lastfilename = None
for line in line_bis:
    
    # Supprimer les espaces
    line = line.strip()

    # recuperer les filename et wordcount
    filenameword, count = line.split()
    filename, word = filenameword.split('|')
    count = int(count)
    
    if lastfilename is None:
        lastfilename = filename
        
    if filename == lastfilename:
        #Sortie avec (word|filename,count|wordprename)
        print("%s|%s\t%d|%d" % (word, files[i], count, files_count[i]))
    else:
        i=+1
        print("%s|%s\t%d|%d" % (word, files[i], count, files_count[i]))

        
        