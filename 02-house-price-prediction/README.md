# House Price Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![CatBoost](https://img.shields.io/badge/CatBoost-FF6F00?style=flat-square&logo=catboost&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

</div>

## 🎯 Problem Statement

Build an accurate regression model to predict house prices based on property features, location, and market conditions. Target: minimize RMSE for real estate valuation.

## 🏗️ Architecture

```
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
```

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| ML Framework | Scikit-learn, CatBoost |
| Optimization | Optuna |
| API | FastAPI |
| Visualization | Matplotlib, Seaborn |

##  📊 Dataset

- **Source:** Kaggle House Prices Dataset
- **Size:** 1,460 training samples
- **Features:** 79 (square footage, bedrooms, location, etc.)
- **Target:** SalePrice (USD)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/prachi-1arch/ai-portfolio.git
cd 02-house-price-prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run training
python train.py --config config.yaml
```

## 📈 Results

| Metric | Value |
|--------|-------|
| **RMSE** | $12,450 |
| **MAE** | $8,200 |
| **R² Score** | 0.92 |
| **Kaggle Rank** | Top 5% |

## 🔮 Future Improvements

- [ ] Add geospatial features with GeoPandas
- [ ] Implement stacking ensemble with neural networks
- [ ] Add price trend forecasting component
- [ ] Deploy to Azure Container Instances

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
