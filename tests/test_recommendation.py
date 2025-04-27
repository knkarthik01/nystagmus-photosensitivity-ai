import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from recommendation_engine.recommend_filter import recommend_filter

def test_recommendation_dark_amber():
    rec = recommend_filter(brightness_level=900, eye_movement_variance=6)
    assert rec['filter'] == 'Dark Amber', "Expected Dark Amber filter"
    print("✅ test_recommendation_dark_amber passed.")

def test_recommendation_light_grey():
    rec = recommend_filter(brightness_level=500, eye_movement_variance=2)
    assert rec['filter'] == 'Light Grey', "Expected Light Grey filter"
    print("✅ test_recommendation_light_grey passed.")

if __name__ == "__main__":
    test_recommendation_dark_amber()
    test_recommendation_light_grey()
