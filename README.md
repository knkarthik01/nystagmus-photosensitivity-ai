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
├── project_tests/            # Unit tests for core modules (safe naming)
├── docs/                     # ACM paper materials
├── notebooks/                # Colab/Notebook workflows
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

3. **Run notebooks** (Google Colab recommended):
   - `notebooks/0_get_started.ipynb` → Setup environment
   - `notebooks/1_data_preprocessing.ipynb` → Generate synthetic dataset
   - `notebooks/2_model_training.ipynb` → Train model and save
   - `notebooks/3_explainability.ipynb` → SHAP-based explainability

4. **Run all project tests**:
   ```bash
   python project_tests/run_all_tests.py
   ```

**Note**:  End to End model implementation is available in [model_implementation_end_to_end.ipynb](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/model_implementation_end_to_end.ipynb)   → Provides Visibility of end to end in notebook (Google Colab)

---

## 📚 Working with Notebooks

### Setting up Environment
- Always run **`0_get_started.ipynb`** first to install dependencies.

### Workflow Order
| Step | Notebook | Purpose |
|:---|:---|:---|
| 1 | `1_data_preprocessing.ipynb` | Generate synthetic dataset |
| 2 | `2_model_training.ipynb` | Train model and save weights |
| 3 | `3_explainability.ipynb` | SHAP explainability on test set |

> ⚡ **Tip:** Clear outputs before uploading to GitHub for clean rendering.

---

### Model Architecture
Our dual-branch neural network processes both brightness levels and eye movement variance:

#### Brightness Branch

Processes environmental brightness information
Feature extraction through multiple dense layers
Outputs a 32-dimensional feature vector

#### Eye Movement Branch

Processes eye movement variance signals
Parallel feature extraction
Outputs a 32-dimensional feature vector

#### Fusion Module

Concatenates features from both branches (64 features total)
Applies dropout for regularization
Final sigmoid activation for risk prediction (0-1)

#### Data Generation
Our project uses both real and synthetic data:
Synthetic Dataset

Brightness levels: 100-1000 lux (indoor to bright outdoor)
Eye movement variance: 0-10 (stable to severe nystagmus)
Risk scores: Generated using a probabilistic model with noise

#### Explainability
Our system uses SHAP (SHapley Additive exPlanations) to provide transparent explanations for model predictions:
SHAP Analysis

Explains how each feature contributes to risk prediction
Identifies whether brightness or eye movement has more impact
Creates visualizations for patient and clinician understanding

#### Recommendation Engine
Our system provides personalized filter recommendations based on environmental factors and user preferences:

 #### Base Recommendation System

Analyzes brightness levels and eye movement patterns
Recommends appropriate filters (Dark Amber, Cool Grey, Light Grey, etc.)
Provides explanatory notes with each recommendation

#### Personalized Recommendations

Adapts to user preferences over time
Accounts for personal sensitivity levels
Adjusts filter types (warmer/cooler) based on feedback
Modifies intensity based on user comfort

#### Web Demo (Local)
We provide a web-based demo using Streamlit:
Running the Web Demo

#### Install Streamlit:
pip install streamlit

#### (Optional)Launch the demo:
streamlit run demo/web_demo.py

Open your browser to the URL displayed in the terminal (typically http://localhost:8501)



## 🧪 Testability

This project includes fully integrated **testability** across core modules:

- `project_tests/test_model.py` → Model forward pass and dummy training
- `project_tests/test_recommendation.py` → Recommendation system unit tests
- `project_tests/test_cli.py` → CLI application behavior test

Run all tests from the project root:
```bash
python project_tests/run_all_tests.py
```

## 🧪 Full Testing Guide

For detailed testing instructions, see [TESTING.md](./TESTING.md).

---

✅ Ensures model, recommendation engine, and CLI app work reliably.

---

## 📂 Important Notes
- **CSV Handling**:  
   - After generating `preprocessed_data.csv`, **download and upload manually** to GitHub under `/data/preprocessed/` if needed.
- **CLI Assumptions**:  
   - Ensure model (`dual_branch_cnn.pth`) is trained and available.
- **Colab Usage**:  
   - Save copies to Drive if metadata issues occur when syncing with GitHub.

---

## 📊 Key Features

- 🧠 **Dual-Branch CNN**: Processes environmental brightness + eye movement variance
- 🔥 **Explainable AI**: SHAP and GradCAM visualizations
- 🧩 **Recommendation Engine**: Suggests optimal filters dynamically
- 🎯 **Synthetic Data Generator**: Flexible experiments and controlled testing

---

## 📚 Technologies Used
- Python
- PyTorch
- SHAP / GradCAM
- Google Colab
- Git & GitHub

---

## 🛠️ Future Directions
- Integration with wearable smart glasses
- Reinforcement learning for adaptive recommendations
- Expansion using real-world clinical datasets

---

## 📄 License
This project is licensed under the [Apache License](LICENSE).

---

## 👨‍💻 Project by
Karthik Prabhakar | [GitHub Profile](https://github.com/knkarthik01)
