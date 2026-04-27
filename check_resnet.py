import torch
from torchvision import models
print("Loading ResNet50...")
try:
    model = models.resnet50(pretrained=True)
    print("ResNet50 loaded successfully")
except Exception as e:
    print(f"Error: {e}")
