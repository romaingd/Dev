#! /usr/bin/env python3

import sys

n = 7967

for line in sys.stdin:
    line = line.strip()
    items = line.split()

    # Isolate the node considered
    i = items[0][:-1]       # Remove the ':' character
    # Isolate the outgoing links
    out_links = items[1:-1]

    # Print the contribution of i to the page rank of outgoing links
    n_i = len(out_links)
    for j in out_links:
        print('%s\t%0.15f' % (j, (1. / n) / n_i))
    
    # Also re-print the outlinks, to correctly chain multiple jobs
    print('%s\t%s' % (i, ','.join(out_links + ['-1'])))