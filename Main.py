import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Gui
import Login

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainGui = Gui.MainGui()  
    mainGui.mainWindow.show()   # 그 상태만 보여주는 문구임을 기억하자.
                                # 추가되는 위젯은 위젯.쇼로 바꿔주자. 
    loginLogic = Login.PageLoginLogic(mainGui)

    sys.exit(app.exec_())