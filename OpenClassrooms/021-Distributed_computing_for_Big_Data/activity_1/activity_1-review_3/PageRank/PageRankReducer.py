#! /usr/bin/env python3
# coding: utf-8

import sys
import os

i_prec = None

s = 0.15
n = 7967 # en dur... comment lire le compteur map_input_records dans streaming ???
#n = int(os.getenv("mapreduce_map_input_records"))

rec_Types = ["linksTo", "linkedFrom"]

v_i = 1.0 / n

for line in sys.stdin:
	row = line.strip().split('\t')
	i = int(row[0])
	record_type = row[1]
	
	if record_type == "linkedFrom":
		j = int(row[2])
		n_j = int(row[3])
	else:
		linksTo = row[2:]

	assert record_type in rec_Types

	if i_prec is None:
		i_prec = i
		x_i = 0.0

	if i_prec == i and record_type == "linkedFrom":
		g_ij = 1.0 / n_j
		x_i += (1.0 - s) * v_i * g_ij
	elif i_prec == i and record_type == "linksTo":
		linksTo_str = "\t".join(["%s" % v for v in linksTo])
	else:
		x_i += s / n * v_i
		print("%d\t%.12f\t%s" % (i_prec, x_i, linksTo_str))
		i_prec = i
		x_i = 0.0
		if record_type == "linkedFrom":
			g_ij = 1.0 / n_j
			x_i += (1.0 - s) * v_i * g_ij
		elif record_type == "linksTo":
			linksTo_str = "\t".join(["%s" % v for v in linksTo])


if i_prec is not None:
	x_i += s / n * v_i
	print("%d\t%.12f\t%s" % (i, x_i, linksTo_str))

