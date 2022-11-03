import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import namegenerator
import lpc_hmm_fisika as new_method

class AudioProc(QMainWindow):
    def __init__(self):

        super(AudioProc,self).__init__()
        loadUi('virtualassistant.ui',self)

        #Function Declaration
        self.record_btn.clicked.connect(self.record_btn_clicked)
        self.exitBtn.clicked.connect(self.exitBtn_clicked)

    @pyqtSlot()
    def record_btn_clicked(self):
        QMessageBox().information(self, 'Information', 'Ready to Record')
        QMessageBox.show(self)

        label_predict = new_method.record(namegenerator.gen())

        QMessageBox().information(self, 'Information', str(label_predict))
        QMessageBox.show(self)

        if label_predict == 'bumi':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
            subprocess.call('start BUMI_DAN_KESEIMBANGAN.pptx', shell=True)
        elif label_predict == 'gerak':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\Doc1.pdf"')
            subprocess.call('start gerak.pptx', shell=True)
        elif label_predict == 'gerak melingkar':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\Doc1.pdf"')
            subprocess.call('start gerak_melingkar_1', shell=True)
            subprocess.call('start gerak_melingkar_2', shell=True)
            subprocess.call('start gerak_melingkar_3', shell=True)
            subprocess.call('start gerak_melingkar_4', shell=True)
        elif label_predict == 'planet':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
            subprocess.call('start planet.pptx', shell=True)
        elif label_predict == 'tata surya':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
            subprocess.call('start Belajar_Tata_Surya.mp4', shell=True)

    @pyqtSlot()
    def exitBtn_clicked(self):
        sys.exit(app.exec_())


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=AudioProc()
    #window.setWindowTitle('Virtual Assisten Fisika')
    window.show()
    sys.exit(app.exec_())
