from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from final_win import Final
from instr import *

class second_win(QWidget):
    
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
    
    def initUI(self):
        lay = QVBoxLayout()
        self.name = QLabel(txt_name)
        self.nameline = QLineEdit(placeholderText=txt_hintname)
        self.title_age = QLabel(txt_hintage)
        self.ageline = QLineEdit(placeholderText=txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.button = QPushButton(txt_starttest1)
        self.puls = QLineEdit(placeholderText=txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.button2 = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.button3 = QPushButton(txt_starttest3)
        self.test3Line = QLineEdit(placeholderText=txt_hinttest1)
        self.test3Line2 = QLineEdit(placeholderText=txt_hinttest1)


        lay.addWidget(self.name)
        lay.addWidget(self.nameline, alignment= Qt.AlignLeft)
        lay.addWidget(self.title_age)
        lay.addWidget(self.ageline, alignment= Qt.AlignLeft)
        lay.addWidget(self.test1)
        lay.addWidget(self.button, alignment= Qt.AlignLeft)
        lay.addWidget(self.puls, alignment= Qt.AlignLeft)
        lay.addWidget(self.test2)
        lay.addWidget(self.button2, alignment= Qt.AlignLeft)
        lay.addWidget(self.test3)
        lay.addWidget(self.button3, alignment= Qt.AlignLeft)
        lay.addWidget(self.test3Line, alignment= Qt.AlignLeft)
        lay.addWidget(self.test3Line2, alignment= Qt.AlignLeft)

        lay1 = QVBoxLayout()
        self.timer_text = QLabel("00:00:00")
        self.timer_text.setFont(QFont('Arial', 36))
        self.button4 = QPushButton(txt_sendresults)

        lay1.addWidget(self.timer_text)
        lay1.addWidget(self.button4, alignment = Qt.AlignLeft)

        line = QHBoxLayout()
        line.addLayout(lay)
        line.addLayout(lay1)

        self.setLayout(line)
    
    def connects(self):
        self.button.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_test2)
        self.button3.clicked.connect(self.timer_test3)
        self.button4.clicked.connect(self.next_win)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_text.setText(time.toString("hh:mm:ss"))
        self.timer_text.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_test2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_text.setText(time.toString("ss"))
        self.timer_text.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("ss") == "00":
            self.timer.stop()

    def timer_test3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_text.setText(time.toString("hh:mm:ss"))
        self.timer_text.setStyleSheet("color: rgb(0, 0, 0)")
        if int(time.toString("ss")) >= 45 or int(time.toString("ss")) <=15:
            self.timer_text.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.timer_text.setStyleSheet("color: rgb(0, 0, 0)")

        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def next_win(self):
        age = int(self.ageline.text())
        test1 = int(self.puls.text())
        test2 = int(self.test3Line.text())
        test3 = int(self.test3Line2.text())
        index = (4*(test1+test2+test3)-200)/10
        if age in [7, 8]:
            if index >= 21:
                heartwork = "Низкая"
            elif index >= 17 and index < 21:
                heartwork = "Удовлетворительная"
            elif index >= 12 and index < 17:
                heartwork = "Средне"
            elif index >= 6.5 and index < 12:
                heartwork = "Выше среднего"
            else:
                heartwork = "Высокий"
        if age in [9, 10]:
            if index >= 19.5:
                heartwork = "Низкая"
            elif index >= 15.5 and index < 19.5:
                heartwork = "Удовлетворительная"
            elif index >= 10.5 and index < 15.5:
                heartwork = "Средне"
            elif index >= 5 and index < 10.5:
                heartwork = "Выше среднего"
            else:
                heartwork = "Высокий"
        if age in [11, 12]:
            if index >= 18:
                heartwork = "Низкая"
            elif index >= 14 and index < 18:
                heartwork = "Удовлетворительная"
            elif index >= 9 and index < 14:
                heartwork = "Средне"
            elif index >= 3.5 and index < 9:
                heartwork = "Выше среднего"
            else:
                heartwork = "Высокий"
        if age in [13, 14]:
            if index >= 16.5:
                heartwork = "Низкая"
            elif index >= 12.5 and index < 16.5:
                heartwork = "Удовлетворительная"
            elif index >= 7.5 and index < 12.5:
                heartwork = "Средне"
            elif index >= 2 and index < 7.5:
                heartwork = "Выше среднего"
            else:
                heartwork = "Высокий"
        if age >= 15:
            if index >= 15:
                heartwork = "Низкая"
            elif index >= 11 and index < 15:
                heartwork = "Удовлетворительная"
            elif index >= 6 and index < 11:
                heartwork = "Средне"
            elif index >= 0.5 and index < 6:
                heartwork = "Выше среднего"
            else:
                heartwork = "Высокий"
        self.hide()
        self.w = Final(index, heartwork)

app = QApplication([])    
win = second_win()
app.exec_()