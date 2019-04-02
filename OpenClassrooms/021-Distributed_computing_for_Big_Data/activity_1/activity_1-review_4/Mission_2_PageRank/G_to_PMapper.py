#! /usr/bin/env python2

from __future__ import division
import sys

s = 0.15
n = 7967.0

for line in sys.stdin:

    # Supprimer les espaces
    line = line.strip().replace('-1', '')

    # recuperer les sites avec leurs liens sortants
    id_site, sites_sortant = line.split(':')
    
    # Compter les liens sortants
    liens_sortants = sites_sortant.split()
    nb_lien = float(len(liens_sortants))
    
    site = 0
    p_lst = []
    
    # Pour chaque ligne du fichier d'entree, on boucle sur les 7967 sites
    while site <= n:
        
        p = (s / n)
        
        # Si le site est un lien sortant du site observe
        if str(site) in liens_sortants:
            
            t = 1.0 / nb_lien
            p = (t * (1-s) + s / n)
            
        p_lst.append(p)
        
        site += 1
        
    print("%s|%s" % (id_site, p_lst))

    