#Detect soil shape 

import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading image
img = cv2.imread('C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//P6.png')

# converting image into grayscale image

# '''Start any shape finding'''
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('shapes', img)

# # setting threshold of gray image
# _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# # using a findContours() function
# contours, _ = cv2.findContours(
# 	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# i = 0

# # list for storing names of shapes
# for contour in contours:

# 	# here we are ignoring first counter because
# 	# findcontour function detects whole image as shape
# 	if i == 0:
# 		i = 1
# 		continue

# 	# cv2.approxPloyDP() function to approximate the shape
# 	approx = cv2.approxPolyDP(
# 		contour, 0.01 * cv2.arcLength(contour, True), True)
	
# 	# using drawContours() function
# 	cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

# 	# finding center point of shape
# 	M = cv2.moments(contour)
# 	if M['m00'] != 0.0:
# 		x = int(M['m10']/M['m00'])
# 		y = int(M['m01']/M['m00'])

# 	# putting shape name at center of each shape
# 	if len(approx) == 3:
# 		cv2.putText(img, 'Triangle', (x, y),
# 					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# 	elif len(approx) == 4:
# 		cv2.putText(img, 'Quadrilateral', (x, y),
# 					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# 	elif len(approx) == 5:
# 		cv2.putText(img, 'Pentagon', (x, y),
# 					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# 	elif len(approx) == 6:
# 		cv2.putText(img, 'Hexagon', (x, y),
# 					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# 	else:
# 		cv2.putText(img, 'circle', (x, y),
# 					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# # displaying the image after drawing contours
# cv2.imshow('shapes', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# '''End any shape finding'''


# Convert to Grayscale

def shape_detector(img):

	'''Detect shapes/polygons in image as some leaves are labelled as ellipses 
	and can be isolated from image to count number of leaves

	Note:
		The python virtual evironment to be used is myenv.
    
    Examples:
        >>>green_detector(img)
        output: 4 windows will be opened and labelled accordingly

    Args:
        img: image=cv2.imread("//psqa//psqa2//Sample_pic//P6.png")


    Returns:
        image (img): images will only be opened when running python script and images will not be saved, command prompt will show number of shapes found

	'''

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	invert = cv2.bitwise_not(gray)
	cv2.imshow('Converted gray from RGB', gray)
	#cv2.imshow('Inverted gray', invert)

	_, th2 = cv2.threshold(invert, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	cv2.imshow('After thresholding', th2)

	# Finding Contours
	# Use a copy of your image e.g. edged.copy(), since findContours alters the image
	contours, hierarchy = cv2.findContours(th2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

	# Draw all contours, note this overwrites the input image (inplace operation)
	# Use '-1' as the 3rd parameter to draw all
	cv2.drawContours(img, contours, -1, (0,255,0), thickness = 2)
	cv2.imshow('Contours overlaid on original image', img)

	print("Number of Contours found = " + str(len(contours)))

	i = 0

	# list for storing names of shapes
	for contour in contours:

		# here we are ignoring first counter because
		# findcontour function detects whole image as shape
		if i == 0:
			i = 1
			continue

		# cv2.approxPloyDP() function to approximate the shape
		approx = cv2.approxPolyDP(
			contour, 0.01 * cv2.arcLength(contour, True), True)
		
		# using drawContours() function
		cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

		# finding center point of shape
		M = cv2.moments(contour)
		if M['m00'] != 0.0:
			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])

		# putting shape name at center of each shape
		if len(approx) == 3:
			cv2.putText(img, 'Triangle', (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

		elif len(approx) == 4:
			cv2.putText(img, 'Quadrilateral', (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

		elif len(approx) == 5:
			cv2.putText(img, 'Pentagon', (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

		elif len(approx) == 6:
			cv2.putText(img, 'Hexagon', (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

		else:
			cv2.putText(img, 'circle', (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

	# displaying the image after drawing contours
	cv2.imshow('shapes', img)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

shape_detector(img=img)



