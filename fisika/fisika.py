import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import uuid
import lpc_hmm_fisika as new_method
import time

class AudioProc(QMainWindow):
    def __init__(self):

        super(AudioProc,self).__init__()
        loadUi('FISIKA.ui',self)

        #Function Declaration
        self.record_btn.clicked.connect(self.record_btn_clicked)
        self.exitBtn.clicked.connect(self.exitBtn_clicked)

        self.gerak_btn.clicked.connect(self.gerak_btn_clicked)
        self.gerak_melingkar_btn.clicked.connect(self.gerak_melingkar_btn_clicked)
        self.bumi_btn.clicked.connect(self.bumi_btn_clicked)
        self.planet_btn.clicked.connect(self.planet_btn_clicked)
        self.tata_surya_btn.clicked.connect(self.tata_surya_btn_clicked)

    @pyqtSlot()
    def record_btn_clicked(self):
        QMessageBox().information(self, 'Information', 'Ready to Record')
        QMessageBox.show(self)

        label_predict = new_method.record(str(uuid.uuid1()))

        QMessageBox().information(self, 'Information', str(label_predict))
        QMessageBox.show(self)

        if label_predict == 'bumi':
            subprocess.call('start BUMI_DAN_KESEIMBANGAN.pptx', shell=True)
        elif label_predict == 'gerak':
            subprocess.call('start gerak.pptx', shell=True)
        elif label_predict == 'gerak melingkar':
       #     subprocess.call('start gerak_melingkar_1', shell=True)
            #time.sleep(10)
            #subprocess.call('start gerak_melingkar_2', shell=True)
            #time.sleep(10)
            #subprocess.call('start gerak_melingkar_3', shell=True)
            #time.sleep(10)
            #subprocess.call('start gerak_melingkar_4', shell=True)
        elif label_predict == 'planet':
            subprocess.call('start planet.pptx', shell=True)
        elif label_predict == 'tata surya':
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
            subprocess.call('start Belajar_Tata_Surya.mp4', shell=True)

    @pyqtSlot()
    def exitBtn_clicked(self):
        sys.exit(app.exec_())

    @pyqtSlot()
    def gerak_btn_clicked(self):
        subprocess.call('start gerak.pptx', shell=True)

    @pyqtSlot()
    def gerak_melingkar_btn_clicked(self):
        subprocess.call('start gerak_melingkar_1', shell=True)
        #time.sleep(10)
        #subprocess.call('start gerak_melingkar_2', shell=True)
        #time.sleep(10)
        #subprocess.call('start gerak_melingkar_3', shell=True)
        #time.sleep(10)
        #subprocess.call('start gerak_melingkar_4', shell=True)

    @pyqtSlot()
    def bumi_btn_clicked(self):
        subprocess.call('start BUMI_DAN_KESEIMBANGAN.pptx', shell=True)

    @pyqtSlot()
    def planet_btn_clicked(self):
        subprocess.call('start planet.pptx', shell=True)

    @pyqtSlot()
    def tata_surya_btn_clicked(self):
        subprocess.call('start Belajar_Tata_Surya.mp4', shell=True)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=AudioProc()
    #window.setWindowTitle('Virtual Assisten Fisika')
    window.show()
    sys.exit(app.exec_())
