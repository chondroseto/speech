import sys
import os
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import lpc_hmm_fisika as new_method
import matplotlib.pyplot as plt
import numpy as np

class editwindow(QWidget):
    def __init__(self):

        super(editwindow,self).__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Berikan Nama File Suara")

        self.editname = QTextEdit(self)
        self.editname.setPlaceholderText("Berikan Nama File Suara")

        self.btnname = QPushButton(self)
        self.btnname.setText("OK")
        self.btnname.clicked.connect(self.record_ok_clicked)

        layout.addWidget(self.editname)
        layout.addWidget(self.btnname)

    @pyqtSlot()
    def record_ok_clicked(self):

        QMessageBox().information(self, 'Information', 'Ready to Record')
        QMessageBox.show(self)

        result, label_predict = new_method.record(self.editname.toPlainText())

        QMessageBox().information(self, 'Information', str(result))
        QMessageBox.show(self)

        #self.result_label.setText(label_predict)

        #label_predict = ""

        if label_predict == 'fisika':
            os.system(r'cmd /c "start C:\Users\chondroseto\Desktop\LinkedIn"')
        elif label_predict == 'matematika':
            os.system(r'cmd /c "start C:\Users\chondroseto\Desktop\Whatsapp"')
        elif label_predict == 'bahasa inggris':
            os.system(r'cmd /c "start C:\Users\chondroseto\Desktop\Gmail"')
        elif label_predict == 'bahasa inggris':
            os.system(r'cmd /c "start C:\Users\chondroseto\Desktop\Gmail"')
        elif label_predict == 'bahasa inggris':
            os.system(r'cmd /c "start C:\Users\chondroseto\Desktop\Gmail"')

        #self.close()


class AudioProc(QMainWindow):
    def __init__(self):

        super(AudioProc,self).__init__()
        loadUi('core.ui',self)

        #Function Declaration
        self.record_btn.clicked.connect(self.record_btn_clicked)

        #UI Output
        self.result_label = QLabel(self)
        self.result_label.setStyleSheet("border : 1px solid black;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.move(150, 150)
        self.result_label.resize(90,30)
        self.result_label.setText("Output")



    @pyqtSlot()
    def record_btn_clicked(self):
        self.en=editwindow()
        self.en.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=AudioProc()
    window.setWindowTitle('Virtual Assisten Fisika')
    window.show()
    sys.exit(app.exec_())
