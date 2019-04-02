#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys
import math

n = 7967
s = 0.15
x_1 = 0  # initialize rankpage which will not be the same

# pij = (1 - s) / n_i + s/n

for line in sys.stdin:
    line = line.strip()
    index, x_1, values = line.split('\t')
    index = int(index)
    x_1 = float(x_1)
    values = values.strip()
    columns = values.split()

    n_i = (len(columns) - 1)
    for column in columns:
        column = int(column)
        if column != -1 and x_1 != 0:
            value = ((1 - s) / n_i + s/n) * x_1  # * 100000
            print ("%d\t%d\t%f" % (column, index, value))
