# TIC_TAC-TOE GAME


import sys
from operator import truediv

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QPushButton, QCheckBox,
                             QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, )
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QSizePolicy


class tic_tac_toe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("demonscollector-tic-tac-toe-7737546.jpg"))
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(600, 100, 800, 800)
        self.board = [""] * 9
        self.player = "x"
        self.game_over = False
        self.winning_combo = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        self.initUI()

    def initUI(self):

        self.reset_button = QPushButton("RESET", self)

        self.button1 = QPushButton("", self)
        self.button2 = QPushButton("", self)
        self.button3 = QPushButton("", self)
        self.button4 = QPushButton("", self)
        self.button5 = QPushButton("", self)
        self.button6 = QPushButton("", self)
        self.button7 = QPushButton("", self)
        self.button8 = QPushButton("", self)
        self.button9 = QPushButton("", self)

        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.label = QLabel("Turn: x")
        self.label.setAlignment(Qt.AlignCenter)

        grid_box = QGridLayout()

        grid_box.addWidget(self.button1, 0, 0)
        grid_box.addWidget(self.button2, 0, 1)
        grid_box.addWidget(self.button3, 0, 2)
        grid_box.addWidget(self.button4, 1, 0)
        grid_box.addWidget(self.button5, 1, 1)
        grid_box.addWidget(self.button6, 1, 2)
        grid_box.addWidget(self.button7, 2, 0)
        grid_box.addWidget(self.button8, 2, 1)
        grid_box.addWidget(self.button9, 2, 2)

        grid_box.setSpacing(0)
        grid_box.setContentsMargins(0, 0, 0, 0)

        vbox = QVBoxLayout()
        vbox.addWidget(self.reset_button)
        vbox.addWidget(self.label)
        vbox.addLayout(grid_box)
        self.setLayout(vbox)

        self.button1.clicked.connect(lambda: self.clicked(0))
        self.button2.clicked.connect(lambda: self.clicked(1))
        self.button3.clicked.connect(lambda: self.clicked(2))
        self.button4.clicked.connect(lambda: self.clicked(3))
        self.button5.clicked.connect(lambda: self.clicked(4))
        self.button6.clicked.connect(lambda: self.clicked(5))
        self.button7.clicked.connect(lambda: self.clicked(6))
        self.button8.clicked.connect(lambda: self.clicked(7))
        self.button9.clicked.connect(lambda: self.clicked(8))
        self.reset_button.clicked.connect(lambda: self.restart_game())

        self.setStyleSheet("""
        QPushButton{
        background-color:white;
        font-family:arial;
        color:green;
        font-size:100px;
        border: 2px solid black;
        }
        QPushButton:hover{
        background-color:cyan;
        }
        QLabel{
        color:black;
        font-size:40px;
        }

        """)

        self.buttons = [self.button1, self.button2, self.button3,
                        self.button4, self.button5, self.button6,
                        self.button7, self.button8, self.button9]

    def clicked(self, index):
        if self.game_over:
            return

        if self.board[index] != "":
            return
        self.board[index] = self.player
        self.buttons[index].setText(self.player)
        if self.Check_winner():
            self.label.setText(f"{self.player} won!")
            self.game_over = True
            return
        if "" not in self.board:
            self.label.setText("Its a tie!")
            self.game_over = True
            return

        self.Switch_turn()
        self.label.setText(f"turn: {self.player.upper()}")

    def Check_winner(self):
        for combos in self.winning_combo:
            a, b, c = combos

            if self.board[a] != "" and self.board[a] == self.board[b] == self.board[c]:
                return True

        return False

    def Switch_turn(self):
        if self.player == "x":
            self.player = "o"
        else:
            self.player = "x"

    def restart_game(self):
        self.board = [""] * 9
        self.player = "x"
        self.game_over = False
        for button in self.buttons:
            button.setText("")

        self.label.setText("Turn:x")


def main():
    app = QApplication(sys.argv)
    tic = tic_tac_toe()
    tic.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
