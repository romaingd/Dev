#! /usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    word, filename, count = line.split()
    key = filename
    value = word + '\t' + count
    print('%s\t%s' % (key, value))