
# 📈 AI Solutions for Nystagmus Patients with Photosensitivity

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Overview
This project develops an AI-driven system to predict photosensitivity risk and recommend real-time visual adaptations for patients suffering from **Nystagmus** with **photosensitivity** issues.

By analyzing **environmental images** and **eye movement patterns**, the model forecasts high-risk scenarios and suggests optimal filter adaptations to improve patient quality of life.

---

## 🏗️ Project Structure

```
nystagmus-photosensitivity-ai/
├── data/                     # Synthetic datasets and preprocessing scripts
├── models/                   # Dual-branch CNN architecture and training scripts
├── visualization/            # GradCAM and risk zone visualizations
├── recommendation_engine/    # Adaptive filter recommendation system
├── demo/                     # Demo application
├── experiments/              # Experiment tracking
├── docs/                     # ACM paper materials
├── presentation/             # Slides and recorded presentation
├── requirements.txt          # Project dependencies
└── README.md                  # This file
```

---

## 🚀 Quick Start

1. **Clone this repository**:
   ```bash
   git clone https://github.com/knkarthik01/nystagmus-photosensitivity-ai.git
   cd nystagmus-photosensitivity-ai
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Open and run notebooks** in `notebooks/` folder (coming soon).

4. **View demo** (basic CLI coming soon in `demo/`).

---

## 📊 Key Features

- 🧠 **Dual-Branch CNN**: Processes environmental brightness + eye movement variance.
- 🔥 **Explainable AI**: GradCAM and SHAP to visualize risk zones.
- 🧩 **Recommendation Engine**: Suggests optimal light filters based on real-time risk prediction.
- 🎯 **Synthetic Data Generator**: For flexible experiments and validation.

---

## 📚 Technologies Used
- Python
- PyTorch / TensorFlow (flexible)
- SHAP / GradCAM
- Google Colab
- Git & GitHub

---

## 🛠️ Future Directions
- Integration with wearable smart glasses.
- Reinforcement learning-based adaptive recommendations.
- Expansion using real-world patient datasets.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Project by
Karthik Prabhakar | [GitHub Profile](https://github.com/knkarthik01)
