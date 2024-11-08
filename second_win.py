from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
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
        #timer_label_font = QFont("Times",36,QFont.Bold)
        #self.timer_label.setFont(timer_label_font)
        #self.timer_label.setStyleSheet("color: rgb(0,0,0)")
        self.timer_label.setStyleSheet("color: black; font-size: 48px; font-family: Times;font-weight: bold;")
        
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
    
    def timer_test(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString("hh:mm:ss"))
        self.timer_label.setFont(QFont("Times",36,QFont.Bold))
        self.timer_label.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        #pass
    
    def timer_sits(self):
        global time
        time = QTime(0,0,30) #timer definido em 30 segundos
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500) #um agachamento a cada 1.5 segundos
    
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString("hh:mm:ss")[6:8])
        self.timer_label.setFont(QFont("Times",36,QFont.Bold))
        self.timer_label.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer_final(self):
        global time
        time = QTime(0,0,5) #timer definido em 1 minuto
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000) #atualização a cada segundo
    
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString("hh:mm:ss"))
        self.timer_label.setFont(QFont("Times",36,QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.timer_label.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.timer_label.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.timer_label.setStyleSheet("color: rgb(0,0,0)")
            
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def connects(self): #manipula o evento click conectando a função com um botão
        self.results_button.clicked.connect(self.next_click)
        
        self.test_button1.clicked.connect(self.timer_test)
        
        self.test_button2.clicked.connect(self.timer_sits)
        
        self.test_button3.clicked.connect(self.timer_final)
        #pass
    
    def next_click(self): #processamento do botão: esconde a janela atual e cria a nova janela
        self.hide() #oculta a janela atual, é o inverso de window.show()
        self.tw = FinalWin()

    
#incluídos para a realização de testes diretos na segunda janela
#app = QApplication([])
#mw = TestWin()
#app.exec()