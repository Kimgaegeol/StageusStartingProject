import Gui
import DB
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Signup
import IdPwFind
import List
import Config


class PageLoginLogic():
    
    def __init__(self,mainGui):
      
        self.db = DB.DataBase()

        self.mainGui = mainGui

        self.pageSignup = None # 멤버 변수는 생성자에서 무조건 써줘야 함
        self.pageIdPwFind = None
        self.pageList = None 

        self.userPk = None # 리스트 페이지에 넘겨줄 userPk
        
        self.mainGui.btnSignup.clicked.connect(self.btnEventGoSignup)
        self.mainGui.btnIdPwFind.clicked.connect(self.btnEventGoIdPwFind)
        self.mainGui.btnLogin.clicked.connect(self.btnEventLogin)

        self.dialogLoginFail = QtWidgets.QDialog()
        self.dialog = Gui.Dialog(self.dialogLoginFail)

    def btnEventGoSignup(self):       #회원가입 페이지로 이동                     
        self.mainGui.stackedWidget.setCurrentIndex(1)
        self.pageSignup = Signup.PageSignupLogic(self.mainGui)

    def btnEventGoIdPwFind(self):      #아디비번 찾기 페이지로 이동
        self.mainGui.stackedWidget.setCurrentIndex(2)
        self.pageIdpwFind = IdPwFind.PageIdPwFindLogic(self.mainGui)

     #버튼이벤트함수의 이름을 잘생각하자 ( 이름 헷갈리지 않도록 하는 것이 중요 )
    
    def btnEventLogin(self):        #로그인 기능 및 리스트 페이지로 이동
        # db = DB.DataBase()
        # result = db.readData()
        
        table = "member"
        colum = ["id","pw"]
        value = [self.mainGui.lineLogin[0].text(),self.mainGui.lineLogin[1].text()]
        if self.db.readData(table,colum,value):
            self.userPk = self.db.result[0][0]               #이벤트는 호출해주면 안된다. 
            self.mainGui.stackedWidget.setCurrentIndex(3)
            self.pageList = List.PageListLogic(self.mainGui,self.userPk)
        else:
            text = QtWidgets.QTextEdit(self.dialogLoginFail)
            text.setGeometry(163,65,320,100)
            text.setStyleSheet("border : 0px; \n color : #ffffff;")
            text.setText("로그인 실패")
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(20)
            text.setFont(font)

            text = QtWidgets.QTextEdit(self.dialogLoginFail)
            text.setGeometry(78,160,470,150)
            text.setStyleSheet("border : 0px; \n color : #ffffff;")
            text.setText("이유 : 아이디 혹은 비밀번호가 잘못되었습니다.")     # 왜 잘못되었습니다. 가 뒤로 안 밀릴까? 질문 
            font.setPointSize(12)
            text.setFont(font)
            self.dialogLoginFail.show()

        
    
    

        


