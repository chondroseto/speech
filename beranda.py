import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *

class Opening(QMainWindow):
    def __init__(self):

        super(Opening,self).__init__()
        loadUi('beranda.ui',self)
        self.mskBtn.clicked.connect(self.mskBtn_clicked)

    @pyqtSlot()
    def mskBtn_clicked(self):
        os.system('python pilih_pelajaran.py')

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Opening()
    #window.setWindowTitle('Virtual Assisten')
    window.show()
    sys.exit(app.exec_())
