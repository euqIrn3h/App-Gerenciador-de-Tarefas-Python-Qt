from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication, QPoint
from PySide6.QtWidgets import *
from layout.layout import  Ui_ToDo
import sys
import datetime
from api import *
import sqlite3 as sq
from database.database import *
import pyperclip as pc


class MainJanela(Ui_ToDo,QMainWindow):
    def __init__(self) -> None:
        super(MainJanela,self).__init__()
        self.setupUi(self)

        #instacia todas as pages e atributos que necessitam de carregar dados do bd ou API
        self.bd = Database()
        self.bd.connect()
        self.api = Clima()
        self.data = str(datetime.date.today())
        self.data = str(self.data[8:]+"/"+self.data[5:7]+"/"+self.data[0:4])
        self.hora = str(datetime.datetime.now().time())
        self.hora = self.hora[:5]
        self.home()
        self.setHeader()
        

        # aciona o botao para abrir o menu
        self.pbtoogle.clicked.connect(self.leftMenu)
        
        #Botoes do menu
        self.pbhome.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpghome))
        self.pbhome.clicked.connect(self.home)

        self.pbtarefasdiarias.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpgtarefasdiarias))
        self.pbtarefasdiarias.clicked.connect(self.tarefasdiarias)

        self.pbgastos.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpggastos))
        self.pbcalendario.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpgcalendario))

        self.maincalendariocalendario.clicked.connect(self.calendario)

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


        tarefas = self.bd.listar_Tarefas('2022-01-20')   #str(datetime.date.today())
        essencial=0
        concluidas=0
        essencialconcluida=0
        for i in range(len(tarefas)):
            if tarefas[i][3] == 1:
                concluidas +=1
            if tarefas[i][2] == 2:
                essencial+=1
                if tarefas[i][3] == 1:
                    essencialconcluida+=1

        if concluidas/(len(tarefas)) < 0.5:
            self.mainhometarconcluida.setStyleSheet("QLabel {background-color:rgb(255,150,0)}")
        elif concluidas/(len(tarefas)) < 0.3:
            self.mainhometarconcluida.setStyleSheet("QLabel {background-color:rgb(255,50,0);color:white;}")

        if essencialconcluida/essencial < 0.5:
            self.mainhometaressencialconluida.setStyleSheet("QLabel {background-color:rgb(255,150,0)}")
        elif essencialconcluida/essencial < 0.3:
            self.mainhometaressencialconluida.setStyleSheet("QLabel {background-color:rgb(255,50,0);color:white;}")

        self.mainhometarefasdiarias.setText(str(len(tarefas)))
        self.mainhometarconcluida.setText(str(concluidas))
        self.mainhometarfaltando.setText(str(len(tarefas)-concluidas))
        self.mainhometaressencial.setText(str(essencial))
        self.mainhometaressencialconluida.setText(str(essencialconcluida))
    
    def tarefasdiarias(self):
        
        tarefas = self.bd.listar_Tarefas('2022-01-20')#str(datetime.date.today())

        self.maintarefasdiariastab.clearContents()
        self.maintarefasdiariastab.setColumnCount(1)
        self.maintarefasdiariastab.setHorizontalHeaderItem(0,QTableWidgetItem('Tarefa Diária'))
        self.maintarefasdiariastab.setColumnWidth(0,self.maintarefasdiariastab.width()-40)
        
        
        linhas = 0
        for i in range(len(tarefas)):
            if tarefas[i][3] == 0:
                self.maintarefasdiariastab.insertRow(linhas)

                tarefa=QTextEdit()
                tarefa.setReadOnly(True)
                tarefa.setText(tarefas[i][1])

                if tarefas[i][2] == 2:
                    tarefa.setStyleSheet("QTextEdit {background-color:rgb(255, 155, 155);}")
                elif tarefas[i][2] == 1:
                    tarefa.setStyleSheet("QTextEdit {background-color:rgb(255, 200, 155);}")

                self.maintarefasdiariastab.setVerticalHeaderItem(linhas,QTableWidgetItem(tarefas[i][0][11:]))
                self.maintarefasdiariastab.setCellWidget(linhas,0,tarefa)

                linhas+=1
        
    def tarefas(self,data):
        self.mainpages.setCurrentWidget(self.mainpgtarefas)
        self.maintarefaslbldia.setText(data)  
        
        ano=int(data[:4])
        anoatual=int(str(datetime.date.today())[:4])
        mes=int(data[5:7])
        mesatual=int(str(datetime.date.today())[5:7])
        dia=int(data[8:])
        diaatual=int(str(datetime.date.today())[8:])

        if ano == anoatual and mes == mesatual:
            if dia >= diaatual and dia-diaatual <10:
                self.maintarefaslblmaxmin.setText("{} ℃ / {} ℃".format(self.api[3][dia-diaatual]['max'],self.api[3][dia-diaatual]['min']))
                self.maintarefaslbldescricao.setText(self.api[3][dia-diaatual]['description'])
        else:
            self.maintarefaslblmaxmin.setText('Sem Prev')
            self.maintarefaslbldescricao.setText('Sem Prev')

        for i in range(self.maintarefastab.rowCount()):
            self.maintarefastab.removeRow(i)

        if data < str(datetime.date.today()):
            self.maintarefaslblmaxmin.setText('')
            self.maintarefaslbldescricao.setText('')

            self.maintarefastab.insertColumn(0)
            self.maintarefastab.setColumnWidth(0,self.maintarefastab.width()+50)
            self.maintarefastab.setHorizontalHeaderItem(0,QTableWidgetItem('ERRO'))
            self.maintarefastab.insertRow(0)

            erro = QLabel()
            erro.setText(f"SELECIONAR UMA DATA MAIOR OU IGUAL A {self.data}")
            erro.setStyleSheet('QLabel {background-color:red;color:white;font:bold;}')

            self.maintarefastab.setCellWidget(0,0,erro)

            self.maintarefaspbalterar.setEnabled(False)
            self.maintarefaspbcadastrar.setEnabled(False)
            
        else:
            self.maintarefaspbalterar.setEnabled(True)
            self.maintarefaspbcadastrar.setEnabled(True)

            tarefas = self.bd.listar_Tarefas('2022-01-20')#str(datetime.date.today())

            self.maintarefastab.clearContents()
            self.maintarefastab.setColumnCount(1)
            self.maintarefastab.setHorizontalHeaderItem(0,QTableWidgetItem('Tarefa Diária'))
            self.maintarefastab.setColumnWidth(0,self.maintarefastab.width()-40)
            
            
            linhas = 0
            for i in range(len(tarefas)):
                if tarefas[i][3] == 0:
                    self.maintarefastab.insertRow(linhas)

                    tarefa=QTextEdit()
                    tarefa.setReadOnly(True)
                    tarefa.setText(tarefas[i][1])

                    if tarefas[i][2] == 2:
                        tarefa.setStyleSheet("QTextEdit {background-color:rgb(255, 155, 155);}")
                    elif tarefas[i][2] == 1:
                        tarefa.setStyleSheet("QTextEdit {background-color:rgb(255, 200, 155);}")

                    self.maintarefastab.setVerticalHeaderItem(linhas,QTableWidgetItem(tarefas[i][0][11:]))
                    self.maintarefastab.setCellWidget(linhas,0,tarefa)

                    linhas+=1


        

    def calendario(self):
        data = self.maincalendariocalendario.selectedDate()
        
        if data.day() < 10:
            dia = f'0{str(data.day())}'
        else:
            dia = data.day()
        
        if data.month() < 10:
            mes = f'0{str(data.month())}'
        else:
            mes = data.month()

        self.tarefas(f"{str(data.year())}-{mes}-{dia}")



if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainJanela()
    window.show()
    app.exec()

    