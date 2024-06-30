import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

import os


# Thư mục gốc
root_dir = 'E:\code\demo\data_raw\IMAGE\FACE'

# Đếm số lượng folder
num_classes = sum(os.path.isdir(os.path.join(root_dir, item))
                   for item in os.listdir(root_dir))

print(f"Tổng số lượng folder: {num_classes}")
# Tải dữ liệu ảnh
import os
import numpy as np
from sklearn.model_selection import train_test_split
import cv2


# Đường dẫn chứa dữ liệu ảnh
data_dir = 'E:\code\demo\data_raw\IMAGE\FACE'

# Đọc dữ liệu ảnh từ file
X = []
y = []
for label in os.listdir(data_dir):
    label_dir = os.path.join(data_dir, label)
    for filename in os.listdir(label_dir):
        img_path = os.path.join(label_dir, filename)
        img = cv2.imread(img_path)
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
X_train = np.array([cv2.resize(img, new_size) for img in X_train])
X_val = np.array([cv2.resize(img, new_size) for img in X_val])

# 3. Chuyển đổi ảnh sang dạng tensor 4D

# 4. One-hot encoding nhãn
from keras.utils import to_categorical
num_classes = len(set(y_train))

from sklearn.preprocessing import LabelEncoder

# Mã hóa y_train
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(y_train)

# Chuyển đổi y_train sang one-hot encoding
y_train = to_categorical(y_train, num_classes)
# Mã hóa y_val
label_encoder = LabelEncoder()
y_val = label_encoder.fit_transform(y_val)

# Chuyển đổi y_val sang one-hot encoding
y_val = to_categorical(y_val, num_classes)

# Tiền xử lý dữ liệu
X_train = X_train / 255.0
X_val = X_val / 255.0

# Tạo mô hình
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=X_train.shape[1:]))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Biên dịch mô hình
model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Huấn luyện mô hình
model.fit(X_train, y_train,
          batch_size=32,
          epochs=10,
          validation_data=(X_val, y_val))

# Train the model

# Evaluate the model
loss, accuracy = model.evaluate(X_val, y_val)
print(f'Validation Loss: {loss:.4f}')
print(f'Validation Accuracy: {accuracy:.4f}')

# Save the model
model.save('my_model.h5')