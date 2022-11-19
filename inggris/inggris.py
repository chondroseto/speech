import sys
import subprocess
import uuid
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import lpc_hmm_inggris as new_method

class AudioProc(QMainWindow):
    def __init__(self):

        super(AudioProc,self).__init__()
        loadUi('INGGRIS.ui',self)

        # Function Declaration
        self.record_btn.clicked.connect(self.record_btn_clicked)
        self.exitBtn.clicked.connect(self.exitBtn_clicked)

        self.diagnostic_test_btn.clicked.connect(self.diagnostic_test_btn_clicked)
        self.verb_btn.clicked.connect(self.verb_btn_clicked)
        self.pct_btn.clicked.connect(self.pct_btn_clicked)
        self.comparison_btn.clicked.connect(self.comparison_btn_clicked)
        self.final_test_btn.clicked.connect(self.final_test_btn_clicked)

    @pyqtSlot()
    def record_btn_clicked(self):
        QMessageBox().information(self, 'Information', 'Ready to Record')
        QMessageBox.show(self)

        label_predict = new_method.record(str(uuid.uuid1()))

        QMessageBox().information(self, 'Information', str(label_predict))
        QMessageBox.show(self)

        if label_predict == 'Comparison':
            subprocess.call('start Comparison.pdf', shell=True)

        elif label_predict == 'Diagnostic Test':
            subprocess.call('start Diagnostic_Test.pdf', shell=True)

        elif label_predict == 'Present Continuous Tense':
            subprocess.call('start Present_Continuous_Tense.pdf', shell=True)

        elif label_predict == 'pronoun':
            subprocess.call('start Noun_Pronouns_Verb.pdf', shell=True)

        elif label_predict == 'Final Test':
            subprocess.call('start Final_Test.pdf', shell=True)
            #os.system(r'cmd /c "start C:\Users\User\Desktop\tiket.pdf"')

    @pyqtSlot()
    def exitBtn_clicked(self):
        sys.exit(app.exec_())

    @pyqtSlot()
    def diagnostic_test_btn_clicked(self):
        subprocess.call('start Diagnostic_Test.pdf', shell=True)

    @pyqtSlot()
    def verb_btn_clicked(self):
        subprocess.call('start Noun_Pronouns_Verb.pdf', shell=True)

    @pyqtSlot()
    def pct_btn_clicked(self):
        subprocess.call('start Present_Continuous_Tense.pdf', shell=True)

    @pyqtSlot()
    def comparison_btn_clicked(self):
        subprocess.call('start Comparison.pdf', shell=True)

    @pyqtSlot()
    def final_test_btn_clicked(self):
        subprocess.call('start Final_Test.pdf', shell=True)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=AudioProc()
    #window.setWindowTitle('Virtual Assisten Inggris')
    window.show()
    sys.exit(app.exec_())
