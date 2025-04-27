
# 📈 AI Solutions for Nystagmus Patients with Photosensitivity

![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)

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

3. **Open and run notebooks** in the `notebooks/` folder.

4. **View demo** (basic CLI coming soon in `demo/`).

---

## 📚 Working with Notebooks

This project uses Google Colab for development.  
Follow these best practices:

### 1. Setting up Environment
- Always run **`0_get_started.ipynb`** first.
- It clones the GitHub repo and installs required packages from `requirements.txt`.

### 2. Running the Workflow
| Step | Notebook | Purpose |
|:---|:---|:---|
| 1 | `1_data_preprocessing.ipynb` | Generate synthetic brightness and eye-movement dataset |
| 2 | `Manual Step` | **Download `preprocessed_data.csv`** and upload it to GitHub under `/data/preprocessed/` |
| 3 | `2_model_training.ipynb` | Train Dual-Branch CNN model using synthetic data |
| 4 | `3_explainability.ipynb` | Apply SHAP explainability on trained model |

> ⚡ **Note:** Always clear outputs before pushing notebooks back to GitHub for clean rendering.

---

## 📂 Important Notes
- **CSV Handling**:  
   - After generating `preprocessed_data.csv`, **download and upload manually** to GitHub under `/data/preprocessed/`.
   - Update notebook code paths accordingly if needed.

- **Notebook Cleanliness**:  
   - For GitHub uploads, ensure notebooks have **cleared outputs** to avoid rendering errors.

- **Colab Tip**:  
   - Saving directly from Colab to GitHub sometimes embeds unwanted metadata. Prefer downloading first if needed.

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
This project is licensed under the [Apache License](LICENSE).

---

## 👨‍💻 Project by
Karthik Prabhakar | [GitHub Profile](https://github.com/knkarthik01)
