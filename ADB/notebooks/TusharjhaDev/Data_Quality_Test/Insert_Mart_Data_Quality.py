# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utlilities

# COMMAND ----------

# MAGIC %py
# MAGIC insert_query="select count(*) from mart_TJdatabase.DIM_UNIQUE_CARRIERS group by code having count(*)>1"
# MAGIC insert_test_cases("mart_TJdatabase",1,"Check if code is duplicated in the dim_uniquecarrier or not ",insert_query,0)

# COMMAND ----------

# MAGIC %py
# MAGIC insert_query="select count(*) from mart_TJdatabase.DIM_AIRPORT group by code having count(*)>1"
# MAGIC insert_test_cases("mart_TJdatabase",2,"Check if code is duplicated in the dim_airport or not ",insert_query,0)
