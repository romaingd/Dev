#! /usr/bin/env python3

import sys
total = 0
lastword = None
lastfilename = None

for line in sys.stdin:
    line = line.strip()

    word, filename, count = line.split()
    count = int(count)

    if lastword is None:
        lastword = word
        lastfilename = filename
    if (word == lastword) & (filename == lastfilename):
        total += count
        lastfilename = filename
    else:
        key = lastword + '\t' + lastfilename
        print("%s\t%d" % (key, total))
        total = count
        lastword = word
        lastfilename = filename

if lastword is not None:
    key = word + '\t' + lastfilename
    print("%s\t%d" % (key, total))
