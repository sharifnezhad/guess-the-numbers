from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from random import randint
import sys

class Select_game(QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load('select-game.ui',None)
        self.ui.show()
        self.select_list=[None for x in range(3)]
        self.select_list[0]=self.ui.btn_1to10
        self.select_list[1]=self.ui.btn_1to100
        self.select_list[2]=self.ui.btn_500
        for i in range(len(self.select_list)):
            self.select_list[i].clicked.connect(self.secend_window)
    def secend_window(self, checked):
        self.ui=Guess_the_numbers(self.sender().objectName())

class Guess_the_numbers(QWidget):
    def __init__(self,btn_name):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('guess-the-numbers.ui', None)
        self.ui.show()
        self.random_number=0
        if btn_name=='btn_1to10': self.random_number=randint(1,10)
        elif btn_name=='btn_1to100': self.random_number=randint(1,100)
        else: self.random_number=randint(-500,500)
        self.ui.btn_back.clicked.connect(self.new_game)
        self.ui.user_number.returnPressed.connect(self.check_number)
    def new_game(self):
        self.ui=Select_game()
    def check_number(self):
        if int(self.ui.user_number.text())>self.random_number:
            self.ui.help_message.setText('lower your number')
        if int(self.ui.user_number.text()) < self.random_number:
            self.ui.help_message.setText('increase your number')
        if int(self.ui.user_number.text()) == self.random_number:
            self.ui.help_message.setText('good job')
            self.ui.user_number.setReadOnly(True)


app=QApplication(sys.argv)
window=Select_game()

app.exec()