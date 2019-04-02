#! /usr/bin/env python3

import sys

s = 0.15
n = 7967

last_i = None
last_out_links = None
last_pagerank = 0

for line in sys.stdin:
    line = line.strip()
    i, item = line.split()

    if last_i is None:
        last_i = i

    if i == last_i:
        if item.find('-1') == -1:       # Contribution of an incoming link
            last_pagerank += float(item)
        if item.find('-1') == 0:        # List of outgoing links is empty
            last_out_links = []
        else:                           # List of outgoing links
            last_out_links = item.split(',')[:-1]
    
    else:
        # First print the <key, value> pairs for the previous i
        # This works because pageranks sum to 1 over all pages

        # Compute the page rank of i at current iteration
        last_pagerank = (1 - s) * last_pagerank + (s / n)

        # Print the contribution of i to the page rank of outgoing links
        n_i = max(len(last_out_links), 1)
        for j in last_out_links:
            print('%s\t%0.15f' % (j, last_pagerank / n_i))
                
        # Also re-print the outlinks, to correctly chain multiple jobs
        print('%s\t%s' % (last_i, ','.join(last_out_links + ['-1'])))

        # Then reinitialize the storage variables
        last_i = i
        last_out_links = None
        last_pagerank = 0

        # And treat the incoming line
        if i == last_i:
            if item.find('-1') == -1:
                last_pagerank += float(item)
            if item.find('-1') == 0:
                last_out_links = []
            else:
                last_out_links = item.split(',')[:-1]


# Also take care of the very last i processed by this Reducer node
if last_i is not None:
    last_pagerank = (1 - s) * last_pagerank + (s / n)
    n_i = max(len(last_out_links), 1)
    for j in last_out_links:
        print('%s\t%0.15f' % (j, last_pagerank / n_i))
    print('%s\t%s' % (last_i, ','.join(last_out_links + ['-1'])))