# STOPWATCH PROGRAM


import sys
from wsgiref.util import application_uri

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QPushButton, QCheckBox,
                             QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, )
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase


class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00")
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.setGeometry(600, 300, 800, 500)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop watch")
        self.setWindowIcon(QIcon("william-warby-VwqMTcsb0Tg-unsplash.jpg"))

        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
        QPushButton{
        font-size:50px;
        font-style:italic;
        padding:20px;
        color:#03ff24; 
        background-color:black;
        }
        QLabel{
        font-size:150px;
        color:hsl(128, 100%, 51%);
        font-style:italic;
        background-color:hsl(128, 3%, 5%);
        }
         QPushButton:hover{
        font-size:50px;
        font-style:italic;
        color:#03ff24; 
        background-color:hsl(120, 4%, 80%)

        }



        """)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.start_button.clicked.connect(self.start_stopwatch)
        self.stop_button.clicked.connect(self.Stop_stopwatch)
        self.reset_button.clicked.connect(self.reset_stopwatch)
        self.timer.timeout.connect(self.update_dsplay)

    def start_stopwatch(self):
        self.timer.start(10)

    def Stop_stopwatch(self):
        self.timer.stop()

    def reset_stopwatch(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_stopwatch_time(self.time))

    def format_stopwatch_time(self, time):
        hours = time.hour()
        min = time.minute()
        sec = time.second()
        milisec = time.msec() // 10

        return f"{hours:02}:{min:02}:{sec:02}:{milisec:02}"

    def update_dsplay(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_stopwatch_time(self.time))


def main():
    app = QApplication(sys.argv)
    clock = stopwatch()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()