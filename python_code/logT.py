import cv2
import numpy as np
img = cv2.imread('cat2.jp,g',0)
cv2.imshow('image',img)
#f = cv2.hconcat((re_img,re_img))
img1 = np.uint8(np.log1p(img))
t = 1
img2 = cv2.threshold(img1,t,255,cv2.THRESH_BINARY)[1]
f = cv2.hconcat((img,img2))
cv2.imshow('image',f)
#cv2.imshow('image',img)
#cv2.imshow('image1',img2)
