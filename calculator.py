# Calculator app


import sys
import requests

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QPushButton, QCheckBox,
                             QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, )
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator app")
        self.setWindowIcon(QIcon("charlesdeluvio-GlavtG-umzE-unsplash.jpg"))
        self.setGeometry(700, 50, 600, 1000)
        self.expression = ""
        self.initUI()



    def initUI(self):
        #display box
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setGeometry(0,0,600,100)


        # number buttons

        self.button1 = QPushButton("1",self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.button4 = QPushButton("4", self)
        self.button5 = QPushButton("5", self)
        self.button6 = QPushButton("6", self)
        self.button7 = QPushButton("7", self)
        self.button8 = QPushButton("8", self)
        self.button9 = QPushButton("9", self)
        self.button0 = QPushButton("0", self)

        # operators buttons
        self.equals_to = QPushButton("=",self)
        self.decimal = QPushButton(".",self)
        self.backspace = QPushButton("⌫",self)
        self.clear = QPushButton("C",self)
        self.add = QPushButton("+",self)
        self.subtract = QPushButton("-",self)
        self.multiply = QPushButton("x",self)
        self.divide = QPushButton("÷",self)
        self.remainder = QPushButton("%",self)
        self.square = QPushButton("x²",self)



        grid = QGridLayout()

        grid.addWidget(self.clear,0,0)
        grid.addWidget(self.backspace,0,1)
        grid.addWidget(self.remainder,0,2)
        grid.addWidget(self.divide,0,3)
        grid.addWidget(self.button1,1,0)
        grid.addWidget(self.button2,1,1)
        grid.addWidget(self.button3,1,2)
        grid.addWidget(self.add,1,3)
        grid.addWidget(self.button4,2,0)
        grid.addWidget(self.button5,2,1)
        grid.addWidget(self.button6,2,2)
        grid.addWidget(self.subtract,2,3)
        grid.addWidget(self.button7,3,0)
        grid.addWidget(self.button8,3,1)
        grid.addWidget(self.button9,3,2)
        grid.addWidget(self.multiply,3,3)
        grid.addWidget(self.square,4,0)
        grid.addWidget(self.decimal,4, 1)
        grid.addWidget(self.button0,4,2)
        grid.addWidget(self.equals_to,4,3)

        self.setLayout(grid)
        grid.setSpacing(0)


        #display box continue

        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0,0,0,0)

        vbox.addWidget(self.display)

        self.setLayout(vbox)

        self.setStyleSheet("""
        QWidget{
        background-color:black;
        }
        QPushButton{
        padding:25px;
        font-size:25px;
        background-color:#568896;
        color:#b0cad1;
        }
        QLineEdit{
        background-color:#568896;
        font-size:25px;
        color:#b0cad1;
        }
        """)



        self.button1.clicked.connect(lambda: self.pressed("1"))
        self.button2.clicked.connect(lambda: self.pressed("2"))
        self.button3.clicked.connect(lambda :self.pressed("3"))
        self.button4.clicked.connect(lambda: self.pressed("4"))
        self.button5.clicked.connect(lambda :self.pressed("5"))
        self.button6.clicked.connect(lambda: self.pressed("6"))
        self.button7.clicked.connect(lambda: self.pressed("7"))
        self.button8.clicked.connect(lambda: self.pressed("8"))
        self.button9.clicked.connect(lambda: self.pressed("9"))
        self.button0.clicked.connect(lambda: self.pressed("0"))

        #Operators

        self.add.clicked.connect(lambda :self.pressed("+"))
        self.subtract.clicked.connect(lambda: self.pressed("-"))
        self.multiply.clicked.connect(lambda: self.pressed("*"))
        self.divide.clicked.connect(lambda: self.pressed("/"))
        self.square.clicked.connect(lambda : self.pressed ("**2"))
        self.remainder.clicked.connect(lambda: self.pressed("%"))
        self.decimal.clicked.connect(lambda: self.pressed("."))

        #Other operators

        self.equals_to.clicked.connect(lambda : self.calculate())
        self.backspace.clicked.connect(lambda: self.do_backspace())
        self.clear.clicked.connect(lambda: self.clear_space())



    def pressed(self, value):
        self.expression += value
        self.display.setText(self.expression)



    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.setText(str(result))
            self.expression = str(result)

        except:
            self.display.setText("error")
            self.expression = ""


    def do_backspace(self):
        self.expression = self.expression[:-1]
        self.display.setText(self.expression)

    def clear_space(self):
        self.expression = ""
        self.display.setText(self.expression)


def main():
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()