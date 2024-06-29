

import cv2

# Mở video
cap_video = 'E:\code\demo\opencv_cut\FACE\e.mp4'
cap = cv2.VideoCapture(cap_video)
print(cap_video)
while True:
    # Đọc một frame từ video
    ret, frame = cap.read()
    
    if not ret:
        # Không thể đọc được frame, kết thúc vòng lặp
        break
    
    # Hiển thị frame
    cv2.imshow('Video', frame)
    
    # Chờ người dùng nhấn 'c' để chụp ảnh
    key = cv2.waitKey(1) & 0xFF
   
    # Nhấn 'q' để thoát
    if key == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
import os

file_path = "E:\code\demo\data\IMAGehaviour_e.mp4"
base_name = os.path.splitext(file_path)[0]
print(base_name)  # Output: E:\code\demo\data\IMAGehaviour_e
import os

base_name = '123'
folder_save = os.path.join('E:\code\demo\data\IMAGE\FACE', base_name)
print(folder_save)  # Output: E:\code\demo\data\IMAGE\FACE\123