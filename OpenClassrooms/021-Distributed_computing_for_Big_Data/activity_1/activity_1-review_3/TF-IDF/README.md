# Calcul du PageRank avec Hadoop

##Execution

Rendre les scripts python executables:

	sudo chmod +x *.py

Créer un lien symbolique vers le hadoop-streaming de votre installation (adapter en fonction de votre installation):

	ln -s $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-X.X.X.jar hadoop-streaming.jar

jobs_tfidf.sh permet d'uploader les données, d'executer consécutivement les 3 jobs et de récupérer les résultats

##TOP 20

###Call of the Wild

     1	buck		0.007931
     2	dogs		0.002599
     3	thornton	0.002247
     4	spitz		0.001432
     5	sled		0.001388
     6	francois	0.001322
     7	trail		0.000903
     8	john		0.000881
     9	perrault	0.000859
    10	hal			0.000815
    11	team		0.000749
    12	sol			0.000639
    13	traces		0.000617
    14	leks		0.000617
    15	ice			0.000617
    16	dave		0.000551
    17	mates		0.000485
    18	mercedes	0.000463
    19	whip		0.000441
    20	dawson		0.000441

###Robinson Crusoe
     1	friday		0.001513
     2	thoughts	0.000908
     3	board		0.000581
     4	corn		0.000507
     5	voyage		0.000483
     6	providence	0.000450
     7	powder		0.000450
     8	labor		0.000425
     9	deliverance	0.000376
    10	coast		0.000344
    11	sail		0.000335
    12	england		0.000335
    13	goat		0.000294
    14	storm		0.000286
    15	purpose		0.000278
    16	brazils		0.000278
    17	wreck		0.000270
    18	round		0.000270
    19	habitation	0.000270
    20	fired		0.000270


##JOB 1

###MAP
* en entrée:
	* key : ligne du fichier d'entrée (string)
	* pas de values

* en sortie:
	* key : 
		* mot (string)
		* doc_id (string)
	
	* values : 1 (int)

###REDUCE
* en entrée :
	* sortie de MAP

* en sortie:
	* key : 
		* mot (string)
		* doc_id (string)
	
	* values: nombre d'occurences dans le doc (int)


##JOB 2

###MAP
* en entrée:
	* sortie de Reducer 1

* en sortie:
	* key : doc_id (string) 
	
	* values :
		* word (string)
		* count = nombre d'occurences de word dans doc_id (int)

###REDUCE
* en entrée :
	* sortie de MAP

* en sortie:
	* key
		* mot (string)
		* doc_id (string)
	* values:
		* count = nombre d'occurences de word dans doc_id (int)
		* wordperdoc = nombre total de mots dans doc_id (int)

##JOB 3

###MAP
renvoie la sortie de reduce_2 tel quel

###REDUCE
* en entrée :
	* sortie de REDUCE_2

* en sortie:
	* key
		* mot (string)
		* doc_id (string)
	* values:
		* key : TF-IDF (float)
