#!/bin/bash

hadoop=$HADOOP_HOME/bin/hadoop
$hadoop fs -mkdir -p input
wget http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt
$hadoop fs -copyFromLocal defoe-robinson-103.txt input
wget http://www.textfiles.com/etext/FICTION/callwild
$hadoop fs -copyFromLocal callwild input
$hadoop fs -ls input
