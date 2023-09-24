-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_TJdatabase;
-- MAGIC

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS DIM_AIRLINES (
  iata_code STRING,
  icao_code STRING,
  name STRING
) USING DELTA LOCATION '/mnt/datalake_mart/DIM_AIRLINES'

-- COMMAND ----------

-- MAGIC  %sql
-- MAGIC INSERT OVERWRITE DIM_AIRLINES
-- MAGIC SELECT 
-- MAGIC iata_code 
-- MAGIC ,icao_code 
-- MAGIC ,name
-- MAGIC    FROM  cleansed_TJdatabase.airline 

-- COMMAND ----------

SELECT * FROM mart_TJdatabase.DIM_AIRLINES

-- COMMAND ----------


