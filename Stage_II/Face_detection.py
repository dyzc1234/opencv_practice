import cv2 as cv
import time
haar_cascade = cv.CascadeClassifier('Face_detection.xml')

#####################################Picture_Input################################# 
###################################################################################
# img_ = cv.imread('F:\A_Ding\Opencv_Learning\opencv_practice\photos/class.JPG')

# def ChangeScale(input_,scale):
#     height = int(input_.shape[0] * scale)
#     width = int(input_.shape[1] * scale)
#     dimension = (width,height)
#     return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

# img = ChangeScale(img_,.5)
####################################################################################
####################################################################################


################################Video_Input##########################################
# capture = cv.VideoCapture(r'F:\A_Ding\Yolo4\yolov4-pytorch-master/10.mp4')
capture = cv.VideoCapture(0)
fps = 0.0
while True:
    t = time.time()

    #获取每一帧
    isTrue,frame = capture.read()

    #haar需要灰度图像因此先转换成灰度图像
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    #faces_rect通过矩阵的形式储存x,y,w,h的值
    faces_rect = haar_cascade.detectMultiScale(gray,1.3,5) 

    #获取FPS
    fps  = int(( fps + (1./(time.time()-t)) ) / 2)
 
    for x,y,h,w in faces_rect:
       cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
       cv.putText(frame,'FACE',(x,y),cv.FONT_HERSHEY_PLAIN,2,(0,0,255),thickness=3)
    cv.putText(frame,'FPS={}'.format(fps),(frame.shape[1]//10,frame.shape[0]//10),cv.FONT_HERSHEY_PLAIN,2,(0,255,255),thickness=2)


    cv.imshow('Detected faces',frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
    print(fps)
capture.release()
cv.destroyAllWindows()