import sys
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
sc = SparkContext()
spark = SparkSession.builder.getOrCreate()

# Réalise des stats sur le document passé en paramètre. Pour le TP sur l'Illiade, voici les résultats:
#Mot le plus long : brothers-in-law-for
#Mot de 4 lettres le plus fréquent : with
#Mot de 15 lettres le plus fréquent : many-fountained

## IMPORTANT : réalisé sous python 3.6x : les tuples ne sont plus pris en charge comme paramètres pour les map. il faut les gérer comme des listes.

def load_text(text_path):
    # text vers ligne puis mot, et traitement des mots, on utilise strip pour les - car il y'en a dans les mots.
    # Suite à opti/Debug, 4 partitions fonctionne plus rapidement (50% pour l'étape sur mon 2 coeurs avec HT)
    vocabulary = sc.textFile(text_path,minPartitions=4)\
        .flatMap(lambda lines: lines.lower().split())\
        .flatMap(lambda word: word.split(","))\
        .flatMap(lambda word: word.split("."))\
        .flatMap(lambda word: word.split(";"))\
        .flatMap(lambda word: word.split(":"))\
        .flatMap(lambda word: word.split("?"))\
        .flatMap(lambda word: word.split("!"))\
        .flatMap(lambda word: word.split("\""))\
        .flatMap(lambda word: word.split("\'"))\
        .map(lambda word: word.strip("-"))\
        .filter(lambda word: '@' not in word and '/' not in word and len(word) > 0)

    
    # Nombre de mots du doc
    wordCount = vocabulary.count()

    # on calcul la fréquence et le nombre de char des mots (map-reduce + map pour générer les colonnes de notre rdd et les nommer)
    word_freq_length = vocabulary.map(lambda word: (word, 1))\
        .reduceByKey(lambda count1, count2: count1 + count2)\
        .map(lambda word_count: (word_count[0], word_count[1]/float(wordCount), len(word_count[0])))\
        .map(lambda word_stats: Row(word=word_stats[0],wordfreq=word_stats[1],wordl=word_stats[2]))    
    #rdd->DF  
    wordFreqLengthDf = spark.createDataFrame(word_freq_length)


    return (wordFreqLengthDf)

def main():
    if (len(sys.argv)!=2) :
        print("usage : spark-submit ./textstats.py ./[filename]")
    else:
        #on charge (un seul DF)
        textDf = load_text(sys.argv[1])
        textDf.createTempView("text_table")
        
        #debug:
        #print(textDf.limit(10).show())
        
        #nos 3 requêtes
        longestWordDf = spark.sql("SELECT word FROM text_table ORDER BY wordl DESC LIMIT 1")
        mostUsedFourWordDf = spark.sql("SELECT word FROM text_table WHERE wordl=4 ORDER BY wordfreq DESC LIMIT 1")
        mostUsedFifteenWordDf = spark.sql("SELECT word FROM text_table WHERE wordl=15 ORDER BY wordfreq DESC LIMIT 1") 

        # on affecte nos variables à imprimer (row->rdd -> string)
        longestWord=longestWordDf.rdd.map(lambda l: "Mot le plus long : " + l.word).collect()
        mostUsedFourWord=mostUsedFourWordDf.rdd.map(lambda l: "Mot de 4 lettres le plus fréquent : " + l.word).collect()
        mostUsedFifteenWord=mostUsedFifteenWordDf.rdd.map(lambda l: "Mot de 15 lettres le plus fréquent : " + l.word).collect()
        
        # et on imprime !!
        print(longestWord[0])
        print(mostUsedFourWord[0])
        print(mostUsedFifteenWord[0])

        #debug/opti :
        #input("press ctrl+c to exit")


if __name__ == "__main__":
    main()