# Power BI Executive Dashboard

<div align="center">

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=power-bi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-Advanced-FF6F00?style=flat-square)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoft-sql-server&logoColor=white)

</div>

## Overview

Enterprise-grade executive dashboard providing real-time KPIs, financial metrics, and operational insights across business units.

## 🏗️ Architecture

```
Data Sources (SQL Server, Excel, APIs)
    ↓
Power Query ETL (Dataflows)
    ↓
Semantic Model (Star Schema)
    ↓
DAX Calculations (Measures + Calculated Columns)
    ↓
Row-Level Security (RLS)
    ↓
Power BI Service (Premium Capacity)
    ↓
Executive Dashboard (Mobile + Desktop)
```

## Dashboard Components

| Page | Description | Key Metrics |
|------|-------------|-------------|
| **Executive Summary** | High-level KPIs | Revenue, Profit, Growth |
| **Sales Analysis** | Regional & product breakdown | YoY Growth, Market Share |
| **Financial Overview** | P&L, Cash Flow | EBITDA, Net Margin |
| **Operational Metrics** | Efficiency & quality | OEE, Defect Rate |
| **Predictive Insights** | ML-powered forecasts | Next Quarter Projection |

## Technical Implementation

### DAX Highlights

```dax
// Year-over-Year Growth
YoY Growth % = 
VAR CurrentYear = [Total Sales]
VAR PreviousYear = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN
    DIVIDE(CurrentYear - PreviousYear, PreviousYear, 0)
```

### Power Query M Code

```m
let
    Source = Sql.Database("server", "database"),
    Filtered = Table.SelectRows(Source, each [Status] = "Active"),
    Transformed = Table.TransformColumnTypes(Filtered, {{"Date", type date}})
in
    Transformed
```

## Key Features

- Row-Level Security — Dynamic filtering by user role
- Incremental Refresh — Optimized for large datasets (50M+ rows)
- Drill-through — From summary to transaction-level detail
- What-if Parameters — Scenario modeling for planning
- AI Visuals — Key influencers and decomposition tree
- Mobile Optimized — Phone layout for executives on-the-go

## Performance Metrics

| Metric | Value |
|--------|-------|
| **Data Refresh** | <15 minutes (incremental) |
| **Report Load** | <3 seconds |
| **Concurrent Users** | 500+ |
| **Data Volume** | 50M+ rows |

## Deployment

1. Publish to Power BI Service
2. Configure Gateway for on-premise data
3. Set up RLS roles in Service
4. Schedule refresh (daily at 6 AM)
5. Distribute via App workspace

## License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
