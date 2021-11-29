import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np

img_ = cv.imread('F:\opencv_learning\photos/wwx.jpg')

def changeRes(input_,scale):
    height = int(input_.shape[0] * scale)
    width = int(input_.shape[1] * scale)
    dimension = (width,height)
    return cv.resize(input_,dimension,interpolation=cv.INTER_AREA)

img = changeRes(img_,.5)

# Gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',Gray)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank,(img.shape[1] // 2,img.shape[0] // 2),200,255,-1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)

# His_cal = cv.calcHist([Gray],[0],masked,[256],[0,256])

plt.figure()
plt.title('RGB Histogram')
plt.xlabel('bins')
plt.ylabel('number of pixels')
# plt.xlim([0,255])
# plt.plot(His_cal)
# plt.show()

#Calculating RGB Histogram
colors = ('b','g','r')
for i,col in enumerate(colors):
    His_cal = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(His_cal,color = col)
    plt.xlim([0,255])
    
plt.show()

cv.waitKey(0)