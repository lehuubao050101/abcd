import cv2

in2_image = r'D:\machine_learning\detect_behavious\in2.png'
frame = cv2.imread(in2_image)

height, width, _ = frame.shape
print(height,width)
xA, yA, xB, yB = 493, 220, 293, 839
#[{493, 220, 293, 839}, {741, 829, 460, 4}]
#xA, yA, xB, yB  =741, 829,  460, 4
#220 293 273 546, 460 4 369 737, 158 537 75 150
cropped_frame = frame[4:737+4,460:460+369]

if cropped_frame.size == 0:
    print("Không thể cắt khung hình.")

cv2.imshow('Cropped Frame', cropped_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()