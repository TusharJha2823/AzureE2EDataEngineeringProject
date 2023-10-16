-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_TJdatabase;
-- MAGIC

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS DIM_PLANE (
  tailid STRING,
  type STRING,
  manufacturer STRING,
  issue_date Date,
  model STRING,
  status String,
  aircraft_type String,
  engine_type String,
  year int
) USING DELTA LOCATION '/mnt/datalake_mart/DIM_PLANE'

-- COMMAND ----------

desc DIM_PLANE

-- COMMAND ----------

-- MAGIC  %sql
-- MAGIC INSERT OVERWRITE DIM_PLANE
-- MAGIC  SELECT 
-- MAGIC  tailid 
-- MAGIC  ,type 
-- MAGIC  ,manufacturer 
-- MAGIC  ,issue_date 
-- MAGIC  ,model 
-- MAGIC  ,status 
-- MAGIC  ,aircraft_type 
-- MAGIC  ,engine_type 
-- MAGIC  ,year
-- MAGIC    FROM  cleansed_TJdatabase.plane 

-- COMMAND ----------

SELECT * FROM mart_TJdatabase.DIM_PLANE

-- COMMAND ----------


