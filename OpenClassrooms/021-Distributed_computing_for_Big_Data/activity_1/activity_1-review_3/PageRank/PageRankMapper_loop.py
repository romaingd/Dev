#! /usr/bin/env python3
# coding: utf-8

import sys

for line in sys.stdin:
	row = line.strip().split('\t')
	i = int(row[0])
	x_i = float(row[1])
	linksTo = row[2:]
	n_i = len(linksTo)

	# on enregistre les liens sortant pour appel recursif Mapper/Reducer
	linksTo_str = '\t'.join(["%s" % j for j in linksTo])
	print("%d\tlinksTo\t%.12f\t%s" % (int(i), x_i, linksTo_str))

	for j in linksTo:
		print("%d\tlinkedFrom\t%d\t%.12f\t%d" % (int(j), i, x_i, n_i))

