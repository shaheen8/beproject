# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3


#from GetPass import pass as ps

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

class Ui_passCheck(object):

        
    def loginCheck(self):
        
        password = ""
        
        username1=self.uname_lineEdit.text()
        username =str(username1)
        
        connection=sqlite3.connect("sign.db")
        s="select *from registration where username='"+username+"'"
        print("query is:"+s)
        result=connection.execute(s)
        t=result.fetchall()
        if(len(t)>0):
            password = t[0][4]
            print(password)
            #print(t[3])
            print("user found!")
            pass_str = "Hi {}! your password is: {}".format(username, password)
            
            #ps.pass(self,username)
            #return self.password          
        else:
            print("user not found!")
            password = "user not found!"
            pass_str = "Sorry, user not found!"
            #return self.password
        #pass_str = "Hi {}! your password is: {}".format(username, password)
        self.pass_label.setText(_translate("Dialog", pass_str, None))
         
        
    def setinUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1200, 800)
        Dialog.setStyleSheet(_fromUtf8("\n""background-image: url(hgr2.jpg);\n"""))
         
        self.u_user_label = QtGui.QLabel(Dialog)
        self.u_user_label.setGeometry(QtCore.QRect(90, 150, 91, 31))
        self.u_user_label.setObjectName(_fromUtf8("u_user_label"))
        
        self.pass_label = QtGui.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(190, 200, 201, 31))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))

       
        
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(190, 149, 201, 31))
        self.uname_lineEdit.setText(_fromUtf8(""))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
       

        
        
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(220, 250, 80, 31))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.login_btn.setStyleSheet("background-color: black")
       #####################Button Event####################################
        self.login_btn.clicked.connect(self.loginCheck)
       ############################################################################
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 90, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Forgote Password", None))
        self.u_user_label.setText(_translate("Dialog", "Enter USERNAME", None))
        #self.pass_label.setText(_translate("Dialog", self.password, None))
      
        self.login_btn.setText(_translate("Dialog", "Get Password", None))
        self.label.setText(_translate("Dialog", "Relogin", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_passCheck()
    ui.setinUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())