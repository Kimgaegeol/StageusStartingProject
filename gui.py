from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import DB
import Config

class MainGui:              #기능이나 위젯마다 라인 하나씩 스페이스바 눌러주자 
    def __init__(self):
        self.db = DB.DataBase()

        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1600,900)
        self.mainWindow.setStyleSheet(Config.black[0])

        self.centralWidget = QtWidgets.QWidget(self.mainWindow)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(0,0,1600,900)
        font = QtGui.QFont()
         
    # 로그인 페이지
        self.pageLogin = QtWidgets.QWidget(self.stackedWidget)

        self.textLogoLogin = QtWidgets.QTextEdit(self.pageLogin)
        self.textLogoLogin.setGeometry(690,100,250,100)
        self.textLogoLogin.setStyleSheet(Config.logoStyleSheet[0]) #투명도는 0부터 256
        self.textLogoLogin.setReadOnly(True)
        self.textLogoLogin.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textLogoLogin.setText(Config.logoText[0])
        font.setFamily(Config.fontEnglish[0])
        font.setPointSize(18)
        self.textLogoLogin.setFont(font)

        self.shapeLogin = []
        for index in range(0,2):
            penEdit = QtWidgets.QLineEdit(self.pageLogin)
            penEdit.setGeometry (150,400 + 200 * index,700,4)
            penEdit.setStyleSheet(Config.white[0])
            penEdit.setReadOnly(True)
            self.shapeLogin.append(penEdit)

        self.textLogin = []
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.pageLogin)
            text.setGeometry(150,300 + 200 * index, 120, 100)
            text.setStyleSheet("border : 0px; \n color : #ffffff;")
            text.setReadOnly(True)
            text.setText(Config.letterLogin[index])
            font = QtGui.QFont()
            font.setFamily(Config.fontEnglish[0])
            font.setPointSize(24)
            text.setFont(font)
            self.textLogin.append(text)

        self.lineLogin = []
        for index in range(0,2):
            line = QtWidgets.QLineEdit(self.pageLogin)
            line.setGeometry(280,306 + 200 * index,570,95)
            line.setStyleSheet("border : 0px; \n color : #ffffff")
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(23)
            line.setFont(font)
            if index == 1:
                line.setEchoMode(QLineEdit.Password)
            self.lineLogin.append(line)

        self.btnLogin = QtWidgets.QPushButton(self.pageLogin)
        self.btnLogin.setGeometry(1050,320, 320,130)
        self.btnLogin.setStyleSheet(Config.btnStyleeSheet[0])
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogin.setText("로그인")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(23)
        self.btnLogin.setFont(font)

        self.btnIdPwFind = QtWidgets.QPushButton(self.pageLogin)
        self.btnIdPwFind.setGeometry(920,520, 270,100)
        self.btnIdPwFind.setStyleSheet(Config.btnStyleeSheet[0])
        self.btnIdPwFind.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnIdPwFind.setText("IDPW 찾기")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(18)
        self.btnIdPwFind.setFont(font)

        self.btnSignup = QtWidgets.QPushButton(self.pageLogin)
        self.btnSignup.setGeometry(1230,520, 270,100)
        self.btnSignup.setStyleSheet(Config.btnStyleeSheet[0])
        self.btnSignup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignup.setText("회원가입")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(18)
        self.btnSignup.setFont(font)

        self.stackedWidget.addWidget(self.pageLogin)

    #회원가입 페이지
        self.pageSignup = QtWidgets.QWidget(self.stackedWidget)

        self.backgroundSignup = QtWidgets.QLabel(self.pageSignup)
        self.backgroundSignup.setGeometry(100,100,1400,760)
        self.backgroundSignup.setStyleSheet(Config.backgroundStyleSheet[0])
        self.backgroundSignup.setText("")

        self.textLogoSignup = QtWidgets.QTextEdit(self.pageSignup)
        self.textLogoSignup.setGeometry(10,10,250,80)
        self.textLogoSignup.setStyleSheet(Config.logoStyleSheet[0])
        self.textLogoSignup.setReadOnly(True)
        self.textLogoSignup.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textLogoSignup.setText(Config.logoText[0])
        font.setFamily(Config.fontEnglish[0]) 
        font.setPointSize(18)
        self.textLogoSignup.setFont(font)

        self.textTitleSignup = QtWidgets.QTextEdit(self.pageSignup)
        self.textTitleSignup.setGeometry(150,120,250,80)
        self.textTitleSignup.setStyleSheet("border : 0px; \n color : #ffffff; \n background-color : #20323232;")
        self.textTitleSignup.setReadOnly(True)
        self.textTitleSignup.setText("회원가입")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(18)
        self.textTitleSignup.setFont(font)

        self.shapeSign = []
        for index in range(0,2):
            Edit = QtWidgets.QTextEdit(self.pageSignup)
            Edit.setGeometry(160,230 + 250 * index,580,130)
            Edit.setStyleSheet("background-color : #ffffff; \n border : 1px #ffffff; \n border-radius:15px")
            Edit.setReadOnly(True)
            self.shapeSign.append(Edit)
        for index in range(0,3):
            Edit = QtWidgets.QTextEdit(self.pageSignup)
            Edit.setGeometry(850,130 + 200 * index,580,130)
            Edit.setStyleSheet("background-color : #ffffff; \n border : 1px #ffffff; \n border-radius:15px")
            Edit.setReadOnly(True)
            self.shapeSign.append(Edit)

        self.textSignGuide = []
        for index in range(0,2):
            if index == 0:
                text = QtWidgets.QTextEdit(self.pageSignup)
                text.setGeometry(168,232 + 250*index, 565,40)
                text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
                text.setText(Config.textSignGuide[index])
                text.setReadOnly(True)
                font.setFamily(Config.fontKorean[0])
                font.setPointSize(7)
                text.setFont(font)
                self.textSignGuide.append(text)
            else:
                text = QtWidgets.QTextEdit(self.pageSignup)
                text.setGeometry(168,232 + 250*index, 565,40)
                text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
                text.setText(Config.textSignGuide[index])
                text.setReadOnly(True)
                font.setFamily(Config.fontKorean[0])
                font.setPointSize(8)
                text.setFont(font)
                self.textSignGuide.append(text)
        for index in range(0,3):
            text = QtWidgets.QTextEdit(self.pageSignup)
            text.setGeometry(858,132 + 200*index, 540,40)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            text.setText(Config.textSignGuide[index+2])
            text.setReadOnly(True)
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(8)
            text.setFont(font)
            self.textSignGuide.append(text)

        self.lineSignInf = [] # 0.아이디 1.이름 2.비밀번호 3.비밀번호확인 4.전화번호
        for index in range(0,2):
            text = QtWidgets.QLineEdit(self.pageSignup)
            text.setGeometry(165,272 + 250*index, 550,85)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(14)
            text.setFont(font)
            self.lineSignInf.append(text)
        for index in range(0,3):
            text = QtWidgets.QLineEdit(self.pageSignup)
            text.setGeometry(858,172 + 200*index, 550,85)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(14)
            text.setFont(font)
            self.lineSignInf.append(text)

        self.textSignNo = []
        for index in range(0,2):
            text = QtWidgets.QLineEdit(self.pageSignup)
            text.setGeometry(162,362 + 250*index, 540,40)
            text.setStyleSheet("background-color : #20323232; \n border : 0px; \n color : #ff0000; ")
            text.setText(Config.textSignNo[index])
            text.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(9)
            text.setFont(font)
            self.textSignNo.append(text)

        for index in range(0,3):
            text = QtWidgets.QLineEdit(self.pageSignup)
            text.setGeometry(852,262 + 200*index, 540,40)
            text.setStyleSheet("background-color : #20323232; \n border : 0px; \n color : #ff0000; ")
            text.setText(Config.textSignNo[index+2])
            text.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(9)
            text.setFont(font)
            self.textSignNo.append(text)

        self.signupSign = [False,False,False,False,False]

        self.btnSignupEnd = QtWidgets.QPushButton(self.pageSignup)
        self.btnSignupEnd.setGeometry(600,730, 400,100)
        self.btnSignupEnd.setStyleSheet(Config.btnStyleeSheet[0])
        self.btnSignupEnd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignupEnd.setText("회원가입")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(21)
        self.btnSignupEnd.setFont(font)
        self.btnSignupEnd.raise_()

        self.btnBackSignup = QtWidgets.QPushButton(self.pageSignup)
        self.btnBackSignup.setGeometry(1300,35,200,80)
        self.btnBackSignup.setStyleSheet("background-color : #000000; color : #ffffff; border : 0px")
        self.btnBackSignup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackSignup.setText("뒤로가기")
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(16)
        self.btnBackSignup.setFont(font)

        self.stackedWidget.addWidget(self.pageSignup)

    #아이디 패스워드 찾기 페이지

        self.pageIdPwFind = QtWidgets.QWidget(self.stackedWidget)

        self.backgroundFind = QtWidgets.QLabel(self.pageIdPwFind)
        self.backgroundFind.setGeometry(100,100,1400,760)
        self.backgroundFind.setStyleSheet(Config.backgroundStyleSheet[0])
        self.backgroundFind.setWindowOpacity(0.25)
        self.backgroundFind.setText("")

        self.textLogoFind = QtWidgets.QTextEdit(self.pageIdPwFind)
        self.textLogoFind.setGeometry(10,10,250,80)
        self.textLogoFind.setStyleSheet(Config.logoStyleSheet[0])
        self.textLogoFind.setReadOnly(True)
        self.textLogoFind.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textLogoFind.setText(Config.logoText[0])
        font.setFamily(Config.fontEnglish[0]) 
        font.setPointSize(18)
        self.textLogoFind.setFont(font)

        self.textTitleFind = QtWidgets.QTextEdit(self.pageIdPwFind)
        self.textTitleFind.setGeometry(150,120,300,80)
        self.textTitleFind.setStyleSheet("border : 0px; \n color : #ffffff; \n background-color : #20323232;")
        self.textTitleFind.setReadOnly(True)
        self.textTitleFind.setText("IDPW 찾기")
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(18)
        self.textTitleFind.setFont(font)

        self.shapeFind = []
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.pageIdPwFind)
            text.setGeometry(160,230 + 250 * index,570,130)
            text.setStyleSheet("background-color : #ffffff; \n border : 1px #ffffff; \n border-radius:15px")
            text.setReadOnly(True)
            self.shapeFind.append(text)

        for index in range(0,3):
            text = QtWidgets.QTextEdit(self.pageIdPwFind)
            text.setGeometry(850,130 + 200 * index,570,130)
            text.setStyleSheet("background-color : #ffffff; \n border : 1px #ffffff; \n border-radius:15px")
            text.setReadOnly(True)
            self.shapeFind.append(text)

        self.textIdPwFindGuide = []
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.pageIdPwFind)
            text.setGeometry(168,232 + 250*index, 540,40)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            text.setText(Config.textIdPwFindGuide[index])
            text.setReadOnly(True)
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(8)
            text.setFont(font)
            self.textIdPwFindGuide.append(text)

        for index in range(0,3):
            text = QtWidgets.QTextEdit(self.pageIdPwFind)
            text.setGeometry(858,132 + 200*index, 540,40)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            text.setText(Config.textIdPwFindGuide[index+2])
            text.setReadOnly(True)
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(8)
            text.setFont(font)
            self.textIdPwFindGuide.append(text)

        self.lineUserInf = []
        for index in range(0,2):
            text = QtWidgets.QLineEdit(self.pageIdPwFind)
            text.setGeometry(165,272 + 250*index, 550,85)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(14)
            text.setFont(font)
            self.lineUserInf.append(text)

        for index in range(0,3):
            text = QtWidgets.QLineEdit(self.pageIdPwFind)
            text.setGeometry(858,172 + 200*index, 550,85)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(14)
            text.setFont(font)
            self.lineUserInf.append(text)

        self.btnIdPwFindEnd = []
        for index in range(0,2):
            btn = QtWidgets.QPushButton(self.pageIdPwFind)
            btn.setGeometry(255+700 * index,730,360,90)
            btn.setStyleSheet(Config.btnStyleeSheet[0])
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setText(Config.textIdPwFind[index])
            font.setFamily(Config.fontKorean[0])
            font.setBold(True)
            font.setPointSize(17)
            btn.setFont(font)
            self.btnIdPwFindEnd.append(btn)

        self.btnBackIdPwFind = QtWidgets.QPushButton(self.pageIdPwFind)
        self.btnBackIdPwFind.setGeometry(1300,35,200,80)
        self.btnBackIdPwFind.setStyleSheet("background-color : #000000; color : #ffffff; border : 0px")
        self.btnBackIdPwFind.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackIdPwFind.setText("뒤로가기")
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(16)
        self.btnBackIdPwFind.setFont(font)

        self.stackedWidget.addWidget(self.pageIdPwFind)

    # 재생목록 페이지
        self.pageList = QtWidgets.QWidget(self.stackedWidget)

        self.backgroundList = QtWidgets.QLabel(self.pageList)
        self.backgroundList.setGeometry(100,100,1400,760)
        self.backgroundList.setStyleSheet(Config.backgroundStyleSheet[0])
        self.backgroundList.setText("")

        self.textLogoList = QtWidgets.QTextEdit(self.pageList)
        self.textLogoList.setGeometry(10,10,250,80)
        self.textLogoList.setStyleSheet(Config.logoStyleSheet[0])
        self.textLogoList.setReadOnly(True)
        self.textLogoList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textLogoList.setText(Config.logoText[0])
        font.setFamily(Config.fontEnglish[0]) 
        font.setPointSize(18)
        self.textLogoList.setFont(font)

        self.searchShape = QtWidgets.QLabel(self.pageList)
        self.searchShape.setGeometry(130,150,1000,100)
        self.searchShape.setStyleSheet("border : 0px; \n background-color : #505050; border-radius : 15px;")
        self.searchShape.setText("")

        self.lineUrlSearch = QtWidgets.QLineEdit(self.pageList)
        self.lineUrlSearch.setGeometry(220,150,900,100)
        self.lineUrlSearch.setStyleSheet("border : 0px; \n background-color : #505050; \n color : #ffffff;")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setPointSize(10)
        self.lineUrlSearch.setFont(font)
        self.lineUrlSearch.raise_() 

        self.btnAddList = QtWidgets.QPushButton(self.pageList)
        self.btnAddList.setGeometry(200,330,130,130)
        self.btnAddList.setStyleSheet("border : 2px solid #ffffff; \n background-color : #000000; \n color : #ffffff;")
        self.btnAddList.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddList.setText("+")
        font.setPointSize(15)
        font.setBold(True)
        self.btnAddList.setFont(font)

        self.btnBackList = QtWidgets.QPushButton(self.pageList)
        self.btnBackList.setGeometry(1300,35,200,80)
        self.btnBackList.setStyleSheet("background-color : #000000; color : #ffffff; border : 0px")
        self.btnBackList.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackList.setText("뒤로가기")
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(16)
        self.btnBackList.setFont(font)

        self.btnUrlSearch = QtWidgets.QPushButton(self.pageList)
        self.btnUrlSearch.setGeometry(1140, 145,150,110)
        self.btnUrlSearch.setStyleSheet(Config.btnStyleeSheet[0])
        self.btnUrlSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUrlSearch.setText("검색")
        font.setFamily(Config.fontKorean[0])
        font.setPointSize(15)
        self.btnUrlSearch.setFont(font)

        self.btnUrlStorage = QtWidgets.QPushButton(self.pageList)
        self.btnUrlStorage.setGeometry(0,0,0,0)
        self.btnUrlStorage.setStyleSheet(Config.btnStyleeSheet[0])
        self.btnUrlStorage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUrlStorage.setText("")
        font.setFamily(Config.fontKorean[0])
        font.setPointSize(15)
        self.btnUrlStorage.setFont(font)

        self.listThumbnail = [] #썸네일        
        self.btnList = [] # 동영상페이지로 가능 리스트 버튼
        self.textListTitle = [] # 리스트 이름
        self.btnListReject = [] #리스트 삭제버튼

        self.btnListNext = [] #리스트 다음 페이지 버튼
        self.btnListPrev = [] #리스트 이전 페이지 버튼 
      
        self.stackedWidget.addWidget(self.pageList)

    # 동영상 페이지    

        self.pageVideo = QtWidgets.QWidget(self.stackedWidget)

        self.backgroundVideo = QtWidgets.QLabel(self.pageVideo)
        self.backgroundVideo.setGeometry(100,100,1400,760)
        self.backgroundVideo.setStyleSheet(Config.backgroundStyleSheet[0])
        self.backgroundVideo.setWindowOpacity(0.25)
        self.backgroundVideo.setText("")

        self.textLogoVideo = QtWidgets.QTextEdit(self.pageVideo)
        self.textLogoVideo.setGeometry(10,10,250,80)
        self.textLogoVideo.setStyleSheet(Config.logoStyleSheet[0])
        self.textLogoVideo.setReadOnly(True)
        self.textLogoVideo.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textLogoVideo.setText(Config.logoText[0])
        font.setFamily(Config.fontEnglish[0]) 
        font.setPointSize(18)
        self.textLogoVideo.setFont(font)

        self.videoFrame = QtWidgets.QFrame(self.pageVideo)
        self.videoFrame.setGeometry(150,150,900,550)

        self.btnMainVideo = []
        for index in range(0,2):
            btn = QtWidgets.QPushButton(self.pageVideo)
            btn.setGeometry(160 + index * 110,710, 100, 100)
            btn.setStyleSheet("border : 2px solid #FFFFFF; \n color : #ffffff; \n background-color : #828282;")
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setText(Config.textMainVideo[index])
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(12)
            btn.setFont(font)
            self.btnMainVideo.append(btn)

        self.textMainVideoTitle = QtWidgets.QTextEdit(self.pageVideo)
        self.textMainVideoTitle.setGeometry(390,710,650,100)
        self.textMainVideoTitle.setStyleSheet("border : 2px solid #FFFFFF; \n color : #FFFFFF; \n background-color : #70323232;")
        self.textMainVideoTitle.setReadOnly(True)
        font.setFamily(Config.fontKorean[0])
        font.setPointSize(10)
        self.textMainVideoTitle.setFont(font)

        self.textListTitleVideoPage = QtWidgets.QTextEdit(self.pageVideo)
        self.textListTitleVideoPage.setGeometry(1070,155,400,80)
        self.textListTitleVideoPage.setStyleSheet("border : 2px solid #FFFFFF; \n color : #FFFFFF; \n background-color : #70323232;")
        self.textListTitleVideoPage.setReadOnly(True)
        font.setFamily(Config.fontKorean[0])
        font.setPointSize(10)
        self.textListTitleVideoPage.setFont(font)

        self.thumbnailVideo = []
        self.btnVideoStart = []
        self.textVideoTitle = []
        self.btnVideoReject = []

        self.btnBackVideo = QtWidgets.QPushButton(self.pageVideo)
        self.btnBackVideo.setGeometry(1300,35,200,80)
        self.btnBackVideo.setStyleSheet("background-color : #000000; color : #ffffff; border : 0px")
        self.btnBackVideo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackVideo.setText("뒤로가기")
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(16)
        self.btnBackVideo.setFont(font)

        self.stackedWidget.addWidget(self.pageVideo)

        self.stackedWidget.setCurrentIndex(0)
        self.mainWindow.setCentralWidget(self.centralWidget)

#다이아로그 클래스
class Dialog:   #멤버변수 지역변수 구분 잘하자 SELF를 잘 붙이자! 이해해서 쓰자!
    def __init__(self,dialog):
        dialog.setObjectName("dialog")
        dialog.resize(630,360)
        dialog.setStyleSheet(Config.black[0])
        font = QtGui.QFont()

        self.textEdit_Logo = QtWidgets.QTextEdit(dialog)
        self.textEdit_Logo.setGeometry(10,15,180,50)
        self.textEdit_Logo.setStyleSheet(Config.logoStyleSheet[0])
        self.textEdit_Logo.setReadOnly(True)
        self.textEdit_Logo.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textEdit_Logo.setText(Config.logoText[0])
        font.setFamily(Config.fontEnglish[0])
        font.setPointSize(10)
        self.textEdit_Logo.setFont(font)

        self.text = []
        self.line = []
        self.btn = []


if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)

    mainGui = MainGui()  
    mainGui.mainWindow.show()

    sys.exit(app.exec_())











# 모듈화를 위해 쓰레드 클래스는 쓰이는 곳에 같이 적어놓는 게 좋다.