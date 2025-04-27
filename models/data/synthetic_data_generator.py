import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

class NystagmusDataset(Dataset):
    def __init__(self, csv_path=None, n_samples=1000, transform=None):
        """
        Either load from CSV or generate synthetic data
        """
        self.transform = transform
        
        if csv_path:
            # Load from existing CSV
            import pandas as pd
            df = pd.read_csv(csv_path)
            self.brightness = torch.tensor(df['brightness_level'].values, dtype=torch.float32)
            self.eye_variance = torch.tensor(df['eye_movement_variance'].values, dtype=torch.float32)
            self.risk = torch.tensor(df['photosensitivity_risk'].values, dtype=torch.float32)
        else:
            # Generate synthetic data
            self.brightness = torch.rand(n_samples) * 900 + 100  # 100 to 1000 lux
            self.eye_variance = torch.rand(n_samples) * 10      # 0 to 10 variance
            
            # Synthetic risk calculation (simplified model)
            b_norm = (self.brightness - 100) / 900  # Normalize to 0-1
            e_norm = self.eye_variance / 10        # Normalize to 0-1
            
            # Higher risk with higher brightness and higher variance
            self.risk = torch.sigmoid(3 * (b_norm - 0.5) + 2 * (e_norm - 0.5))
            # Threshold to binary for convenience
            self.risk = (self.risk > 0.5).float()
    
    def __len__(self):
        return len(self.brightness)
    
    def __getitem__(self, idx):
        features = torch.tensor([self.brightness[idx], self.eye_variance[idx]])
        target = torch.tensor([self.risk[idx]])
        
        if self.transform:
            features = self.transform(features)
            
        return features, target

def get_data_loaders(batch_size=32, csv_path=None):
    dataset = NystagmusDataset(csv_path=csv_path)
    
    # Split into train and test
    train_size = int(0.8 * len(dataset))
    test_size = len(dataset) - train_size
    train_dataset, test_dataset = torch.utils.data.random_split(
        dataset, [train_size, test_size])
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size)
    
    return train_loader, test_loader
