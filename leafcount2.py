import cv2
import numpy as np

"""Assumes that the leaves are circular in shape and counts the circular shape blobs after applying Otsu thresholding and watershed segmentation"""
# Load the input image
img = cv2.imread('C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//test_image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary image
threshold_val, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find the contours in the thresholded image
contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Create a marker image to mark the regions
marker_image = np.zeros(gray.shape, dtype=np.int32)

# Loop through all the contours and mark them with different colors
for i, contour in enumerate(contours):
    cv2.drawContours(marker_image, contours, i, (i+1), -1)

# Perform the watershed transformation
marker_image = cv2.watershed(img, marker_image)

# Count the number of leaves
leaf_count = 0
for i in range(1, np.max(marker_image) + 1):
    # Get the region with the given label
    region = np.zeros(gray.shape, dtype=np.uint8)
    region[marker_image == i] = 255
    
    # Check if the region has a circular shape
    if cv2.countNonZero(region) > 0:
        region_contours, _ = cv2.findContours(region, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(region_contours) > 0:
            c = max(region_contours, key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(c)
            center = (int(x), int(y))
            radius = int(radius)
            circle = cv2.circle(img, center, radius, (0, 255, 0), 2)
            leaf_count += 1

print('Number of leaves:', leaf_count)
cv2.imshow('Leaf Count', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




