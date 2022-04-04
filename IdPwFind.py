from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Gui
import DB
import Config


class PageIdPwFindLogic:
    def __init__(self,Gui):
        self.mainGui = Gui
        self.db = DB.DataBase()

        self.mainGui.btnBackIdPwFind.clicked.connect(self.btnEventBack)
        self.mainGui.btnIdPwFindEnd[0].clicked.connect(self.btnEventIdFind)
        self.mainGui.btnIdPwFindEnd[1].clicked.connect(self.btnEventPwFind)

    def btnEventBack(self): 
        self.mainGui.lineLogin[0].clear() # 로그인 페이지 라인 위젯 초기화 
        self.mainGui.lineLogin[1].clear()

        self.mainGui.stackedWidget.setCurrentIndex(0) # 로그인 페이지로 이동

        for index in range(0,5): #
            self.mainGui.lineUserInf[index].clear()

    def btnEventIdFind(self):
        table = "member"
        colum = ["name","phonenumber"]
        value = [self.mainGui.lineUserInf[0].text(),self.mainGui.lineUserInf[1].text()]

        if self.db.readData(table,colum,value):
            self.dialogIdFind = QtWidgets.QDialog()                  #다이아로그는 멤버변수가 아니라 상황마다 지역변수에만 써주자 
            self.dialog = Gui.Dialog(self.dialogIdFind)           #멤버변수로 하면 메모리가 너무 소모된다.
            
            text = QtWidgets.QTextEdit(self.dialogIdFind)
            text.setGeometry(70,150,400,100)
            text.setStyleSheet("border : 0px; \n color : #ffffff; \n background-color : #000000;")
            text.setText("아이디는 " + self.db.result[0][1] + "입니다.")

            self.dialogIdFind.show()

            for index in range(0,5):
                self.mainGui.lineUserInf[index].clear()    
        else:
            self.dialogFindFail = QtWidgets.QDialog()
            self.dialog = Gui.Dialog(self.dialogFindFail)

            text = QtWidgets.QTextEdit(self.dialogFindFail)
            text.setGeometry(200,60,300,45)
            text.setStyleSheet(Config.infTextStylesheet[0])
            text.setText(Config.textFindFail[0])
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(10)
            text.setFont(font)

            text = QtWidgets.QTextEdit(self.dialogFindFail)
            text.setGeometry(70,158,450,90)
            text.setStyleSheet(Config.infTextStylesheet[0])
            text.setText(Config.textFindFail[1])
            text.setFont(font)

            self.dialogFindFail.show()

    def btnEventPwFind(self):
        table = "member"
        colum = ["id","name","phonenumber"]
        value = [self.mainGui.lineUserInf[2].text(),self.mainGui.lineUserInf[3].text(),self.mainGui.lineUserInf[4].text()]
    
        if self.db.readData(table,colum,value):
            self.dialogPwFind = QtWidgets.QDialog()
            self.dialog = Gui.Dialog(self.dialogPwFind)

            text = QtWidgets.QTextEdit(self.dialogPwFind)
            text.setGeometry(70,150,400,100)
            text.setStyleSheet("border : 0px; \n color : #ffffff; \n background-color : #000000;")
            text.setText("비밀번호는 " + self.db.result[0][1] + "입니다.")

            self.dialogPwFind.show()
    
            for index in range(0,5):
                self.mainGui.lineUserInf[index].clear() 

        else:
            self.dialogFindFail = QtWidgets.QDialog()
            self.dialog = Gui.Dialog(self.dialogFindFail)

            text = QtWidgets.QTextEdit(self.dialogFindFail)
            text.setGeometry(200,60,300,45)
            text.setStyleSheet(Config.infTextStylesheet[0])
            text.setText(Config.textFindFail[0])
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(10)
            text.setFont(font)

            text = QtWidgets.QTextEdit(self.dialogFindFail)
            text.setGeometry(70,158,450,90)
            text.setStyleSheet(Config.infTextStylesheet[0])
            text.setText(Config.textFindFail[1])
            text.setFont(font)

            self.dialogFindFail.show()
            


