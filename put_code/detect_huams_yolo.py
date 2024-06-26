import cv2

# Load YOLO model
net = cv2.dnn.readNet("weights/yolov3-tiny.weights", "cfg/yolov3-tiny.cfg")

# Load input image
image_path = "path/to/your/image.jpg"
image = cv2.imread(image_path)

# Preprocess image
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)

# Set input to the network
net.setInput(blob)

# Perform forward pass and get output layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
outputs = net.forward(output_layers)

# Process the outputs
confidence_threshold = 0.5
nms_threshold = 0.4

boxes = []
confidences = []
class_ids = []

for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > confidence_threshold:
            center_x = int(detection[0] * image.shape[1])
            center_y = int(detection[1] * image.shape[0])
            width = int(detection[2] * image.shape[1])
            height = int(detection[3] * image.shape[0])

            x = int(center_x - width / 2)
            y = int(center_y - height / 2)

            boxes.append([x, y, width, height])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply non-maximum suppression to remove overlapping boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)

# Draw bounding boxes around detected people
for i in indices:
    i = i[0]
    x, y, width, height = boxes[i]
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

# Display the result
cv2.imshow("Person Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()