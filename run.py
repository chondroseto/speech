import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *

class MainProg(QMainWindow):
    def __init__(self):

        super(MainProg,self).__init__()
        loadUi('main.ui',self)
        self.btnFsk.clicked.connect(self.btnFsk_clicked)
        self.btnMtk.clicked.connect(self.btnMtk_clicked)
        self.btnIng.clicked.connect(self.btnIng_clicked)


    @pyqtSlot()
    def btnFsk_clicked(self):
        os.system('python fisika/fisika.py')

    @pyqtSlot()
    def btnMtk_clicked(self):
        os.system('python matematika/matematika.py')

    @pyqtSlot()
    def btnIng_clicked(self):
        os.system('python inggris/inggris.py')

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainProg()
    window.setWindowTitle('Virtual Assisten')
    window.show()
    sys.exit(app.exec_())
