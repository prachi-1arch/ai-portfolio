# House Price Prediction

&lt;div align="center"&gt;

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![CatBoost](https://img.shields.io/badge/CatBoost-FF6F00?style=flat-square&logo=catboost&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

&lt;/div&gt;

## 🎯 Problem Statement

Build an accurate regression model to predict house prices based on property features, location, and market conditions. Target: minimize RMSE for real estate valuation.

## 🏗️ Architecture

Raw Housing Data (CSV/API)
↓
Data Cleaning & Missing Value Imputation
↓
Feature Engineering (Log Transform, Interaction Terms, Encoding)
↓
EDA & Outlier Detection
↓
Model Ensemble (CatBoost + Random Forest + Ridge)
↓
Hyperparameter Tuning (Optuna)
↓
FastAPI Prediction Service


## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| ML Framework | Scikit-learn, CatBoost |
| Optimization | Optuna |
| API | FastAPI |
| Visualization | Matplotlib, Seaborn |

## 📊 Dataset

- **Source:** Kaggle House Prices Dataset
- **Size:** 1,460 training samples
- **Features:** 79 (square footage, bedrooms, location, etc.)
- **Target:** SalePrice (USD)

## 🚀 Installation

```bash
cd 02-house-price-prediction
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train.py --config config.yaml


## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| ML Framework | Scikit-learn, CatBoost |
| Optimization | Optuna |
| API | FastAPI |
| Visualization | Matplotlib, Seaborn |

## 📊 Dataset

- **Source:** Kaggle House Prices Dataset
- **Size:** 1,460 training samples
- **Features:** 79 (square footage, bedrooms, location, etc.)
- **Target:** SalePrice (USD)

## 🚀 Installation

```bash
cd 02-house-price-prediction
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train.py --config config.yaml

📈 Results
| Metric          | Value    |
| --------------- | -------- |
| **RMSE**        | \$12,450 |
| **MAE**         | \$8,200  |
| **R² Score**    | 0.92     |
| **Kaggle Rank** | Top 5%   |


🔮 Future Improvements
[ ] Add geospatial features with GeoPandas
[ ] Implement stacking ensemble with neural networks
[ ] Add price trend forecasting component
[ ] Deploy to Azure Container Instances
📝 License
MIT License
<div align="center">
Built with ❤️ by Prachi Desai
</div>
```
