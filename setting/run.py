import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *

class MainProgram(QMainWindow):
    def __init__(self):

        super(MainProgram,self).__init__()
        loadUi('default.ui',self)
        self.btnSetting.clicked.connect(self.btnSetting_clicked)

    @pyqtSlot()
    def btnSetting_clicked(self):
        os.system('python setting.py')

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainProgram()
    #window.setWindowTitle('Virtual Assisten')
    window.show()
    sys.exit(app.exec_())
