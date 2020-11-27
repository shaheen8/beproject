# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from UploadImage import Ui_MainWindow
from view.userhome1 import one_HomePage
from view.userhome2 import two_HomePage
from numpy.distutils.exec_command import filepath_from_subprocess_output


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName(_fromUtf8("HomePage"))
        HomePage.resize(1300,800)
        HomePage.setStyleSheet(_fromUtf8("\n""background-image: url(dp01.jpg);\n"""))
        self.centralwidget = QtGui.QWidget(HomePage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 80, 250, 41))
        self.pushButton.clicked.connect(self.upload)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 170, 250, 41))
        self.pushButton_2.clicked.connect(self.one)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 260, 250, 41))
        self.pushButton_3.clicked.connect(self.two)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.label = QtGui.QLabel(HomePage)
        self.label.setGeometry(QtCore.QRect(100, 20, 600, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
       
        
        HomePage.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(HomePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        HomePage.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(HomePage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        HomePage.setStatusBar(self.statusbar)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(_translate("HomePage", "Two Way Communication", None))
        self.label.setText(_translate("HomePage", "REAL TIME TWO WAY COMMUNICATION INTERPRETER", None))
        self.pushButton.setText(_translate("HomePage", "Image Processing", None))
        self.pushButton_2.setText(_translate("HomePage", "ONE WAY COMMUNICATION", None))
        self.pushButton_3.setText(_translate("HomePage", "TWO WAY COMMUNICATION", None))


    def upload(self):
        self.videoWindow=QtGui.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUii(self.videoWindow)
        self.videoWindow.show()

    def one(self):
        self.oneCheck()

    def two(self):
        self.twoCheck()

    def oneCheck(self):
        self.oneWindow = QtGui.QDialog()
        self.ui = one_HomePage()
        self.ui.setupUi(self.oneWindow)
        self.oneWindow.show()

    def twoCheck(self):
        self.oneWindow = QtGui.QDialog()
        self.ui = two_HomePage()
        self.ui.setupUi(self.oneWindow)
        self.oneWindow.show()
           
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomePage = QtGui.QMainWindow()
    ui = Ui_HomePage()
    ui.setupUi(HomePage)
    HomePage.move(550, 170)
    HomePage.show()
    sys.exit(app.exec_())

