#!/bin/bash

rm -r input
rm results.txt

hadoop=$HADOOP_HOME/bin/hadoop
$hadoop fs -mkdir -p input
wget -P input http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt
$hadoop fs -copyFromLocal input/defoe-robinson-103.txt input
wget -P input http://www.textfiles.com/etext/FICTION/callwild
$hadoop fs -copyFromLocal input/callwild input
$hadoop fs -ls input
