import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *
import subprocess as sub

baslikfont = QFont("Century Gothic",28)
font = QFont("Century Gothic", 20)

class intro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome :)")

        yatay = QHBoxLayout()

        self.text = QLabel("PowerOffUI")

        yatay.addStretch()
        yatay.addWidget(self.text)
        yatay.addStretch()

        self.text.setFont(baslikfont)

        self.setLayout(yatay)

        self.setGeometry(500,300,170,108)
        self.show()

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.enter = intro()
        QTest.qWait(2000)
        self.enter.close()

        self.setWindowTitle("PowerOffUI")
        
        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        self.buton1 = QPushButton("Kapat")
        self.buton1.setFont(font)
        self.buton1.clicked.connect(self.p)

        self.buton2 = QPushButton("Yeniden Başlat")
        self.buton2.setFont(font)
        self.buton2.clicked.connect(self.r)

        dikey.addStretch()
        dikey.addWidget(self.buton1)
        dikey.addWidget(self.buton2)

        self.setLayout(dikey)
        
        self.setGeometry(500,300,100,100)
        self.show()

    def p(self):
        self.buton1.setText("Kapanıyor..")
        sub.call("shutdown -s", shell = True)

        
    def r(self):
        self.buton2.setText("Yeniden başlatılıyor..")
        sub.call("shutdown -r", shell = True)

        
uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())
