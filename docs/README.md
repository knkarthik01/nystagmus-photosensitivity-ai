# AI-Driven Assistive System for Visual Risk Prediction in Nystagmus Patients

## Abstract

Nystagmus patients with photosensitivity face significant daily challenges due to involuntary eye movements exacerbated by environmental brightness conditions. Current assistive solutions are limited to symptomatic treatments without predictive personalization. This project proposes an AI-driven system that predicts high-risk visual environments and recommends real-time visual adaptations. Using a dual-branch convolutional neural network (CNN) trained on synthetic and augmented datasets, the system estimates a "photosensitivity risk score" based on environmental brightness and eye movement variance. The model achieves a prototype accuracy of 75% on synthetic validation data. Explainability techniques such as SHAP and GradCAM are integrated to highlight environmental risk zones, improving trust and interpretability. The project includes full GitHub repository integration, with unit tests, explainability visualizations, and a working CLI demo, emphasizing reproducibility and expandability. Future directions include deployment via smart glasses and reinforcement learning for adaptive recommendations.

## 1. Introduction

Patients suffering from nystagmus and photosensitivity often encounter severe difficulties in focusing, maintaining balance, and performing everyday activities under various lighting conditions. Current treatments, such as tinted lenses, offer partial relief but are reactive rather than predictive. There is a strong need for proactive, personalized assistive technology that can predict and adapt to visual risks in real time. This paper presents an AI-based system designed to forecast photosensitivity risk levels and suggest optimal visual adaptations dynamically, thus aiming to improve quality of life for affected individuals.

## 2. Related Work

Existing research has made strides in gaze estimation (e.g., Gaze360) using convolutional neural networks to understand eye movement in varied environments. Separately, projects like AI-assisted migraine aura predictors have demonstrated the feasibility of using environmental data for health-related risk forecasting. Assistive technologies for visual impairment, such as the eSight wearable, showcase the effectiveness of real-time environmental adaptation, although none specifically target the unique challenges faced by nystagmus patients with photosensitivity. Recent work by Lee et al. [5] introduced ANyEye, a deep learning-based system for automated extraction of nystagmus from video-nystagmography recordings, addressing challenges such as motion artifacts and manual evaluation. While their focus was on diagnosing benign paroxysmal positional vertigo (BPPV) through pupil trajectory analysis, our approach targets real-time photosensitivity risk prediction and proactive adaptation for nystagmus patients.

## 3. Methodology

### 3.1 Data Generation and Preprocessing

- **Synthetic Dataset**: Controlled variations of brightness levels (300-1200 lux) and eye movement variances (2-10 pixel standard deviation) were synthetically generated.
- **Preprocessing**: Normalization, random noise addition, and variance smoothing were used to simulate real-world eye movement patterns under different lighting conditions.

### 3.2 Model Architecture

- **Dual-Branch CNN**:
  - Branch 1: Processes environmental brightness images (input resolution: 128x128 grayscale).
  - Branch 2: Processes time series vectors representing eye movement variance.
- **Fusion Layer**: Fully connected layers merging both branches.
- **Output**: Photosensitivity risk score (continuous 0-1).
- **Training**: Adam optimizer (learning rate 0.001), MSE loss, trained over 30 epochs on 80/20 synthetic train-test split.

*(Figure 1: Model Workflow Diagram)*

![Figure 1: Model Workflow Diagram](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/flow.png?raw=true)

### 3.3 Explainability Techniques

- **SHAP**: Used on the fused feature layer to determine contribution of brightness vs eye movement variance.
- **GradCAM**: Applied on environmental images to visualize high-risk zones likely to trigger photosensitivity events.

*(Figure 2: GradCAM Visualization Example)*

![Figure 2: GradCAM Visualization Example](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/riskzone.png?raw=true)

### 3.4 Recommendation Engine and GitHub Mapping

- **Risk Thresholding**:
  - Risk score > 0.7: Recommend "Dark Amber" filter.
  - Risk score 0.4-0.7: Recommend "Cool Grey" filter.
  - Risk score < 0.4: No adaptation required.

- **GitHub Files**:
  - `models/cnn_dual_branch/model.py` - Dual-branch architecture.
  - `recommendation_engine/engine.py` - Simple rule-based recommender.
  - `demo/demo_cli.py` - CLI demo app.
  - `project_tests/` - Unit and integration tests for reliability.

*(Figure 3: Method + Recommendation Flow)*

![Figure 3: Method + Recommendation Flow](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/methodflow.png?raw=true)

## 4. Results

- **Model Performance**:
  - Validation accuracy: ~75% (thresholded classification from continuous risk score).

- **Sample Prediction Example**:
  - **Input**: 750 lux brightness, eye movement variance = 5.
  - **Predicted Risk**: 0.64 (Moderate Risk)
  - **Recommended Filter**: "Cool Grey"

- **Feature Importance via SHAP**:

| Feature | SHAP Importance Score |
|:---|:---|
| Brightness Level | 0.65 |
| Eye Movement Variance | 0.35 |

*(Mini chart can be added if needed)*

## 5. Conclusion and Future Work

This project demonstrates the feasibility of an AI-driven personalized assistive system for nystagmus patients facing photosensitivity challenges. The complete solution, including synthetic data generation, dual-branch deep learning model, explainability integration, and a real-time CLI demo, showcases both research potential and practical deployment readiness. Future work includes:

- Expansion to real patient datasets with wearable eye-trackers.
- Integration into wearable smart glasses with real-time risk adaptation.
- Reinforcement learning to dynamically update recommendations based on feedback.

## References

[1] Kellnhofer, P., et al. "Gaze360: Physically unconstrained gaze estimation in the wild." *ICCV 2019.*

[2] Ribeiro, M.T., et al. "Why Should I Trust You?" Explaining the Predictions of Any Classifier." *KDD 2016.*

[3] Bach, S., et al. "On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation." *PLOS ONE 2015.*

[4] eSight Corporation. "eSight Eyewear: Assistive technology for low vision." (Accessed 2024).

[5] Lee, Y., Lee, S., Han, J., Seo, Y. J., & Yang, S. (2023). "A nystagmus extraction system using artificial intelligence for video-nystagmography." *Scientific Reports, 13*(1), 11975.

---
