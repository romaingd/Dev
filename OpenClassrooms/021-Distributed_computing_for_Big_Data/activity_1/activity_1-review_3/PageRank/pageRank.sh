#ln -s /usr/local/hadoop-3.1.2/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar hadoop-streaming.jar
hdfs dfs -mkdir /pagerank
hdfs dfs -put adj_list /pagerank
hdfs dfs -rm -r /pagerank/tmp
hdfs dfs -rm -r /pagerank/out
echo iteration 1 
hadoop jar hadoop-streaming.jar -D stream.num.map.output.key.fields=1 -D stream.num.reduce.output.fields=1 -files PageRankMapper.py,PageRankReducer.py -input /pagerank/adj_list -mapper PageRankMapper.py -reducer PageRankReducer.py -output /pagerank/tmp
for it in {2..8}
do
		echo iteration $it
		hadoop jar hadoop-streaming.jar -D stream.num.map.output.key.fields=1 -D stream.num.reduce.output.fields=1 -files PageRankMapper_loop.py,PageRankReducer_loop.py -input /pagerank/tmp -mapper PageRankMapper_loop.py -reducer PageRankReducer_loop.py -output /pagerank/out
		hdfs dfs -rm -r /pagerank/tmp
		hdfs dfs -mv /pagerank/out /pagerank/tmp
done

echo iteration finale
hadoop jar hadoop-streaming.jar -D stream.num.map.output.key.fields=1 -D stream.num.reduce.output.fields=1 -files PageRankMapper_loop.py,PageRankReducer_final.py -input /pagerank/tmp -mapper PageRankMapper_loop.py -reducer PageRankReducer_final.py -output /pagerank/out
hdfs dfs -rm -r /pagerank/tmp
