# Databricks notebook source
# MAGIC %run /TusharjhaDev/Utilities

# COMMAND ----------

list_table_info = [
    ("Write", "plane", 10000),
    ("Write", "flights", 20000),
    ("Write", "airport", 10000),
    ("Write", "cancellation", 10000),
    ("Write", "unique_carriers", 5000),
    ("Write", "airline", 1000),
]
for i in list_table_info:
    f_count_check("cleansed_TJdatabase", i[0], i[1], i[2])

# COMMAND ----------


