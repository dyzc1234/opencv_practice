import cv2 as cv
import numpy as np

def rescaleIput(input_,scale = .6):
    height = int(input_.shape[0] * scale)
    width = int(input_.shape[1] * scale)
    dimension = (width,height)

    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

blank = np.zeros((500,500,3),dtype='uint8')

# img = cv.imread('F:\opencv_learning\photos/wwx.jpg')

# resized_img=rescaleIput(img)

#1.Paint The Image a certain colour
blank[100:400,300:400] = 255,255,0

#2.Draw a Rectangle
cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,150),thickness=cv.FILLED)

#3.Draw a Cicle
cv.circle(blank,(250,250),100,(0,255,150),thickness=cv.FILLED)

#4.Draw a Line
cv.line(blank,(0,0),(blank.shape[0],blank.shape[1]),(255,140,120),thickness=2)

#5.Write Text
cv.putText(blank,'wwx',(250,250),cv.FONT_HERSHEY_PLAIN,3,(0,255,255),thickness=3,)

#cv.imshow('wenxuan',img)
# cv.imshow('with wenxuan',resized_img)
cv.imshow('blank',blank)

cv.waitKey(0)