import cv2 as cv
import numpy as np


img_ = cv.imread('F:\opencv_learning\photos/Doraemen.jpg')

def changeRes(input_,scale):
    height = int(input_.shape[0] * scale)
    width = int(input_.shape[1] * scale)
    dimension = (width,height)
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

img = changeRes(img_,.3)

#Translation
def translate(img,x,y):
    transMat = np.float64([[1,0,x],[0,1,y]])
    dimension_2 = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension_2)
#x-->Right
#y-->Down

#Rotation
def rotate(img,angle,rotPoint=None):
  
 if rotPoint is None:
        rotPoint = (img.shape[0]//2,img.shape[1]//2) 

  
 rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
 dimension_3 = (img.shape[:2])
 
 return cv.warpAffine(img,rotMat,dimension_3)

#Flipping
flipped = cv.flip(img,2)
#1-->Mirror Flip
#0-->Flip Upside Down
#-1-->Mirror Up and Down

translated = translate(img,10,10)
rotated = rotate(img,45,None)

cv.imshow('Ori_Dora',img)
cv.imshow('Translated',translated)
cv.imshow('Rotated',rotated)
cv.imshow('flipped',flipped)

cv.waitKey(0)