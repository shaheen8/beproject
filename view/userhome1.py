# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from HandGesture import classify_webcam2 as fs2
from HandGesture import classify_webcam3 as fs3
from methods import text_speech1 as ts3
from methods import gesture as fs4
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

class one_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName(_fromUtf8("HomePage"))
        HomePage.resize(1300,800)
        HomePage.setStyleSheet(_fromUtf8("\n""background-image: url(dp01.jpg);\n"""))


        self.pushButton = QtGui.QPushButton(HomePage)
        self.pushButton.setGeometry(QtCore.QRect(250, 80, 160, 41))
        self.pushButton.clicked.connect(self.HGR1)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.pushButton_2 = QtGui.QPushButton(HomePage)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 170, 160, 41))
        self.pushButton_2.clicked.connect(self.HGR2)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.pushButton_3 = QtGui.QPushButton(HomePage)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 260, 160, 41))
        self.pushButton_3.clicked.connect(self.HGR3)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_4 = QtGui.QPushButton(HomePage)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 350, 160, 41))
        self.pushButton_4.clicked.connect(self.text_speech)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.label = QtGui.QLabel(HomePage)
        self.label.setGeometry(QtCore.QRect(100, 20, 510, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))



        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(_translate("HomePage", "Two Way Communication", None))
        self.label.setText(_translate("HomePage", "DEAF PERSON TO NORMAL COMMUNICATION", None))
        self.pushButton.setText(_translate("HomePage", "NUMBER DETECTION", None))
        self.pushButton_2.setText(_translate("HomePage", "ALPHABET RECONITION", None))
        self.pushButton_3.setText(_translate("HomePage", "WORD DETECTION", None))
        self.pushButton_4.setText(_translate("HomePage", "VOICE CONVERSION", None))

    def HGR1(self):
        print('Process Start')
        fs4.gesture(self)

    def HGR2(self):
        print('Process Start')
        fs2.classify_Web(self)

    def HGR3(self):
        print('Process Start')
        fs3.classify_Web(self)

    def text_speech(self):
        fileName = 'C:\\Users\\shaheen\\Desktop\\input-sign\\abc.txt'
        print('Process Start')
        ts3.audio(self, fileName)

           
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomePage = QtGui.QMainWindow()
    ui = one_HomePage()
    ui.setupUi(HomePage)
    HomePage.move(550, 170)
    HomePage.show()
    sys.exit(app.exec_())

