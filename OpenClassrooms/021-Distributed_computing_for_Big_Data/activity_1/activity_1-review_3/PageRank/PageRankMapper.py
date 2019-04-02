#! /usr/bin/env python3
# coding: utf-8

import sys

for line in sys.stdin:
    i, values = line.strip().split(':')
    values = values.split()[:-1]
    n_i = len(values)
    
    # on enregistre les liens sortant pour appel recursif
    linksTo_str = '\t'.join(["%s" % j for j in values])
    print("%d\tlinksTo\t%s" % (int(i), linksTo_str))

    for j in values:
        print("%d\tlinkedFrom\t%d\t%d" % (int(j), int(i), int(n_i)))

