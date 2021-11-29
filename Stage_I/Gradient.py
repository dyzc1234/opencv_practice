import cv2 as cv
import numpy as np

img_ = cv.imread('F:\opencv_learning\photos/wwx.jpg')

def changeRes(input_,scale):
    height = int(input_.shape[0] * scale)
    width = int(input_.shape[1] * scale)
    dimension = (width,height)
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

img = changeRes(img_,.5)

Gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',Gray)

#Laplacian
Lap  = cv.Laplacian(Gray,cv.CV_64F)
Lap = np.uint8(np.abs(Lap))
cv.imshow('Laplacian',Lap)

#Sobel
Sobelx = cv.Sobel(Gray,cv.CV_64F,0,1)
Sobely = cv.Sobel(Gray,cv.CV_64F,1,0)
Sobel_merged = cv.bitwise_or(Sobelx,Sobely,None)

cv.imshow('Sobelx',Sobelx)
cv.imshow('Sobely',Sobely)
cv.imshow('Sobel_merged',Sobel_merged)

#Canny
Canny = cv.Canny(img,120,200)
cv.imshow('Canny',Canny)


cv.waitKey(0)