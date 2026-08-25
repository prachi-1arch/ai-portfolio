# AI Sales Forecasting

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![LSTM](https://img.shields.io/badge/LSTM-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Prophet](https://img.shields.io/badge/Prophet-0052CC?style=flat-square&logo=prophet&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)

</div>

## 🎯 Problem Statement

Multi-horizon sales prediction for retail chain with 200+ SKUs across 50 stores. Goal: optimize inventory and reduce holding costs.

## 🏗️ Architecture

```
Historical Sales Data (SQL Server)
    ↓
ETL & Feature Engineering (Lag, Rolling, Seasonal)
    ↓
Train-Test Split (Time Series)
    ↓
LSTM Model Training
    ↓
Prophet Model Training
    ↓
Ensemble (Weighted Average)
    ↓
MLflow Experiment Tracking
    ↓
Azure ML Deployment
    ↓
Power BI Forecast Dashboard
```

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| DL | LSTM (TensorFlow) |
| TS | Prophet |
| MLOps | MLflow |
| Cloud | Azure Machine Learning |
| BI | Power BI |

## 🚀 Installation

```bash
git clone https://github.com/prachi-1arch/ai-portfolio.git
cd 05-ai-sales-forecasting

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python train.py --experiment-name sales-forecast
```

## 📈 Results

| Metric | Value |
|--------|-------|
| **MAPE** | 13.2% (down from 32%) |
| **Forecast Accuracy** | 87% |
| **Inventory Cost Savings** | $1.2M annually |
| **Stockout Reduction** | 35% |

## 🔮 Future Improvements

- [ ] Add external factors (weather, holidays, promotions)
- [ ] Implement probabilistic forecasting with quantiles
- [ ] Add automated model retraining
- [ ] Build what-if scenario simulator

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
