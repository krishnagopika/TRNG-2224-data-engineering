from pyspark.sql.functions import (
    current_timestamp, col, unix_timestamp, to_date,
    dayofweek, avg, round, count
)
from pyspark.sql.types import (
    StructType, StructField, StringType, TimestampType,
    DoubleType, IntegerType, LongType
)
from pyspark import pipelines

# Define the schema for the streaming source
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

# Get the path from config
source = spark.conf.get("source")

# Bronze: Raw data ingestion with schema
@pipelines.table(format="delta")
def bronze_taxi():
    return (
        spark.readStream.format("parquet")
        .schema(taxi_schema)
        .load(f"{source}/yellow_taxi/")
        .withColumn("processing_time", current_timestamp())
    )

# Silver: Clean and enrich with additional columns
@pipelines.table(format="delta")
def silver_taxi():
    return (
        spark.read.table("bronze_taxi")
        .filter(col("tpep_pickup_datetime").isNotNull() & col("tpep_dropoff_datetime").isNotNull())
        .withColumn("trip_duration_seconds",
                    unix_timestamp("tpep_dropoff_datetime") - unix_timestamp("tpep_pickup_datetime"))
        .withColumn("trip_date", to_date("tpep_pickup_datetime"))
        .withColumn("pickup_day_of_week", dayofweek("tpep_pickup_datetime"))
    )

# Gold: Aggregated daily summary
@pipelines.materialized_view()
def gold_taxi_daily_summary():
    return (
        spark.read.table("silver_taxi")
        .groupBy("trip_date")
        .agg(
            count("*").alias("total_trips"),
            round(avg("trip_duration_seconds"), 2).alias("avg_duration_secs")
        )
    )
