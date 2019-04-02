#! /bin/bash

# Aliases are not working, so we need to redefine where $hadoop is
hadoop=$HADOOP_HOME/bin/hadoop

# Delete previous result folders to avoid errors
$hadoop fs -rm -r -f wordcount_results wordperdoc_results results
# Run WordCount and store results in an intermediate folder
$hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar \
    -D stream.num.map.output.key.fields=2 \
    -files stopwords_en.txt \
    -input input/* \
    -output wordcount_results \
    -mapper ~/Workspace/Exercises/02-TF_IDF/WordCountMapper.py \
    -reducer ~/Workspace/Exercises/02-TF_IDF/WordCountReducer.py
# Run WordPerDoc and store results in an intermediate folder
$hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar \
    -D stream.num.map.output.key.fields=1 \
    -input wordcount_results/* \
    -output wordperdoc_results \
    -mapper ~/Workspace/Exercises/02-TF_IDF/WordPerDocMapper.py \
    -reducer ~/Workspace/Exercises/02-TF_IDF/WordPerDocReducer.py
# Run TF-IDF and store definitive results
$hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar \
    -D stream.num.map.output.key.fields=1 \
    -input wordperdoc_results/* \
    -output results \
    -mapper ~/Workspace/Exercises/02-TF_IDF/TFIDFMapper.py \
    -reducer ~/Workspace/Exercises/02-TF_IDF/TFIDFReducer.py
# Delete intermediate results folders
$hadoop fs -rm -r wordcount_results wordperdoc_results
# Display results
$hadoop fs -cat results/part* > results.txt