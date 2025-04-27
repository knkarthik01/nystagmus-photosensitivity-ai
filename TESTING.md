
# 🧪 TESTING Instructions for Nystagmus Photosensitivity AI Project

Welcome to the testing guide!  
This document explains **how to test and verify** that all parts of this project work correctly.

---

## 🚀 Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/knkarthik01/nystagmus-photosensitivity-ai.git
   cd nystagmus-photosensitivity-ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you are always at the project root when running tests.

---

## 🧩 Step 1: Run Notebooks

| Notebook | Purpose |
|:---|:---|
| `0_get_started.ipynb` | Setup environment |
| `1_data_preprocessing.ipynb` | Generate synthetic dataset and save CSV |
| `2_model_training.ipynb` | Train the model and save as `dual_branch_cnn.pth` |
| `3_explainability.ipynb` | Visualize SHAP explanations on test set |

> ⚡ **Tip:** Download generated CSVs and model checkpoints and upload to correct folders if needed.

✅ Ensure you can run each notebook end-to-end without errors.

---

## 🧩 Step 2: Run Project Tests

This project has full unit + integration tests inside `project_tests/`.

Run all tests from project root:

```bash
python project_tests/run_all_tests.py
```

It will automatically:
- Test model's forward pass and dummy training
- Test recommendation engine logic
- Test CLI demo behavior

✅ All tests should pass successfully.

---

## 🧩 Step 3: Test CLI Application Manually

You can also test the CLI demo manually:

```bash
python demo/demo_cli.py --brightness 750 --variance 5 --model_path dual_branch_cnn.pth
```

✅ Expected output:
- Predicted risk score
- Risk category (Low/High)
- Recommended filter suggestion (e.g., Dark Amber, Cool Grey)

---

## 📋 Troubleshooting Tips

| Issue | Solution |
|:---|:---|
| `ModuleNotFoundError: No module named 'models'` | Make sure you are running from project root, not inside a subfolder. |
| `dual_branch_cnn.pth not found` | Ensure model is trained and saved in project root or specify correct path. |
| `CSV file missing` | Regenerate using `1_data_preprocessing.ipynb`. |
| Notebook metadata rendering issues | Clear notebook outputs before pushing to GitHub. |

---

## 📦 Summary

✅ Run all notebooks  
✅ Run `python project_tests/run_all_tests.py`  
✅ Test CLI app manually

**Congratulations, your project is fully tested and verified!** 🎯

---

