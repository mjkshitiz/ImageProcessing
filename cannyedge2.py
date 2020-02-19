import cv2
import numpy as np


img = cv2.imread('kawasaki.tif',0)


#ret, frame = img
	
#converting BGR to HSV
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
#define range of red color in HSVl

	
	# create a red HSV colour boundary and  
    # threshold HSV image 

    # Bitwise-AND mask and original image 

    # Display an original image 
cv2.imshow('Original',img) 
  
    # finds edges in the input image image and 
    # marks them in the output map edges 
edges = cv2.Canny(img,2.0,0.1,0.3) 
  
    # Display edges in a frame 
cv2.imshow('Edges',edges) 

  
    # Wait for Esc key to stop 
#cv2.imshow("images", np.hstack([image,output]))
cv2.waitKey(0)
