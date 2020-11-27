# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from tkinter.constants import ALL
from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QRegExpValidator
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re
import sys
from tkinter.constants import ALL

from tkinter.constants import ALL
from login import Ui_Dialog
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

class Ui_signUp(object):
     def insertData(self):

        username1 = self.uname_lineEdit.text()
        username=str(username1)
        email1 = self.email_lineEdit.text()
        email = str(email1)
        mob1= self.mob_lineEdit.text()
        mob=str(mob1)
        password1 = self.password_lineEdit.text()
        password =str(password1)
        gender1= self.gender_lineEdit.text()
        gender=str(gender1)
        
        connection = sqlite3.connect("sign.db")
        s="insert into registration (username,email,mob,password,gender) values('"+username+"','"+email+"','"+mob+"','"+password+"','"+gender+"')"
        print("query is:-"+s)
        result=connection.execute(s)
        if result:
            s1="select * from registration"
            result=connection.execute(s1)
            print("Success"+s1)
        
        connection.commit()
        connection.close()
        self.showmsg()

     def showmsg(self):
        self.showdialog()
     def showdialog(self):
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Information)

         msg.setText("Registration Status")
         msg.setInformativeText("Registration Successful")
         msg.setWindowTitle("Status")
         # msg.setDetailedText("The details are as follows:")
         msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

         retval = msg.exec_()
         print
         "value of pressed message box button:", retval
     def signInCheck(self):
        print("hello signin button")
        self.signInWindow=QtGui.QDialog()
        self.ui=Ui_Dialog()
        print("i'm in self signin")
        self.ui.setinUi(self.signInWindow)
        print("i'm in self setupUi method")
        self.signInWindow.show()
        print("i'm in self signin windows")   
     
     def signInButton(self):
            self.signInCheck()
                    
     def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1300, 800)
        Dialog.setStyleSheet(_fromUtf8("\n""background-image: url(hgr2.jpg);\n"""))
   
   
#############################################################################
 
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 100, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
               
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        
        self.label_M = QtGui.QLabel(Dialog)
        self.label_M.setGeometry(QtCore.QRect(100, 200, 91, 20))
        self.label_M.setObjectName(_fromUtf8("label_M"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_M.setFont(font)
        
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 250, 91, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
                
        self.label_G = QtGui.QLabel(Dialog)
        self.label_G.setGeometry(QtCore.QRect(100, 300, 91, 20))
        self.label_G.setObjectName(_fromUtf8("label_G"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_G.setFont(font)
        #############################################################

        
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(210, 100, 211, 27))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        
        
        self.email_lineEdit = QtGui.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(210, 150, 211, 27))
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        
        self.mob_lineEdit = QtGui.QLineEdit(Dialog)
        self.mob_lineEdit.setGeometry(QtCore.QRect(210, 200, 211, 27))
        self.mob_lineEdit.setObjectName(_fromUtf8("mob_lineEdit"))
        
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(210, 250, 211, 27))
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        
        self.gender_lineEdit = QtGui.QLineEdit(Dialog)
        self.gender_lineEdit.setGeometry(QtCore.QRect(210, 300, 211, 27))
        self.gender_lineEdit.setObjectName(_fromUtf8("gender_lineEdit"))
        
        ###################################################################
        
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(217, 19, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(210, 350, 91, 27))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        self.signup_btn.setStyleSheet("background-color: black")
        #########################EVENT##############
        self.signup_btn.clicked.connect(self.insertData)
############################################
        
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(328, 350, 91, 27))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.login_btn.setStyleSheet("background-color: black")
        self.login_btn.clicked.connect(self.signInButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

     def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        
  
        self.label.setText(_translate("Dialog", "USERNAME", None))
        self.label_2.setText(_translate("Dialog", "EMAIL ID", None))
        self.label_M.setText(_translate("Dialog", "MOBILE", None))
        self.label_3.setText(_translate("Dialog", "PASSWORD", None))
        self.label_G.setText(_translate("Dialog", "GENDER", None))
        self.label_4.setText(_translate("Dialog", "Registration Form", None))
        self.signup_btn.setText(_translate("Dialog", "REGISTER", None))
        self.login_btn.setText(_translate("Dialog", "LOGIN", None))
        
     

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

