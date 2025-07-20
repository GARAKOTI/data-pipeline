from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
import json

spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .getOrCreate()
      
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","kafka:9092")\
    .option("subscribe", "random_users") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING) as json_str")

parsed_df = json_df.select("json_str")

query = parsed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
