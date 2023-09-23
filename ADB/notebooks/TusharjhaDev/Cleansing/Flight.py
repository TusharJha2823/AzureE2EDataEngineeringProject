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

spark.conf.set("spark.sql.legacy.timeParserPolicy","LEGACY")

# COMMAND ----------

from pyspark.sql.functions import concat_ws

df_bro = df1.selectExpr(
"to_date(concat_ws('-',year,month,dayofmonth),'yyyy-MM-dd') as date",
"from_unixtime(unix_timestamp(case when DepTime=2400 then 0 else DepTime End,'HHmm'),'HH:mm')  as deptime",
"from_unixtime(unix_timestamp(case when DepTime=2400 then 0 else DepTime End,'HHmm'),'HH:mm')  as CRSDepTime",
"from_unixtime(unix_timestamp(case when DepTime=2400 then 0 else DepTime End,'HHmm'),'HH:mm')  as ArrTime",
"from_unixtime(unix_timestamp(case when DepTime=2400 then 0 else DepTime End,'HHmm'),'HH:mm')  as CRSArrTime",
"UniqueCarrier",
"cast(FlightNum as int) as FlightNum",
"cast(TailNum as int) as TailNum" ,
"cast(ActualElapsedTime as int) as ActualElapsedTime",
"cast(CRSElapsedTime as int) as CRSElapsedTime",
"cast(AirTime as int) as AirTime",
"cast(ArrDelay as int) as ArrDelay",
"cast(DepDelay as int) as DepDelay",
 "Origin",
 "Dest",
 "cast(Distance as int) as  Distance",
 "cast(TaxiIn as int) as TaxiIn",
 "cast(TaxiOut as int) as TaxiOut",
 "Cancelled",
 "CancellationCode",
 "cast(Diverted as int) as castDiverted",
 "cast(CarrierDelay as int) as CarrierDelay",
 "cast(WeatherDelay as int) as WeatherDelay" ,
 "cast(NASDelay as int) as NASDelay",
 "cast(SecurityDelay as int) as SecurityDelay",
 "cast(LateAircraftDelay as int) as LateAircraftDelay" ,
 "to_date(Date_Part,'yyyy-MM-dd') as Date_Part "
)

# COMMAND ----------

df_bro.writeStream.trigger(once=True).format("delta").option(
    "checkpointLocation", "/dbfs/FileStore/tables/checkpointLocation/flights2"
).start("/mnt/cleansed_datalake/flights")

# COMMAND ----------

dbutils.fs.rm("/dbfs/FileStore/tables/checkpointLocation/flights1",  recurse=True)
display(dbutils.fs.ls("/dbfs/FileStore/tables/checkpointLocation/"))

# COMMAND ----------

f_delta_cleansed_load('flights','/mnt/cleansed_datalake/flights','cleansed_TJdatabase')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cleansed_TJdatabase.flights

# COMMAND ----------


