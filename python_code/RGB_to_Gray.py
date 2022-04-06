import cv2
import numpy
img = cv2.imread('E:/Image_processing/python_code/images/cat2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('Original image',img)
cv2.imshow('Gray imag',gray)
