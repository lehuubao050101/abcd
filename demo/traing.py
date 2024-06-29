import tensorflow as tf
print("xiun chao")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv3D, MaxPool3D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

'''
# Định nghĩa siêu tham số
input_shape = (16, 112, 112, 3)  # Kích thước của các video đầu vào
num_classes = 6  # Số lớp hành vi cần phân loại
learning_rate = 0.001
batch_size = 32
epochs = 50

# Xây dựng mô hình
model = Sequential()
model.add(Conv3D(filters=64, kernel_size=(3, 3, 3), activation='relu', input_shape=input_shape))
model.add(MaxPool3D(pool_size=(2, 2, 2)))
model.add(Conv3D(filters=128, kernel_size=(3, 3, 3), activation='relu'))
model.add(MaxPool3D(pool_size=(2, 2, 2)))
model.add(Conv3D(filters=256, kernel_size=(3, 3, 3), activation='relu'))
model.add(MaxPool3D(pool_size=(2, 2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Biên dịch mô hình
model.compile(optimizer=Adam(lr=learning_rate),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Fit mô hình
model.fit(X_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(X_val, y_val),
          verbose=1)

# Đánh giá mô hình
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test loss: {loss:.4f}')
print(f'Test accuracy: {accuracy:.4f}')

'''