import cv2
import numpy as np
import detect_openpose

detect_openpose = detect_openpose.dect_open_pose()

class detect_humans():
        def __init__(self):
              
                self.hog = cv2.HOGDescriptor()
                self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
                self.new_width = 800
                self.new_height = 600
        def detect_human(self,fram):
                axy= []
                
                num_ =0
                frame  = cv2.imread(fram)
                gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
           
    # detect people in the image
    # returns the bounding boxes for the detected objects
                (boxes, _) = self.hog.detectMultiScale(frame, 
                                    winStride=(4, 4),
                                    padding=(4, 4),
                                    scale=1.05)
                
                '''
                for (x, y, w, h) in boxes:
                        print(x, y, w, h)
                boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
               
                print("humans",len(boxes))
                for (xA, yA, xB, yB) in boxes:                     
                        w = xB - xA
                        h = yB - yA
                        area = w*h                  
                        
                        if(area >100000):
                                print("area detect",area)
                                axy.append({xA, yA, xB, yB})
                                
                                print(axy[num_])
                                print(num_)
                                num_ += 1
                                cv2.rectangle(frame, (xA, yA), (xB, yB),
                                                        (0, 255, 0), 2)
                '''
                return  frame,boxes
        def display_detect_humans(self,frame):
                frame,data = self.detect_human(frame)
                cropped_frame
                '''
                in2_image= r'D:\machine_learning\detect_behavious\in2.png'
        # Đọc ảnh
                num_ =0
                cv2.namedWindow('People Detection', cv2.WINDOW_NORMAL)

                cv2.resizeWindow('People Detection', self.new_width, self.new_height)

                cv2.imshow('People Detection', frame)
                '''
                for x,y,w,h in data:
                        print("dien tich",w*h)
                        if w*h >100000:
                               
                                cropped_frame = frame[y: y + h, x: x + w]
                                '''
                                cv2.namedWindow(str(num_), cv2.WINDOW_NORMAL)

                                cv2.resizeWindow(str(num_), w, h)
                        
                                cv2.imshow(str(num_), cropped_frame)
                                num_ +=1
                                '''
                        
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()
                return cropped_frame
                
        def change_humans_wh(self,new_width,new_height):
                self.new_width = new_width
                self.new_height = new_height


detect_humans = detect_humans()
# Đường dẫn đến file ảnh
def test_dect_humas():
        image_path = r'D:\machine_learning\detect_behavious\in.png'
        in2_image= r'D:\machine_learning\detect_behavious\in2.png'
        # Đọc ảnh
        frame= cv2.imread(image_path)
      
        detect_hu = detect_humans()
        detect_hu.display_detect_humans(image_path)

def test_onsopen_humans():
        
        
        image_path = r'D:\machine_learning\detect_behavious\in.png'
     
        # Đọc ảnh
        #frame= cv2.imread(image_path)
      
        
        _,humans = detect_humans.detect_human(image_path)
        for i in humans:
                detect_openpose.detect_onsopen(i)
                detect_openpose.display_detect_onsopen()


#test_dect_humas()
test_onsopen_humans()
# Tạo một bộ phân loại dựa trên HOG


#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#boxes, _ = hog.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#print(len(boxes))


# Hiển thị ảnh kết quả

