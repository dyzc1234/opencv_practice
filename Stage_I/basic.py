import cv2 as cv


img_ = cv.imread('F:\opencv_learning\photos/Doraemen.jpg')

def changeRes(input_,scale):
    height = int(input_.shape[0] * scale)
    width = int(input_.shape[1] * scale)
    dimension = (width,height)
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

img = changeRes(img_,.3)

cv.imshow('This is Draemen',img)

# Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Doraemen Gray',gray)

#Blur
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
canny = cv.Canny(blur,80,180)
cv.imshow('canny',canny)

#Dilating The Image
dilated = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('Dilated',dilated)

#Eroding
eroded = cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded',eroded)

#Resize
# resized = cv.resize(img,(200,200),interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized',resized)

#Cropped
cropped = img[100:250,200:300]
cv.imshow('Cropped',cropped)

cv.waitKey(30000)
cv.destroyAllWindows()