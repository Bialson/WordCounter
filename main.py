import sys
import math
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QGridLayout, QApplication, QTextEdit, QLabel, QDesktopWidget)
from PyQt5.QtGui import *


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
               
    def initUI(self):
        self.resize(1070, 900)
        self.center()
        self.setWindowTitle('WordCounter')
        self.setStyleSheet('background-color: #DCF0FE')

        self.inputTxt = QTextEdit()
        self.btn1 = QPushButton('Oblicz')
        self.lbl1 = QLabel('Ilość słów: ')

        self.btn1.clicked.connect(self.oblicz)

        self.btn1.setStyleSheet('font-size: 13px; font-family: Futura,Trebuchet MS,Arial,sans-serif;')
        self.btn1.setFixedSize(100, 50)
        self.lbl1.setStyleSheet('font-size: 20px; font-family: Futura,Trebuchet MS,Arial,sans-serif; margin-top: 30px;')
        self.inputTxt.setAlignment(Qt.AlignJustify)
        self.inputTxt.setStyleSheet("""
        QTextEdit{
            font-size: 15px; 
            font-family: Futura,Trebuchet MS,Arial,sans-serif; 
            padding: 20px; 
            background-color: #858E92; 
            color: whitesmoke; 
            font-weight: bolder;
        }
        QScrollBar:vertical {
            border: 0px solid #999999;
            background:white;
            width:10px;    
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {         
       
            min-height: 0px;
          	border: 0px solid red;
			background-color: #535A5D;
        }
        QScrollBar::add-line:vertical {       
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        """)

        lbox = QGridLayout()
        lbox.addWidget(self.inputTxt, 0, 0)
        lbox.addWidget(self.btn1, 0, 1)
        lbox.addWidget(self.lbl1, 1, 0)
        lbox.setContentsMargins(30, 30, 30, 30)
        lbox.setHorizontalSpacing(50)
        self.setLayout(lbox)
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def oblicz(self):
        text = self.inputTxt.toPlainText()
        word_list = text.split()
        wordCount = len(word_list)
        self.lbl1.setText('Ilość słów: ' + str(wordCount))
        
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main = StartWindow()
    main.setWindowIcon(QIcon('icon.ico'))   
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()