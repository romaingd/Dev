#! /usr/bin/env python3

import sys
from math import log

last_word = None
last_word_filenames_and_tfs = []
df = 0.
N = 2.

for line in sys.stdin:
    line = line.strip()

    word, filename, tf = line.split()
    tf = float(tf)

    if last_word is None:
        last_word = word
    
    if word == last_word:
        last_word_filenames_and_tfs.append((filename, tf))
        if tf > 0:
            df += 1.
    
    else:
        for lw_fn, lw_tf in last_word_filenames_and_tfs:
            tf_idf = lw_tf * log(N / df)
            key = last_word + '\t' + lw_fn
            value = str(tf_idf)
            print('%s\t%s' % (key, value))
        
        last_word = word
        last_word_filenames_and_tfs = [(filename, tf)]
        df = 0.
        if tf > 0:
            df += 1.
            

if last_word is not None:
    for lw_fn, lw_tf in last_word_filenames_and_tfs:
        tf_idf = lw_tf * log(N / df)
        key = last_word + '\t' + lw_fn
        value = str(tf_idf)
        print('%s\t%s' % (key, value))

