import cv2
from keras.models import load_model
import numpy as np

# Load the pre-trained model
model = load_model('my_model.h5')

# Define the list of class labels
class_labels = ['class1', 'class2', 'class3']

# Function to classify an image
def classify_image(img):
    # Preprocess the image
    img = cv2.resize(img, (64, 64))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    # Make a prediction using the model
    pred = model.predict(img)
    class_index = np.argmax(pred[0])
    class_label = class_labels[class_index]

    return class_label

# Load an image and classify it
img = cv2.imread(r'E:\code\demo\captured_image1.jpg')
predicted_class = classify_image(img)
print(f"Predicted class: {predicted_class}")