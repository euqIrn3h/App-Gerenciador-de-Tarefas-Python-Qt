from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication, QPoint
from PySide6.QtWidgets import *
from layout.layout import  Ui_ToDo
import sys
import datetime
from api import *
import sqlite3 as sq

class MainJanela(Ui_ToDo,QMainWindow):
    def __init__(self) -> None:
        super(MainJanela,self).__init__()
        self.setupUi(self)

        #instacia todas as pages e atributos que necessitam de carregar dados do bd ou API
        self.api = Clima()
        self.data = str(datetime.date.today())
        self.data = str(self.data[8:]+"-"+self.data[5:7]+"-"+self.data[0:4])
        self.hora = str(datetime.datetime.now().time())
        self.hora = self.hora[:5]
        self.home()
        self.setHeader()

        # aciona o botao para abrir o menu
        self.pbtoogle.clicked.connect(self.leftMenu)
        
        #Botoes do menu
        self.pbhome.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpghome))
        self.pbhome.clicked.connect(self.home)

        self.pbtarefas.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpgtarefas))
        self.pbtarefas.clicked.connect(self.tarefas)

        self.pbcontas.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpgcontas))
        self.pbcalendario.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpgcalendario))

    def setHeader(self):
        self.headerlbldia.setText(self.data)
        self.headerlblhorario.setText(self.hora)
        self.headerlbltemperatura.setText(str(self.api[1])+" ℃")
        
    def leftMenu(self):
        x = self.lcontainer.width()

        if x == 0:
            nx = 130
            self.pbtoogle.setText("<<<")
        else:
            nx = 0
            self.pbtoogle.setText(">>>")

        self.animation = QtCore.QPropertyAnimation(self.lcontainer,b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(x)
        self.animation.setEndValue(nx)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def home(self):
        
        self.mainhomecidade.setText(str(self.api[0]))
        self.mainhomedata.setText(self.data)
        self.mainhometemperatura.setText(str(self.api[1])+" ℃")
        self.mainhomeclima.setText(str(self.api[2]))
        self.mainhomemaxmin.setText("{} ℃ / {} ℃".format(self.api[3][0]['max'],self.api[3][0]['min']))
        self.mainhometarconcluida.setText("")
        self.mainhometarfaltando.setText("")
        self.mainhometaressencial.setText("")
        self.mainhometaressencialconluida.setText("")

    def tarefas(self):
        pass

if __name__ == "__main__":

    
    app = QApplication(sys.argv)
    window = MainJanela()
    window.show()
    app.exec()