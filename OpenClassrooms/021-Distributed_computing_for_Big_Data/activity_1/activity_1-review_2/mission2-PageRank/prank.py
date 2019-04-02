#!/bin/env python3

import numpy as np

#
# Auteur: Alexandre Sauve 
#
# Script de test pour la validation de la chaine Hadoop
# et le debug de la formule de la matrice P
#
# Prevoir 1Go de RAM
#


def load_T():
    with open("_movies/graph/adj_list") as f:
        lines = f.readlines()
    n = len(lines)
    T = np.zeros((n,n), dtype=np.float64)
    for l in lines:
        values = l.split()
        if values[0].endswith(":"):
            pid   = int(values[0][0:-1])
            nlink = 0
            for link in values[1:]:
                link = int(link)
                if link >= 0:
                    T[pid,link] = 1
                    nlink+=1
            if nlink > 0:
                T[pid,:] /= nlink
    return T



def printBestFun(xn, i):
    best = np.argsort(xn)
    best = (best[::-1])[0:20]
    print("iter=%3d"%(i), " ".join([ "%4d"%(b) for b in best ]))


def prank_Page(T, x0, s, niter, printBest=False):
    n = len(x0)
    xn = x0
    for i in range(niter):
        xn1    = s/n + (1-s)*np.dot( xn, T )
        if printBest:
            printBestFun(xn1, i)
        else:
            print("iter=",i+1," mean(x_i+1/x_i)=",np.mean(xn1/xn), "sum(x_i+1)=",np.sum(xn1))
        xn = xn1
    return xn



def prank_Course(T, x0, s, niter, printBest=False):

    ## compute matrix P
    P = T.copy()
    
    ## !!! This step is missing in the course !!!
    ## convertion to a stochatic matrix by filling empty rows with 1/n
    ## see eq (2) in https://www.i2m.univ-amu.fr/perso/thierry.gallouet/licence.d/anum.d/projet-pagerank.pdf
    ##   note: the P matrix of the document is the transposed of the one used here
    n = P.shape[0]
    for i in range(n):
        if P[i,:].sum() == 0:
            P[i,:] = 1.0 / n
    del T # free memory

    # production of the final P matrix
    P = (1-s)*P + s/n
    print(P[:,0])


    ## iterations
    xn = x0
    for i in range(niter):
        xn1  = np.dot( xn, P )
        print("iter=",i+1," std(x_i-x_i-1)=",np.std(xn1[xn1>0]-xn[xn1>0]), "sum(x_i+1)=",np.sum(xn1))
        #print("iter=",i+1," 20bests: ",str(np.argsort(xn1)[::-1][0:20]))
        xn = xn1
    return xn



if __name__ == '__main__':
    # problem parameters
    s     = 0.15
    niter = 20
    printBest = True # print 20 best at each iteration if True

    # methode de calcul:
    #  - original: formule de Brin et Page
    #  - course:   formule du cours (non convergente avec cette implementation)
    method = "course"
    
    # load transition matrix
    T = load_T()
    n = T.shape[0]
    
    # initial page rank vector
    x0 = np.ones(n, dtype=np.float64) / n

    if method=="original":
        xn = prank_Page(T, x0, s, niter, printBest)
    elif method == "course":
        xn = prank_Course(T, x0, s, niter)
    else:
        raise Exception("Retire tes moufles")
    
    # Print best 20 results
    w = np.argsort(xn)[::-1]
    print("==== Les 20 meilleurs Page rank pour method="+method)
    for i in range(20):
        print("%2d  pid: %4d\tPR(%4d)=%s" % (i, w[i], w[i], xn[w[i]]))




