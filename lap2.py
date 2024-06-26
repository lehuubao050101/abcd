import os
import torch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import cv2

# Định nghĩa lớp Dataset
class VideoDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.video_files = os.listdir(root_dir)

    def __len__(self):
        return len(self.video_files)

    def __getitem__(self, idx):
        vid_path = os.path.join(self.root_dir, self.video_files[idx])
        cap = cv2.VideoCapture(vid_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if self.transform:
                frame = self.transform(frame)
            frames.append(frame)
        cap.release()
        return torch.stack(frames, dim=0)

# Cấu hình mô hình
num_classes = 10
batch_size = 16
num_epochs = 50
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Tải dữ liệu từ file
train_dataset = VideoDataset(root_dir="data/train", transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
]))
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

val_dataset = VideoDataset(root_dir="data/val", transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
]))
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Khởi tạo mô hình, optimizer và loss function
model = YourVideoModelArchitecture(num_classes=num_classes).to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Huấn luyện mô hình
for epoch in range(num_epochs):
    # Huấn luyện
    model.train()
    for inputs, labels in train_loader:
        inputs = inputs.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    
    # Đánh giá trên tập validation
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in val_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    print(f"Epoch [{epoch+1}/{num_epochs}], Validation Accuracy: {100 * correct / total:.2f}%")

# Sử dụng mô hình để dự đoán
model.eval()
test_dataset = VideoDataset(root_dir="data/test", transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
]))
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

with torch.no_grad():
    correct = 0
    total = 0
    for inputs, labels in test_loader:
        inputs = inputs.to(device)
        labels = labels.to(device)
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Test Accuracy: {100 * correct / total:.2f}%")