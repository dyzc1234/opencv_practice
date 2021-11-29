import cv2 as cv
import numpy as np


img_ = cv.imread('F:\opencv_learning\photos/wwx.jpg')

def ChangeRes(input_,scale):
    dimension = (int(input_.shape[1] * scale),int(input_.shape[0] * scale))
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

#Resize the Image
img = ChangeRes(img_,.3)
cv.imshow('Dy and Wangwenxuan',img)

#Create a Blank array
blank = np.zeros(img.shape[:2],dtype='uint8')

#Split the Image
B,G,R = cv.split(img)
Blue = cv.merge([B,blank,blank])
Green = cv.merge([blank,G,blank])
Red = cv.merge([blank,blank,R])

cv.imshow('Blue',Blue)
cv.imshow('Green',Green)
cv.imshow('Red',Red)

print(img.shape)
print(B.shape)
print(G.shape)
print(R.shape)

#Merge the Channels
Merged = cv.merge([B,G,R])
cv.imshow('Merged',Merged)

cv.waitKey(0)  