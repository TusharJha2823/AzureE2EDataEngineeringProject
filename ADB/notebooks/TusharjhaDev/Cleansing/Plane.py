# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utilities

# COMMAND ----------

spark.conf.set("spark.sql.legacy.timeParserPolicy","LEGACY")

# COMMAND ----------

#dbutils.fs.rm("/dbfs/FileStore/tables/checkpointLocation/PLANE",  recurse=True)
display(dbutils.fs.ls("/dbfs/FileStore/tables/checkpointLocation/"))

# COMMAND ----------

df = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", "/dbfs/FileStore/tables/schema/Planes1")
    .load("/mnt/raw_datalake/Plane/")
)

# COMMAND ----------

df.display()

# COMMAND ----------

df_base = df.selectExpr(
    "tailnum as tailid",
    "type",
    "manufacturer",
    "to_date(issue_date) as issue_date",
    "model",
    "status",
    "aircraft_type",
    "engine_type",
    "cast(year as int) as year",
    "to_date('Date_Part','yyyy-MM-dd') as Date_Part",
)
df_base.writeStream.trigger(once=True).format("delta").option(
    "checkpointLocation", "/dbfs/FileStore/tables/checkpointLocation/Planes1"
).start("/mnt/cleansed_datalake/plane")

# COMMAND ----------

f_delta_cleansed_load('plane','/mnt/cleansed_datalake/plane','cleansed_TJdatabase')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cleansed_TJdatabase.plane

# COMMAND ----------

# MAGIC %sql
# MAGIC update cleansed_TJdatabase.plane 
# MAGIC set Date_Part = "2023-09-23"

# COMMAND ----------


