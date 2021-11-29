import cv2 as cv

img_ = cv.imread('F:\opencv_learning\photos/wwx.jpg')

def changeRes(input_,scale):
    height = int(input_.shape[0] * scale)
    width = int(input_.shape[1] * scale)
    dimension = (width,height)
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

img = changeRes(img_,.5)

Gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',Gray)

threshold,thresh = cv.threshold(Gray,150,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)

threshold,thresh_inv = cv.threshold(Gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Threshold_inv',thresh_inv)

Adaptive_Thresh = cv.adaptiveThreshold(Gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,3)
cv.imshow('Threshold_Adptive',Adaptive_Thresh)


cv.waitKey(0)