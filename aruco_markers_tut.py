# import the necessary packages

import numpy as np
import imutils
from imutils import contours
from imutils import perspective
import cv2
from scipy.spatial import distance as dist
from typing import Union

# detect aruco marker
def findArucoMarkers(img, markerSize = 6, totalMarkers=100, draw=True):
    """To find an existing aruco marker based on multiple inputs

    Note: 
        The python virtual evironment to be used is aruco_env. 
    
    Examples:
        >>>findArucoMarkers(img, markerSize = 6, totalMarkers=100)
        output: {opens multiple windows}

        >>>findArucoMarkers(img)
        output: {opens multiple windows and uses default values from 1st example}

        >>>findArucoMarkers(img, markerSize = int_value)
        output: {opens multiple windows}
                {[363. 617.][484. 617][485. 737.][363. 738.]} #shows location
                {pixel to inch 60.5}

        >>>findArucoMarkers(img, totalMarkers = int_value)
        output: {opens multiple windows}

    Args:
        img (img): image=cv2.imread("//psqa//psqa2//Sample_pic//20230110-150032.jpg")
        markerSize (int): An interger value based on generated aruco marker size and different values will produce different 
        different dimensions as the aruco marker is used as reference object
        totalMarkers (int): An interger value used to detect multiple aruco marker in img and will use default 
        markerSize = 6 to produce dimensions 

    Returns:
        img (img): image saved under //psqa//psqa2// and the image will be saved as size3.jpg as defined by i=3 line code 139}

        """

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(cv2.aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    #print(key)

    #Load the dictionary that was used to generate the markers.
    arucoDict = cv2.aruco.Dictionary_get(key)
    
    # Initialize the detector parameters using default values
    arucoParam = cv2.aruco.DetectorParameters_create()
    
    # Detect the markers
    bboxs, ids, rejected = cv2.aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    return bboxs, ids, rejected
# find object size 

#Load image
image=cv2.imread("C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//20230110-150032.jpg")

# resize image
image = imutils.resize(image, width=500)

# convert BGR image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# remove Gaussian noise from the image
gray = cv2.GaussianBlur(gray, (7, 7), 0)

# perform edge detection, then perform a dilation + erosion to
# close gaps in between object edges
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# sort the contours from left-to-right and initialize the
(cnts, _) = contours.sort_contours(cnts)

# for pixel to inch calibration 
pixelsPerMetric = None

# Detect Aruco marker and use 
#it's dimension to calculate the pixel to inch ratio
arucofound =findArucoMarkers(image, totalMarkers=100)
# arucofound =findArucoMarkers(image, markerSize = 4)
if  len(arucofound[0])!=0:
    print(arucofound[0][0][0])
    aruco_perimeter = cv2.arcLength(arucofound[0][0][0], True)
    print(aruco_perimeter)
    # Pixel to Inch ratio
    # perimeter of the aruco marker is 8 inches
    # pixelsPerMetric = aruco_perimeter / 8

    # perimeter of the aruco marker is 20.32 cm

    pixelsPerMetric = aruco_perimeter / 20.32
    print(" pixel to inch",pixelsPerMetric)
else:
    pixelsPerMetric=38.0

# loop over the contours individually
for c in cnts:
    
    # if the contour is not sufficiently large, ignore it
    if cv2.contourArea(c) < 2000:
        continue
    ''' bounding rectangle is drawn with minimum area, so it considers the rotation also. 
    The function used is cv.minAreaRect(). It returns a Box2D structure which contains following details - 
    ( center (x,y), (width, height), angle of rotation ). 
    But to draw this rectangle, we need 4 corners of the rectangle. 
    It is obtained by the function cv.boxPoints()
    '''      
    # compute the rotated bounding box of the contour
    box = cv2.minAreaRect(c)
    box = cv2.boxPoints(box)
    box = np.int0(box)
    cv2.drawContours(image,[box],0,(0,0,255),2)
    
    # Draw the centroid   
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(image, (cX, cY), 5, (255, 255, 255), -1)
       
    # order the points in the contour such that they appear
    # in top-left, top-right, bottom-right, and bottom-left
    # order, then draw the outline of the rotated bounding
    # box  
    (tl, tr, br, bl) = box
    width_1 = (dist.euclidean(tr, tl))
    height_1 = (dist.euclidean(bl, tl))
    d_wd= width_1/pixelsPerMetric
    d_ht= height_1/pixelsPerMetric
    
    #display the image with object width and height in inches
    cv2.putText(image, "{:.1f}cm".format(d_wd),((int((tl[0]+ tr[0])*0.5)-15, int((tl[1] + tr[1])*0.5)-15)), cv2.FONT_HERSHEY_SIMPLEX,0.65, (255, 255, 255), 2)
    cv2.putText(image, "{:.1f}cm".format(d_ht),((int((tr[0]+ br[0])*0.5)+10, int((tr[1] + br[1])*0.5)+10)), cv2.FONT_HERSHEY_SIMPLEX,0.65, (255, 255, 255), 2)
    # show the output image
    cv2.imshow("Image-dim", image)
    # initialize i 
    i=3
    fname="size{}.jpg".format(str(i))
    cv2.imwrite(fname, image)
    key = cv2.waitKey(0)

cv2.destroyAllWindows()