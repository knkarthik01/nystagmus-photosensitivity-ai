# AI-Driven Assistive System for Visual Risk Prediction in Nystagmus Patients

## Abstract

Nystagmus patients with photosensitivity face significant daily challenges due to involuntary eye movements exacerbated by environmental brightness conditions. Current assistive solutions are limited to symptomatic treatments without predictive personalization. This project proposes an AI-driven system that predicts high-risk visual environments and recommends real-time visual adaptations. Using a dual-branch convolutional neural network (CNN) trained on synthetic and augmented datasets, the system estimates a "photosensitivity risk score" based on environmental brightness and eye movement variance. The model achieves a prototype accuracy of 75% on synthetic validation data. Explainability techniques such as SHAP and GradCAM are integrated to highlight environmental risk zones, improving trust and interpretability. The project includes full GitHub repository integration, with unit tests, explainability visualizations, and a working CLI demo, emphasizing reproducibility and expandability. Future directions include deployment via smart glasses and reinforcement learning for adaptive recommendations.

## 1. Introduction

Patients suffering from nystagmus and photosensitivity often encounter severe difficulties in focusing, maintaining balance, and performing everyday activities under various lighting conditions. Current treatments, such as tinted lenses, offer partial relief but are reactive rather than predictive. There is a strong need for proactive, personalized assistive technology that can predict and adapt to visual risks in real time. This paper presents an AI-based system designed to forecast photosensitivity risk levels and suggest optimal visual adaptations dynamically, thus aiming to improve quality of life for affected individuals.

## 2. Related Work

Existing research has made strides in gaze estimation (e.g., Gaze360) using convolutional neural networks to understand eye movement in varied environments. Separately, projects like AI-assisted migraine aura predictors have demonstrated the feasibility of using environmental data for health-related risk forecasting. Assistive technologies for visual impairment, such as the eSight wearable, showcase the effectiveness of real-time environmental adaptation, although none specifically target the unique challenges faced by nystagmus patients with photosensitivity. Recent work by Lee et al. [5] introduced ANyEye, a deep learning-based system for automated extraction of nystagmus from video-nystagmography recordings, addressing challenges such as motion artifacts and manual evaluation. While their focus was on diagnosing benign paroxysmal positional vertigo (BPPV) through pupil trajectory analysis, our approach targets real-time photosensitivity risk prediction and proactive adaptation for nystagmus patients.

## 3. Methodology

### 3.1 Data Generation and Preprocessing

We created a synthetic dataset to simulate real-world conditions for patients experiencing photosensitivity with nystagmus. Brightness levels ranged from 300 to 1200 lux, representing environments from dimly lit rooms to bright outdoor settings. Eye movement variances were generated with controlled standard deviations (2 to 10 pixels) to mimic mild to severe nystagmus symptoms.

Preprocessing involved:
- **Normalization**: Scaling brightness levels and variance values.
- **Noise Injection**: Simulating real-world irregularities in eye tracking.
- **Data Augmentation**: Brightness jittering, cropping, and mirroring to increase dataset diversity.
- **Synthetic Blurring**: For images to replicate vision disruption under severe photosensitivity.

This pipeline ensured the model could generalize across a wide range of possible patient experiences.

### 3.2 Model Architecture

The architecture was based on a dual-branch convolutional neural network:
- **Branch 1 (Environmental Brightness)**:
  - Input: 128x128 grayscale images.
  - Layers: 3 convolutional blocks (Conv -> BatchNorm -> ReLU -> MaxPool).
  - Output: Flattened feature vector.

- **Branch 2 (Eye Movement Variance)**:
  - Input: 1D vector of movement variances.
  - Layers: 2 fully connected dense layers.
  - Output: Feature embedding.

- **Fusion and Prediction**:
  - Concatenation of both branch outputs.
  - Two fully connected layers with dropout.
  - Sigmoid activation to output risk score between 0-1.

Training setup:
- **Loss Function**: Mean Squared Error (MSE) Loss.
- **Optimizer**: Adam (learning rate 0.001).
- **Epochs**: 30 with early stopping on validation loss.
- **Split**: 80% training / 20% validation.

