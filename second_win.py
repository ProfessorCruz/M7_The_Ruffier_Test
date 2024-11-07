from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from inst import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        #pass
        
    def set_appear(self):
        self.setWindowTitle(txt_title) #adiciona um nome a janela
        self.resize(win_width, win_height) #redimensiona a janela
        self.move(win_x,win_y) #faz a janela aparecer em um ponto específico 
        #pass
    
    def initUI(self):
        #widgets
        self.name_label = QLabel('Enter Your Full Name')
        self.name_line = QLineEdit('Full name')
        
        self.years_label = QLabel('Full years')
        self.years_line = QLineEdit('0')
        
        self.test_label1 = QLabel('Lie on your back and take your pulse for 15 seconds. Click the "Start first test" button to start the timer.\nWrite down the result in the appropriate field.')
        self.test_button1 = QPushButton('Start first test')
        self.test_line1 = QLineEdit('0')
        
        self.test_label2 = QLabel('Perform 30 squats in 45 seconds. To do this, click the "Start doing squats" button to start the squat counter.')
        self.test_button2 = QPushButton('Start doing squats')
        
        self.test_label3 = QLabel('Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute.\nPress the "Start final test" button to start the timer.\nThe seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black.\nWrite down the results in the appropriate fields.')
        self.test_button3 = QPushButton('Start the final test')
        self.test_line2 = QLineEdit('0')
        self.test_line3 = QLineEdit('0')
        
        self.timer_label = QLabel('00:00:00')
        
        self.results_button = QPushButton('Send the results')
        
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        
        #add widgets a self.l_line
        self.l_line.addWidget(self.name_label, alignment = Qt.AlignLeft) #adiciona uma label no layout vertical no lado esquerdo
        self.l_line.addWidget(self.name_line, alignment = Qt.AlignLeft) #adiciona uma linha no layout vertical no lado esquerdo
        self.l_line.addWidget(self.years_label, alignment = Qt.AlignLeft) #adiciona uma label no layout vertical no lado esquerdo
        self.l_line.addWidget(self.years_line, alignment = Qt.AlignLeft) #adiciona uma linha no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_label1, alignment = Qt.AlignLeft) #adiciona uma label no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_button1, alignment = Qt.AlignLeft) #adiciona um botão no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_line1, alignment = Qt.AlignLeft) #adiciona uma linha no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_label2, alignment = Qt.AlignLeft) #adiciona uma label no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_button2, alignment = Qt.AlignLeft) #adiciona um botão no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_label3, alignment = Qt.AlignLeft) #adiciona uma label no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_button3, alignment = Qt.AlignLeft) #adiciona um botão no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_line2, alignment = Qt.AlignLeft) #adiciona uma linha no layout vertical no lado esquerdo
        self.l_line.addWidget(self.test_line3, alignment = Qt.AlignLeft) #adiciona uma linha no layout vertical no lado esquerdo
        self.l_line.addWidget(self.results_button, alignment = Qt.AlignRight) #adiciona um botão no layout vertical no lado esquerdo
        
        #add widgets a self.r_line
        self.r_line.addWidget(self.timer_label, alignment = Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
        #pass
    
    def connects(self): #manipula o evento click conectando a função com um botão
        self.results_button.clicked.connect(self.next_click)
        #pass
    
    def next_click(self): #processamento do botão: esconde a janela atual e cria a nova janela
        self.hide() #oculta a janela atual, é o inverso de window.show()
        self.tw = FinalWin()

app = QApplication([])
mw = TestWin()
app.exec()