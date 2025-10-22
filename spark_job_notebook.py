from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL_CICD_Pipeline").getOrCreate()
df = spark.read.option("header", True).csv("/mnt/raw/data.csv")
clean_df = df.dropna()
clean_df.write.mode("overwrite").parquet("/mnt/processed/data_clean.parquet")
print("✅ ETL job completed successfully.")
