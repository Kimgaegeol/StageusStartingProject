import DB
import Config
import Gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import * 

import youtube_dl
import vlc
import pafy
import time

import urllib.request

class PageVideoLogic():
    def __init__(self,Gui,listNum):                                                                                                        
        self.db = DB.DataBase()

        self.mainGui = Gui
        self.listNum = listNum

        self.videorUrl = None
        self.videoList = [] #비디오 리스트
        self.videoNumber = [] #비디오 Pk

        self.mainVideoUrl = None # 메인 동영상
        self.media = None
        self.videoThread = None
        self.videoPauseValue = False #멈춤이나 재생으로 바꿈 

        self.listNameSet()

        self.mainUrlSetFirst() #Url 설정 
        self.mainVideoNameSet()
        self.mainVideoSet() #메인 비디오 설정
        self.videoListShape()

        self.mainGui.btnMainVideo[0].clicked.connect(self.btnEventStop)
        self.mainGui.btnMainVideo[1].clicked.connect(self.btnEventPauseRestart)
        
        self.mainGui.btnBackVideo.clicked.connect(self.btnEventBack)

    def btnEventBack(self): #뒤로가기
        self.media.stop()

        self.media = None

        self.listShapeReject()
        self.mainGui.stackedWidget.setCurrentIndex(3)
        
    def mainVideoNameSet(self): #메인 동영상 이름 생성
        video = pafy.new(self.mainVideoUrl)
        self.mainGui.textMainVideoTitle.setText(video.title)

    def mainUrlSetFirst(self):
        table = "video"
        colum = ["listnum"]
        value = [self.listNum]
        self.db.readData(table,colum,value)
        
        self.mainVideoUrl = self.db.result[0][1]

    def mainVideoSet(self): # videoUrl을 메인 동영상으로 설정 
        video = pafy.new(self.mainVideoUrl)
        best = video.getbest()
        self.media = vlc.MediaPlayer(best.url)
        self.media.set_hwnd(self.mainGui.videoFrame.winId())
        self.videoThread = VideoThread(self.media)
        self.videoThread.start()

        self.videoPauseValue = False
        self.mainGui.btnMainVideo[1].setText("멈춤")

    def btnEventPauseRestart(self): #일시정지, 일시재생
        if not self.videoPauseValue:
            self.videoPauseValue = True
            self.mainGui.btnMainVideo[1].setText("재생")
            self.media.pause()
            
        else:
            self.videoPauseValue = False
            self.mainGui.btnMainVideo[1].setText("멈춤")
            self.media.play()
            
    def btnEventStop(self): #동영상 중지
        self.media.stop()

    def listNameSet(self):  # 리스트 이름 생성
        table = "list"
        colum = ["sequence"]
        value = [self.listNum]
        self.db.readData(table,colum,value)
        listName = self.db.result[0][1]
        self.mainGui.textListTitleVideoPage.setText(listName)

    def btnEventOtherVideoStart(self,event,videoUrl):
        self.media.stop()
        self.videoThread = None
        self.mainVideoUrl = videoUrl
        self.mainVideoSet()

    def setThumb(self,value,index):
        label = QtWidgets.QLabel(self.mainGui.pageVideo)
        label.setPixmap(value)
        label.setGeometry(1070, 235 + index * 123, 80, 120)
        self.mainGui.thumbnailVideo.append(label)
        label.show()

        self.mainGui.btnVideoStart[index].raise_()

    def videoListShape(self): #동영상 리스트 
        self.mainGui.thumbnailVideo = [] #Gui 초기화 
        self.mainGui.btnVideoStart = []
        self.mainGui.textVideoTitle = []
        self.mainGui.btnVideoReject = []

        self.thumb = []

        table = "video"
        colum = ["listnum"]
        value = [self.listNum]
        self.db.readData(table,colum,value)
        
        for index in range(0,len(self.db.result)):
            video = pafy.new(self.db.result[index][1])

            thumbThread = BringThumbnail(self.db.result[index][1],index)
            thumbThread.start()
            self.thumb.append(thumbThread)
            thumbThread.sign.connect(self.setThumb)

            btn = QtWidgets.QPushButton(self.mainGui.pageVideo)      #동영상 버튼
            btn.setGeometry(1070, 235 + index * 123, 80, 120)
            btn.setStyleSheet("border : 1px solid #ffffff; \n background-color : #00828282; \n color : #ffffff;")
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.mainGui.btnVideoStart.append(btn)
            self.mainGui.btnVideoStart[index].show()

                  #동영상 이름
            text = QtWidgets.QTextEdit(self.mainGui.pageVideo)
            text.setGeometry(1151,235 + index *123, 240,120)
            text.setStyleSheet("border : 1px solid #ffffff; \n background-color : #80323232; \n color : #ffffff;")
            text.setReadOnly(True)
            text.setText(video.title)
            font = QtGui.QFont()
            font.setFamily(Config.fontKorean[0])
            font.setBold(True)
            font.setPointSize(9)
            text.setFont(font)
            self.mainGui.textVideoTitle.append(text)
            self.mainGui.textVideoTitle[index].show()

            btn = QtWidgets.QPushButton(self.mainGui.pageVideo)      #동영상 삭제버튼
            btn.setGeometry(1392, 235 + index * 123, 80, 120)
            btn.setStyleSheet(Config.btnStyleeSheet[0])
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setText("삭제")
            font.setFamily(Config.fontKorean[0])
            font.setBold(True)
            font.setPointSize(9)
            btn.setFont(font)
            self.mainGui.btnVideoReject.append(btn)
            self.mainGui.btnVideoReject[index].show()

        for index in range(0,len(self.db.result)):
            self.mainGui.btnVideoStart[index].clicked.connect(lambda event, videoUrl = self.db.result[index][1] : self.btnEventOtherVideoStart(event,videoUrl))
        
        for index in range(0,len(self.db.result)):
            self.mainGui.btnVideoReject[index].clicked.connect(lambda event, videoNum = self.db.result[index][0] : self.btnEventVideoReject(event,videoNum))
        
    def listShapeReject(self):
        for index in range(0,len(self.db.result)):
            self.mainGui.thumbnailVideo[index].setGeometry(0,0,0,0)
            self.mainGui.btnVideoStart[index].setGeometry(0,0,0,0)
            self.mainGui.textVideoTitle[index].setGeometry(0,0,0,0)
            self.mainGui.btnVideoReject[index].setGeometry(0,0,0,0)

        self.mainGui.thumbnailVideo = [] #Gui 초기화 
        self.mainGui.btnVideoStart = []
        self.mainGui.textVideoTitle = []
        self.mainGui.btnVideoReject = []

    def btnEventVideoReject(self,event,videoNum):
        self.dialogVideoReject = QtWidgets.QDialog()
        self.dialog = Gui.Dialog(self.dialogVideoReject)

        text = QtWidgets.QTextEdit(self.dialogVideoReject)
        text.setGeometry(110,120,430,130)
        text.setStyleSheet(Config.infTextStylesheet[0])
        text.setText("정말 삭제하시겠습니까?")
        font = QtGui.QFont()
        font.setFamily(Config.fontKorean[0])
        font.setBold(True)
        font.setPointSize(14)
        text.setFont(font)

        btn =QtWidgets.QPushButton(self.dialogVideoReject)
        btn.setGeometry(220,200,150,120)
        btn.setStyleSheet(Config.btnStyleeSheet[0])
        btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn.setText("확인")
        font.setPointSize(17)
        btn.setFont(font)

        self.dialog.btn.append(btn)

        self.dialogVideoReject.show()

        self.dialog.btn[0].clicked.connect(lambda event, videoNumber = videoNum : self.btnEventDialogVideoReject(event,videoNumber))

    def btnEventDialogVideoReject(self,event,videoNum):
        self.listShapeReject()

        table = "video"
        colum = ["sequence"]
        value = [videoNum]

        self.db.deleteData(table,colum,value)

        self.videoListShape()

        self.dialogVideoReject.reject()


class VideoThread(QThread):
    def __init__(self,media):
        super().__init__()
        self.media = media

    def run(self):
        self.media.play()

    
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
        qpixmapVar = qpixmapVar.scaled(80,120)
        self.sign.emit(qpixmapVar,self.index)
        