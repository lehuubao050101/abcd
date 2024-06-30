import os
import numpy as np
from sklearn.model_selection import train_test_split
from skimage.io import imread
from skimage.transform import resize

# Đường dẫn chứa dữ liệu ảnh
data_dir = 'path/to/image/data'

# Đọc dữ liệu ảnh từ file
X = []
y = []
for label in os.listdir(data_dir):
    label_dir = os.path.join(data_dir, label)
    for filename in os.listdir(label_dir):
        img_path = os.path.join(label_dir, filename)
        img = imread(img_path)
        X.append(img)
        y.append(label)

# Chuyển đổi dữ liệu thành numpy array
X = np.array(X)
y = np.array(y)

# Chia dữ liệu thành tập train/val
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Tiền xử lý dữ liệu
# 1. Chuẩn hóa ảnh
X_train = X_train / 255.0
X_val = X_val / 255.0

# 2. Resize ảnh về cùng kích thước
new_size = (64, 64)
X_train = np.array([resize(img, new_size) for img in X_train])
X_val = np.array([resize(img, new_size) for img in X_val])

# 3. Chuyển đổi ảnh sang dạng tensor 4D

# 4. One-hot encoding nhãn
from keras.utils import to_categorical
num_classes = len(set(y_train))
y_train = to_categorical(y_train, num_classes)
y_val = to_categorical(y_val, num_classes)

# Sử dụng numpy array với model.fit()
model.fit(
    X_train, 
    y_train,
    batch_size=32,
    epochs=10,
    validation_data=(X_val, y_val),
    verbose=1
)