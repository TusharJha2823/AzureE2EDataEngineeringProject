# Databricks notebook source
# MAGIC %py
# MAGIC def insert_test_cases(database,insert_id,insert_test_cases,insert_test_query,insert_expected_result):
# MAGIC     try:
# MAGIC         spark.sql(f"""create table if not exists {database}.insert_test_cases(
# MAGIC                  id int,
# MAGIC                  test_cases string,
# MAGIC                  test_query string,
# MAGIC                  expected_result int
# MAGIC
# MAGIC         )""")
# MAGIC         spark.sql(f"""insert into {database}.insert_test_cases(id,test_cases,test_query,expected_result) values({insert_id},'{insert_test_cases}','{insert_test_query}',{insert_expected_result})""")
# MAGIC     except Exception as err:
# MAGIC         print("Error occurred", str(err))

# COMMAND ----------

# MAGIC %py
# MAGIC def excecute_test_case(database):
# MAGIC     df=spark.sql(f"""select * from {database}.insert_test_cases """).collect()
# MAGIC     for i in df:
# MAGIC         orginal_result=spark.sql(f"""{i.test_query}""").collect()
# MAGIC         if(len(orginal_result)==i.expected_result):
# MAGIC             print("Test case is passed")
# MAGIC         else:
# MAGIC             raise Exception (f"{test_cases} is failed, Kindly check")
# MAGIC

# COMMAND ----------

# MAGIC %py
# MAGIC def pre_schema(location):
# MAGIC     try:
# MAGIC         df=spark.read.format('delta').load(f'{location}').limit(1)
# MAGIC         schema=""
# MAGIC         for i in df.dtypes:
# MAGIC            schema=schema+i[0]+" "+i[1]+","
# MAGIC         return schema[0:-1]
# MAGIC     except Exception as err:
# MAGIC         print("Error Ocurred ",str(err))
# MAGIC

# COMMAND ----------

# MAGIC %py
# MAGIC def f_delta_cleansed_load(table_name,location,database):
# MAGIC     try:
# MAGIC         schema=pre_schema(f'{location}')
# MAGIC         spark.sql(f"""DROP TABLE IF EXISTS {database}.{table_name}""");
# MAGIC         spark.sql(f"""
# MAGIC         Create table if not exists {database}.{table_name}
# MAGIC         ({schema})
# MAGIC         using delta
# MAGIC         location '{location}'
# MAGIC         """)
# MAGIC     except Exception as err:
# MAGIC         print("Error Occured ",str(err))

# COMMAND ----------

# MAGIC %py
# MAGIC def f_count_check(database,operation_type,table_name,number_diff):    
# MAGIC         spark.sql(f"""DESC HISTORY {database}.{table_name}""").createOrReplaceTempView("Table_count")
# MAGIC         count_current=spark.sql(f"""select operationMetrics.numOutputRows from Table_count where version=(select max(version) from Table_count where trim(lower(operation))=lower('{operation_type}'))""")
# MAGIC         if(count_current.first() is None):
# MAGIC            final_count_current=0
# MAGIC         else:
# MAGIC            final_count_current=int(count_current.first().numOutputRows)
# MAGIC         count_previous=spark.sql(f"""select operationMetrics.numOutputRows from Table_count where version<(select version from Table_count where lower(trim(operation))=lower('{operation_type}') order by version desc limit 1)""")
# MAGIC         if(count_previous.first() is None):
# MAGIC            final_count_previous=0
# MAGIC         else:
# MAGIC             final_count_previous=int(count_previous.first().numOutputRows)
# MAGIC         if((final_count_current-final_count_previous) > number_diff):
# MAGIC             #print("Differnce is huge in ",table_name)
# MAGIC             raise Exception("Differnce is huge in ",table_name)
# MAGIC         else:
# MAGIC             pass
# MAGIC

# COMMAND ----------


