# AI-Driven Assistive System for Visual Risk Prediction in Nystagmus Patients

## Abstract
Nystagmus patients with photosensitivity face significant daily challenges due to involuntary eye movements exacerbated by environmental brightness conditions. Current assistive solutions are limited to symptomatic treatments without predictive personalization. This project proposes an AI-driven system that predicts high-risk visual environments and recommends real-time visual adaptations. Using a dual-branch convolutional neural network (CNN) trained on synthetic and augmented datasets, the system estimates a "photosensitivity risk score" based on environmental brightness and eye movement variance. The model achieves a prototype accuracy of 75% on synthetic validation data. Explainability techniques such as SHAP and GradCAM are integrated to highlight environmental risk zones, improving trust and interpretability. Future directions include deployment via smart glasses and reinforcement learning for adaptive recommendations.

## 1. Introduction
Patients suffering from nystagmus and photosensitivity often encounter severe difficulties in focusing, maintaining balance, and performing everyday activities under various lighting conditions. Current treatments, such as tinted lenses, offer partial relief but are reactive rather than predictive. There is a strong need for proactive, personalized assistive technology that can predict and adapt to visual risks in real time. This paper presents an AI-based system designed to forecast photosensitivity risk levels and suggest optimal visual adaptations dynamically, thus aiming to improve quality of life for affected individuals.

## 2. Related Work
Existing research has made strides in gaze estimation (e.g., Gaze360) using convolutional neural networks to understand eye movement in varied environments. Separately, projects like AI-assisted migraine aura predictors have demonstrated the feasibility of using environmental data for health-related risk forecasting. Assistive technologies for visual impairment, such as the eSight wearable, showcase the effectiveness of real-time environmental adaptation, although none specifically target the unique challenges faced by nystagmus patients with photosensitivity. Our system aims to bridge this gap.

## 3. Methodology

### 3.1 Data Generation
- **Synthetic Dataset**: Generated controlled variations of brightness levels and eye movement variances.
- **Preprocessing**: Normalization and augmentation techniques applied to simulate diverse real-world lighting scenarios.

### 3.2 Model Architecture
- **Dual-Branch CNN**:
  - Branch 1: Environmental image brightness features.
  - Branch 2: Eye movement signal features.
- Output: Photosensitivity risk score (0-1 scale).

### 3.3 Explainability
- **SHAP**: Feature attribution for input variance and brightness.
- **GradCAM**: Visualization of environmental "risk zones" contributing most to model predictions.

*(Insert Figure 1: Model Workflow Diagram Here)*

### 3.4 Recommendation Engine
A rule-based recommendation engine suggests real-time visual adaptations such as "Dark Amber" or "Cool Grey" filters based on predicted risk scores and environmental contexts.

## 4. Results
- Prototype achieved 75% accuracy on synthetic validation set.
- Typical output: Low risk in indoor LED environments, high risk under outdoor noon sunlight.
- Example recommendation: "Cool Grey" filter for moderate brightness with unstable eye movement.

*(Insert Figure 2: Example GradCAM visualization of high-risk zones in environmental images)*

## 5. Conclusion and Future Work
This project demonstrates the feasibility of an AI-driven personalized assistive system for nystagmus patients facing photosensitivity challenges. Despite using synthetic datasets initially, results indicate strong potential for real-world deployment. Future work includes:
- Expansion to real patient datasets.
- Integration into wearable smart glasses.
- Reinforcement learning for dynamic, user-adaptive visual risk mitigation.

## References
[1] Kellnhofer, P., et al. "Gaze360: Physically unconstrained gaze estimation in the wild." *ICCV 2019.*

[2] Ribeiro, M.T., et al. "Why Should I Trust You?" Explaining the Predictions of Any Classifier." *KDD 2016.*

[3] Bach, S., et al. "On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation." *PLOS ONE 2015.*

[4] eSight Corporation. "eSight Eyewear: Assistive technology for low vision." (Accessed 2024).

---
