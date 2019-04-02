Calcul de TD-IDF

TOP 20 de callwild.txt

buck	callwild.txt	0.007002
dogs	callwild.txt	0.002505

thornton	callwild.txt	0.001812

sled	callwild.txt	0.001342

spitz	callwild.txt	0.001342

francois	callwild.txt	0.001163

bucks	callwild.txt	0.001051

trail	callwild.txt	0.000917
john	callwild.txt	0.000895

perrault	callwild.txt	0.000828
hal	callwild.txt	0.000671

team	callwild.txt	0.000671
traces	callwild.txt	0.000626

ice	callwild.txt	0.000626

solleks	callwild.txt	0.000604
dave	callwild.txt	0.000537

thorntons	callwild.txt	0.000470
dawson	callwild.txt	0.000447

mercedes	callwild.txt	0.000447

whip	callwild.txt	0.000425

throat	callwild.txt	0.000425
======================================================
TOP 20 defoe-robinson-103.txt

friday	defoe-robinson-103.txt	0.001472
thoughts	defoe-robinson-103.txt	0.000913
board	defoe-robinson-103.txt	0.000584
corn	defoe-robinson-103.txt	0.000502

cave	defoe-robinson-103.txt	0.000493
voyage	defoe-robinson-103.txt	0.000485

providence	defoe-robinson-103.txt	0.000444

powder	defoe-robinson-103.txt	0.000428

labor	defoe-robinson-103.txt	0.000428
england	defoe-robinson-103.txt	0.000337

deliverance	defoe-robinson-103.txt	0.000378

coast	defoe-robinson-103.txt	0.000329

sail	defoe-robinson-103.txt	0.000329

ships	defoe-robinson-103.txt	0.000321

purpose	defoe-robinson-103.txt	0.000280

goats	defoe-robinson-103.txt	0.000280

brazils	defoe-robinson-103.txt	0.000280

storm	defoe-robinson-103.txt	0.000288
habitation	defoe-robinson-103.txt	0.000271

dreadful	defoe-robinson-103.txt	0.000271
==========================================================
Nombre de tâches MAPREDUCE impliquées : 4

MAPREDUCE 1
MAP : WordCountMapper_1.py - REDUCE : WordCountReducer_1.py
Récupère entrée les fichiers txt des textes renvoie en sortie le triplet mot - docid - occurence
mot - docid constitue la clé (docid est dans notre cas le nom du fichier) 
occurence constitue le nombre d'occurence du mot par document

MAPREDUCE 2
MAP : WordCountMapper_2.py - REDUCE : WordCountReducer_2.py
Récupère entrée la sortie de la 1e tâche et renvoie en sortie le quadruplet mot - docid - occurence - mot_par_doc
mot - docid constitue la clé la même que précédemment 
occurence - mot_par =_doc constitue le couple de valeur nombre d'occurence du mot par document - nombre total de mot par document

MAPREDUCE 3
MAP : WordCountMapper_3.py - REDUCE : WordCountReducer_3.py
Récupère entrée la sortie de la 2e tache et renvoie en sortie le triplet mot - docid - td-idf
mot - docid constitue la clé (docid est dans notre cas le nom du fichier) 
td-idf constitue la valeur de td-idf calculée

MAPREDUCE 4
MAP : WordCountMapper_4.py - REDUCE : WordCountReducer_4.py
Récupère entrée la sortie de la 3e tache et renvoie en sortie le triplet mot - docid - td-idf triée par td-idf
Le MAP renvoie en sortie le triplet td-idf - mot - docid ce qui permet de récuperer les données triées par valeur de td-idf
Le REDUCE réajuste la sortie dans le sens mot - docid - td-idf
