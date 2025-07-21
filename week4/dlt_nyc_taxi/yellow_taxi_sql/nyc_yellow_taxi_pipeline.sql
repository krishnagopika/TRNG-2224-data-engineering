-- Create the bronze streaming table 
CREATE OR REFRESH STREAMING TABLE bronze_taxi
COMMENT "Streaming ingest of NYC Yellow Taxi data with metadata"
TBLPROPERTIES ('delta.feature.timestampNtz' = 'supported')
AS
SELECT 
  *,
  current_timestamp() AS processing_time
FROM STREAM read_files("${source}/yellow_taxi/",
  format => 'parquet'
);

-- Create the silver table
CREATE OR REFRESH STREAMING LIVE TABLE silver_taxi(
CONSTRAINT valid_trip_duration EXPECT (DATEDIFF(second, tpep_pickup_datetime, tpep_dropoff_datetime) > 0) ON VIOLATION DROP ROW,
CONSTRAINT positive_passenger_count EXPECT (passenger_count >= 0 AND passenger_count <= 6) ON VIOLATION DROP ROW,
CONSTRAINT reasonable_distance EXPECT (trip_distance >= 0 AND trip_distance <= 100) ON VIOLATION DROP ROW,
CONSTRAINT valid_fare EXPECT (fare_amount >= 0 AND fare_amount <= 1000) ON VIOLATION DROP ROW,
CONSTRAINT pickup_before_dropoff EXPECT (tpep_pickup_datetime < tpep_dropoff_datetime) ON VIOLATION DROP ROW
)
COMMENT "Cleaned & enriched taxi data"
TBLPROPERTIES ('delta.feature.timestampNtz' = 'supported')
AS
SELECT
  *,
  DATEDIFF(second, tpep_pickup_datetime, tpep_dropoff_datetime) AS trip_duration_seconds,
  DATE(tpep_pickup_datetime) AS trip_date,
  dayofweek(tpep_pickup_datetime) AS pickup_day_of_week
FROM
  STREAM bronze_taxi
WHERE 
  tpep_pickup_datetime IS NOT NULL AND tpep_dropoff_datetime IS NOT NULL;

-- Create a gold materialized view for dialy aggregates

CREATE OR REFRESH MATERIALIZED VIEW gold_taxi_daily_summary
COMMENT "Daily aggregated trip metrics"
AS
SELECT
  trip_date,
  COUNT(*) AS total_trips,
  ROUND(AVG(trip_duration_seconds), 2) AS avg_duration_secs
FROM  silver_taxi
GROUP BY trip_date;


