import cv2
import torch
from torchvision.transforms import functional as F
from loftr import LoFTR, default_cfg

# Load pre-trained LoFTR model
model = LoFTR(config=default_cfg)
model.load_state_dict(torch.load('loftr_model.pth'))
model.eval()

# Load input image
image = cv2.imread('input_image.jpg')

# Preprocess image
image_tensor = F.to_tensor(image).unsqueeze(0)

# Perform forward pass with LoFTR
with torch.no_grad():
    pred = model(image_tensor)

# Get keypoints and descriptors
keypoints = pred['keypoints'][0].cpu().numpy()
descriptors = pred['descriptors'][0].cpu().numpy()

# Display keypoints on the image
for i, (x, y) in enumerate(keypoints):
    cv2.circle(image, (int(x), int(y)), 2, (0, 255, 0), -1)
    cv2.putText(image, str(i+1), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

# Display the image with keypoints
cv2.imshow('Image with Keypoints', image)
cv2.waitKey(0)
cv2.destroyAllWindows()