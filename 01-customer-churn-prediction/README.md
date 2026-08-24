# Customer Churn Prediction

&lt;div align="center"&gt;

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EB5424?style=flat-square&logo=xgboost&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-FF6F00?style=flat-square&logo=shap&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

&lt;/div&gt;

## 🎯 Problem Statement

A telecom client was experiencing 15% annual customer churn. The goal was to build a predictive model that identifies at-risk customers 30 days before churn, enabling proactive retention campaigns.

## 🏗️ Architecture
Raw Data (SQL Server)
↓
ETL Pipeline (Python/Pandas)
↓
Feature Engineering (RFM, Tenure, Usage Patterns)
↓
Model Training (XGBoost + Cross-Validation)
↓
SHAP Explainability Layer
↓
FastAPI REST Service
↓
Power BI Monitoring Dashboard

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| ML Framework | XGBoost, Scikit-learn |
| Explainability | SHAP |
| API | FastAPI |
| Container | Docker |
| Database | SQL Server |
| Visualization | Power BI |

## 📊 Dataset

- **Source:** Telecom customer dataset
- **Size:** 7,043 customers
- **Features:** 21 (tenure, monthly charges, contract type, etc.)
- **Target:** Churn (Yes/No)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/prachi-1arch/ai-portfolio.git
cd 01-customer-churn-prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app:app --reload

## 📈 Results
| Metric        | Value |
| ------------- | ----- |
| **Accuracy**  | 91.2% |
| **Precision** | 89.0% |
| **Recall**    | 87.3% |
| **F1-Score**  | 88.1% |
| **AUC-ROC**   | 0.94  |

##  Business Impact:
Identified 2,400 high-risk customers in first month
Retention campaigns reduced churn by 22%
##  🔮 Future Improvements
[ ] Add real-time streaming with Kafka
[ ] Implement A/B testing framework for retention campaigns
[ ] Add automated retraining pipeline with MLflow
[ ] Deploy to Azure Kubernetes Service
##  📝 License
This project is licensed under the MIT License.


<div align="center">

Built with ❤️ by Prachi Desai

</div>
```
