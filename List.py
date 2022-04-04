from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *  # 쓰레드 

import threading

import Gui
import DB
import validators
import math
import Video
import pafy
import urllib.request
import Config

import time

# db값의 리드데이터는 리턴값으로 처리해주는 것이 좋다. 

class PageListLogic(): #파일 이름은 파스칼로 적어야 한다.

# 쓰레드는 손 못 대는 것만

    def __init__(self,Gui,userPk):

        self.db = DB.DataBase()
        self.mainGui = Gui
        self.userNumber = userPk  # 멤버 pk   #usernumber가 더욱 좋다.

        self.listNumber = []  # 리스트 pk

        self.urlStoragePossible = False #저장가능한지 불가능한지 체크 

        self.videoUrl = None #Url을 저장해놓지 않으면 저장했을 때 라인의 text값을 건드리면 이상한 Url값이 들어간다. 

        self.videoPage = None

        self.listShapeSet() #유저에 따라 리스트 만들면서 시작

        self.mainGui.btnBackList.clicked.connect(self.btnEventBack)
        self.mainGui.btnUrlSearch.clicked.connect(self.btnEventUrlSearch)
        self.mainGui.btnUrlStorage.clicked.connect(self.btnEventUrlStorage)
        self.mainGui.btnAddList.clicked.connect(self.btnEventAddList)
        
    def btnEventBack(self): 
        self.listShapeClear()
        self.mainGui.lineLogin[0].clear()
        self.mainGui.lineLogin[1].clear()
        self.mainGui.stackedWidget.setCurrentIndex(0)

    def btnEventGoVideo(self,event,listNum):
        table = "video"
        colum = ["listnum"]
        value = [listNum]

        if self.db.readData(table,colum,value):
            self.mainGui.stackedWidget.setCurrentIndex(4)
            self.pageVideo = Video.PageVideoLogic(self.mainGui,listNum)

        else:
            self.dialogNoVideo = QtWidgets.QDialog()
            self.dialog = Gui.Dialog(self.dialogNoVideo)

            text = QtWidgets.QTextEdit(self.dialogNoVideo)
            text.setGeometry(52,140,540,250)
            text.setStyleSheet("border : 0px; \n background-color : #000000; \n color : #ffffff;")
            text.setReadOnly(True)
            text.setText("동영상이 들어있지 않습니다.")
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setPointSize(15)
            text.setFont(font)

            self.dialogNoVideo.show()

    def btnEventUrlSearch(self):
        if validators.url(self.mainGui.lineUrlSearch.text()):
            self.videoUrl = self.mainGui.lineUrlSearch.text() 
            self.urlStoragePossible = True
            self.mainGui.btnUrlStorage.setGeometry(1303,145,150,110)
            self.mainGui.btnUrlStorage.setText("저장")
        
        else:
            self.urlStoragePossible = False
            self.mainGui.btnUrlStorage.setGeometry(0,0,0,0)
            self.mainGui.btnUrlStorage.setText("")

            self.dialogSearchFail = QtWidgets.QDialog()
            self.dialog = Gui.Dialog(self.dialogSearchFail)
            
            text = QtWidgets.QTextEdit(self.dialogSearchFail)
            text.setGeometry(110,150,470,150)
            text.setStyleSheet("border : 0px; \n color : #ffffff;")
            text.setText("올바르지 않은 URL입니다.")     # 왜 잘못되었습니다. 가 뒤로 안 밀릴까? 질문
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0]) 
            font.setPointSize(12)
            text.setFont(font)

            self.dialogSearchFail.show()

            self.mainGui.lineUrlSearch.clear()
            
    def btnEventUrlStorage(self):
        if self.urlStoragePossible:
            self.dialogAddVideo = QtWidgets.QDialog()
            self.dialog = Gui.Dialog(self.dialogAddVideo)

            for index in range(0,len(self.db.result)): #다이아로그의 재생목록 이름과 저장목록 생성
                text = QtWidgets.QTextEdit(self.dialogAddVideo)
                text.setGeometry(60 + index%2 * 250, 70 + math.floor(index/2) * 55,190,55)
                text.setStyleSheet(Config.dialogTextStyleSheet[0])
                text.setReadOnly(True)
                text.setText(self.db.result[index][1])
                font = QtGui.QFont()
                font.setFamily(Config.fontKorean[0])
                font.setPointSize(11)
                text.setFont(font)

                self.dialog.text.append(text)

                btn = QtWidgets.QPushButton(self.dialogAddVideo)
                btn.setGeometry(250 + index%2 * 250, 70 + math.floor(index/2) * 55,55,55)
                btn.setStyleSheet(Config.dialogBtnStyleSheet[0])
                btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                btn.setText("저장")
                font.setBold(True)
                font.setPointSize(8)
                btn.setFont(font)

                self.dialog.btn.append(btn)

            self.dialogAddVideo.show()  #다이아로그 보여주기
            
            for index in range(0,len(self.db.result)):
                self.dialog.btn[index].clicked.connect(lambda event, listNum = self.db.result[index][0] : self.btnEventDialogUrlStorage(event,listNum))

    def btnEventDialogUrlStorage(self,event,listNum):
        if not self.db.readDataVideoList(listNum):
            self.listShapeClear() #먼저 지워야 오류가 나지 않는다.

            table = "video"
            colum = ["videourl","listnum"]
            value = [self.videoUrl,listNum]
            self.db.insertData(table,colum,value)

            self.listShapeSet()

            self.dialogAddVideo.reject()

            self.urlStoragePossible = False
            self.mainGui.btnUrlStorage.setGeometry(0,0,0,0)
            self.mainGui.btnUrlStorage.setText("")
            self.mainGui.lineUrlSearch.clear()
            
        else:
            table = "video"
            colum = ["videourl","listnum"]
            value = [self.videoUrl,listNum]
            self.db.insertData(table,colum,value)

            self.dialogAddVideo.reject()
            
            self.urlStoragePossible = False
            self.mainGui.btnUrlStorage.setGeometry(0,0,0,0)
            self.mainGui.btnUrlStorage.setText("")
            self.mainGui.lineUrlSearch.clear()

    def btnEventAddList(self):
        self.dialogAddList = QtWidgets.QDialog()
        self.dialog = Gui.Dialog(self.dialogAddList)

        text = QtWidgets.QTextEdit(self.dialogAddList)
        text.setGeometry(50,90,70,60)
        text.setStyleSheet("border : 0px; \n background-color : #000000; \n color : #ffffff;")
        text.setReadOnly(True)
        text.setText("이름 :")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setPointSizeF(9)
        text.setFont(font)

        line = QtWidgets.QLineEdit(self.dialogAddList)
        line.setGeometry(122,88,440,60)
        line.setStyleSheet("border : 1px solid #ffffff; \n background-color : #ffffff; \n border-radius : 10px;")
        line.setFont(font)

        self.dialog.line.append(line)

        btn = QtWidgets.QPushButton(self.dialogAddList)
        btn.setGeometry(220,220,200,80)
        btn.setStyleSheet(Config.btnStyleeSheet[0])
        btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn.setText("재생목록 추가")
        font.setBold(True)
        btn.setFont(font)

        self.dialog.btn.append(btn)

        self.dialog.btn[0].clicked.connect(self.btnEventDialogAddList)
        self.dialogAddList.show()
        
    def btnEventDialogAddList(self):
        name = self.dialog.line[0].text()

        table = "list"
        colum = ["listname","user"]
        value = [name,self.userNumber]
        self.db.insertData(table,colum,value)

        self.dialogAddList.reject()
        self.listShapeClear()
        self.listShapeSet()

    def bringUserData(self):
        table = "list"
        colum = ["user"]
        value = [self.userNumber]
        self.db.readData(table,colum,value)

    def setThumb(self,value,index):
        label = QtWidgets.QLabel(self.mainGui.pageList)
        label.setPixmap(value)
        label.setGeometry(170 + index%4 * 350, 290 + math.floor(index/4) * 270, 200, 200)
        self.mainGui.listThumbnail.append(label)
        if index < 8:
            label.show()

        self.mainGui.btnList[index].raise_()

    def listShapeSet(self):   
        #리스트 초기화      #각각의 리스트들이 가지고 있는 위젯을 딜리트
        self.mainGui.listThumbnail = [] #리스트 삭제도 클리어 함수에서 해주는 것이 좋다. 
        self.mainGui.btnList = []          # 클리어 함수에는 이벤트 해제(disconnect), 위젯 삭제, 위젯들이 담겨있던 리스트 초기화 
        self.mainGui.textListTitle = []
        self.mainGui.btnListReject =[]
        self.mainGui.btnListNext = []
        self.mainGui.btnListPrev = []

        self.thumb = [] #애는 생성자에 있어야 한다.  ## 메로리 관리에 신경을 많이 쓰자!

        self.btnNextPrevCount = 0

        self.bringUserData()

        # math.floor = 내림
        for index in range(0,len(self.db.result)): #리스트 생성 
            if self.db.readDataVideoList(self.db.result[index][0]):
                url = self.db.video[0][1]

                thumbThread = BringThumbnail(url,index)
                thumbThread.start()
                self.thumb.append(thumbThread)
                thumbThread.sign.connect(self.setThumb) 

                btn = QtWidgets.QPushButton(self.mainGui.pageList)
                btn.setGeometry(170 + index%4 * 350, 290 + math.floor(index/4) * 270, 200, 200)
                btn.setStyleSheet("border : 0px; \n background-color : #00323232; ")
                btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                btn.raise_()
                self.mainGui.btnList.append(btn)
                if index < 8:
                    self.mainGui.btnList[index].show()

            else:
                btn = QtWidgets.QPushButton(self.mainGui.pageList)
                btn.setGeometry(170 + index%4 * 350, 290 + math.floor(index/4) * 270, 200, 200)
                btn.setStyleSheet("border : 0px; \n background-color : #80323232; ")
                btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                btn.raise_()
                self.mainGui.btnList.append(btn)
                if index < 8:
                    self.mainGui.btnList[index].show()
            
            text = QtWidgets.QLabel(self.mainGui.pageList)
            text.setStyleSheet("border : 0px; \n background-color : #ffffff; \n color : #000000;")
            text.setGeometry(170 + index%4 * 350, 490 + math.floor(index/4) * 270, 200, 40)
            text.setText(str(self.db.result[index][1]))
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setBold(True)
            font.setPointSize(9)
            text.setFont(font)
            self.mainGui.textListTitle.append(text)
            if index < 8:
                self.mainGui.textListTitle[index].show()

            btn = QtWidgets.QPushButton(self.mainGui.pageList)
            btn.setStyleSheet(Config.btnStyleeSheet[0])
            btn.setGeometry(370 + index%4 * 350, 290 + math.floor(index/4) * 270, 50, 90)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setText("삭제")
            font.setBold(True)
            font.setPointSize(9)
            btn.setFont(font)
            self.mainGui.btnListReject.append(btn)
            if index < 8:
                self.mainGui.btnListReject[index].show()

        self.mainGui.btnAddList.setGeometry(200 + len(self.db.result)%4 * 350, 330 + math.floor(len(self.db.result)/4) * 300,130,130) #추가버튼

        for index in range(0,int(len(self.db.result)/8)):
            btn = QtWidgets.QPushButton(self.mainGui.pageList)
            btn.setGeometry(560,830,130,40)
            btn.setStyleSheet(Config.btnStyleeSheet[0])
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setText("이전 페이지")
            btn.setFont(font)

            self.mainGui.btnListPrev.append(btn)

            btn = QtWidgets.QPushButton(self.mainGui.pageList)
            btn.setGeometry(850,830,130,40)
            btn.setStyleSheet(Config.btnStyleeSheet[0])
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setText("다음 페이지")
            btn.setFont(font)

            self.mainGui.btnListNext.append(btn)

            self.btnNextPrevCount += 1

        if len(self.db.result) >= 8:
            self.mainGui.btnListNext[0].show()

        for index in range(0,len(self.db.result)): # 리스트를 클릭할 시 생기는 이벤트
            self.mainGui.btnList[index].clicked.connect(lambda event, listNum = self.db.result[index][0] : self.btnEventGoVideo(event,listNum))

        for index in range(0,len(self.db.result)): # 리스트를 클릭할 시 생기는 이벤트
            self.mainGui.btnListReject[index].clicked.connect(lambda event, listNum = self.db.result[index][0] : self.btnEventListReject(event,listNum))

        for index in range(0,self.btnNextPrevCount):
            self.mainGui.btnListNext[index].clicked.connect(lambda event, num = index + 1 : self.btnEventNextList(event,num))

        for index in range(0,self.btnNextPrevCount):
            self.mainGui.btnListPrev[index].clicked.connect(lambda event, num = index : self.btnEventPrevList(event,num))

    def btnEventPrevList(self,event,num):
        for index in range(0,len(self.db.result)):
            if self.db.readDataVideoList(self.db.result[index][0]):
                self.mainGui.listThumbnail[index].hide()
            self.mainGui.btnList[index].hide()
            self.mainGui.textListTitle[index].hide()
            self.mainGui.btnListReject[index].hide()

        for index in range(0,len(self.db.result)):
            if self.db.readDataVideoList(self.db.result[index][0]):
                self.mainGui.listThumbnail[index].move(170 + index%4 * 350, 290 + math.floor(index%8/4) * 270)
                if index < 8:
                    self.mainGui.listThumbnail[index].show()

            self.mainGui.btnList[index].move(170 + index%4 * 350, 290 + math.floor(index%8/4) * 270)
            if index < 8:
                self.mainGui.btnList[index].show()

            self.mainGui.textListTitle[index].move(170 + index%4 * 350, 490 + math.floor(index%8/4) * 270)
            if index < 8:
                self.mainGui.textListTitle[index].show()

            self.mainGui.btnListReject[index].move(370 + index%4 * 350, 290 + math.floor(index%8/4) * 270)
            if index < 8:
                self.mainGui.btnListReject[index].show()

        self.mainGui.btnAddList.move(200 + len(self.db.result)%4 * 350, 330 + math.floor(len(self.db.result)/4) * 300)
        self.mainGui.btnAddList.show()

        self.mainGui.btnListNext[num].show()
        self.mainGui.btnListPrev[num].hide()

    def btnEventNextList(self,event,num):
        for index in range(0,len(self.db.result)):
            if self.db.readDataVideoList(self.db.result[index][0]):
                self.mainGui.listThumbnail[index].hide()
            self.mainGui.btnList[index].hide()
            self.mainGui.textListTitle[index].hide()
            self.mainGui.btnListReject[index].hide()

        for index in range(8*num,len(self.db.result)%8 + 8*num):
            if self.db.readDataVideoList(self.db.result[index][0]):
                self.mainGui.listThumbnail[index].move(170 + index%4 * 350, 290 + math.floor(index%8/4) * 270)
                self.mainGui.listThumbnail[index].show()
            self.mainGui.btnList[index].move(170 + index%4 * 350, 290 + math.floor(index%8/4) * 270)
            self.mainGui.btnList[index].show()
            self.mainGui.textListTitle[index].move(170 + index%4 * 350, 490 + math.floor(index%8/4) * 270)
            self.mainGui.textListTitle[index].show()
            self.mainGui.btnListReject[index].move(370 + index%4 * 350, 290 + math.floor(index%8/4) * 270)
            self.mainGui.btnListReject[index].show()

        self.mainGui.btnAddList.move(200 + len(self.db.result)%4 * 350, 330 + math.floor(len(self.db.result)%8/4) * 300)
        self.mainGui.btnAddList.show()

        self.mainGui.btnListNext[num-1].hide()
        self.mainGui.btnListPrev[num-1].show()

    def listShapeShow(self,num):
        for index in range(0,len(self.db.result)):
            if self.db.readDataVideoList(self.db.result[index][0]):
                print(len(self.mainGui.listThumbnail))
                self.mainGui.listThumbnail[index].hide()
            self.mainGui.btnList[index].hide()
            self.mainGui.textListTitle[index].hide()
            self.mainGui.btnListReject[index].hide()

        for index in range(8*num,8*num+len(self.db.result)%8):
            if self.db.readDataVideoList(self.db.result[index][0]):
                self.mainGui.listThumbnail[index].show()
            self.mainGui.btnList[index].show()
            self.mainGui.textListTitle[index].show()
            self.mainGui.btnListReject[index].show()

    def listShapeClear(self):  #리스트 모양을 없애지 않으면 남아있기 때문에 만든 함수  #이벤트도 삭제해줘야됨 그리고 위젯 지우는건 딜리트함수 써야됨
        for index in range(0,len(self.db.result)): 
            if self.db.readDataVideoList(self.db.result[index][0]):
                self.mainGui.listThumbnail[index].setGeometry(0,0,0,0)
            self.mainGui.btnList[index].setGeometry(0,0,0,0)
            self.mainGui.textListTitle[index].setGeometry(0,0,0,0)
            self.mainGui.btnListReject[index].setGeometry(0,0,0,0)

        for index in range(0,self.btnNextPrevCount):
            self.mainGui.btnListNext[index].setGeometry(0,0,0,0)
            self.mainGui.btnListPrev[index].setGeometry(0,0,0,0)     #위젯 삭제하는 법 쳐보자

    def btnEventListReject(self,event,listNum):
        self.dialogListReject = QtWidgets.QDialog()
        self.dialog = Gui.Dialog(self.dialogListReject)

        text = QtWidgets.QTextEdit(self.dialogListReject)
        text.setGeometry(110,120,430,130)
        text.setStyleSheet(Config.infTextStylesheet[0])
        text.setText("정말 삭제하시겠습니까?")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(14)
        text.setFont(font)

        btn =QtWidgets.QPushButton(self.dialogListReject)
        btn.setGeometry(220,200,150,120)
        btn.setStyleSheet(Config.btnStyleeSheet[0])
        btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn.setText("확인")
        font.setPointSize(17)
        btn.setFont(font)

        self.dialog.btn.append(btn)

        self.dialogListReject.show()
        self.dialog.btn[0].clicked.connect(lambda event, listNum = listNum : self.btnEventDialogListReject(event,listNum))

    def btnEventDialogListReject(self,event,listNum):
        self.listShapeClear()

        table = "list"
        colum = ["sequence"]
        value = [listNum]
        self.db.deleteData(table,colum,value)

        self.listShapeSet()

        self.dialogListReject.reject()
        

class BringThumbnail(QThread):
    sign = pyqtSignal(QPixmap,int) 

    def __init__(self,url,index):
        super().__init__()
        self.url = url
        self.index = index
        
    def run(self):
        video = pafy.new(self.url)
        value = video.bigthumb
        imapgeFromWeb = urllib.request.urlopen(value).read()
        qpixmapVar = QPixmap()
        qpixmapVar.loadFromData(imapgeFromWeb)
        qpixmapVar = qpixmapVar.scaled(200,200)
        self.sign.emit(qpixmapVar,self.index)


    
        
        


    

    








    
    







