import DB
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#QThread 임포트 A
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 

import re
import Config
 
# 회원가입 예외처리 기능은 re 사용!  #회원가입 실패 시 그 이유 말해주기, 회원가입 성공과 실패 텍스트 색깔 바꾸기

class PageSignupLogic:
    def __init__(self,mainGui):
        self.db = DB.DataBase()
        self.mainGui = mainGui
    
        self.memberId = []
        self.memberName = []

        self.putIdName()
 
        self.mainGui.btnBackSignup.clicked.connect(self.btnEventBack) #뒤로가기
        self.mainGui.btnSignupEnd.clicked.connect(self.btnEventSignup) #회원가입 버튼

        self.mainGui.lineSignInf[0].textChanged.connect(self.checkId)   #회원가입 조건 확인
        self.mainGui.lineSignInf[1].textChanged.connect(self.checkName)   #textChanged - 글씨가 바뀔떄마다
        self.mainGui.lineSignInf[2].textChanged.connect(self.checkPw)     #               이벤트 발생
        self.mainGui.lineSignInf[3].textChanged.connect(self.checkPwSure)
        self.mainGui.lineSignInf[4].textChanged.connect(self.checkPhone)

    def putIdName(self): #아이디,이름 중복체크를 위해 이름과 아이디 넣음 
        table = "member"
        colum = []
        value = []
        self.db.readData(table,colum,value)                      # 회원가입시 중복 코드를 처리할 때 
        for index in range(0,len(self.db.result)):               # 회언 정보를 다 가져오는 것은 보안적으로 위험하다.
            self.memberId.append(self.db.result[index][1])       # 값을 보내서 리턴되는 값을 확인함으로써 중복되는 지 안 되는 지
            self.memberName.append(self.db.result[index][3])     # 체크하는 것이 맞다. 
                                                                 # 보통 아이디 중복체크는 버튼으로 확인하는 게 낫다.

    def btnEventBack(self): # 로그인 페이지로 가능 동시에 관련 페이지의 라인위젯 클리어
        self.mainGui.lineLogin[0].clear()
        self.mainGui.lineLogin[1].clear()
        self.mainGui.stackedWidget.setCurrentIndex(0) 
        for index in range(0,5):
                self.mainGui.lineSignInf[index].clear()

    def checkId(self):  #회원가입 조건을 만족하는 지 체크
        if len(self.mainGui.lineSignInf[0].text()) < 8 or len(self.mainGui.lineSignInf[0].text()) > 12 and not re.findall('[0-9]+', self.mainGui.lineSignInf[0].text()) and not re.findall('[a-z]',self.mainGui.lineSignInf[0].text()) or not re.findall('[A-Z]', self.mainGui.lineSignInf[0].text()) and not re.findall('[`~!@#$%^&*(),<.>/?]+', self.mainGui.lineSignInf[0].text()):
                self.mainGui.textSignNo[0].setText(Config.textConditionNo[0])
                self.mainGui.textSignNo[0].setStyleSheet(Config.textConditionNoStyleSheet[0])
                self.mainGui.signupSign[0] = False

        else:
            if self.mainGui.lineSignInf[0].text() in self.memberId:
                self.mainGui.textSignNo[0].setText(Config.textConditionNo[5])
                self.mainGui.textSignNo[0].setStyleSheet(Config.textConditionNoStyleSheet[0])
                self.mainGui.signupSign[0] = False
                
            else:
                self.mainGui.textSignNo[0].setText(Config.textConditionOk[0])
                self.mainGui.textSignNo[0].setStyleSheet(Config.textConditionOkStyleSheet[0])
                self.mainGui.signupSign[0] = True

    def checkName(self):
        if  len(self.mainGui.lineSignInf[1].text()) == 0 or re.findall('[0-9]+' , self.mainGui.lineSignInf[1].text()) or re.findall('[`~!@#$%^&*(),<.>/?]+', self.mainGui.lineSignInf[1].text()):
                self.mainGui.textSignNo[1].setText(Config.textConditionNo[1])
                self.mainGui.textSignNo[1].setStyleSheet(Config.textConditionNoStyleSheet[0])
                self.mainGui.signupSign[1] = False

        else:
            if self.mainGui.lineSignInf[1].text() in self.memberName:
                self.mainGui.textSignNo[1].setText(Config.textConditionNo[6])
                self.mainGui.textSignNo[1].setStyleSheet(Config.textConditionNoStyleSheet[0])
                self.mainGui.signupSign[1] = False

            else:
                self.mainGui.textSignNo[1].setText(Config.textConditionOk[1])
                self.mainGui.textSignNo[1].setStyleSheet(Config.textConditionOkStyleSheet[0])
                self.mainGui.signupSign[1] = True

    def checkPw(self):
        if  len(self.mainGui.lineSignInf[2].text()) < 8 or len(self.mainGui.lineSignInf[2].text()) > 12 and not re.findall('[0-9]+', self.mainGui.lineSignInf[2].text()) and not re.findall('[a-z]',self.mainGui.lineSignInf[2].text()) or not re.findall('[A-Z]', self.mainGui.lineSignInf[2].text()) and not re.findall('[`~!@#$%^&*(),<.>/?]+', self.mainGui.lineSignInf[2].text()):
                self.mainGui.textSignNo[2].setText(Config.textConditionNo[2])
                self.mainGui.textSignNo[2].setStyleSheet(Config.textConditionNoStyleSheet[0])
                self.mainGui.signupSign[2] = False

        else:
            self.mainGui.textSignNo[2].setText(Config.textConditionOk[2])
            self.mainGui.textSignNo[2].setStyleSheet(Config.textConditionOkStyleSheet[0])
            self.mainGui.signupSign[2] = True

    def checkPwSure(self):
        if self.mainGui.lineSignInf[2].text() != self.mainGui.lineSignInf[3].text() or self.mainGui.lineSignInf[3].text() == "":
            self.mainGui.textSignNo[3].setText(Config.textConditionNo[3])
            self.mainGui.textSignNo[3].setStyleSheet(Config.textConditionNoStyleSheet[0])
            self.mainGui.signupSign[3] = False

        else:
            self.mainGui.textSignNo[3].setText(Config.textConditionOk[3])
            self.mainGui.textSignNo[3].setStyleSheet(Config.textConditionOkStyleSheet[0])
            self.mainGui.signupSign[3] = True

    def checkPhone(self):
        if  len(self.mainGui.lineSignInf[4].text()) != 11 or re.findall('[a-z]',self.mainGui.lineSignInf[4].text()) or re.findall('[A-Z]',self.mainGui.lineSignInf[4].text()) or re.findall('[`~!@#$%^&*(),<.>/?]+',self.mainGui.lineSignInf[4].text()):
            self.mainGui.textSignNo[4].setText(Config.textConditionNo[4])
            self.mainGui.textSignNo[4].setStyleSheet(Config.textConditionNoStyleSheet[0])
            self.mainGui.signupSign[4] = False

        else:
            self.mainGui.textSignNo[4].setText(Config.textConditionOk[4])
            self.mainGui.textSignNo[4].setStyleSheet(Config.textConditionOkStyleSheet[0])
            self.mainGui.signupSign[4] = True

    def btnEventSignup(self):  # _는 소문자 같이 쓴다   snake : 단어 사이에 _로 끊어줌, 카멜 : 단어사이를 대문자로 끊어줌
     # SignupBtnEvent로 변수 변경하는 게좋음
        if not False in self.mainGui.signupSign:
            table = "member"
            colum = ["id","pw","name","phonenumber"]
            value = [self.mainGui.lineSignInf[0].text(),self.mainGui.lineSignInf[2].text(),self.mainGui.lineSignInf[1].text(),self.mainGui.lineSignInf[4].text()]
            self.db.insertData(table,colum,value)
            self.mainGui.lineLogin[0].clear()
            self.mainGui.lineLogin[1].clear()
            self.mainGui.stackedWidget.setCurrentIndex(0)
            
            for index in range(0,5):
                self.mainGui.lineSignInf[index].clear()
            




    

            

        
        
        


