from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from inst import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
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
        self.result_label = QLabel(txt_workheart + self.results())
        self.message_label = QLabel(txt_index + str(self.index))
        self.line = QVBoxLayout()
        self.line.addWidget(self.result_label, alignment = Qt.AlignCenter)
        self.line.addWidget(self.message_label, alignment = Qt.AlignCenter)
        self.setLayout(self.line)
        #pass

    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "there is no data for this age"
        
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        #ou
        # self.index = 4 * int(self.exp.t1) + 4 * int(self.exp.t2) + 4 * int(self.exp.t3)
        # self.index = self.index - 200
        # self.index = self.index / 10
        print(self.index)
        
        #resultados para idades iguais ou maiores que 15 anos
        if self.exp.age >= 15:
            if self.index >=15:
                return txt_res1
            elif self.index <= 14.9 and self.index >= 11:
                return txt_res2
            elif self.index <= 10.9 and self.index >= 6:
                return txt_res3
            elif self.index <= 5.9 and self.index >= 0.5:
                return txt_res4
            elif self.index <= 0.4:
                return txt_res5
        
        #resultados para idades iguais a 13 ou 14 anos
        elif self.exp.age == 13 or self.exp.age == 14:
            if self.index >=16.5:
                return txt_res1
            elif self.index <= 16.4 and self.index >= 12.5:
                return txt_res2
            elif self.index <= 12.4 and self.index >= 7.5:
                return txt_res3
            elif self.index <= 7.4 and self.index >= 2:
                return txt_res4
            elif self.index <= 1.9:
                return txt_res5
        
        #resultados para idades iguais a 11 ou 12 anos
        elif self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index <= 17.9 and self.index >= 14:
                return txt_res2
            elif self.index <= 13.9 and self.index >= 9:
                return txt_res3
            elif self.index <= 8.9 and self.index >= 3.5:
                return txt_res4
            elif self.index <= 3.4:
                return txt_res5

        #resultados para idades iguais a 9 ou 10 anos
        elif self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index <= 19.4 and self.index >= 15.5:
                return txt_res2
            elif self.index <= 15.4 and self.index >= 10.5:
                return txt_res3
            elif self.index <= 10.4 and self.index >= 5:
                return txt_res4
            elif self.index <= 4.9:
                return txt_res5

        #resultados para idades iguais a 7 ou 8 anos
        elif self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index <= 20.9 and self.index >= 17:
                return txt_res2
            elif self.index <= 16.9 and self.index >= 12:
                return txt_res3
            elif self.index <= 11.9 and self.index >= 5.5:
                return txt_res4
            elif self.index <= 6.4:
                return txt_res5