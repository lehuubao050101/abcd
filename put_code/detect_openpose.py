import cv2

import matplotlib.pyplot as plt
video = r'D:\machine_learning\detect_behavious\a.mp4'
cap = cv2.VideoCapture()
class dect_open_pose():
    def __init__ (self):
   
        self.up =0
        self.new_width = 800
        self.new_height = 600
        self.nPoints = 15
        self.POSE_PAIRS = [[0,1],[1,2],[2,3],[3,4],[1,5],[5,6],[6,7],[1,14],[14,8],[8,9],[9,10],[14,11],[11,12],[12,13]]
        self.protot = r'D:\machine_learning\detect_behavious\OpenPose_models\pose\mpi\pose_deploy_linevec_faster_4_stages.prototxt'
        self.caffe_model =r'D:\machine_learning\detect_behavious\OpenPose_models\pose\mpi\pose_iter_160000.caffemodel'
        self.net = cv2.dnn.readNetFromCaffe(self.protot,self.caffe_model)
        self.imPoints2=0
        self.imSkeleton2=0
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self.frame =0
        self.imPoints = 0
        self.imSkeleton = 0
    def check_in(self,image_read):
        return image_read
        im  = cv2.imread(image_read)

        if im is not None and im.size > 0:
            # Chuyển đổi từ BGR sang RGB
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            return im
        else:
            print("Hình ảnh không hợp lệ hoặc rỗng.")

    def dect_humans_onsopen(self,fram):
        frame  = cv2.imread(fram)
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        self.imPoints= frame.copy()
        self.imSkeleton = frame.copy()
# detect people in the image
# returns the bounding boxes for the detected objects
        (boxes, _) = self.hog.detectMultiScale(frame, 
                            winStride=(4, 4),
                            padding=(4, 4),
                            scale=1.05)
        #return frame,boxes
        for x,y,w,h in boxes:
                       
                        if w*h >100058:
                            print("dien tich",w*h)
                            cropped_frame = frame[y: y + h, x: x + w]
                            #return frame,cropped_frame,x,y
                            self.detect_onsopen(frame,cropped_frame,x,y)
                            
        self.display_detect_onsopen()



    def detect_onsopen(self,frame,cropped_frame,x,y):
        x1 =x
        y1 =y
        im = cropped_frame
        #im = self.check_in(im)
       # in2_image= r'D:\machine_learning\detect_behavious\in2.png'
        #frame,im,x1,y1 = self.dect_human(in2_image)
      
        inwight = im.shape[1]
        inheight = im.shape[0]
                
        netInputSize = (368,368)
        inBlob = cv2.dnn.blobFromImage(im,1.0/225,netInputSize,(0,0,0),swapRB=True,crop=False)
        
        self.net.setInput(inBlob)
        output = self.net.forward()

        plt.figure(figsize=(20,5))
        for i in range(self.nPoints):
            probMap= output[0,i,:,:]
            displayMap = cv2.resize(probMap,(inwight,inheight),cv2.INTER_LINEAR)
            plt.subplot(2,8,i+1); plt.axis('off');plt.imshow(displayMap,cmap='jet')
            scaleX = inwight/ output.shape[3]
            scaleY  = inheight/output.shape[2]

            points = []
            threshold = 0.1
        for i in range(self.nPoints):
            probMap= output[0,i,:,:]
            minVal,prob,minLoc,point = cv2.minMaxLoc(probMap)

            x = scaleX*point[0]
            y = scaleY*point[1]

            if prob > threshold:
                points.append((int(x)+x1,int(y)+y1))
            else:points.append(None)

        
        for i,p in enumerate(points):
            
         
            cv2.circle(self.imPoints,p,8,(255,255,0),thickness= -1, lineType=cv2.FILLED)
            cv2.putText(self.imPoints,"{}".format(i),p,cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,lineType=cv2.LINE_AA)


        for pair in   self.POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]
            if points[partA] and points[partB]:
                

                cv2.line(self.imSkeleton,points[partA],points[partB],(255,255,0),2)
                cv2.circle(self.imSkeleton,points[partA],8,(255,0,0),thickness=-1,lineType=cv2.FILLED)
        self.up =1
        
        
    def dect_data_onsopen(self,im):
        self.detect_onsopen(self,im)
        if(self.upd() ==1):
            self.up =0
            return self.imPoints2,self.imSkeleton2
    def upd(self):
        return self.up
    
        
    def destroy(self):
        cv2.waitKey()
# Đóng tất cả các cửa sổ hiển thị
        cv2.destroyAllWindows()
    def display_detect_onsopen(self):
        up = self.up
        if up ==1:
            up =0
            print("update okey")
           # imPoints, imSkeleton = self.detect_1()
            cv2.namedWindow('Image 1', cv2.WINDOW_NORMAL)
            cv2.namedWindow('Image 2', cv2.WINDOW_NORMAL)

            # Kích thước mới cho cửa sổ hiển thị
            

            # Thay đổi kích thước cửa sổ hiển thị
            cv2.resizeWindow('Image 1', self.new_width, self.new_height)
            cv2.resizeWindow('Image 2', self.new_width, self.new_height)
            
            cv2.imshow('Image 1', self.imPoints)
            cv2.imshow('Image 2', self.imSkeleton)
            
        else:
             print("update error")
    def change_wh(self,new_width,new_height):
        self.new_width = new_width
        self.new_height = new_height
#net = cv2.dmn.readNetFromCaffe(protot,caffe_model)

def test_detect_onsopen():

    in2_image= r'D:\machine_learning\detect_behavious\in2.png'
    image_read = r'D:\machine_learning\detect_behavious\in.png'
    dect = dect_open_pose()
    dect.dect_humans_onsopen(in2_image)
    dect.destroy()

'''
    while(1):
        video = r'D:\machine_learning\detect_behavious\a.mp4'
        cap = cv2.VideoCapture()
        ret, frame = cap.read()
        if not ret:
             break
        dect = dect_open_pose()
        dect.dect_human(frame)
'''
   # dect.detect_onsopen(image_read)
    #dect.display_detect_onsopen()

test_detect_onsopen()
#from IPython.display import Image
#Image(filename=out_image)

#cv2.imshow('Image', im)
#cv2.imshow('Im2', im2)
  # Chờ người dùng nhấn một phím bất kỳ để đóng cửa sổ





#plt.tight_layout()  # Chỉnh sửa khoảng cách giữa các ô con
#plt.show()  # Hiển thị lưới\






'''
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.axis('off')
plt.imshow(imPoints)

plt.subplot(122)
plt.axis('off')
plt.imshow(imSkeleton)
'''
