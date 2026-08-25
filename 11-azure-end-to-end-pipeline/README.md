# Azure End-to-End Data Pipeline

<div align="center">

![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
![Data Factory](https://img.shields.io/badge/Azure%20Data%20Factory-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
![Databricks](https://img.shields.io/badge/Azure%20Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
![Synapse](https://img.shields.io/badge/Azure%20Synapse-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)

</div>

## Overview

Production-grade ETL pipeline ingesting data from multiple sources, processing with Databricks, and serving via Synapse Analytics and Power BI.

## Architecture

```
Source Systems (SQL Server, SAP, APIs, Files)
    ↓
Azure Data Factory (Orchestration & Ingestion)
    ↓
Azure Data Lake Gen2 (Raw Zone)
    ↓
Azure Databricks (Transformation - Spark)
    ↓
Azure Data Lake Gen2 (Curated Zone)
    ↓
Azure Synapse Analytics (Serving Layer)
    ↓
Power BI (Visualization)
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Orchestration | Azure Data Factory |
| Compute | Azure Databricks (Spark) |
| Storage | ADLS Gen2 (Delta Lake) |
| Warehouse | Azure Synapse Analytics |
| BI | Power BI |
| CI/CD | Azure DevOps |
| Monitoring | Azure Monitor, Log Analytics |

## Repository Structure

```
├── pipelines/              # ADF pipeline definitions
│   ├── ingestion.json
│   ├── transformation.json
│   └── loading.json
├── notebooks/              # Databricks notebooks
│   ├── bronze_to_silver.py
│   └── silver_to_gold.py
├── scripts/                # SQL scripts for Synapse
│   ├── create_tables.sql
│   └── create_views.sql
├── infrastructure/         # Terraform / Bicep
│   ├── main.tf
│   └── variables.tf
├── tests/                  # Unit & integration tests
│   └── test_transformations.py
└── docs/                   # Documentation
    └── architecture.md
```

## CI/CD Pipeline

```yaml
# azure-pipelines.yml
stages:
- stage: Build
  jobs:
  - job: Validate
    steps:
      - script: pytest tests/
      - script: databricks workspace import-dir notebooks/

- stage: Deploy
  jobs:
  - job: DeployADF
    steps:
      - task: AzureResourceManagerTemplateDeployment@3
        inputs:
          deploymentScope: Resource Group
          templateLocation: Linked artifact
          csmFile: pipelines/
```

## Key Features

- CI/CD Integration — Automated deployment via Azure DevOps
- Data Quality — Great Expectations validation at each stage
- Monitoring — Azure Monitor alerts for pipeline failures
- Security — Managed Identity, Key Vault for secrets
- Scalability — Auto-scaling Databricks clusters
- Disaster Recovery — Geo-redundant storage

## Performance

| Metric | Value |
|--------|-------|
| **Daily Data Volume** | 500GB+ |
| **Pipeline Duration** | 45 minutes (end-to-end) |
| **Synapse Query** | <3s for complex joins |
| **Uptime** | 99.9% |

## License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
