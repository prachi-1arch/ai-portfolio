# Resume Screening using NLP

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![BERT](https://img.shields.io/badge/BERT-FF6F00?style=flat-square&logo=bert&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=flat-square&logo=spacy&logoColor=white)

</div>

## 🎯 Problem Statement

Automate candidate-job matching by classifying resumes into relevant job categories using NLP and transformer models, reducing HR screening time by 80%.

## 🏗️ Architecture

```
Resume PDFs / Text Files
    ↓
Text Extraction (PyPDF2 / pdfplumber)
    ↓
Preprocessing (Tokenization, Cleaning, NER)
    ↓
BERT Fine-tuning (Job Category Classification)
    ↓
Skill Extraction (spaCy NER)
    ↓
Matching Algorithm (Cosine Similarity)
    ↓
FastAPI Screening API
```

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| NLP | BERT, Hugging Face |
| NER | spaCy |
| Framework | PyTorch |
| API | FastAPI |

## 📊 Dataset

- **Source:** Kaggle Resume Dataset
- **Size:** 2,400 resumes
- **Categories:** 25 job roles
- **Format:** PDF and text files

## 🚀 Installation

```bash
git clone https://github.com/prachi-1arch/ai-portfolio.git
cd 03-resume-screening-nlp

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python train.py
```

## 📈 Results

| Metric | Value |
|--------|-------|
| **Accuracy** | 94.5% |
| **F1-Score (Macro)** | 93.8% |
| **Processing Time** | <2s per resume |
| **HR Time Saved** | 80% reduction |

## 🔮 Future Improvements

- [ ] Add multi-language resume support
- [ ] Implement zero-shot classification for new roles
- [ ] Add ATS integration
- [ ] Build candidate ranking dashboard

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
