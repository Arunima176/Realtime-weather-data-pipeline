
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

def process_weather_data():
    spark = SparkSession.builder \
        .appName("Weather Data Analysis") \
        .getOrCreate()

    df = spark.read.option("header", "true").csv("data/weather.csv")

    df.show()

    df = df.withColumn("temperature", df["temperature"].cast("float"))
    df.groupBy("city").agg(avg("temperature").alias("avg(temperature)")).show()

    spark.stop()
