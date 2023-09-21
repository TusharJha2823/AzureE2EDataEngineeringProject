# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utilities

# COMMAND ----------

df = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", "/dbfs/FileStore/tables/schema/Airlines")
    .load("/mnt/raw_datalake/airlines/")
)

# COMMAND ----------

df1 = spark.read.json("/mnt/raw_datalake/airlines/")
df1.display()

# COMMAND ----------

from pyspark.sql.functions import explode
df2= df1.select(explode("response"),"Date_Part")
display(df2)

# COMMAND ----------

df_final=df2.select("col.*","Date_Part")

# COMMAND ----------

df_final.write.format("delta").mode("overwrite").save("/mnt/cleansed_datalake/airline")

# COMMAND ----------

f_delta_cleansed_load('airline','/mnt/cleansed_datalake/airline','cleansed_TJdatabase')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cleansed_TJdatabase.airline

# COMMAND ----------


