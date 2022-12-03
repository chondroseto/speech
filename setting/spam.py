from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication
    window = QWidget()
    window.setGeometry(100,100,200,300)
    window.setWindowTitle("R And D GUI python")

    layout = QVBoxLayout()


    button = QPushButton("press Button")
    label = QLabel("as")

    layout.addWidget(label)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    app.exec_()

if __name__== '__main__':
    main()