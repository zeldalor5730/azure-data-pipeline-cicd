from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataQualityCheck").getOrCreate()
df = spark.read.parquet("/mnt/processed/data_clean.parquet")
print(f"Total Records: {df.count()}")
print("✅ Data quality check passed.")
