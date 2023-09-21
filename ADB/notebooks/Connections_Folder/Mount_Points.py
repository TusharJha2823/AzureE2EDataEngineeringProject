# Databricks notebook source
# tj-DatabricksScope

# COMMAND ----------

# MAGIC %scala 
# MAGIC // first we will create a mount point for the blob storage
# MAGIC // Databricks notebook source
# MAGIC
# MAGIC
# MAGIC val containerName = dbutils.secrets.get(scope="tj-DatabricksScope",key="containername")
# MAGIC val storageAccountName = dbutils.secrets.get(scope="tj-DatabricksScope",key="storageaccountname")
# MAGIC val sas = dbutils.secrets.get(scope="tj-DatabricksScope",key="sas-token")
# MAGIC val config = "fs.azure.sas." + containerName+ "." + storageAccountName + ".blob.core.windows.net"
# MAGIC

# COMMAND ----------

# MAGIC %scala
# MAGIC
# MAGIC dbutils.fs.mount(
# MAGIC source = dbutils.secrets.get(scope="tj-DatabricksScope",key="blob-mnt-path"),
# MAGIC mountPoint = "/mnt/source_blob/",
# MAGIC extraConfigs = Map(config -> sas))

# COMMAND ----------

# MAGIC
# MAGIC %py
# MAGIC configs = { "fs.azure.account.auth.type": "OAuth",
# MAGIC             "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
# MAGIC             "fs.azure.account.oauth2.client.id": dbutils.secrets.get(scope = "tj-DatabricksScope", key = "data-app-id"),
# MAGIC             "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="tj-DatabricksScope",key="data-app-secret-3"),
# MAGIC             "fs.azure.account.oauth2.client.endpoint": dbutils.secrets.get(scope = "tj-DatabricksScope", key = "data-client-refresh-url")}
# MAGIC  
# MAGIC   #Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC mountPoint="/mnt/raw_datalake/"
# MAGIC if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
# MAGIC     dbutils.fs.mount(
# MAGIC       source = dbutils.secrets.get(scope = "tj-DatabricksScope", key = "datalake-raw"),
# MAGIC       mount_point = mountPoint,
# MAGIC       extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls('/mnt/raw_datalake/')

# COMMAND ----------

# MAGIC %py
# MAGIC configs = { "fs.azure.account.auth.type": "OAuth",
# MAGIC             "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
# MAGIC             "fs.azure.account.oauth2.client.id": dbutils.secrets.get(scope = "tj-DatabricksScope", key = "data-app-id"),
# MAGIC             "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="tj-DatabricksScope",key="data-app-secret-3"),
# MAGIC             "fs.azure.account.oauth2.client.endpoint": dbutils.secrets.get(scope = "tj-DatabricksScope", key = "data-client-refresh-url")}
# MAGIC  
# MAGIC   #Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC mountPoint="/mnt/cleansed_datalake/"
# MAGIC if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
# MAGIC     dbutils.fs.mount(
# MAGIC       source = dbutils.secrets.get(scope = "tj-DatabricksScope", key = "datalake-cleansed"),
# MAGIC       mount_point = mountPoint,
# MAGIC       extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls('/mnt/cleansed_datalake/')
