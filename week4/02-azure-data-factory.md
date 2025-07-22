# Azure Data Factory + Databricks Integration

## Data Ingestion

Supports ingesting data from multiple sources, including:

- Azure Data Lake Storage (Gen1 & Gen2)
- Azure SQL Database / SQL Managed Instance
- Azure Blob Storage
- On-premises databases via integration runtime
- REST APIs, SaaS platforms, and more

## Connecting Azure Data Factory to Azure Databricks

- Use **Azure Databricks Linked Service** in ADF.
- Supported authentication methods:
  - Access Token (recommended for simplicity)
  - Managed Identity (User Assigned / System Assigned)
- Configure:
  - Workspace URL
  - Cluster (existing or job cluster)

## Creating Databricks Pipelines in ADF

- Add Databricks Notebooks or JAR tasks as individual ADF **activities**.
- Configure:
  - Base parameters
  - Dependency handling (On success, On failure, On skip)
- Supports chaining with other ADF activities like data movement, transformation, and conditional logic.

## Accessing Azure Blob Storage / Data Lake from Databricks

### Using Databricks Secrets

```sh
# create a scope
databricks secrets create-scope <scope-name>

# list scopes
databricks secrets list-scopes

# create the secret

databricks secrets put-secret --json '{
  "scope": "<scope-name>",
  "key": "<key-name>",
  "string_value": "<secret>" 
}'
# azure storage account key -> secret

```
```py
# account key

spark.conf.set(
    "fs.azure.account.key.<storage-account>.dfs.core.windows.net",
    dbutils.secrets.get(scope="<scope>", key="<storage-account-access-key>"))
```

<i><b>note:</b> for data consistency in azure blob storage, disable soft delete on blobs and container under data protection</i>

### monitoring pipelines

- monitor pipeline and activity runs via ADF Monitoring tab.
- enable alerts and metrics via Azure Monitor.
- debug data flows with run history and data preview.
- integrate logs and metrics into dashboards using Azure Monitor and Log Analytics.

**references:**

- [databricks secrets management](https://docs.databricks.com/aws/en/security/secrets/)
- [connect to azure blob storage or data lake](https://learn.microsoft.com/en-us/azure/databricks/connect/storage/azure-storage)