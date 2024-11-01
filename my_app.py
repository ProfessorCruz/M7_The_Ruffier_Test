from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from inst import *
from second_win import *

#txt_title = 'The Ruffier Test'
#win_x , win_y = 200,100
#win_width, win_height = 1000, 600

#txt_hello = 'Welcome to the Health status detection program!'
#txt_instruction = 'This application allows you to use the Rufier test for...'
#txt_next = 'Start'

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() #define como a janela aparecerá
        self.initUI() #cria e configura os elementos gráficos
        self.connects() #estabelece as conexões entre os elementos
        self.show() #exibe a janela

    def set_appear(self):
        self.setWindowTitle(txt_title) #adiciona um nome a janela
        self.resize(win_width, win_height) #redimensiona a janela
        self.move(win_x,win_y) #faz a janela aparecer em um ponto específico
        #pass

    def initUI(self):
        #descrição dos elementos da interface
        self.hello_text = QLabel(txt_hello)#cria uma label
        self.instruction = QLabel(txt_instruction)#cria uma inscrição
        self.button = QPushButton(txt_next) #cria um botão
        self.layout_ = QVBoxLayout() #cria um layout
        self.layout_.addWidget(self.hello_text, alignment = Qt.AlignLeft) #adiciona uma label no layout
        self.layout_.addWidget(self.instruction, alignment = Qt.AlignLeft) #adiciona uma inscricão no layout
        self.layout_.addWidget(self.button, alignment = Qt.AlignCenter) #adiciona um botão no layout
        self.setLayout(self.layout_)
        #pass

    def connects(self): #manipula o evento click conectando a função com um botão
        self.button.clicked.connect(self.next_click)
        #pass
    
    def next_click(self): #processamento do botão: esconde a janela atual e cria a nova janela
        self.hide() #oculta a janela atual, é o inverso de window.show()
        self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec()