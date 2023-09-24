-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_TJdatabase;
-- MAGIC

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS DIM_CANCELLATIONS (
code STRING,
  description STRING
) USING DELTA LOCATION '/mnt/datalake_mart/DIM_CANCELLATIONS'

-- COMMAND ----------

desc DIM_CANCELLATIONS


-- COMMAND ----------

-- MAGIC  %sql
-- MAGIC INSERT OVERWRITE DIM_CANCELLATIONS
-- MAGIC SELECT 
-- MAGIC code 
-- MAGIC ,description 
-- MAGIC    FROM  cleansed_TJdatabase.cancellation 

-- COMMAND ----------

SELECT * FROM DIM_CANCELLATIONS
