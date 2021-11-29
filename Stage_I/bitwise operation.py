import cv2 as cv 
import numpy as np


blank = np.zeros((400,400),dtype='uint8')

Rectangle = cv.rectangle(blank.copy(),(50,50),(350,350),255,-1)
Cicle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',Rectangle)
cv.imshow('Cicle',Cicle)

# Bitwise and
Bitwise_and = cv.bitwise_and(Rectangle,Cicle)
cv.imshow('Bitwise_and',Bitwise_and)

# Bitwise or
Bitwise_or = cv.bitwise_or(Rectangle,Cicle)
cv.imshow('Bitwise_or',Bitwise_or)

# Bitwise xor
Bitwise_xor = cv.bitwise_xor(Rectangle,Cicle)
cv.imshow('Bitwise_xor',Bitwise_xor)

#Bitwise not
Bitwise_not = cv.bitwise_not(Rectangle)
cv.imshow('No Rectangle',Bitwise_not)

cv.waitKey(0)