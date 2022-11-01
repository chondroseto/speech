import sys
import subprocess
import namegenerator
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import lpc_hmm_inggris as new_method

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

        if label_predict == 'Comparison':
            subprocess.call('start Comparison.pdf', shell=True)
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
        elif label_predict == 'Diagnostic Test':
            subprocess.call('start Diagnostic_Test.pdf', shell=True)
            #os.system(r'cmd /c "start C:\Users\User\Desktop\Doc1.pdf"')
        elif label_predict == 'Present Continuous Tense':
            subprocess.call('start Present_Continuous_Tense.pdf', shell=True)
            #os.system(r'cmd /c "start C:\Users\User\Desktop\Doc1.pdf"')
        elif label_predict == 'Pronoun':
            subprocess.call('start Noun-Pronouns_Verb.pdf', shell=True)
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')
        elif label_predict == 'Final Test':
            subprocess.call('start Final_Test.pdf', shell=True)
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')

    @pyqtSlot()
    def exitBtn_clicked(self):
        sys.exit(app.exec_())

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=AudioProc()
    #window.setWindowTitle('Virtual Assisten Inggris')
    window.show()
    sys.exit(app.exec_())
