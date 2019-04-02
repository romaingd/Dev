#! /bin/bash

# Aliases are not working, so we need to redefine where $hadoop is
hadoop=$HADOOP_HOME/bin/hadoop

# Delete previous result folders to avoid errors
$hadoop fs -rm -r -f intermediate_input intermediate_results results

# Run the first step of PageRank, which is specific
$hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar \
    -D stream.num.map.output.key.fields=1 \
    -input input/* \
    -output intermediate_results \
    -mapper ~/Workspace/Exercises/03-PageRank/PageRankFirstMapper.py \
    -reducer ~/Workspace/Exercises/03-PageRank/PageRankEarlyReducer.py
$hadoop fs -rm -r intermediate_input
$hadoop fs -mv intermediate_results intermediate_input

# Run a loop of PageRank propagation steps
for i in 1 2 3      # 5 total steps 0 1 2 3 4
do
    $hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar \
        -D stream.num.map.output.key.fields=1 \
        -input intermediate_input/* \
        -output intermediate_results \
        -mapper ~/Workspace/Exercises/03-PageRank/PageRankSubsequentMapper.py \
        -reducer ~/Workspace/Exercises/03-PageRank/PageRankEarlyReducer.py
    $hadoop fs -rm -r intermediate_input
    $hadoop fs -mv intermediate_results intermediate_input
done

# Run the last step of PageRank, which is specific
$hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar \
    -D stream.num.map.output.key.fields=1 \
    -input intermediate_input/* \
    -output results \
    -mapper ~/Workspace/Exercises/03-PageRank/PageRankSubsequentMapper.py \
    -reducer ~/Workspace/Exercises/03-PageRank/PageRankLastReducer.py

# Delete intermediate results folders
$hadoop fs -rm -r intermediate_results
# Display results
$hadoop fs -cat results/*

# Copy the result to a local folder, to find the top n pages
$hadoop fs -cat results/part* > results.txt
# Find the top n pages, ranked by PageRank
python3 PageRankFindTopPages.py