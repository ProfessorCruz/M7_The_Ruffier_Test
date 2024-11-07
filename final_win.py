from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from inst import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        #self.connects() #não há botões de navegação nesta janela.
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title) #adiciona um nome a janela
        self.resize(win_width, win_height) #redimensiona a janela
        self.move(win_x,win_y) #faz a janela aparecer em um ponto específico 
        #pass

    def initUI(self):
        self.result_label = QLabel('Result')
        self.message_label = QLabel('Message')
        self.line = QVBoxLayout()
        self.line.addWidget(self.result_label, alignment = Qt.AlignCenter)
        self.line.addWidget(self.message_label, alignment = Qt.AlignCenter)
        self.setLayout(self.line)

