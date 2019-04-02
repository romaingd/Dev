python -c "import nltk; nltk.download('stopwords')"

rm -r input
mkdir input

wget -P input http://classics.mit.edu/Homer/iliad.mb.txt
wget -P input http://classics.mit.edu/Homer/odyssey.mb.txt

hadoop=$HADOOP_HOME/bin/hadoop
$hadoop fs -rm -r input
$hadoop fs -mkdir -p input
$hadoop fs -copyFromLocal input/* input