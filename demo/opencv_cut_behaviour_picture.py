import cv2
import os
# Load the pre-trained face detection model

import numpy as np


name_folder = []
def cut(video_dir,num):
    for video_file in os.listdir(video_dir):
    
        name_folder.append(video_file)
        #print(video_file)
        video = os.path.join(video_dir, video_file)
        #print(video)
        base_name = os.path.splitext(video_file)[0]
        if(num ==0):
            
            folder_save = os.path.join('E:\code\demo\data\IMAGE\FACE', base_name)
        else:
            folder_save = os.path.join('E:\code\demo\data\IMAGE\BH', base_name)
        
        #print(folder_save)
        net = cv2.dnn.readNetFromCaffe("weights-prototxt.txt", "res_ssd_300Dim.caffeModel") 
        
        vs =cv2.VideoCapture(r'E:\code\demo\opencv_cut\FACE\videoplayback.mp4')



       
   
        while True:
            ret, frame =    vs.read()
            if not ret:
                break
            cv2.imshow("Window", frame)
         
            (height, width) = frame.shape[:2]
            # Tiếp tục xử lý frame
          
            # Xử lý trường hợp frame là None
	# convert frame dimensions to a blob and 300x300 dim
            
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                (300, 300), (104.0, 177.0, 123.0))
        
            # pass the blob into dnn 
            net.setInput(blob)
            detections = net.forward()

            # loop over the detections to extract specific confidence
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]

		# greater than the minimum confidence
            if confidence < 0.5:
                continue

		# compute the boxes (x, y)-coordinates
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x1, y1, x2, y2) = box.astype("int")
 
		# draw the bounding box of the face along with the associated
		# probability
            text = "{:.2f}%".format(confidence * 100) + " ( " + str(y2-y1) + ", " + str(x2-x1) + " )"
            y = y1 - 10 if y1 - 10 > 10 else y1 + 10
            cv2.rectangle(frame, (x1, y1), (x2, y2),
                (0, 0, 255), 2)
            cv2.putText(frame, text, (x1, y),
                cv2.LINE_AA, 0.45, (0, 0, 255), 2)

	# show the output frame
            cv2.imshow("Window", frame)
            key = cv2.waitKey(1) & 0xFF
        
            # Nhấn 'q' để thoát
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
        vs.stop()            # Đọc một frame từ video
        
            
 
        #
            # Chờ người dùng nhấn 'c' để chụp ảnh
          
        


cap_video_face = r'E:\code\demo\opencv_cut\FACE'
num_face = 0 
cap_video_bh = r'E:\code\demo\opencv_cut\BEHAVIOUR'
num_bh =1
cut(cap_video_face,num_face)
cut(cap_video_bh,num_bh)


print(name_folder) 

#-----------------------------------------

# import packages


# load SSD and ResNet network based caffe model for 300x300 dim imgs

# video stream initialization
# stop capturing

'''
for video_file in os.listdir(video_dir):
    video = cv2.VideoCapture(os.path.join(video_dir, video_file))
    while(1):
        ret, frame = video.read()
        
        if not ret:
            # Không thể đọc được frame, kết thúc vòng lặp
            break
    # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Face Detection', frame)
# Display the output image

cv2.waitKey(0)
cv2.destroyAllWindows()

'''