
import torch
import torch.nn as nn
import torch.optim as optim

class DualBranchNet(nn.Module):
    """
    Dual-Branch Neural Network to process brightness and eye movement variance
    """
    def __init__(self):
        super(DualBranchNet, self).__init__()
        self.fc1 = nn.Linear(2, 16)
        self.dropout1 = nn.Dropout(0.3)
        self.fc2 = nn.Linear(16, 8)
        self.dropout2 = nn.Dropout(0.3)
        self.fc3 = nn.Linear(8, 1)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout1(x)
        x = torch.relu(self.fc2(x))
        x = self.dropout2(x)
        x = torch.sigmoid(self.fc3(x))
        return x

class ModelWrapper:
    """
    Wrapper for training and evaluating the DualBranchNet model.
    """
    def __init__(self, model, learning_rate=0.001):
        self.model = model
        self.criterion = nn.BCELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
    
    def train(self, train_loader, num_epochs=10):
        self.model.train()
        for epoch in range(num_epochs):
            running_loss = 0.0
            for inputs, labels in train_loader:
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {running_loss/len(train_loader):.4f}")
    
    def evaluate(self, test_loader):
        self.model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for inputs, labels in test_loader:
                outputs = self.model(inputs)
                predicted = (outputs > 0.5).float()
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        accuracy = 100 * correct / total
        print(f"Test Accuracy: {accuracy:.2f}%")
        return accuracy

if __name__ == "__main__":
    # Quick test
    model = DualBranchNet()
    sample_input = torch.randn(5, 2)
    output = model(sample_input)
    print("Sample output:", output)
