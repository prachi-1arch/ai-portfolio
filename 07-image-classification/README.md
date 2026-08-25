# Image Classification with Transfer Learning

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![ResNet](https://img.shields.io/badge/ResNet-FF6F00?style=flat-square&logo=resnet&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

</div>

## 🎯 Problem Statement

Multi-class image classification using transfer learning with ResNet and EfficientNet architectures for product categorization.

## 🏗️ Architecture

```
Image Dataset
    ↓
Data Augmentation (Albumentations)
    ↓
Transfer Learning (ResNet50 / EfficientNet-B4)
    ↓
Fine-tuning (Last 3 layers + Classifier)
    ↓
Training with Learning Rate Scheduling
    ↓
Model Evaluation & Confusion Matrix
    ↓
ONNX Export for Inference
```

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| DL | PyTorch |
| Models | ResNet, EfficientNet |
| CV | OpenCV |
| Augmentation | Albumentations |

## 📊 Dataset

- **Source:** Custom product image dataset
- **Size:** 50,000 images
- **Classes:** 100 categories
- **Split:** 80/10/10 (train/val/test)

## 🚀 Installation

```bash
git clone https://github.com/prachi-1arch/ai-portfolio.git
cd 07-image-classification

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python train.py --model resnet50 --epochs 50
```

## 📈 Results

| Metric | Value |
|--------|-------|
| **Accuracy** | 96.3% |
| **Top-5 Accuracy** | 99.1% |
| **Inference Time** | 45ms (GPU) |
| **Model Size** | 85MB (ONNX) |

## 🔮 Future Improvements

- [ ] Add Grad-CAM visualization
- [ ] Implement model quantization for edge deployment
- [ ] Add active learning pipeline
- [ ] Deploy to Azure ML Managed Endpoints

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
