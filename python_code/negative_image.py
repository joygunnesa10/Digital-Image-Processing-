import cv2
import numpy as np
img = cv2.imread('E:/Image_processing/python_code/images/rose.jpg')
print (img.dtype)
img_neg = 255 - img
cv2.imshow('negative',img_neg)
cv2.waitKey(0)
