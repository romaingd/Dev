#
# Download inputs and import into HDFS
#

FILES=defoe-robinson-103.txt callwild
NDOC_CORPUS=2
OUTPUT1=/user/$(USER)/results1
OUTPUT2=/user/$(USER)/results2
STOPWORDS=stopwords_en.txt
HADOOP_STREAM=$$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar


all: input run


input: hdfs-input $(FILES) $(STOPWORDS)


run: task1 task2 best20


task1:
	hadoop jar "$(HADOOP_STREAM)"  \
		-D mapreduce.job.name="Mission1-Task1-Count" \
		-D mapreduce.framework.name=local \
		-input `for F in $(FILES); do echo input/$$F; done` \
		-output $(OUTPUT1)  \
		-file  $(STOPWORDS) -file WordCountMapper.py -file WordPerDocReducer.py \
		-mapper "WordCountMapper.py"  \
		-reducer "WordPerDocReducer.py" \
	&& touch task1


task2: task1
	hadoop jar "$(HADOOP_STREAM)"  \
		-D mapreduce.job.name="Mission1-Task2-TFIDF" \
		-D mapreduce.framework.name=local \
		-input $(OUTPUT1)/ \
		-output $(OUTPUT2) \
		-file   Identity.sh \
		-file   TFIDF_Reducer.py \
		-mapper Identity.sh \
		-cmdenv NDOC=$(NDOC_CORPUS) \
		-reducer "TFIDF_Reducer.py" \
	&& touch task2


best20: task1 task2
	hdfs dfs -cat $(OUTPUT2)/* | python3 ./TFIDF_Sorter.py | head -20


clean: clean-input clean-run


clean-input:
	rm -f $(FILES) $(STOPWORDS)
	hdfs dfs -rm -f -r input
	rm -f hdfs-input


clean-run:
	hdfs dfs -rm -r -f $(OUTPUT1) $(OUTPUT2)
	rm -f task1 task2


hdfs-input:
	hdfs dfs -mkdir -p input
	touch hdfs-input


defoe-robinson-103.txt:
	wget -q http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt
	hdfs dfs -put -f defoe-robinson-103.txt input/


callwild:
	wget -q http://www.textfiles.com/etext/FICTION/callwild
	hdfs dfs -put -f callwild input/callwild


$(STOPWORDS):
	wget -q https://sites.google.com/site/kevinbouge/stopwords-lists/stopwords_en.txt


test1: hdfs-input
	( for F in $(FILES) ; do \
		cat $$F \
		| mapreduce_map_input_file=$$F ./WordCountMapper.py \
		| ./WordPerDocReducer.py ; \
	done ) \
	| sort

test2: hdfs-input
	( for F in $(FILES) ; do \
		cat $$F \
		| mapreduce_map_input_file=$$F ./WordCountMapper.py \
		| ./WordPerDocReducer.py ; \
	done ) \
	| sort \
	| NDOC=2 ./TFIDF_Reducer.py

