#! /usr/bin/env python2

import sys

for line in sys.stdin:

    # Supprimer les espaces
    line = line.strip()

    # recuperer les sites avec leurs valeurs de liens sortants
    id_site, sites_lst = line.split('|')
    
    sites_lst = sites_lst.replace('[', '').replace(']', '')
    
    site_values = map(float, sites_lst.split(','))
    
    total = sum(site_values)
    
    print("%s|%s" % (id_site, total))
    
    