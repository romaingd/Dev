
hdfs dfs -mkdir /input_tfidf/
hdfs dfs -mkdir /output_tfidf/
hdfs dfs -put callwild defoe-robinson-103.txt /input_tfidf/
# job 1 : wordcount dans chaque document
hadoop jar hadoop-streaming.jar -D stream.num.map.output.key.fields=2 -D stream.num.reduce.output.fields=2 -input /input_tfidf/* -output /output_tfidf/job1/ -file TFIDF_Mapper.py -mapper TFIDF_Mapper.py -file TFIDF_Reducer.py -reducer TFIDF_Reducer.py -file stopwords_en.txt

# job 2 : calcul du nombre de mots significatifs dans un document
hadoop jar hadoop-streaming.jar -D stream.num.map.output.key.fields=1 -D stream.num.reduce.output.fields=2 -input /output_tfidf/job1/part-00000 -output /output_tfidf/job2/ -file TFIDF_Mapper_2.py -mapper TFIDF_Mapper_2.py -file TFIDF_Reducer_2.py -reducer TFIDF_Reducer_2.py

# job 3 : calcul du TF-IDF sur 2 documents
hadoop jar hadoop-streaming.jar -D stream.num.map.output.key.fields=2 -D stream.num.reduce.output.fields=2 -input /output_tfidf/job2/part-00000 -output /output_tfidf/job3/ -file TFIDF_Mapper_3.py -mapper TFIDF_Mapper_3.py -file TFIDF_Reducer_3.py -reducer TFIDF_Reducer_3.py

hdfs dfs -get /output_tfidf/job3
#more job3/part-00000 | grep /input_tfidf/callwild | sort -r -t$'\t' -k3 | head -n 20

echo "top 20 Robinson"
cat job3/part-00000 | grep /defoe | cut -f 1,3 | LC_ALL=C sort -nr -k 2 | head -n20 | nl

echo ""
echo "top 20 Call of the Wild"
cat job3/part-00000 | grep /callwild | cut -f 1,3 | LC_ALL=C sort -nr -k 2 | head -n20 | nl
