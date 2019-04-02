import pyspark
from pyspark.sql import Row

from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import StringIndexer

from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


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
# This is an Estimator, and its API is close to scikit-learn's fit/transform
vectorizer_transformer = vectorizer.fit(train_data)
# Fitting this Estimator yields a Transformer
train_bag_of_words = vectorizer_transformer.transform(train_data)
test_bag_of_words = vectorizer_transformer.transform(test_data)


# Convert the String labels to numbers for classification
label_indexer = StringIndexer(inputCol='label', outputCol='label_index')
label_indexer_transformer = label_indexer.fit(train_bag_of_words)
train_bag_of_words = label_indexer_transformer.transform(train_bag_of_words)
test_bag_of_words = label_indexer_transformer.transform(test_bag_of_words)


# Define an fit a classifier
classifier = NaiveBayes(
    labelCol='label_index',
    featuresCol='bag_of_words',
    predictionCol='label_index_predicted'
)
classifier_transformer = classifier.fit(train_bag_of_words)
# Predict the test labels
test_predicted = classifier_transformer.transform(test_bag_of_words)


# Evaluate the model's performance
evaluator = MulticlassClassificationEvaluator(
    labelCol='label_index',
    predictionCol='label_index_predicted',
    metricName='accuracy'
)
accuracy = evaluator.evaluate(test_predicted)
print('Accuracy = {:.2f}'.format(accuracy))