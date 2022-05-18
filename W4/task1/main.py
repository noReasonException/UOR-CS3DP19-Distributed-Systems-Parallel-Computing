# Import SparkSession
from pyspark import StorageLevel
from pyspark.sql import SparkSession
import pandas as pd
# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate()

rddA = spark.read.option("header",True).csv("data/crime.csv").toDF("cdatetime", "address", "district", "beat", "grid", "crimedescr", "ucr_ncic_code", "latitude", "longitude")
df = rddA.select(rddA.crimedescr)
dfb=df.groupBy(df.crimedescr).count()
pandas = dfb.toPandas().to_csv("data/results.csv")
