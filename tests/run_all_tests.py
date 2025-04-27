
import subprocess

def run_test(script):
    print(f"Running {script}...")
    result = subprocess.run(["python", f"tests/{script}"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ {script} FAILED.")
    else:
        print(f"✅ {script} PASSED.")

if __name__ == "__main__":
    tests = [
        "test_model.py",
        "test_recommendation.py",
        "test_cli.py"
    ]
    for test in tests:
        run_test(test)
