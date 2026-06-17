# DIGITAL CLOCK PROGRAM


import sys
from wsgiref.util import application_uri

from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                             QWidget,QHBoxLayout,QVBoxLayout,
                             QGridLayout,QPushButton,QCheckBox,
                             QRadioButton,QButtonGroup,QLineEdit,
                             QHBoxLayout)
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont,QFontDatabase

class Digitalclock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.label_time = QLabel(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setGeometry(320,300,700,500)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_time)
        self.setLayout(vbox)
        self.label_time.setAlignment(Qt.AlignCenter)
        self.label_time.setStyleSheet("color:#bfab75")
        self.setStyleSheet("background-color:black")

        font_id = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font_choice = QFont(font_family,150)
        self.label_time.setFont(font_choice)


        self.update_time()

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)



    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.label_time.setText(current_time)






def main():
    app = QApplication(sys.argv)
    clock = Digitalclock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()