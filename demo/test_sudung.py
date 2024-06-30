import cv2
from keras.models import load_model
import numpy as np

# Load the pre-trained model
model = load_model('E:\code\my_model.h5')

# Define the list of class labels
class_labels = ['class1', 'class2', 'class3']

# Function to classify a frame
def classify_frame(frame):
    # Preprocess the frame
    frame = cv2.resize(frame, (224, 224))
    frame = np.expand_dims(frame, axis=0)
    frame = frame / 255.0

    # Make a prediction using the model
    pred = model.predict(frame)
    class_index = np.argmax(pred[0])
    class_label = class_labels[class_index]

    return class_label

# Open the video capture
cap = cv2.VideoCapture(r'E:\code\demo\opencv_cut\FACE\videoplayback.mp4')

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Classify the frame
    predicted_class = classify_frame(frame)

    # Display the predicted class on the frame
    cv2.putText(frame, predicted_class, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Video', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()