import numpy as np
import cv2 as cv

img = cv.imread('F:\opencv_learning\photos/wwx.jpg')
print(img.shape)

blank = np.zeros(img.shape[:2],dtype='uint8')

mask = cv.circle(blank,(img.shape[1] // 2,img.shape[0] // 2),200,255,-1)

mask_img = cv.bitwise_and(img,img,mask=mask)

cv.imshow('Mask Image',mask_img)

cv.waitKey(0)