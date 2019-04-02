rm -r input
mkdir input

wget -P input http://ana.cachopo.org/datasets-for-single-label-text-categorization/20ng-train-all-terms.txt
wget -P input http://ana.cachopo.org/datasets-for-single-label-text-categorization/20ng-test-all-terms.txt

hadoop=$HADOOP_HOME/bin/hadoop
$hadoop fs -rm -r input
$hadoop fs -mkdir -p input
$hadoop fs -copyFromLocal input/* input