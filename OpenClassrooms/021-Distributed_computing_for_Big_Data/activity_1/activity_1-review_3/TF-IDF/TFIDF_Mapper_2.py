#! /usr/bin/env python3
# coding: utf-8

import sys

# la cle de tri doit etre doc_id 
for line in sys.stdin:

    word, doc_id, count = line.strip().split("\t")
    print("%s\t%s\t%s" % (doc_id, word, count))
