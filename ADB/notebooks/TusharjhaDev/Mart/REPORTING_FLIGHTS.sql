-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_TJdatabase;

-- COMMAND ----------

DESC cleansed_tjdatabase.flights

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS REPORTING_FLIGHTS (
  date date,
  ArrDelay int,
  DepDelay int,
  Origin string,
  Cancelled string,
  CancellationCode string,
  UniqueCarrier string,
  FlightNum int,
  TailNum string,
  deptime string
) 
USING DELTA 
PARTITIONED BY (date_year int) 
LOCATION '/mnt/datalake_mart/REPORTING_FLIGHTS'

-- COMMAND ----------

desc REPORTING_FLIGHTS

-- COMMAND ----------

-- MAGIC %py
-- MAGIC #max_year=spark.sql("select year(max(date)) from cleansed_geekcoders.flight").collect()[0][0]
-- MAGIC max_year=2006

-- COMMAND ----------

-- MAGIC %py 
-- MAGIC
-- MAGIC spark.sql(f"""
-- MAGIC INSERT
-- MAGIC   OVERWRITE REPORTING_FLIGHTS PARTITION (date_year = {max_year}) 
-- MAGIC SELECT
-- MAGIC   date,
-- MAGIC   ArrDelay,
-- MAGIC   DepDelay,
-- MAGIC   Origin,
-- MAGIC   Cancelled,
-- MAGIC   CancellationCode,
-- MAGIC   UniqueCarrier,
-- MAGIC   FlightNum,
-- MAGIC   TailNum,
-- MAGIC   deptime
-- MAGIC FROM
-- MAGIC   cleansed_TJdatabase.flights where year(date)={max_year} """)

-- COMMAND ----------

select * from mart_TJdatabase.REPORTING_FLIGHTS

-- COMMAND ----------


