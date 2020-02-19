"""
 * Python script to demonstrate Canny edge detection.
 *
 * usage: python CannyEdge.py <filename> <sigma> <low_threshold> <high_threshold>
"""
import skimage
from skimage import feature
from skimage import viewer
import sys

# read command-line arguments
def main():
	filename = sys.argv[1]
	sigma = float(sys.argv[2])
	low_threshold = float(sys.argv[3])
	high_threshold = float(sys.argv[4])

	# load and display original image as grayscale

	image = skimage.io.imread(fname=filename, as_gray=True)
	viewer = skimage.viewer(image=image)
	viewer.show(image)

	#Using canny edge detection
	edges = skimage.feature.canny(
		image=image,
		sigma=sigma,
		low_threshold=low_threshold,
		high_threshold=high_threshold,
	)

	# display edges
	viewer = skimage.viewer.ImageViewer(edges)
	viewer.show()
if __name__ == "__main__":
	main()