
import torch
import torch.nn.functional as F

class GradCAM:
    """
    Simple GradCAM implementation for CNN models.
    """
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None
        self._register_hooks()
    
    def _register_hooks(self):
        def forward_hook(module, input, output):
            self.activations = output.detach()
        
        def backward_hook(module, grad_input, grad_output):
            self.gradients = grad_output[0].detach()
        
        target_module = dict(self.model.named_modules())[self.target_layer]
        target_module.register_forward_hook(forward_hook)
        target_module.register_backward_hook(backward_hook)
    
    def generate_cam(self, input_tensor, target_class=None):
        """
        Generate the GradCAM heatmap.
        """
        self.model.eval()
        output = self.model(input_tensor)
        
        if target_class is None:
            target_class = output.argmax(dim=1)
        
        loss = output[:, target_class]
        self.model.zero_grad()
        loss.backward(retain_graph=True)
        
        weights = self.gradients.mean(dim=[0, 2], keepdim=True)
        cam = (weights * self.activations).sum(dim=1)
        cam = F.relu(cam)
        cam = cam.squeeze().cpu().numpy()
        cam = (cam - cam.min()) / (cam.max() - cam.min() + 1e-9)  # Normalize
        return cam

if __name__ == "__main__":
    print("GradCAM module loaded. To use: instantiate with model and layer name.")
