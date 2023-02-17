    #import libraries for image detection

import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

    #loading and viewing the image

img = cv2.imread('C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//test_image.png')

def leaf_counter(img):
    """Find number of leaves in image using classical object counting method using Python OpenCV as seen in https://www.geeksforgeeks.org/count-number-of-object-using-python-opencv/

    Note: 
        The python virtual evironment to be used is myenv.
    
    Examples:
        >>>leaf_counter(img)
        output: opens multiple windows

    Args:
        image (img): image=cv2.imread("//psqa//psqa2//Sample_pic//P6.png")


    Returns:
        images will only be opened when running python script and images will not be saved, command prompt will show number of leaves and hierarchy found

        """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #bluring the image

    plt.imshow(gray, cmap = 'gray');
    blur = cv2.GaussianBlur(gray, (11, 11), 0)
    plt.imshow(blur, cmap = 'gray')

        #canny the image

    canny = cv2.Canny(blur, 30, 150, 3)
    plt.imshow(canny, cmap='gray')

        #connect the edges

    dilated = cv2.dilate(canny, (1, 1), iterations=2)
    plt.imshow(dilated, cmap = 'gray')

        #add contour to image
        
    (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0,255,0), 2)
    plt.imshow(rgb)

    leaf_detected=len(cnt)

        #count objects in the image


    #plt.imshow(cnt, cmap = 'cnt')
    print('Number of Leaves: ', leaf_detected)
    print('Number of Hierarchy: ', heirarchy)
    plt.show()

leaf_counter(img=img)
#print('Number of Leaves: ', len(cnt))

#resize, set threshold (set leaf size)