
import argparse
import torch
from models.cnn_dual_branch.model import DualBranchNet
from recommendation_engine.recommend_filter import recommend_filter

def load_model(model_path):
    model = DualBranchNet()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def predict_risk(model, brightness_level, eye_movement_variance):
    input_tensor = torch.tensor([[brightness_level, eye_movement_variance]], dtype=torch.float32)
    with torch.no_grad():
        risk_score = model(input_tensor).item()
    return risk_score

def main():
    parser = argparse.ArgumentParser(description='Photosensitivity Risk Predictor and Filter Recommender')
    parser.add_argument('--brightness', type=float, required=True, help='Environmental brightness level (lux)')
    parser.add_argument('--variance', type=float, required=True, help='Eye movement variance')
    parser.add_argument('--model_path', type=str, default='dual_branch_cnn.pth', help='Path to the trained model')
    
    args = parser.parse_args()

    model = load_model(args.model_path)
    risk_score = predict_risk(model, args.brightness, args.variance)
    recommendation = recommend_filter(args.brightness, args.variance)

    print("\n=== Prediction Result ===")
    print(f"Predicted Photosensitivity Risk Score: {risk_score:.4f}")
    if risk_score > 0.5:
        print("High Risk detected!")
    else:
        print("Low Risk detected.")
    
    print("\n=== Filter Recommendation ===")
    print(f"Suggested Filter: {recommendation['filter']}")
    print(f"Note: {recommendation['note']}")

if __name__ == "__main__":
    main()
