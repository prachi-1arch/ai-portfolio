# Recommendation System

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Surprise](https://img.shields.io/badge/Surprise-9C27B0?style=flat-square&logo=surprise&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)

</div>

## 🎯 Problem Statement

Hybrid recommendation engine combining collaborative filtering and content-based methods for e-commerce product recommendations.

## 🏗️ Architecture

```
User-Item Interaction Matrix
    ↓
Collaborative Filtering (SVD)
    ↓
Content-Based Filtering (TF-IDF on product descriptions)
    ↓
Hybrid Ensemble (Weighted Combination)
    ↓
Cold Start Handler (Popularity + Demographics)
    ↓
FastAPI Recommendation API
```

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| ML | Surprise, Scikit-learn |
| Matrix | SVD, NMF |
| API | FastAPI |

## 📊 Dataset

- **Source:** MovieLens / E-commerce dataset
- **Size:** 100K+ interactions
- **Users:** 1,000+
- **Items:** 1,700+

## 🚀 Installation

```bash
git clone https://github.com/prachi-1arch/ai-portfolio.git
cd 06-recommendation-system

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python train.py
```

## 📈 Results

| Metric | Value |
|--------|-------|
| **Precision@10** | 0.18 |
| **Recall@10** | 0.24 |
| **NDCG** | 0.31 |
| **CTR Improvement** | 28% |

## 🔮 Future Improvements

- [ ] Add deep learning collaborative filtering (Neural CF)
- [ ] Implement real-time user behavior updates
- [ ] Add A/B testing framework
- [ ] Deploy to Azure Container Apps

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
