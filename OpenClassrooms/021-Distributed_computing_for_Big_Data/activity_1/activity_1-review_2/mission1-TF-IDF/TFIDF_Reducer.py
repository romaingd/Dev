#!/usr/bin/env python3

# Un appel a eval() est utilise : importation du minimum de symboles
from sys import stdin, stdout
from os import environ
from math import log


# initialisation des accumulateurs
stats       = []
lastword    = None

# le nombre total de documents estime a partir du contenu du dossier input
NDOC=int(environ["NDOC"])

# fonction de calcul et de sortie du TF-IDF
def out_tf_idf(word, stats):
    df_t = len(stats)
    for doc_id, wordperdoc, wordcount in stats:
#        print("DBG:",word,"NDOC=",NDOC, "df_t(len(stats))=",df_t, "\t(doc_id, wordperdoc, wordcount)",stats,
#            "  (wordcount / wordperdoc)=",  (wordcount / wordperdoc), " log(NDOC / df_t)=", log(NDOC / df_t))
        # wordcount  = (tf_t,d) nb d'occurence du mot dans le document
        # wordperdoc = (n_d)    nb total de mots dans le document
        w_td = (float(wordcount) / wordperdoc) * log(float(NDOC) / df_t)
        print( "%s\t%s" % ((word, doc_id), w_td) )

# traitement du flux en entree de la forme:
#   (word, doc_id)\t(wordcount, wordperdoc)
for line in stdin:
    line = line.strip()

    # conversion des inputs en variables python
    key, value = line.split("\t")
    word, doc_id          = eval(key)
    wordcount, wordperdoc = [ int(n) for n in eval(value) ]

    # condition initiale
    if lastword is None:
        lastword = word

    # sortie du TF-IDF en fin d'accumulation
    if not (word == lastword):
        out_tf_idf(lastword, stats)
        stats     = []
        lastword  = word
    stats.append( (doc_id, wordperdoc, wordcount) )



if lastword is not None:
    out_tf_idf(lastword, stats)


