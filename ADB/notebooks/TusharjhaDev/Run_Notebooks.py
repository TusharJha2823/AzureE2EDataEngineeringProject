# Databricks notebook source
# Databricks notebook source
dbutils.widgets.text("Layer_Name","")
Layer_Name=dbutils.widgets.getArgument("Layer_Name")

# COMMAND ----------

Notebook_Path_Json = {
    "Raw": ["/TusharjhaDev/Raw_Sourcing/Raw_Plane"],
    "Cleansed": [
            "/TusharjhaDev/Cleansing/Airlines",
            "/TusharjhaDev/Cleansing/Airport",
            "/TusharjhaDev/Cleansing/Cancellation",
            "/TusharjhaDev/Cleansing/Flight",
            "/TusharjhaDev/Cleansing/Plane",
            "/TusharjhaDev/Cleansing/Unique_Carrier",    
    ],
    "Data_Quality_Cleansed": 
        ["/TusharjhaDev/Data_Quality_Test/Cleansing_Data_Quality"]
    ,
    "Mart": 
        [
            "/TusharjhaDev/Mart/DIM_AIRLINES",
            "/TusharjhaDev/Mart/DIM_AIRPORT",
            "/TusharjhaDev/Mart/DIM_PLANE",
            "/TusharjhaDev/Mart/DIM_UNIQUE_CARRIERS",
            "/TusharjhaDev/Mart/DIM_CANCELLATIONS",
            "/TusharjhaDev/Mart/REPORTING_FLIGHTS",
    ],
    "Data_Quality_Mart":["/TusharjhaDev/Data_Quality_Test/Excecute_Mart_Data_Quality"]
}

# COMMAND ----------

for notebook_paths in Notebook_Path_Json[Layer_Name]:
    print(notebook_paths)
    #dbutils.notebook.run(notebook_paths,0)

# COMMAND ----------


