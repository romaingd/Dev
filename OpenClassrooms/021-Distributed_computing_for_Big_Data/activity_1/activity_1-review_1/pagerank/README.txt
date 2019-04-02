Liste des 20 noeuds ayant le plus ofrt Page Rank

1126	3.805542
4230	3.964409
6676	4.518405
111	4.522444
6529	4.530887
3636	4.544552
4000	5.037303
164	5.085181
6938	5.085181
4002	5.168764
3017	5.550402
3019	5.550402
3020	5.550402
218	6.569346
6896	7.222009
6897	7.276916
2790	7.395304
2791	7.395304
7386	8.578339
2999	9.405668

========================================================
Nombre de tâches MAPREDUCE : 5 ( 4 multiplications de vecteur * matrice + 1 tri)

MAPREDUCE 1
MAP : PageRankMapper_1.py - 
      Récupère entrée le fichier adj_list - 
	  Renvoie en sortie la clé j où column représente la colonne Vj 
	    et en valeur la paire (i, value) où i représente la ligne i de la matrice adjacente et value = Pij 
REDUCE : PageRankReducer_1.py
      Récupère en entrée la sortie de MAP
	  Renvoie en sortie la clé (i, value) où i représente la ligne i de la matrice adjacente et value = x_1i
	    et en valeur le tableau de colonnes de la matrice adjacente. 
On retrouve ainsi non seulement le vecteur x_1 mais aussi tous les colonne de la matrice adjacente 

MAPREDUCE 2 et MAPREDUCE 3
MAP : PageRankMapper_2.py
	Récupère entrée la sortie de MAPREDUCE 1 -
	La sortie est basée sur le même principe que MAPREDUCE 1
REDUCE : PageRankReducer_2.py

MAPREDUCE 4
MAP : PageRankMapper_4.py
	Récupère entrée la sortie de MAPREDUCE 1 -
	La sortie est basée sur le même principe que MAPREDUCE 1
REDUCE : PageRankReducer_4.py
    Idem que pour les taches reduce precedente sauf que là, plus besoin de recupérer la matrice puisque c'est notre dernier calcul
	
MAPREDUCE 5 : Tache pour trier et obtenir les plus fort Page Rank
MAP : 	PageRankMapper_5.py
REDUCE : PageRankReducer_5.py

