# run_all_tests.py
import sys
import os
sys.path.insert(0, os.getcwd())

from project_tests import test_model
from project_tests import test_recommendation
from project_tests import test_cli

if __name__ == "__main__":
    print("Running model tests...")
    test_model.run_all_tests()

    print("\nRunning recommendation tests...")
    test_recommendation.run_all_tests()

    print("\nRunning CLI tests...")
    test_cli.run_all_tests()

    print("\n✅ All tests completed.")
