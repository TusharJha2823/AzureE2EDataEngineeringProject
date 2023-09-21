# Databricks notebook source
pip install tabula-py

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

pip install commons

# COMMAND ----------

import tabula

# COMMAND ----------

from datetime import date
def f_source_pdf_datalake(source_path,sink_path,output_format,page,file_name):
    try:
        dbutils.fs.mkdirs(f"/{sink_path}{file_name.split('.')[0]}/Date_Part={date.today()}/")
        tabula.convert_into(f'{source_path}{file_name}',f"/dbfs/{sink_path}{file_name.split('.')[0]}/Date_Part={date.today()}/{file_name.split('.')[0]}.{output_format}",output_format=output_format,pages=page)
    except Exception as err:
        print("Error Occured ",str(err))

list_files=[(i.name,i.name.split('.')[1]) for i in dbutils.fs.ls('/mnt/source_blob/') if(i.name.split('.')[1]=='pdf')]
for i in list_files:
    f_source_pdf_datalake('/dbfs/mnt/source_blob/','mnt/raw_datalake/','csv','all',i[0])


# COMMAND ----------


