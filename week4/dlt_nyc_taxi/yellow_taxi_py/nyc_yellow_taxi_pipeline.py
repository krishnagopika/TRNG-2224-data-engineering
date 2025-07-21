from pyspark.sql.functions import (
    current_timestamp, col, unix_timestamp, to_date,
    dayofweek, avg, round, count
)
from pyspark.sql.types import (
    StructType, StructField, StringType, TimestampType,
    DoubleType, IntegerType, LongType
)

# Define schema
taxi_schema = StructType([
    StructField("VendorID", IntegerType(), True),
    StructField("tpep_pickup_datetime", TimestampType(), True),
    StructField("tpep_dropoff_datetime", TimestampType(), True),
    StructField("passenger_count", LongType(), True),
    StructField("trip_distance", DoubleType(), True),
    StructField("RatecodeID", LongType(), True),
    StructField("store_and_fwd_flag", StringType(), True),
    StructField("PULocationID", IntegerType(), True),
    StructField("DOLocationID", IntegerType(), True),
    StructField("payment_type", LongType(), True),
    StructField("fare_amount", DoubleType(), True),
    StructField("extra", DoubleType(), True),
    StructField("mta_tax", DoubleType(), True),
    StructField("tip_amount", DoubleType(), True),
    StructField("tolls_amount", DoubleType(), True),
    StructField("improvement_surcharge", DoubleType(), True),
    StructField("total_amount", DoubleType(), True),
    StructField("congestion_surcharge", DoubleType(), True),
    StructField("Airport_fee", DoubleType(), True)
])

# Paths (can be parameterized)
source_path = "/Volumes/workspace/nyc_taxi"
bronze_output_path = f"{source_path}/bronze"
bronze_checkpoint_path = f"{source_path}/checkpoints/bronze"
silver_output_path = f"{source_path}/silver"
silver_checkpoint_path = f"{source_path}/checkpoints/silver"
gold_output_path = f"{source_path}/gold"

#  Bronze 
bronze_df = (
    spark.readStream.format("parquet")
    .schema(taxi_schema)
    .load(f"{source_path}/yellow_taxi/")
    .withColumn("processing_time", current_timestamp())
)

bronze_df.writeStream \
    .format("delta") \
    .option("checkpointLocation", bronze_checkpoint_path) \
    .outputMode("append") \
    .trigger(once=True) \
    .start(bronze_output_path) \
    .awaitTermination()
#  Silver 
silver_df = (
    spark.readStream.format("delta")
    .load(bronze_output_path)
    .filter(col("tpep_pickup_datetime").isNotNull() & col("tpep_dropoff_datetime").isNotNull())
    .withColumn("trip_duration_seconds",
                unix_timestamp("tpep_dropoff_datetime") - unix_timestamp("tpep_pickup_datetime"))
    .withColumn("trip_date", to_date("tpep_pickup_datetime"))
    .withColumn("pickup_day_of_week", dayofweek("tpep_pickup_datetime"))
)

silver_df.writeStream \
    .format("delta") \
    .option("checkpointLocation", silver_checkpoint_path) \
    .outputMode("append") \
    .trigger(once=True) \
    .start(silver_output_path) \
    .awaitTermination()


# Gold
silver_batch_df = spark.read.format("delta").load(silver_output_path)

gold_df = (
    silver_batch_df.groupBy("trip_date")
    .agg(
        count("*").alias("total_trips"),
        round(avg("trip_duration_seconds"), 2).alias("avg_duration_secs")
    )
)

gold_df.write.format("delta").mode("overwrite").save(gold_output_path)
