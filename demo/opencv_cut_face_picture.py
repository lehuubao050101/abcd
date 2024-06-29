import cv2

# Mở video
cap = cv2.VideoCapture('input_video.mp4')

# Lặp qua từng frame của video
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
    if key == ord('c'):
        # Chụp ảnh và lưu vào tệp
        cv2.imwrite('captured_image.jpg', frame)
        print('Đã chụp ảnh và lưu vào tệp "captured_image.jpg"')
    
    # Nhấn 'q' để thoát
    if key == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()