# Azure End-to-End Data Engineering Project

So I have tried to build an Azure Data engineering project, where I have analyzed airline data and built a project around it. I have taken data from multiple sources which include - CSV, TXT, Parquet, JSON, excel files, and from an API. The data sources were either stored in blob or data lake storage with the exception of an API-based source. Using these data sources I have built a data pipeline in Azure Data Factory to first set up a raw layer where all the data was first brought in. Then using Databricks I created delta tables to clean the data and store it in an Azure Data Lake, This became my silver layer. To orchestrate all of this I used the Azure Data Factory. I further created a gold layer where I could put all my finalized data and publish it to an Azure Synapse SQL pool to act as a Data Warehouse.

I created an email notification option using logic apps webhook feature to notify whenever the pipeline was triggered.

