/////////////////////////////////////////
// Tâche 1 : WordCount
//
// -- Commande : 
//hadoop jar /$HADOOP/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.5.0-292.jar -input /movies/graph/adj_list -output /movies/result -file ./G_to_PMapper.py -file ./G_to_PReducer.py -mapper ./G_to_PMapper.py -reducer ./G_to_PReducer.py
//
// -- Mapper : 	Récupération du fichier adj_list
//				Calcul de la matrice de transition T puis de la probabilité P
//				Sortie sous la forme (site | [P1,P2, P3, ..., Pn]
//
// -- Reducer : Somme des probabilités P pour chaque site
//
// -- output : clé (site | PageRank)


///////////////////////////////////////
// Résultat :
Les 20 nœuds qui ont le plus fort page rank sont : 

	132		==> 0,85762520
	109		==> 0,85417974
	93		==> 0,85344546
	3701	==> 0,85276767
	7469	==> 0,85178863
	98		==> 0,85154387
	12		==> 0,85126145
	5322	==>	0,85120497
	6471	==>	0,85112966
	6507	==> 0,85112966
	3939	==> 0,85111083
	3953	==> 0,85111083
	6485	==> 0,85109200
	6526	==> 0,85109200
	146		==> 0,85103552
	5987	==> 0,85099787
	6521	==> 0,85097904
	6846	==> 0,85096021
	144		==> 0,85094138
	4003	==> 0,85092256
