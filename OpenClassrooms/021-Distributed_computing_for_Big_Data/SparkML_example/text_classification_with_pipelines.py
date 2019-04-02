import pyspark
from pyspark.sql import Row

from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import StringIndexer

from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

from pyspark.ml import Pipeline


sc = pyspark.SparkContext()
spark = pyspark.sql.session.SparkSession(sc)


# Load the training and test data
def load_dataframe(path):
    rdd = sc.textFile(path) \
            .map(lambda line: line.split()) \
            .map(lambda words: Row(label=words[0], words=words[1:]))
    return(spark.createDataFrame(rdd))

train_data = load_dataframe('input/20ng-train-all-terms.txt')
test_data = load_dataframe('input/20ng-test-all-terms.txt')


# Create a Bag of Words
vectorizer = CountVectorizer(inputCol='words', outputCol='bag_of_words')
# Convert the String labels to numbers for classification
label_indexer = StringIndexer(inputCol='label', outputCol='label_index')
# Learn using a Naive Bayes classifier
classifier = NaiveBayes(
    labelCol='label_index',
    featuresCol='bag_of_words',
    predictionCol='label_index_predicted'
)
# Build the pipeline
pipeline = Pipeline(stages=[vectorizer, label_indexer, classifier])
pipeline_model = pipeline.fit(train_data)


# Predict the test labels
test_predicted = pipeline_model.transform(test_data)


# Evaluate the model's performance
evaluator = MulticlassClassificationEvaluator(
    labelCol='label_index',
    predictionCol='label_index_predicted',
    metricName='accuracy'
)
accuracy = evaluator.evaluate(test_predicted)
print('Accuracy = {:.2f}'.format(accuracy))


# Trick to keep access to profiling GUI
input("Press Ctrl+C to exit")