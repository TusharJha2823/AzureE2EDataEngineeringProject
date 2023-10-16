-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_TJdatabase;
-- MAGIC

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS DIM_UNIQUE_CARRIERS (
    code STRING,
  description STRING
) USING DELTA LOCATION '/mnt/datalake_mart/DIM_UNIQUE_CARRIERS'

-- COMMAND ----------

desc DIM_UNIQUE_CARRIERS

-- COMMAND ----------

-- MAGIC  %sql
-- MAGIC INSERT OVERWRITE DIM_UNIQUE_CARRIERS
-- MAGIC SELECT 
-- MAGIC   code STRING,
-- MAGIC   description STRING
-- MAGIC    FROM  cleansed_TJdatabase.unique_carriers 

-- COMMAND ----------

SELECT * FROM mart_TJdatabase.DIM_UNIQUE_CARRIERS

-- COMMAND ----------


