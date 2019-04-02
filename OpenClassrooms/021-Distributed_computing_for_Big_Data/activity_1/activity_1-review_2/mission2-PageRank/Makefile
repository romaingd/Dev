DBARCHIVE=_movies.tar.Z
INPUT=input
DBFILE=_movies/graph/adj_list
PACKAGE=asauve

# Task 1
OUTPUT=prank
FMT=%03d
JAR=pmatrix.jar
PARAM_N=7967
PARAM_S=0.15
PARAM_NITER=14


run: task

best20: task
	hdfs dfs -cat `printf $(OUTPUT)$(FMT) $(PARAM_NITER)`/* | grep x | sed -e s/x// | python3 ./TFIDF_Sorter.py | head -20

zip:
	ZIP="mission-hadoop" && make clean && cd ../.. && zip -r $$ZIP.zip ./$$ZIP

task: $(INPUT) $(JAR)
	hadoop jar $(JAR) asauve.pagerank.PageRankDriver $(INPUT) $(OUTPUT)$(FMT) $(PARAM_N) $(PARAM_S) $(PARAM_NITER)
	touch task

$(INPUT): $(DBARCHIVE)
	tar -zxvf $(DBARCHIVE)
	hdfs dfs -mkdir -p $(INPUT)
	hdfs dfs -put -f $(DBFILE) $(INPUT)
	touch $(INPUT)

$(DBARCHIVE):
	wget https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/realisez-des-calculs-distribues-sur-des-donnees-massives/_movies.tar.Z -O $(DBARCHIVE)
	

$(JAR): asauve/pagerank/*.java
	mkdir -p classes
	javac -classpath $$HADOOP_CLASSPATH -d classes  asauve/pagerank/*.java
	jar cvf $(JAR) -C classes asauve

clean: clean-task
	hdfs dfs -rm -r -f $(INPUT)
	rm -f input $(DBARCHIVE)
	rm -rf _movies classes

clean-task: 
	hdfs dfs -rm -r -f "$(OUTPUT)*"
	rm -f task


clean-bluej:
	find . -name *.bluej -exec rm '{}' ';'


