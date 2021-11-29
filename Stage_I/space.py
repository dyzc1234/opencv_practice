import cv2 as cv
import matplotlib.pyplot as plt

img_ = cv.imread()

def ChangeRes(input_,scale):
    dimension = (int(input_.shape[1] * scale),int(input_.shape[0] * scale))
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

#Resize the Image
img = ChangeRes(img_,.3)
cv.imshow('Dy and Wangwenxuan',img)

#BGR to Grayscale
Gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',Gray)

#BGR to HSV
HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',HSV)

#BGR to LAB
LAB = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',LAB)

#BGR to RGB
RGB = cv.cvtColor(img,cv.COLOR_BGRA2RGB)
cv.imshow('RGB',RGB)
plt.imshow(RGB)
plt.show()


cv.waitKey(0)


