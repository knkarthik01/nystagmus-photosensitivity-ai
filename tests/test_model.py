
import torch
from models.cnn_dual_branch.model import DualBranchNet

def test_model_forward_pass():
    model = DualBranchNet()
    input_tensor = torch.randn(4, 2)  # 4 samples, 2 features each
    output = model(input_tensor)
    assert output.shape == (4, 1), "Output shape mismatch"
    print("✅ test_model_forward_pass passed.")

def test_dummy_training_step():
    model = DualBranchNet()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = torch.nn.BCELoss()

    input_tensor = torch.randn(8, 2)
    target = torch.randint(0, 2, (8, 1)).float()

    optimizer.zero_grad()
    output = model(input_tensor)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

    assert loss.item() > 0, "Loss should be greater than zero"
    print("✅ test_dummy_training_step passed.")

if __name__ == "__main__":
    test_model_forward_pass()
    test_dummy_training_step()
