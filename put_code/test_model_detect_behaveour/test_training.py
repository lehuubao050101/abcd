import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os

# Cấu hình tham số
img_width, img_height = 224, 224
batch_size = 32

epochs = 20

# Tải dữ liệu
data_dir = 'D:/machine_learning/detect_behavious/test_model_detect_behaveour/training/data'

# Lấy danh sách các thư mục trong "data"
subdirs = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]

# In ra danh sách các thư mục
print("Các thư mục trong 'data':")
for subdir in subdirs:
    print(subdir)
#Để đọc các tên thư mục trong một thư mục "data",


num_classes = len(subdir) -1
print(num_classes)

train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        'D:/machine_learning/detect_behavious/test_model_detect_behaveour/training/data',
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='categorical')
print("==============")
print(train_generator)
print("==============")
val_datagen = ImageDataGenerator(rescale=1./255)
val_generator = val_datagen.flow_from_directory(
        'D:/machine_learning/detect_behavious/test_model_detect_behaveour/validation/data',
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='categorical')

# Xây dựng mô hình
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

#model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
model.compile(optimizer=Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, amsgrad=False), loss='categorical_crossentropy', metrics=['accuracy'])
# Huấn luyện mô hình
model.fit(
        train_generator,
        steps_per_epoch=train_generator.n // batch_size,
        epochs=epochs,
        validation_data=val_generator,
        validation_steps=val_generator.n // batch_size)

# Đánh giá mô hình
score = model.evaluate(val_generator, verbose=0)
print('Validation loss:', score[0])
print('Validation accuracy:', score[1])