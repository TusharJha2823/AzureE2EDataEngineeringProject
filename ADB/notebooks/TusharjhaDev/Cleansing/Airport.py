# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utilities

# COMMAND ----------

df = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", "/dbfs/FileStore/tables/schema/Airport1")
    .load("/mnt/raw_datalake/Airport/")
)

# COMMAND ----------

display(dbutils.fs.ls("/dbfs/FileStore/tables/checkpointLocation/"))

# COMMAND ----------

df.display()

# COMMAND ----------

spark.conf.set("spark.sql.legacy.timeParserPolicy","LEGACY")

# COMMAND ----------

df_base = df.selectExpr(
    "Code as code",
    "split('Description',',')[0] as city",
    "split(split('Description',',')[1],':')[0] as country",
    "split(split('Description',',')[1],':')[1] as airport",
    "to_date('Date_Part','yyyy-MM-dd') as Date_Part"
)

# COMMAND ----------

df_base.writeStream.trigger(once=True).format("delta").option(
    "checkpointLocation", "/dbfs/FileStore/tables/checkpointLocation/Airport"
).start("/mnt/cleansed_datalake/airport")

# COMMAND ----------

f_delta_cleansed_load('airport','/mnt/cleansed_datalake/airport','cleansed_TJdatabase')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cleansed_TJdatabase.airport

# COMMAND ----------

# MAGIC %sql
# MAGIC update cleansed_TJdatabase.airport
# MAGIC set Date_Part = "2023-09-20";

# COMMAND ----------


