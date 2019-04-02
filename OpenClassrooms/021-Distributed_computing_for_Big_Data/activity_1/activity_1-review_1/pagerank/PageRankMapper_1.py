#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys
import math

n = 7967
s = 0.15
x_0 = 1/n  # the same value for every page at the beginning

# pij = (1 - s) / n_i + s/n

for line in sys.stdin:
    line = line.strip()
    values = line.split(':')
    index = int(values[0])

    values[1] = values[1].strip()
    columns = values[1].split()
    for column in columns:
        column = int(column)
        if column != -1:
            value = (1 - s) / (len(columns) - 1) + s/n * x_0 # * 100000
            print ("%d\t%d\t%f" % (column, index, value))
