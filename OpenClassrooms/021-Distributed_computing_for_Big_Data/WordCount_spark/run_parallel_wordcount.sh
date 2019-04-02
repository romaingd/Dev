# Define a shorthand alias for readability
spark_submit=$SPARK_HOME/bin/spark-submit

# Prepare a long input
wget http://classics.mit.edu/Homer/iliad.mb.txt
for i in {1..100}
do
    cat iliad.mb.txt >> iliad100.txt
done

hadoop fs -mkdir -p input
hadoop fs -copyFromLocal ./iliad100.txt input

# Run and time WordCount using a single core
time ($spark_submit --master local[1] ./wordcount.py input/iliad100.txt)
# Run and time WordCount using 4 cores
time ($spark_submit --master local[4] ./wordcount.py input/iliad100.txt)