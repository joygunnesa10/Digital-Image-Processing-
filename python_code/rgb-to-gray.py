import cv2

img = cv2.imread("cat2.jpg")
cv2.imshow("Original",img)
cv2.waitKey(0)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image",gray_img)
cv2.waitKey(0)
cv2.destroyAllwindows()
                 

                 
