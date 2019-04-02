#! /usr/bin/env python3
# coding: utf-8

import sys
from os import getenv
import re

#os.environ["map.input.file"]
doc_id = getenv("mapreduce_map_input_file")
#doc_id = 1

f = open("./stopwords_en.txt", 'r')
stopword_list = f.read().split()
f.close()


for line in sys.stdin:

    # Mise en forme de la ligne et remplacement de la ponctuation par des espaces
    line = re.sub(r"[,;:.?!\'\"(){}-]", " ", line).strip().lower()
    # line = re.sub(r"[\W+]", " ", line).strip().lower() # pour supprimer tous les caractères spéciaux

    # recupérer les mots
    words = line.split()

    # operation map, pour chaque mot, generer la paire (mot, 1)
    for word in words:
        
        # on exclut les mots de moins de 3 caractères ou contenant des caractères numériques ou spéciaux 
        if re.search(r"^[a-z]{3,}$", word) is None:
            # print("%s excluded" % word)
            continue
 
        if word not in stopword_list:
            # print("OK : %s" % word)
            print("%s\t%s\t%d" % (word, doc_id, 1))
        # else:
        #     print("%s rejected" % word)
