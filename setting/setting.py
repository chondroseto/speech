import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import lpc_hmm_setting as new_method

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
        loadUi('setting.ui',self)

        # Function Declaration
        self.train_btn.clicked.connect(self.train_btn_clicked)
        self.record_btn.clicked.connect(self.record_btn_clicked)
        self.test_btn.clicked.connect(self.test_btn_clicked)
        self.app_btn.clicked.connect(self.app_btn_clicked)

        # UI Output
        self.result_label = QLabel(self)
        self.result_label.setStyleSheet("border : 1px solid black;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.move(150, 150)
        self.result_label.resize(90, 30)
        self.result_label.setText("Output")


    @pyqtSlot()
    def train_btn_clicked(self):
        QMessageBox().information(self, 'Information', 'Training Start')
        QMessageBox.show(self)
        new_method.lpc_hmm_train()
        QMessageBox().information(self,'Information','Training Done')
        QMessageBox.show(self)

    @pyqtSlot()
    def record_btn_clicked(self):
        self.en=editwindow()
        self.en.show()

    @pyqtSlot()
    def test_btn_clicked(self):
        fname, unused = QFileDialog.getOpenFileName(self, 'Open file','C:\\Users\\chondroseto\\PycharmProjects\\assist\\code\\umum',"Audio files (*.wav)")
        if len(fname)>0:
            QMessageBox().information(self, 'Information', 'Load File Success')
            QMessageBox.show(self)

            result,label_actual, label_predict,status =  new_method.lpc_hmm_uji_one(fname)

            QMessageBox().information(self, 'Information', str(result))
            QMessageBox.show(self)
            #status='undetected'
            if len(label_predict)>1:
                self.result_label.setText(label_predict)
            else:
                self.result_label.setText("undetected")

            #label_predict = ""

            if status=='detected':
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

    @pyqtSlot()
    def app_btn_clicked(self):
        QMessageBox().information(self, 'Information', 'Test All Start')
        QMessageBox.show(self)

        result=new_method.lpc_hmm_uji_all()

        QMessageBox().information(self, 'Information', result)
        QMessageBox.show(self)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=AudioProc()
    window.setWindowTitle('Virtual Assisten Setting')
    window.show()
    sys.exit(app.exec_())
