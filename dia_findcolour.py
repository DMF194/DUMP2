#Detect soil shape 

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//test_image.png')

lower_green = np.array([36, 25, 25], dtype = "uint8") 

upper_green= np.array([70, 255,255], dtype = "uint8")

def green_detector(image, lower_green, upper_green):

    '''Detect green plant colour in selected image

    Note: 
        The python virtual evironment to be used is myenv.
    
    Examples:
        >>>green_detector(image = <image_file_path>, lower_green = lower_green, upper_green=upper_green)
        output: {windows with green regions highlighted}

    Args:
        image (img): image=cv2.imread("//psqa//psqa2//Sample_pic//test_image.png")
        lower_green (array): Values in the [] on line 9 np.array([36, 25, 25], dtype = "uint8"), all three values must be integer and will use default 
        lower_green = [[36, 25, 25]] to produce image
        upper_green (array): Values in the [] on line 11 np.array([70, 255,255], dtype = "uint8"), all three values must be integer and will use default 
        upper_green = [[70, 255,255]] to produce image

    Returns:
        image (img): image saved under //psqa//psqa2// and the image will be saved as green.png 
'''

    # reading image
    # image = cv2.imread('C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//P11.jpeg')

    ## convert to hsv
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    ## mask of green (36,25,25) ~ (86, 255,255)
    # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
    # mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))
    mask = cv2.inRange(hsv, lower_green, upper_green)

    ## slice the green
    imask = mask>0
    green = np.zeros_like(image, np.uint8)
    green[imask] = image[imask]   

    print(imask)
    cv2.imshow("green", green)
    cv2.waitKey(0) 

    # save 
    cv2.imwrite("green.png", green)

    cv2.destroyAllWindows()

green_detector(image=image, lower_green=lower_green, upper_green=upper_green)

'''Detect soil brown colour in selected image'''

# # reading image
# img = cv2.imread('C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//P11.jpeg')

# ## convert to hsv
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ## mask of green (36,25,25) ~ (86, 255,255)
# # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
# mask = cv2.inRange(hsv, (10, 100, 20), (20, 255, 200))

# ## slice the brown
# imask = mask>0
# brown = np.zeros_like(img, np.uint8)
# brown[imask] = img[imask]   

# print(imask)
# cv2.imshow("brown", brown)
# cv2.waitKey(0)

## save 
#cv2.imwrite("green.png", green)

# reading image
img = cv2.imread('C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//test_image.png')

lower_green = np.array([25, 146, 190], dtype = "uint8") 

upper_green= np.array([62, 174, 250], dtype = "uint8")

mask = cv2.inRange(img, lower_green, upper_green)


detected_output = cv2.bitwise_and(img, img, mask =  mask) 

cv2.imshow("green color detection", detected_output) 

cv2.waitKey(0) 

