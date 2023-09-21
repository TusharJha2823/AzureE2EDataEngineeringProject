# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utilities

# COMMAND ----------

df1 = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", "/dbfs/FileStore/tables/schema/flights")
    .load("/mnt/raw_datalake/flight/")
)

# COMMAND ----------

df1.display()

# COMMAND ----------

df1.dtypes

# COMMAND ----------

df_bro = df1.selectExpr(
    "Year",
     "Month",
    "DayofMonth",
    "DayOfWeek",
    "DepTime",
    "CRSDepTime",
    "ArrTime",
    "CRSArrTime",
    "UniqueCarrier",
    "FlightNum",
    "TailNum",
    "ActualElapsedTime",
    "CRSElapsedTime",
    "AirTime",
    "ArrDelay",
    "DepDelay",
     "Origin",
    "Dest",
    "Distance",
    "TaxiIn",
    "TaxiOut",
    "Cancelled",
    "CancellationCode",
    "Diverted",
    "CarrierDelay",
    "WeatherDelay",
    "NASDelay",
    "SecurityDelay",
    "LateAircraftDelay",
    "Date_Part"
)

# COMMAND ----------

df_bro.writeStream.trigger(once=True).format("delta").option(
    "checkpointLocation", "/dbfs/FileStore/tables/checkpointLocation/flights"
).start("/mnt/cleansed_datalake/flights")

# COMMAND ----------

f_delta_cleansed_load('flights','/mnt/cleansed_datalake/flights','cleansed_TJdatabase')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cleansed_TJdatabase.flights

# COMMAND ----------


