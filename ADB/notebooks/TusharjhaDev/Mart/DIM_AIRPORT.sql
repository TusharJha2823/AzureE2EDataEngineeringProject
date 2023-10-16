-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_TJdatabase;
-- MAGIC

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS DIM_AIRPORT (
  code STRING,
  city STRING,
  country STRING,
  airport STRING
) USING DELTA LOCATION '/mnt/datalake_mart/DIM_AIRPORT'

-- COMMAND ----------

-- MAGIC  %sql
-- MAGIC INSERT OVERWRITE DIM_AIRPORT
-- MAGIC SELECT 
-- MAGIC code 
-- MAGIC ,city 
-- MAGIC ,country 
-- MAGIC ,airport 
-- MAGIC    FROM  cleansed_TJdatabase.airport 

-- COMMAND ----------

SELECT * FROM DIM_AIRPORT
