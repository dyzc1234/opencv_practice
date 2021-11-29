import cv2 as cv
import numpy as np

img_ = cv.imread('F:\opencv_learning\photos/wwx.jpg')

def ChangeRes(input_,scale):
    dimension = (int(input_.shape[1] * scale),int(input_.shape[0] * scale))
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

img = ChangeRes(img_,.5)
blank = np.zeros(img.shape)
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(grey,(3,3),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,40,150)

#ret 代表一个布尔值表示True or False
ret,thresh = cv.threshold(blur,100,200,cv.THRESH_BINARY) 

contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print('{} contour(s) found'.format(len(contours)))

cv.drawContours(blank,contours,-1,(255,100,0),3)

cv.imshow('wwx',img)
cv.imshow('grey',grey)
cv.imshow('Canny',canny)
cv.imshow('Blur',blur)
cv.imshow('Thresh',thresh)
cv.imshow('Draw contours',blank)

cv.waitKey(0)