import cv2 as cv
from matplotlib.pyplot import imsave
from numpy.lib.function_base import average


img_ = cv.imread('F:\opencv_learning\photos/wwx.jpg')

def ChangeRes(input_,scale):
    dimension = (int(input_.shape[1] * scale),int(input_.shape[0] * scale))
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

#Resize the Image
img = ChangeRes(img_,.5)
cv.imshow('Dy and Wangwenxuan',img)

#Average blur
averaged = cv.blur(img,(5,5))
cv.imshow('Average blur',averaged)

#Gaussian Blur
gauss = cv.GaussianBlur(img,(5,5),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
Median = cv.medianBlur(img,5)
cv.imshow('Median Blur',Median)

#Bilateral Blur
Bilateral = cv.bilateralFilter(img,10,35,40)
cv.imshow('Bilateral',Bilateral)

cv.waitKey(0)