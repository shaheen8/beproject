# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from view.speechUI import Speech_Page
from methods import signShow as sh
from methods import signShow1 as sh1
import speech_recognition as sr
from gtts import gTTS
import pyaudio
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

class two_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName(_fromUtf8("HomePage"))
        HomePage.resize(1300,800)
        HomePage.setStyleSheet(_fromUtf8("\n""background-image: url(dp01.jpg);\n"""))

        
        self.pushButton = QtGui.QPushButton(HomePage)
        self.pushButton.setGeometry(QtCore.QRect(210, 170, 180, 41))
        self.pushButton.clicked.connect(self.speech_text)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton1 = QtGui.QPushButton(HomePage)
        self.pushButton1.setGeometry(QtCore.QRect(210, 250, 180, 41))
        self.pushButton1.clicked.connect(self.speech_text1)
        self.pushButton1.setStyleSheet(_fromUtf8("background-color: black"))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))

        self.label = QtGui.QLabel(HomePage)
        self.label.setGeometry(QtCore.QRect(100, 20, 520, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.label1 = QtGui.QLabel(HomePage)
        self.label1.setGeometry(QtCore.QRect(50, 100, 1000, 20))
        self.label1.setObjectName(_fromUtf8("label1"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def speech(self):
        self.videoWindow=QtGui.QMainWindow()
        self.ui=Speech_Page()
        self.ui.setupUi(self.videoWindow)
        self.videoWindow.show()


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
            with open('C:\\Users\\shaheen\\Desktop\\input-sign\\speechText.txt','w') as file:
                file.write(response)
                self.label1.setText(_translate("HomePage", "I think you said :"+response, None))
                print('sign to image')
                sh.signRecog(self, response)

    def speech_text1(self):
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
            with open('C:\\Users\\shaheen\\Desktop\\input-sign\\speechText.txt','w') as file:
                file.write(response)
                self.label1.setText(_translate("HomePage", "I think you said :"+response, None))
                print('sign to action')
                sh1.signRecog(self, response)

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(_translate("HomePage", "Two Way Communication", None))
        self.label.setText(_translate("HomePage", "NORMAL PERSON TO DEAF COMMUNICATION", None))
        self.label1.setText(_translate("Dialog", "I think you said :", None))
        self.pushButton.setText(_translate("HomePage", "SPEECH To SIGN TRANSLATOR", None))
        self.pushButton1.setText(_translate("HomePage", "SPEECH To ACTION TRANSLATOR", None))




           
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomePage = QtGui.QMainWindow()
    ui = two_HomePage()
    ui.setupUi(HomePage)
    HomePage.move(550, 170)
    HomePage.show()
    sys.exit(app.exec_())

