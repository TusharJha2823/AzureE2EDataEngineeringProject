# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utilities

# COMMAND ----------

df = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("cloudFiles.schemaLocation", "/dbfs/FileStore/tables/schema/Unique_Carriers")
    .load("/mnt/raw_datalake/Unique_Carriers/")
)

# COMMAND ----------

df_base = df.selectExpr(
    "Code as code",
    "Description as description",
    "to_date('Date_Part','yyyy-MM-dd') as Date_Part"
)

# COMMAND ----------

df_base.writeStream.trigger(once=True).format("delta").option(
    "checkpointLocation", "/dbfs/FileStore/tables/checkpointLocation/Unique_Carriers"
).start("/mnt/cleansed_datalake/Unique_Carriers")

# COMMAND ----------

f_delta_cleansed_load('unique_carriers','/mnt/cleansed_datalake/Unique_Carriers','cleansed_TJdatabase')


# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cleansed_TJdatabase.unique_carriers
