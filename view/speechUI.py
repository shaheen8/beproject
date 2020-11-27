'''
Created on May 31, 2019

@author: Vinod Bhosale
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import speech_recognition as sr
from gtts import gTTS
import pyaudio
#from pygame import mixer
import os
from numpy.random.mtrand import choice
from PyQt4 import QtCore, QtGui
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

class Speech_Page(object):
    def speech_text(self):
        response=''               
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
              print("Listening from microphone........")
              print("Say something!")
              audio = r.listen(source,phrase_time_limit=15)
              response = r.recognize_google(audio)
              print("I think you said '" + response + "'")
              tts = gTTS(text="I think you said "+str(response), lang='en')
              print(tts)
        except sr.UnknownValueError:
            print("GTTS could not understand audio")
        except sr.RequestError as e:
            print("GTTS error; {0}".format(e))
        if response!=0:        
            with open('C:\\Users\\snehal\\Documents\\input-sign\\speechText.txt','w') as file:
                file.write(response)
                self.label.setText(_translate("HomePage", "I think you said :"+response, None))
                
    def setupUi(self, HomePage):
        HomePage.setObjectName(_fromUtf8("HomePage"))
        HomePage.resize(1300,800)
        HomePage.setStyleSheet(_fromUtf8("\n""background-image: url(hgr2.jpg);\n"""))
        self.centralwidget = QtGui.QWidget(HomePage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        HomePage.setCentralWidget(self.centralwidget)
        
        self.label = QtGui.QLabel(HomePage)
        self.label.setGeometry(QtCore.QRect(50, 100, 1000, 20))
        self.label.setObjectName(_fromUtf8("label"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
               
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 170, 160, 41))
        self.pushButton_3.clicked.connect(self.speech_text)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        



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
        HomePage.setWindowTitle(_translate("HomePage", "MainWindow", None))
        self.pushButton_3.setText(_translate("HomePage", "Say Something", None))
        self.label.setText(_translate("Dialog", "I think you said :", None))

        
   
           
           
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomePage = QtGui.QMainWindow()
    ui = Speech_Page()
    ui.setupUi(HomePage)
    HomePage.move(550, 170)
    HomePage.show()
    sys.exit(app.exec_())

