import cv2
import numpy as np

image = cv2.imread('nagoyashi.tif',0)

#hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#lower_range = np.array([110, 50, 50], dtype="uint8")
#upper_range = np.array([130, 255, 255], dtype="uint8")

mask = cv2.inRange(image, np.array([110,50,50]), np.array([130, 255, 255]))

cv2.imshow("Masked", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()