# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utilities

# COMMAND ----------

df = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", "/dbfs/FileStore/tables/schema/Plane1")
    .load("/mnt/raw_datalake/Plane/")
)

# COMMAND ----------

df.display()

# COMMAND ----------

df_base = df.selectExpr(
    "'tailnum' as tailid",
    "type",
    "manufacturer",
    "to_date(issue_date) as issue_date",
    "model",
    "status",
    "aircraft_type",
    "engine_type",
    "year",
    "to_date('Date_Part','yyyy-MM-dd') as Date_Part",
)

# COMMAND ----------

df_base.writeStream.trigger(once=True).format("delta").option(
    "checkpointLocation", "/dbfs/FileStore/tables/checkpointLocation/PLANE"
).start("/mnt/cleansed_datalake/plane")

# COMMAND ----------

f_delta_cleansed_load('plane','/mnt/cleansed_datalake/plane','cleansed_TJdatabase')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cleansed_TJdatabase.plane

# COMMAND ----------


