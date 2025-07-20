from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("WordCountTest") \
    .getOrCreate()

# Sample data
data = ["hello world", "hello data", "hello spark"]

# Create RDD
rdd = spark.sparkContext.parallelize(data)

# Word Count Logic
word_counts = rdd.flatMap(lambda line: line.split()) \
                 .map(lambda word: (word, 1)) \
                 .reduceByKey(lambda a, b: a + b)

# Print result
for word, count in word_counts.collect():
    print(f"{word}: {count}")

spark.stop()
