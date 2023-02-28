# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from instr import *


class Final(QWidget):

    def __init__(self, index, heartwork):
        super().__init__()
        self.index = index
        self.heartwork = heartwork
        self.set_appear()
        self.initUI()
        self.show()
    
    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_finalwin)

    def initUI(self):
        self.title = QLabel(txt_index + str(self.index))
        self.title2 = QLabel(txt_workheart + str(self.heartwork))

        lan = QVBoxLayout()
        lan.addWidget(self.title, alignment=Qt.AlignCenter)
        lan.addWidget(self.title2, alignment=Qt.AlignCenter)

        self.setLayout(lan)
