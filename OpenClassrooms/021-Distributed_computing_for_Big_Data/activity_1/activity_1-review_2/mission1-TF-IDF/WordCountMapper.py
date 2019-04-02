#!/usr/bin/env python3

import sys
import os
import re


# lit les stop words via le fichier passe avec l'option -file
# et stocke le contenu dans une table de hash 
stop_words = {}
with open('stopwords_en.txt', 'r') as f:
    for line in f:
        stop_words[line.strip()] = True


# recupere le nom de fichier passe via stdin
file_id = os.environ['mapreduce_map_input_file']


for line in sys.stdin:

    # (A) mise en minuscules
    line = line.lower()

    # (C) Supprimer les ponctuations
    line = re.sub(r'[;,:!.?/"\(\)]', ' ', line)

    # recuperer les mots et suppression des espaces
    words = line.split()

    # operation map, pour chaque mot, generer la paire ( (file_id, mot), 1)
    for word in words:
        # (B) filtrage des mots inutiles
        # (D) suppression des mots de moins de 3 caracteres
        if not (word in stop_words) and (len(word) > 3):
            print("%s\t%d" % ((word, file_id), 1))


