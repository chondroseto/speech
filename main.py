import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *

class Main(QMainWindow):
    def __init__(self):

        super(Main,self).__init__()
        loadUi('main.ui',self)
        self.btnFsk.clicked.connect(self.btnFsk_clicked)
        self.btnMtk.clicked.connect(self.btnMtk_clicked)
        self.btnIng.clicked.connect(self.btnIng_clicked)
        self.exitBtn.clicked.connect(self.exitBtn_clicked)
        #self.btnSetting.clicked.connect(self.btnSetting_clicked)

    @pyqtSlot()
    def btnFsk_clicked(self):
        os.system('python fisika/fisika.py')

    @pyqtSlot()
    def btnMtk_clicked(self):
        os.system('python matematika/matematika.py')

    @pyqtSlot()
    def btnIng_clicked(self):
        os.system('python inggris/inggris.py')

    @pyqtSlot()
    def exitBtn_clicked(self):
        sys.exit(app.exec_())

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Main()
    #window.setWindowTitle('Virtual Assisten')
    window.show()
    sys.exit(app.exec_())
