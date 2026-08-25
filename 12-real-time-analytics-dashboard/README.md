# Real-time Analytics Dashboard

<div align="center">

![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
![Event Hubs](https://img.shields.io/badge/Azure%20Event%20Hubs-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
![Stream Analytics](https://img.shields.io/badge/Stream%20Analytics-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
![Cosmos DB](https://img.shields.io/badge/Azure%20Cosmos%20DB-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)

</div>

## Overview

Real-time streaming analytics pipeline processing IoT sensor data and business events for live operational dashboards.

## Architecture

```
Event Sources (IoT Sensors, Web Apps, APIs)
    ↓
Azure Event Hubs (Ingestion)
    ↓
Azure Stream Analytics (Real-time Processing)
    ↓
Azure Cosmos DB (Hot Store)
    ↓
Power BI (Real-time Dashboard)
    ↓
Azure Data Lake (Cold Store for History)
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Ingestion | Azure Event Hubs |
| Processing | Azure Stream Analytics (ASA) |
| Hot Store | Azure Cosmos DB |
| Cold Store | Azure Data Lake Gen2 |
| Visualization | Power BI Streaming Dataset |
| Alerts | Azure Logic Apps |

## Stream Analytics Query

```sql
-- Real-time aggregation per minute
SELECT
    DeviceId,
    System.Timestamp() AS WindowEnd,
    AVG(Temperature) AS AvgTemp,
    MAX(Temperature) AS MaxTemp,
    MIN(Temperature) AS MinTemp,
    COUNT(*) AS EventCount
INTO
    [CosmosDBOutput]
FROM
    [EventHubInput]
TIMESTAMP BY EventTime
GROUP BY
    DeviceId,
    TumblingWindow(minute, 1)
HAVING
    AVG(Temperature) > 75
```

## Key Features

- Sub-second Latency — From event ingestion to dashboard
- Tumbling Windows — 1-minute, 5-minute, 1-hour aggregations
- Anomaly Detection — ASA ML functions for outlier detection
- Auto-scaling — Event Hubs throughput units auto-scale
- Alerts — Logic Apps trigger on threshold breaches
- Historical Analysis — Data Lake for batch analytics

## Performance

| Metric | Value |
|--------|-------|
| **Events/Second** | 10,000+ |
| **End-to-End Latency** | <2 seconds |
| **Dashboard Refresh** | Real-time (push dataset) |
| **Data Retention** | 90 days (Cosmos DB), 7 years (Data Lake) |

## License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
