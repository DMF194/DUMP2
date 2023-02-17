Please read site/reference/index.html for more technical details of running code in psqa2 folder

Tips on moving forward(not covered in site/reference/index.html as it is incomplete) :

leafcount2.py is a variation of leafcount.py which focuses on using different thresholding techniques to find and isolate leafs from image

leafcount3.py is a variation of leafcount.py which focuses on using different clustering techniques to find and isolate leafs from image

line_detect.py is a variation of aruco_markers_tut.py which focuses on using different line detection techniques to 
estimate size(height and width) of plant by detecting the straight line by plant stem 

testui.py is used to display all the different modules such as leafcount,aruco_markers_tut and others in the form of a dashboard

Optional tools to use when testing/filtering images(not covered in site/reference/index.html as it not compulsory to include in final calculations) :

hsv_range_detector.py is used to find the appropriate range of HSV used to isolate parts of an image by colour region


Description of pictures generated:

size0.jpg is the result of running aruco_markers_tut.py with printed aruco marker

size1.jpg is the result of running aruco_markers_tut.py with the same printed aruco marker of larger size, producing similar dimensions

size2.jpg is the result of running aruco_markers_tut.py on one of the pictures from Sample_pic folder

size3.jpg is the result of running aruco_markers_tut.py on one of the pictures from Sample_pic folder when setting markerSize parameter

green.png is the result of dia_findcolour.py on one of the pictures from Sample_pic folder

IMPORTANT NOTE: requirements_myenv.txt has different(older) version of open-cv compared to requirements_aruco_env.txt. aruco_markers_tut.py will not work with the latest version of 
		open-cv listed in requirements_myenv.txt but will work in requirements_aruco_env.txt.

Please use pip install -r requirements.txt to install python packages into virtual environment of your choice.

Note that myenv and aruco_env as stated in site/reference/index.html will not be in this folder, 
you need to create the virtual environments myenv and aruco_env from the requirements_myenv.txt and requirements_aruco_env.txt respectively.








