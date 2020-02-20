import numpy as np
import cv2

img = cv2.imread('savedImage.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[4]
imge = cv2.drawContours(imgray, [cnt], 3, (0,255,0), 2)
cv2.imshow(imge)