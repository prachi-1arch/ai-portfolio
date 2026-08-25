# Face Mask Detection (YOLOv8)

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=flat-square&logo=yolo&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

</div>

## 🎯 Problem Statement

Real-time face mask detection system using YOLOv8 for workplace safety compliance monitoring.

## 🏗️ Architecture

```
Video Stream / Images
    ↓
Frame Extraction
    ↓
YOLOv8 Object Detection (Face + Mask Classification)
    ↓
Real-time Annotation
    ↓
Compliance Logging
    ↓
Alert System (Optional)
```

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.9+ |
| CV | YOLOv8 |
| Framework | PyTorch |
| Stream | OpenCV |

## 📊 Dataset

- **Source:** Custom labeled dataset
- **Size:** 10,000 images
- **Classes:** With Mask, Without Mask, Incorrect Mask
- **Format:** YOLO format

## 🚀 Installation

```bash
git clone https://github.com/prachi-1arch/ai-portfolio.git
cd 08-face-mask-detection

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Run inference on video
python detect.py --source video.mp4 --weights best.pt
```

## 📈 Results

| Metric | Value |
|--------|-------|
| **mAP@0.5** | 0.94 |
| **FPS** | 30+ (NVIDIA T4) |
| **False Positive Rate** | 2.1% |
| **Detection Range** | 0.5m - 5m |

## 🔮 Future Improvements

- [ ] Add face recognition integration
- [ ] Implement edge deployment (Raspberry Pi / Jetson)
- [ ] Add analytics dashboard
- [ ] Support for multiple camera feeds

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by [Prachi Desai](https://github.com/prachi-1arch)**

</div>
