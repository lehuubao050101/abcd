import cv2
import os
import numpy as np
video_dir = 'path/to/video/directory'

X_train = []
for video_file in os.listdir(video_dir):
    video = cv2.VideoCapture(os.path.join(video_dir, video_file))
    frames = []
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)
    X_train.append(np.array(frames))
X_train = np.array(X_train)

'''
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(...)
train_generator = train_datagen.flow_from_directory(
    'path/to/train/directory',
    target_size=(112, 112),
    frames_per_step=16,
    batch_size=32,
    class_mode='categorical')

'''