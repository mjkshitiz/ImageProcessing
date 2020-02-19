#import the necessary packages
import cv2
import numpy as np
import argparse

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
args = vars(ap.parse_args())

#load the image
image = cv2.imread(args["image"])

# Define the list of boundaries

boundaries = [
    ([110, 50, 50], [130, 255, 255])
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	print(lower)
	print(upper)
	#find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	res = cv2.bitwise_and(image, image, mask= mask)
	cv2.imshow("masked",mask)
	cv2.imshow("Res",res)
	output = cv2.bitwise_and(image, image, mask = mask)
	#edges = cv2.Canny(image,100,200)
	
	
	# show the images
	cv2.imshow("images", np.hstack([image,output]))
	cv2.waitKey(0)