*(Figure 1: Model Workflow Diagram)*

![Figure 1: Model Workflow Diagram](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/flow.png?raw=true)

### 3.3 Experimentation Process

Our experimentation followed a phased approach:
1. **Baseline Training**: Simple brightness-only models were first trained to set a performance baseline.
2. **Adding Eye Movement Variance**: Inclusion of variance features significantly boosted accuracy (~+10%).
3. **Tuning Hyperparameters**: Different learning rates (0.0001-0.01), optimizers (Adam, RMSprop), and architectures (deeper CNN vs shallower) were explored.
4. **Explainability Layer**: Integrated SHAP values to verify model reliance on correct features.
5. **Realistic Testing**: Used manually created "difficult" synthetic examples to stress-test model.

We observed that the dual-branch approach consistently outperformed single-modality models by a margin of 8-12% in accuracy.

### 3.4 Explainability Techniques

Explainability was critical for patient trust:
- **SHAP**: Applied after the fusion layer to attribute risk prediction to brightness vs eye movement inputs.
- **GradCAM**: Heatmaps overlaid on environmental images to identify high-risk visual zones.

*(Figure 2: GradCAM Visualization Example)*

![Figure 2: GradCAM Visualization Example](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/riskzone.png?raw=true)

### 3.5 Recommendation Engine and GitHub Mapping

Risk scores were interpreted via a simple rule-based engine:
- Risk score > 0.7: Recommend "Dark Amber" filter.
- Risk score 0.4-0.7: Recommend "Cool Grey" filter.
- Risk score < 0.4: No adaptation required.

**GitHub Mapping**:
- `models/cnn_dual_branch/model.py`: Dual-branch CNN implementation.
- `recommendation_engine/engine.py`: Risk scoring to filter mapping.
- `demo/demo_cli.py`: Command-line demo application.
- `project_tests/`: Comprehensive unit and integration tests.

*(Figure 3: Method + Recommendation Flow)*

![Figure 3: Method + Recommendation Flow](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/methodflow.png?raw=true)

## 4. Results

- **Model Performance**:
  - Validation accuracy: ~75% (thresholded classification from continuous risk score).

- **Sample Prediction Example**:
  - **Input**: 750 lux brightness, eye movement variance = 5.
  - **Predicted Risk**: 0.64 (Moderate Risk)
  - **Recommended Filter**: "Cool Grey"

- **Risk Score Visualization**:

*(Figure 4: Risk Score by Brightness and Eye Movement Variance)*

![Figure 4: Risk Score Visualization](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/riskfactors.png?raw=true)

- **Feature Importance via SHAP**:

*(Figure 5: SHAP Feature Importance)*

![Figure 5: SHAP Feature Importance](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/feature_importance.png?raw=true)

*(Figure 6: SHAP Summary Plot)*

![Figure 6: SHAP Summary Plot](https://github.com/knkarthik01/nystagmus-photosensitivity-ai/blob/main/data/img/SHAPvalue.png?raw=true)

- **Base Filter Recommendations**:

| Brightness | Eye Movement Variance | Suggested Filter | Note |
|:---|:---|:---|:---|
| High | High | Dark Amber | Maximum protection recommended |
| High | Low | Neutral Density | Stable eye movement, reduce brightness |
| Medium | High | Cool Grey | Moderate brightness + instability |
| Medium | Low | Light Grey | Moderate brightness + stable vision |
| Low | High/Low | No Filter | Natural vision sufficient |

- **Personalized Recommendations After User Feedback**:

| Brightness | Eye Movement Variance | Personalized Filter | Note |
|:---|:---|:---|:---|
| High | High | Dark Grey | Cooler preference, maximum protection |
| High | Low | Neutral Density | Stable, minor adjustment |
| Medium | High | Cool Grey | Cooler preference for strain reduction |
| Medium | Low | Medium Amber | Warmer tone, increased intensity |
| Low | High/Low | No Filter | Natural vision sufficient |

- **Feedback Simulation Summary**:
  - Updated profile: preference for cooler filters, sensitivity +0.175 adjustment.
  - Real-time adaptation of recommendations based on dynamic user input.

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
 

