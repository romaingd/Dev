/////////////////////////////////////////
// Tâche 1 : WordCount
//
// -- Commande : 
//hadoop jar /$HADOOP/hadoop-mapreduce/hadoop-streaming.jar -input ./input -output ./result/WordCount -file ./WordCountMapper.py -file ./WordCountReducer.py -mapper ./WordCountMapper.py -reducer ./WordCountReducer.py
//
// -- Mapper : Génération de paires (word, 1) avec les étapes 
//			- Mise en minuscule
//			- Filtrage des mots inutiles stopwords
//			- Suppression des ponctuations et des caracteres numeriques
//            - Suppression des mots de moins de 3 caracteres
//
// -- Reducer : Comptages
//
// -- output : clé (word | filename, wordCount)


////////////////////////////////////////
// Tâche 2 : WordPerDoc
//
// -- Commande : 
//hadoop jar /$HADOOP/hadoop-mapreduce/hadoop-streaming.jar -input ./result/WordCount -output ./result/WordPerDoc -file ./WordPerDocMapper.py -file ./WordPerDocReducer.py -mapper ./WordPerDocMapper.py -reducer ./WordPerDocReducer.py
//
// -- Mapper : Génération de paires (filename | word, wordCount)
//
// -- Reducer : Comptages WordPerDoc. Puis reconstitution de la liste initiale en ajoutant le wordperdoc
//
// -- output : clé (word | filename, wordCount | wordPerDoc)


/////////////////////////////////////////
// Tâche 3 : Calcul TF IDF
//
//Commande : 
//hadoop jar /$HADOOP/hadoop-mapreduce/hadoop-streaming.jar -input ./result/WordPerDoc -output ./result/TFIDF -file ./TFIDFMapper.py -file ./TFIDFReducer.py -mapper ./TFIDFMapper.py -reducer ./TFIDFReducer.py
//
// -- Mapper : Pas d'opération
//
// -- Reducer : Calcul du TF IDF. Puis reconstitution de la liste initiale en ajoutant le TF IDF
//
// -- output : clé (word | filename, TF_IDF)



///////////////////////////////////////
// Résultat :
Les 20 mots qui ont la plus forte pondération TF-IDF dans Callwild sont : 
	buck
	dogs
	thornton
	sled
	spitz
	francois
	bucks
	trail
	john
	perrault
	hal
	team
	ice
	traces
	solleks
	dave
	thorntons
	dawson
	mercedes
	throat
Les 20 mots qui ont la plus forte pondération TF-IDF dans defoe-robinson-103.txt sont : 
	friday
	thoughts
	myself
	board
	viz
	corn
	cave
	voyage
	had
	providence
	labor
	powder
	deliverance
	england
	coast
	sail
	ships
	brazils
	goats
	purpose