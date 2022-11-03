import sys
import subprocess
import namegenerator
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import lpc_hmm_matematika as new_method

class AudioProc(QMainWindow):
    def __init__(self):

        super(AudioProc,self).__init__()
        loadUi('virtualassistant.ui',self)

        # Function Declaration
        self.record_btn.clicked.connect(self.record_btn_clicked)
        self.exitBtn.clicked.connect(self.exitBtn_clicked)

    @pyqtSlot()
    def record_btn_clicked(self):
        QMessageBox().information(self, 'Information', 'Ready to Record')
        QMessageBox.show(self)

        label_predict = new_method.record(namegenerator.gen())

        QMessageBox().information(self, 'Information', str(label_predict))
        QMessageBox.show(self)

        if label_predict == 'bangun ruang':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
            subprocess.call('start BANGUN_RUANG.mp4', shell=True)
        elif label_predict == 'luas bangun ruang':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\Doc1.pdf"')
            subprocess.call('start LUAS_BANGUN_RUANG.mp4', shell=True)
        elif label_predict == 'operasi pecahan':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\Doc1.pdf"')
            subprocess.call('start Operasi_pada_pecahan.ppt', shell=True)
        elif label_predict == 'pecahan':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
            subprocess.call('start Pecahan.ppt', shell=True)
        elif label_predict == 'perbandingan':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
            subprocess.call('start Perbandingan.pdf', shell=True)

    @pyqtSlot()
    def exitBtn_clicked(self):
        sys.exit(app.exec_())

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=AudioProc()
    #window.setWindowTitle('Virtual Assisten Matematika')
    window.show()
    sys.exit(app.exec_())
