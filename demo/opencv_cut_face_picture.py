# import packages
import numpy as np
import cv2

import os
# load SSD and ResNet network based caffe model for 300x300 dim imgs
file_txt = r'E:\code\demo\weights-prototxt.txt'
file_model = r'E:\code\demo\res_ssd_300Dim.caffeModel'

# Mở video



def cut_image_from_video(vs,name):
    stat_cut =0
    num =0
    net = cv2.dnn.readNetFromCaffe(file_txt, file_model)
    while True:
        ret, frame =    vs.read()
        
    
        
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


              # Tạo đường dẫn đến thư mục
            save_path = f"E:\code\demo\data\IMAGE\FACE\{name}"
     
                # Kiểm tra xem thư mục có tồn tại chưa
            if not os.path.exists(save_path):
                # Nếu chưa tồn tại, tạo mới thư mục
                os.makedirs(save_path)
                print(f"Thư mục '{save_path}' đã được tạo.")


            # Kiểm tra xem thư mục có tồn tại không, nếu không thì tạo mới
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            # Lưu ảnh vào t;hư mục
            if stat_cut == 1:
                num = num + 1
                cv2.imwrite(os.path.join(save_path, f'captured_image{num}.jpg'), frame)
                state = f"Đã chụp ảnh và lưu vào tệp captured_image{ num}.jpg"
                print(state)
                if num % 20 ==0:
                    stat_cut =0

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
        if key == ord('p'):
            stat_cut =1
        # Nhấn 'q' để thoát
        if key == ord('q'):
            break
    cv2.destroyAllWindows()
    vs.stop()            # Đọc một frame từ video


video = cv2.VideoCapture(r'E:\code\demo\opencv_cut\FACE\videoplayback.mp4')
cut_image_from_video(video,"mot")

