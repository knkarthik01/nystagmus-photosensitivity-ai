import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import subprocess

def test_cli_demo():
    cmd = [
        "python", "demo/demo_cli.py",
        "--brightness", "750",
        "--variance", "5",
        "--model_path", "dual_branch_cnn.pth"
    ]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        assert "Predicted Photosensitivity Risk Score" in result.stdout, "CLI output missing risk score"
        print("✅ test_cli_demo passed.")
    except Exception as e:
        print("❌ test_cli_demo failed:", e)

if __name__ == "__main__":
    test_cli_demo()
