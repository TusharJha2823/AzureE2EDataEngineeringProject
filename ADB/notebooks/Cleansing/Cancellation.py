# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utilities

# COMMAND ----------

df = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("cloudFiles.schemaLocation", "/dbfs/FileStore/tables/schema/Cancellation1")
    .load("/mnt/raw_datalake/Cancellation/")
)

# COMMAND ----------

df.display()

# COMMAND ----------

df_base = df.selectExpr(
    "Code as code",
    "Description as description",
    "to_date('Date_Part','yyyy-MM-dd') as Date_Part"
)

# COMMAND ----------

df_base.writeStream.trigger(once=True).format("delta").option(
    "checkpointLocation", "/dbfs/FileStore/tables/checkpointLocation/Cancellation"
).start("/mnt/cleansed_datalake/Cancellation")

# COMMAND ----------

f_delta_cleansed_load('cancellation','/mnt/cleansed_datalake/Cancellation','cleansed_TJdatabase')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cleansed_TJdatabase.cancellation

# COMMAND ----------


