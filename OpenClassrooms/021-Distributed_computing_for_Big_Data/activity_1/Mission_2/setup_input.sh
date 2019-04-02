#!/bin/bash

rm results.txt

hadoop=$HADOOP_HOME/bin/hadoop
$hadoop fs -rm -r input
$hadoop fs -mkdir -p input
$hadoop fs -copyFromLocal _movies/graph/adj_list input
$hadoop fs -ls input