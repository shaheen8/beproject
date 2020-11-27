# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UploadVideo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import tkinter
import tkinter.filedialog

from PyQt4 import QtCore, QtGui
from methods import grayscale as fs
from methods import binarization as fs1
from methods import EdgeDetection as fs2


root=tkinter.Tk()

print('******Start*****')
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

class Ui_MainWindow(object):
    

    def setupUii(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1300, 800)
        MainWindow.setStyleSheet(_fromUtf8("\n""background-image: url(finger.png);\n"""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 180, 131, 27))
        self.pushButton.clicked.connect(self.grayscale)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: white"))
       
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#################################################################
        
######################################################################
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 50, 241, 31))
        
        self.textEdit.setStyleSheet(_fromUtf8("background-color: white"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 220, 131, 27))
        self.pushButton_4.clicked.connect(self.binarization)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: white"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 260, 131, 27))
        self.pushButton_5.clicked.connect(self.edgedetection)
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: white"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 120, 99, 27))
        self.pushButton_3.clicked.connect(self.browse)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: white"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 41, 17))
        self.label.setStyleSheet(_fromUtf8("background-color: white"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Upload Image", None))
        self.pushButton_3.setText(_translate("MainWindow", "Select Image", None))
        self.pushButton.setText(_translate("MainWindow", "Grayscale", None))
        self.pushButton_4.setText(_translate("MainWindow", "Binarization", None))
        self.pushButton_5.setText(_translate("MainWindow", "Edge Detection", None))
        self.label.setText(_translate("MainWindow", "Path", None))

    def quit(self):
        print ('Process end')
        print ('******End******')
        quit()
         
    def browse(self):
        global fileName
        root.withdraw()
        filename = tkinter.filedialog.askopenfilename()
        fileName = filename
        self.textEdit.setText(fileName)
        return fileName 
    
    def grayscale(self):
        print ('Process Start')
        fs.grayscale(self,fileName)
    
    def binarization(self):
        print ('Process Start')
        fs1.binarization(self,fileName)
        
    def edgedetection(self):
        print ('Process Start')
        fs2.edgedetection(self,fileName)
    

         
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUii(MainWindow)
    MainWindow.move(550, 170)
    MainWindow.show()
    sys.exit(app.exec_())
    

