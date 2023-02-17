import math
from PyQt5 import QtCore, QtGui, QtWidgets
# from leafcount import *
from aruco_markers_tut import *


#from tensorflow.python.keras.layers import dense

class Ui_MainWindow(object):
    # PROVIDE PATH TO IMAGE DIRECTORY
    IMAGE_PATHS = 'C://Users//derkm//Develop3//psqa//psqa//Leaf Count//Picture2//P6.jpeg'
    #IMAGE_PATHS = 'C:/Users/user/Desktop/ACE/PSQA/Dataset/Test image.png'
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(57, 90, 831, 470))
   
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(self.IMAGE_PATHS))
        self.label_9.setObjectName("label_9")
        self.label_9.setScaledContents(True)
        self.horizontalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 20, 151, 51))
        
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 26))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        #print('I am here #?')
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #print('I am here #6')
        # leaf = self.leafs()
        #print('I am here #7')
        #dia,hi,rat = ["Root Collar Diameter", "Plant Height", "Straightness"]
        #diameter,
        
        #dia,hi,rat = [angle_between(p1, p2),angle_between(p1, p2),angle_between(p1, p2)]
        
        #self.other()
      
        #diameter,h,ratio = [self.other(),self.other(),self.other()]

        #return lambda: self.other()
        # print(self.other)
        # diameter,h,ratio = self.other()

        
        
        #print('I am here #13')
        # ws,col = self.whitespot()
        #print('I am here #14')
        # cent = self.center()
        # self.label_3.setText(_translate("MainWindow", "Leaf Count : {}".format(leaf_counter)))
        self.label_5.setText(_translate("MainWindow", "Plant Height: {}cm".format(d_wd)))
        # self.label_6.setText(_translate("MainWindow", "Straightness: {}Degree".format(ratio)))
        # self.label_2.setText(_translate("MainWindow", "WhiteSpot: {}".format(ws)))
        # self.label_7.setText(_translate("MainWindow", "Root Collar Diameter: {}cm".format(diameter)))
        # self.label_4.setText(_translate("MainWindow", "Colour: {}".format(col)))
        # self.label.setText(_translate("MainWindow", "Central Position: {}%".format(cent)))
        self.label_8.setText(_translate("MainWindow", "PSQA"))

        # return diameter,h,ratio

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
