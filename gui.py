from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# 유지보수를 위해 폰트와 스타일시트는 변수로 설정해놓자. 

class MainGui:
    
    def __init__(self):

        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1600,900)
        self.mainWindow.setStyleSheet("background-color : #000000;")

        self.centralWidget = QtWidgets.QWidget(self.mainWindow)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(0,0,1600,900)


    # 로그인 페이지
        self.page_Login = QtWidgets.QWidget(self.stackedWidget)

        self.textEdit_LOGO_Login = QtWidgets.QTextEdit(self.page_Login)
        self.textEdit_LOGO_Login.setGeometry(690,100,250,100)
        self.textEdit_LOGO_Login.setStyleSheet("border : 0px; \n color : #FF0000;") #투명도는 0부터 256
        self.textEdit_LOGO_Login.setReadOnly(True)
        self.textEdit_LOGO_Login.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textEdit_LOGO_Login.setText("NETFLIX")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.textEdit_LOGO_Login.setFont(font)

        self.penEdit_LoginPage = []
        for index in range(0,2):
            penEdit = QtWidgets.QLineEdit(self.page_Login)
            penEdit.setGeometry (150,400 + 200 * index,700,4)
            penEdit.setStyleSheet("background-color : #ffffff;")
            penEdit.setReadOnly(True)
            self.penEdit_LoginPage.append(penEdit)

        self.textEdit_LoginPage = []
        self.login_Text = ["ID","PW"]
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.page_Login)
            text.setGeometry(150,300 + 200 * index, 120, 100)
            text.setStyleSheet("border : 0px; \n color : #ffffff;")
            text.setReadOnly(True)
            text.setText(self.login_Text[index])
            font = QtGui.QFont()
            font.setFamily("Arial Black")
            font.setPointSize(24)
            text.setFont(font)
            self.textEdit_LoginPage.append(text)

        self.lineEdit_LoginPage = []
        for index in range(0,2):
            line = QtWidgets.QTextEdit(self.page_Login)
            line.setGeometry(280,306 + 200 * index,570,95)
            line.setStyleSheet("border : 0px; \n color : #ffffff")
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(23)
            line.setFont(font)
            self.lineEdit_LoginPage.append(line)

        self.pushButton_Login = QtWidgets.QPushButton(self.page_Login)
        self.pushButton_Login.setGeometry(1050,320, 320,130)
        self.pushButton_Login.setStyleSheet("border : 1px; \n background-color : #828282; \n color : #ffffff;")
        self.pushButton_Login.setText("로그인")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setPointSize(23)
        self.pushButton_Login.setFont(font)

        self.pushButton_IdPwFind = QtWidgets.QPushButton(self.page_Login)
        self.pushButton_IdPwFind.setGeometry(920,520, 270,100)
        self.pushButton_IdPwFind.setStyleSheet("border : 1px; \n background-color : #828282; \n color : #ffffff;")
        self.pushButton_IdPwFind.setText("IDPW 찾기")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setPointSize(20)
        self.pushButton_Login.setFont(font)

        self.pushButton_SignUp = QtWidgets.QPushButton(self.page_Login)
        self.pushButton_SignUp.setGeometry(1230,520, 270,100)
        self.pushButton_SignUp.setStyleSheet("border : 1px; \n background-color : #828282; \n color : #ffffff;")
        self.pushButton_SignUp.setText("회원가입")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setPointSize(20)
        self.pushButton_Login.setFont(font)


        self.stackedWidget.addWidget(self.page_Login)

        
    #회원가입 페이지
        self.page_SignUp = QtWidgets.QWidget(self.stackedWidget)

        self.backgroundEdit_SignUp = QtWidgets.QLabel(self.page_SignUp)
        self.backgroundEdit_SignUp.setGeometry(100,100,1400,760)
        self.backgroundEdit_SignUp.setStyleSheet("border : 0px; \n background-color : #323232; \n opacity : 0.1;")
        self.backgroundEdit_SignUp.setWindowOpacity(0.25)
        self.backgroundEdit_SignUp.setText("")

        self.textEdit_LOGO_Sign = QtWidgets.QTextEdit(self.page_SignUp)
        self.textEdit_LOGO_Sign.setGeometry(10,10,250,80)
        self.textEdit_LOGO_Sign.setStyleSheet("border : 0px; \n color : #FF0000;")
        self.textEdit_LOGO_Sign.setReadOnly(True)
        self.textEdit_LOGO_Sign.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textEdit_LOGO_Sign.setText("NETFLIX")
        font = QtGui.QFont()
        font.setFamily("Arial Black") 
        font.setPointSize(18)
        self.textEdit_LOGO_Sign.setFont(font)

        self.textEdit_Title_Sign = QtWidgets.QTextEdit(self.page_SignUp)
        self.textEdit_Title_Sign.setGeometry(150,120,250,80)
        self.textEdit_Title_Sign.setStyleSheet("border : 0px; \n color : #ffffff; \n background-color : #323232;")
        self.textEdit_Title_Sign.setReadOnly(True)
        self.textEdit_Title_Sign.setText("회원가입")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setPointSize(18)
        self.textEdit_Title_Sign.setFont(font)

        self.penEdit_Sign = []
        for index in range(0,2):
            Edit = QtWidgets.QTextEdit(self.page_SignUp)
            Edit.setGeometry(160,230 + 250 * index,570,130)
            Edit.setStyleSheet("background-color : #ffffff; \n border : 1px #ffffff; \n border-radius:15px")
            Edit.setReadOnly(True)
            self.penEdit_Sign.append(Edit)
        for index in range(0,3):
            Edit = QtWidgets.QTextEdit(self.page_SignUp)
            Edit.setGeometry(850,130 + 200 * index,570,130)
            Edit.setStyleSheet("background-color : #ffffff; \n border : 1px #ffffff; \n border-radius:15px")
            Edit.setReadOnly(True)
            self.penEdit_Sign.append(Edit)



        self.textEdit_SignGuide = []
        self.text_SignGuide = ["아이디 (영어, 숫자, 특수기호 포함, 8~12자리)", "이름 (동일인물 불가)", "비밀번호 (영어, 숫자, 특수기호 포함, 8~12자리)", "비밀번호 확인", "전화번호 (띄어쓰기나 '-'없이 11자리)"]
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.page_SignUp)
            text.setGeometry(168,232 + 250*index, 540,40)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            text.setText(self.text_SignGuide[index])
            text.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(8)
            text.setFont(font)
            self.textEdit_SignGuide.append(text)
        for index in range(0,3):
            text = QtWidgets.QTextEdit(self.page_SignUp)
            text.setGeometry(858,132 + 200*index, 540,40)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            text.setText(self.text_SignGuide[index+2])
            text.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(8)
            text.setFont(font)
            self.textEdit_SignGuide.append(text)


        self.textEdit_SignInf = []
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.page_SignUp)
            text.setGeometry(165,272 + 250*index, 550,85)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(14)
            text.setFont(font)
            self.textEdit_SignInf.append(text)
        for index in range(0,3):
            text = QtWidgets.QTextEdit(self.page_SignUp)
            text.setGeometry(858,172 + 200*index, 550,85)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(14)
            text.setFont(font)
            self.textEdit_SignInf.append(text)

        self.textEdit_SignNo = []
        self.text_SignNo = ["사용 불가능한 아이디 입니다!", "사용 불가능한 이름 입니다!", "사용 불가능한 비밀번호 입니다!", "올바르지 않은 비밀번호 입니다!", "사용 불가능한 전화번호 입니다!"]
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.page_SignUp)
            text.setGeometry(162,362 + 250*index, 540,40)
            text.setStyleSheet("background-color : #323232; \n border : 0px; \n color : #ff0000; ")
            text.setText(self.text_SignNo[index])
            text.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(9)
            text.setFont(font)
            self.textEdit_SignNo.append(text)
        for index in range(0,3):
            text = QtWidgets.QTextEdit(self.page_SignUp)
            text.setGeometry(852,262 + 200*index, 540,40)
            text.setStyleSheet("background-color : #323232; \n border : 0px; \n color : #ff0000; ")
            text.setText(self.text_SignNo[index+2])
            text.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(9)
            text.setFont(font)
            self.textEdit_SignNo.append(text)


        self.pushButton_SignUp_end = QtWidgets.QPushButton(self.page_SignUp)
        self.pushButton_SignUp_end.setGeometry(600,730, 400,100)
        self.pushButton_SignUp_end.setStyleSheet("border : 1px; \n background-color : #828282; \n color : #ffffff;")
        self.pushButton_SignUp_end.setText("회원가입")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setPointSize(21)
        self.pushButton_SignUp_end.setFont(font)
        self.pushButton_SignUp_end.raise_()

        self.stackedWidget.addWidget(self.page_SignUp)

    #아이디 패스워드 찾기 페이지

        self.page_IdPwfind = QtWidgets.QWidget(self.stackedWidget)


        self.backgroundEdit_Find = QtWidgets.QLabel(self.page_IdPwfind)
        self.backgroundEdit_Find.setGeometry(100,100,1400,760)
        self.backgroundEdit_Find.setStyleSheet("border : 0px; \n background-color : #323232; \n opacity : 0.1;")
        self.backgroundEdit_Find.setWindowOpacity(0.25)
        self.backgroundEdit_Find.setText("")

        self.textEdit_LOGO_Find = QtWidgets.QTextEdit(self.page_IdPwfind)
        self.textEdit_LOGO_Find.setGeometry(10,10,250,80)
        self.textEdit_LOGO_Find.setStyleSheet("border : 0px; \n color : #FF0000;")
        self.textEdit_LOGO_Find.setReadOnly(True)
        self.textEdit_LOGO_Find.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textEdit_LOGO_Find.setText("NETFLIX")
        font = QtGui.QFont()
        font.setFamily("Arial Black") 
        font.setPointSize(18)
        self.textEdit_LOGO_Find.setFont(font)

        self.textEdit_Title_Find = QtWidgets.QTextEdit(self.page_IdPwfind)
        self.textEdit_Title_Find.setGeometry(150,120,300,80)
        self.textEdit_Title_Find.setStyleSheet("border : 0px; \n color : #ffffff; \n background-color : #323232;")
        self.textEdit_Title_Find.setReadOnly(True)
        self.textEdit_Title_Find.setText("IDPW 찾기")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setPointSize(18)
        self.textEdit_Title_Find.setFont(font)

        self.penEdit_Find = []
        for index in range(0,2):
            Edit = QtWidgets.QTextEdit(self.page_IdPwfind)
            Edit.setGeometry(160,230 + 250 * index,570,130)
            Edit.setStyleSheet("background-color : #ffffff; \n border : 1px #ffffff; \n border-radius:15px")
            Edit.setReadOnly(True)
            self.penEdit_Find.append(Edit)
        for index in range(0,3):
            Edit = QtWidgets.QTextEdit(self.page_IdPwfind)
            Edit.setGeometry(850,130 + 200 * index,570,130)
            Edit.setStyleSheet("background-color : #ffffff; \n border : 1px #ffffff; \n border-radius:15px")
            Edit.setReadOnly(True)
            self.penEdit_Find.append(Edit)

        self.textEdit_IdPwFindGuide = []
        self.text_IdPwFindGuide = ["이름", "전화번호", "아이디", "이름", "전화번호"]
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.page_IdPwfind)
            text.setGeometry(168,232 + 250*index, 540,40)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            text.setText(self.text_IdPwFindGuide[index])
            text.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(8)
            text.setFont(font)
            self.textEdit_IdPwFindGuide.append(text)
        for index in range(0,3):
            text = QtWidgets.QTextEdit(self.page_IdPwfind)
            text.setGeometry(858,132 + 200*index, 540,40)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            text.setText(self.text_IdPwFindGuide[index+2])
            text.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(8)
            text.setFont(font)
            self.textEdit_IdPwFindGuide.append(text)


        self.textEdit_userInf = []
        for index in range(0,2):
            text = QtWidgets.QTextEdit(self.page_IdPwfind)
            text.setGeometry(165,272 + 250*index, 550,85)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(14)
            text.setFont(font)
            self.textEdit_SignInf.append(text)
        for index in range(0,3):
            text = QtWidgets.QTextEdit(self.page_IdPwfind)
            text.setGeometry(858,172 + 200*index, 550,85)
            text.setStyleSheet("background-color : #ffffff; \n border : 0px; \n color : #000000; ")
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(14)
            text.setFont(font)
            self.textEdit_SignInf.append(text)

        self.pushButton_IdPwFind = []
        self.pushButtonText = ["ID 찾기", "PW 찾기"]
        for index in range(0,2):
            pushButton = QtWidgets.QPushButton(self.page_IdPwfind)
            pushButton.setGeometry(255+700 * index,730,360,90)
            pushButton.setStyleSheet("border : 1px; \n background-color : #828282; \n color : #ffffff;")
            pushButton.setText(self.pushButtonText[index])
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setBold(True)
            font.setPointSize(17)
            pushButton.setFont(font)
            self.pushButton_IdPwFind.append(pushButton)


        self.stackedWidget.addWidget(self.page_IdPwfind)



        
        
        self.stackedWidget.setCurrentIndex(1)
        self.mainWindow.setCentralWidget(self.centralWidget)
    

if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)

    mainGui = MainGui()  
    mainGui.mainWindow.show() 

    sys.exit(app.exec_())