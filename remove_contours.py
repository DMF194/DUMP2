# import the necessary packages
import numpy as np
import imutils
import cv2


def is_contour_bad(c, removed_shape = 4):
	"""Detect shapes/polygons in image and labels them as bad shapes/polygons 
	and removes detected shapes/polygons from final image

	Note: 
		The python virtual evironment to be used is myenv.
    
    Examples:
        >>>is_contour_bad(c, removed_shape = 4)
        output: 3 windows will be opened and labelled accordingly

        >>>is_contour_bad(c)
        output: 3 windows will be opened and labelled accordingly as the default value for removed_shape=4

        >>>is_contour_bad(c, removed_shape = int_value)
        output: 3 windows will be opened and labelled accordingly 
		and int_value represents the number of vertices the shapes/polygons have. 

    Args:
		c (str): default is c as the c variable is used to loop over the contours found in line 53,
		therefore whenever the is_contour_bad() function is called, it must have c in ()
		removed_shape (int): An integer value used for number of vertices the shapes/polygons have.
		When removed_shape = 4, only the shapes/polygons that are rectangular in shape will not be highlighted.


    Returns:
        images (img): will only be opened when running python script and images will not be saved

	"""
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# the contour is 'bad' if it is not a rectangle

	remove_shape=len(approx)
	return not remove_shape == removed_shape

# load the shapes image, convert it to grayscale, and edge edges in
# the image
image = cv2.imread("C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//P6.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 100)
cv2.imshow("Original", image)
# find contours in the image and initialize the mask that will be
# used to remove the bad contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
mask = np.ones(image.shape[:2], dtype="uint8") * 255
# loop over the contours
for c in cnts:
	# if the contour is bad, draw it on the mask
	if is_contour_bad(c):
		cv2.drawContours(mask, [c], -1, 0, -1)
# remove the contours from the image and show the resulting images
image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("After", image)
cv2.waitKey(0)