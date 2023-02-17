# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//P6.png", cv2.IMREAD_GRAYSCALE)

def BlobDetector(im, inertia_switch = True):

    '''Using existing algo in opencv2-python to Find and Label Plant Pot 

        Note: 
            The python virtual evironment to be used is myenv.
        
        Examples:
            >>>BlobDetector(im, inertia_switch = True)
            output: opens window image with red circle highlighting the detected blob as defined 

            >>>BlobDetector(im)
            output: opens window image with red circle highlighting the detected blob.
            Highlighted blob will be rectangular blobs since the default inertia_switch = True

        Args:
            im (img): image=cv2.imread("//psqa//psqa2//Sample_pic//20230110-150032.jpg")
            inertia_switch (bool): An boolean value based on the paramaters set in line 61-64 
            different dimensions as the aruco marker is used as reference object

        Returns:
            image (img): images will only be opened when running python script and images will not be saved, command prompt will show size of image
    '''

    print(im.shape)

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 50;
    params.maxThreshold = 200;

    # Filter by Area. Example minArea=100<=100 pixels
    params.filterByArea = True
    params.minArea = 1000
    #params.maxArea = 2000

    # Filter by Circularity
    params.filterByCircularity = False
    # params.minCircularity = 0.1 is default
    params.minCircularity = 1.0 #For perfect circle

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.87
    # params.minConvexity = 0.8 is default


    # Filter by Inertia
    params.filterByInertia = inertia_switch
    0 <= params.minInertiaRatio <= 1
    params.maxInertiaRatio <= 1

    # params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)

    # Set up the detector with default parameters.
    # detector = cv2.SimpleBlobDetector_create()

    # Detect blobs.
    keypoints = detector.detect(im)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)

    # https://learnopencv.com/blob-detection-using-opencv-python-c/

BlobDetector(im, inertia_switch = True)



