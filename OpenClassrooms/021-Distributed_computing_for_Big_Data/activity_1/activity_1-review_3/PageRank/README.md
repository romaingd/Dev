# Calcul du PageRank avec Hadoop

## Mise en place

Rendre les scripts python executables:

	sudo chmod +x *.py

Créer un lien sybolique vers hadoop-streaming (adapter en fonction de votre installation):

	ln -s $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-X.X.X.jar hadoop-streaming.jar

pageRank.sh execute l'ensemble des 9 jobs consécutivement : 1 job intitial, 7 jobs itératifs (\_loop), 1 job final

##TOP 20

|  # |       pagerank |  pid |
| --:| --------------:| ----:|
|  1 | 0.000642947756 | 2999 |
|  2 | 0.000503533719 | 4002 |
|  3 | 0.000446822076 | 2126 |
|  4 | 0.000410445873 | 6896 |
|  5 | 0.000343968576 | 6897 |
|  6 | 0.000339267627 | 6938 |
|  6 | 0.000339267627 |  164 |
|  8 | 0.000314739318 | 6230 |
|  9 | 0.000293503803 | 7386 |
| 10 | 0.000198086505 | 4000 |
| 11 | 0.000191064260 | 4001 |
| 12 | 0.000188934845 | 3017 |
| 13 | 0.000188928741 | 3020 |
| 13 | 0.000188928741 | 3019 |
| 15 | 0.000183255203 |  278 |
| 16 | 0.000183254184 |  276 |
| 17 | 0.000170462490 | 4230 |
| 18 | 0.000152075234 | 2786 |
| 19 | 0.000148010169 | 2789 |
| 19 | 0.000148010169 | 2788 |

##JOB 1:

###MAP (PageRankMapper.py)
* en entrée:
	* key : ligne du fichier d'entrée (string)
	* pas de values

* en sortie:
	* key : j : pid de la page (int)
	
	* values pour type enregistrement = linkedFrom
		* linkedFrom (string)
		* i: pid de la page source (int)
		* n_i : nombre de liens sortants de la page i (int)

	* values pour type enregistrement = linksTo
		* linksTo (string)
		* liste des liens sortants de la page (list<int>)

###REDUCE (PageRankReducer.py)
* en entrée :
	* sortie de MAP

* en sortie:
	* key : i : pid de la page (int)
	* values:
	* x_i : pagerannk (float)
	* liste des liens sortants de la page (list<int>)


##JOBS intermediaires:

###MAP (PageRankMapper_loop.py)
* en entrée:
	* key : i : pid de la page (int)
	* values:
	* x_i : pagerannk (float)
	* liste des liens sortants de la page (list<int>)

* en sortie:
	* key : j
	
	* values pour type enregistrement = linkedFrom
		* linkedFrom (string)
		* i: pid de la page source (int)
		* x_i : pagerank de la page i (float)
		* n_i : nombre de liens sortants de la page i (int)

	* values pour type enregistrement = linksTo
		* linksTo (string)
		* x_j : pagerank de la page j (float)
		* liste des liens sortants de la page j (list<int>)

###REDUCE (PageRankReducer_loop.py)
* en entrée :
	* sortie de MAP

* en sortie:
	* key : i : pid de la page (int)
	* values:
		* x_i : pagerannk (float)
		* liste des liens sortants de la page (list<int>)

##JOB final:

###MAP (PageRankMapper_loop.py)
identique au jobs intermediaires

###REDUCE (PageRankReducer_final.py)
* en entrée :
	* sortie de MAP

* en sortie:
	* key : pagerank (float)
	* value : pid (int)
