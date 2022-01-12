from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication, QDate, QPoint, QSize, QTime
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import *
from layout.layout import  Ui_ToDo
import sys
import datetime
from api import *
import sqlite3 as sq
from database.database import *
import pyperclip as pc
import os


class MainJanela(Ui_ToDo,QMainWindow):
    def __init__(self) -> None:
        super(MainJanela,self).__init__()
        self.setupUi(self)

        #instacia todas as pages e atributos que necessitam de carregar dados do bd ou API
        self.bd = Database()
        self.bd.connect()
        self.api = Clima()
        self.data = str(datetime.date.today())
        self.data = str(self.data[8:]+"/"+self.data[5:7]+"/"+self.data[:4])
        self.hora = str(datetime.datetime.now().time())
        self.hora = self.hora[:5]
        self.home()
        self.set_Header()
        

        # aciona o botao para abrir o menu
        self.pbtoogle.clicked.connect(self.left_Menu)
        
        #Botoes do menu
        self.pbhome.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpghome))
        self.pbhome.clicked.connect(self.home)

        self.pbtarefasdiarias.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpgtarefasdiarias))
        self.pbtarefasdiarias.clicked.connect(self.tarefas_diarias)

        self.pbgastos.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpggastos))
        self.pbgastos.clicked.connect(self.gastos)

        self.pbcalendario.clicked.connect(lambda: self.mainpages.setCurrentWidget(self.mainpgcalendario))

        self.maincalendariocalendario.clicked.connect(self.calendario)

        self.maintarefasdiariastab.itemSelectionChanged.connect(self.mostrar_botao_tarefaconcluida)
        self.maintarefasdiariaspbtarefaconcluida.clicked.connect(self.tarefa_concluida)

        self.maintarefastab.itemSelectionChanged.connect(self.mostrar_botao_alterar)

        self.maintarefaspbcadastrar.clicked.connect(self.mostrar_cadastrar_tarefa)
        self.maintarefaspbalterar.clicked.connect(self.mostrar_alterar_tarefa)
        self.maintarefaspbdeletar.clicked.connect(self.exclui_tarefa)

        self.maincadastrartarefapbsalvar.clicked.connect(self.cadastrar_tarefa)
        self.maincadastrartarefapbalterar.clicked.connect(self.alterar_tarefa)

        self.maingastostab.itemSelectionChanged.connect(self.mostrar_botao_gastos)
        
        self.maingastospbdeletar.clicked.connect(self.deletar_gasto)

        self.maingastospbcadastrar.clicked.connect(self.mostar_cadastro_gasto)
        self.maincadastrargastolegasto.textEdited.connect(self.mostrar_botao_gasto_salvar)
        self.maincadastrargastopbsalvar.clicked.connect(self.insere_gasto)

    def set_Header(self) -> None:
        self.headerlbldia.setText(self.data)
        self.headerlblhorario.setText(self.hora)
        self.headerlbltemperatura.setText(str(self.api[1])+" ℃")
        
    def left_Menu(self) -> None:
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

    def home(self) -> None:
        
        self.mainhomecidade.setText(str(self.api[0]))
        self.mainhomedata.setText(self.data)
        self.mainhometemperatura.setText(str(self.api[1])+" ℃")
        self.mainhomeclima.setText(str(self.api[2]))
        self.mainhomemaxmin.setText("{} ℃ / {} ℃".format(self.api[3][0]['max'],self.api[3][0]['min']))


        tarefas = self.bd.listar_Tarefas(str(datetime.date.today()))   #str(datetime.date.today())
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

        if len(tarefas):
            if concluidas/(len(tarefas)) < 0.3:
                self.mainhometarconcluida.setStyleSheet("QLabel {background-color:rgb(255,50,0);color:white;}")
            elif concluidas/(len(tarefas)) < 0.5:
                self.mainhometarconcluida.setStyleSheet("QLabel {background-color:rgb(255,150,0)}")

            if essencialconcluida/essencial < 0.3:
                self.mainhometaressencialconluida.setStyleSheet("QLabel {background-color:rgb(255,50,0);color:white;}")
            elif essencialconcluida/essencial < 0.5:
                self.mainhometaressencialconluida.setStyleSheet("QLabel {background-color:rgb(255,150,0)}")

        self.mainhometarefasdiarias.setText(str(len(tarefas)))
        self.mainhometarconcluida.setText(str(concluidas))
        self.mainhometarfaltando.setText(str(len(tarefas)-concluidas))
        self.mainhometaressencial.setText(str(essencial))
        self.mainhometaressencialconluida.setText(str(essencialconcluida))
        if len(tarefas):
            self.mainhomeprogressbar.setValue((concluidas/(len(tarefas)))*100)
        else:
            self.mainhomeprogressbar.setValue(100)

    def tarefas_diarias(self) -> None:
        tabela = self.maintarefasdiariastab
        tarefas = self.bd.listar_Tarefas(str(datetime.date.today()))
        
        self.maintarefasdiariasframepb.close()

        faltando = 0
        for i in range(len(tarefas)):
            if tarefas[i][3] == 0:
                faltando+=1

        tabela.setRowCount(faltando)
        tabela.setColumnCount(1)
        tabela.setHorizontalHeaderItem(0,QTableWidgetItem('Tarefa Diária'))
        

        linha = 0
        for i in range(len(tarefas)):
            if tarefas[i][3] == 0:

                tarefa=QTextEdit()
                tarefa.setMaximumHeight(60)            
                tarefa.setReadOnly(True)
                tarefa.setText(tarefas[i][1])

                if tarefas[i][2] == 2:
                    tarefa.setStyleSheet("QTextEdit {background-color:rgb(255, 155, 155);}")
                elif tarefas[i][2] == 1:
                    tarefa.setStyleSheet("QTextEdit {background-color:rgb(255, 200, 155);}")

                tabela.setVerticalHeaderItem(linha,QTableWidgetItem(tarefas[i][0][11:]))
                tabela.setCellWidget(linha,0,tarefa)

                linha+=1
        tabela.resizeColumnsToContents()

    def mostrar_botao_tarefaconcluida(self) -> None:
        self.maintarefasdiariasframepb.show()

    def tarefa_concluida(self) -> None:

        tabela = self.maintarefasdiariastab
        data = str(datetime.date.today())+" "+str(tabela.verticalHeaderItem(tabela.currentRow()).text())
        
        self.bd.concluir_Tarefa(data)
        self.tarefas_diarias()

    def tarefas(self,data) -> None:
        tabela = self.maintarefastab

        if data >= str(datetime.date.today()): 

            tarefas = self.bd.listar_Tarefas(data)
            faltando = 0
            self.mainpages.setCurrentWidget(self.mainpgtarefas)
            self.maintarefasframepb.close()
            self.maintarefasframepbcadastrar.show()
            

            self.maintarefaslbldia.setText('{}'.format(str(data[8:]+"/"+data[5:7]+"/"+data[:4])))  
            ano=int(data[:4])
            anoatual=int(str(datetime.date.today())[:4])
            mes=int(data[5:7])
            mesatual=int(str(datetime.date.today())[5:7])
            dia=int(data[8:])
            diaatual=int(str(datetime.date.today())[8:])

            if ano == anoatual and mes == mesatual:
                if dia-diaatual <10:
                    self.maintarefaslblmaxmin.setText("{} ℃ / {} ℃".format(self.api[3][dia-diaatual]['max'],self.api[3][dia-diaatual]['min']))
                    self.maintarefaslbldescricao.setText("{}".format(self.api[3][dia-diaatual]['description']))
                else:
                    self.maintarefaslblmaxmin.setText('Sem Prev')
                    self.maintarefaslbldescricao.setText('Sem Prev')
            else:
                self.maintarefaslblmaxmin.setText('Sem Prev')
                self.maintarefaslbldescricao.setText('Sem Prev')

            
            for i in range(len(tarefas)):
                if tarefas[i][3] == 0:
                    faltando+=1

            tabela.setRowCount(faltando)
            tabela.setColumnCount(1)
            tabela.setHorizontalHeaderItem(0,QTableWidgetItem('Tarefa Diária'))
            

            linha = 0
            for i in range(len(tarefas)):
                if tarefas[i][3] == 0:

                    tarefa=QTextEdit()
                    tarefa.setReadOnly(True)
                    tarefa.setText(tarefas[i][1])

                    if tarefas[i][2] == 2:
                        tarefa.setStyleSheet("QTextEdit {background-color:rgb(255, 155, 155);}")
                    elif tarefas[i][2] == 1:
                        tarefa.setStyleSheet("QTextEdit {background-color:rgb(255, 200, 155);}")

                    tabela.setVerticalHeaderItem(linha,QTableWidgetItem(tarefas[i][0][11:]))
                    tabela.setCellWidget(linha,0,tarefa)

                    linha+=1
            tabela.resizeColumnsToContents()

    def mostrar_botao_alterar(self) -> None:
        self.maintarefasframepb.show()

    def mostrar_cadastrar_tarefa(self) -> None:
        self.mainpages.setCurrentWidget(self.mainpgcadastrartarefa)

        self.maincadastrartarefashorariotimeEdit.setReadOnly(False)

        self.maincadastrartarefafrapbalterar.close()
        self.maincadastrartarefafrapbsalvar.show()

        data = self.maincalendariocalendario.selectedDate()
        
        if data.day() < 10:
            dia = f'0{str(data.day())}'
        else:
            dia = data.day()
        
        if data.month() < 10:
            mes = f'0{str(data.month())}'
        else:
            mes = data.month()
        
        data = f"{str(data.year())}-{mes}-{dia}"

        self.maincadastrartarefalbdia.setText(data)
    
    def mostrar_alterar_tarefa(self) -> None:
        self.mainpages.setCurrentWidget(self.mainpgcadastrartarefa)

        tabela = self.maintarefastab
        hora=tabela.verticalHeaderItem(tabela.currentRow()).text()[:2]
        self.maincadastrartarefashorariotimeEdit.setTime(QTime(int(hora),0,0,0))
        self.maincadastrartarefashorariotimeEdit.setReadOnly(True)

        self.maincadastrartarefafrapbalterar.show()
        self.maincadastrartarefafrapbsalvar.close()

        data = self.maincalendariocalendario.selectedDate()
        
        if data.day() < 10:
            dia = f'0{str(data.day())}'
        else:
            dia = data.day()
        
        if data.month() < 10:
            mes = f'0{str(data.month())}'
        else:
            mes = data.month()
        
        data = f"{str(data.year())}-{mes}-{dia}"

        self.maincadastrartarefalbdia.setText(data)

    def cadastrar_tarefa(self) -> None:
    
        self.maincadastrartarefatextedit.selectAll()
        self.maincadastrartarefatextedit.copy()
        texto = pc.paste()
        
        if not texto:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Necessário descrever a tarefa!")
            msg.exec()
        else:
            if self.maincadastrartarefarbessencial.isChecked():
                prioridade = 2
            elif self.maincadastrartarefarbsecudaria.isChecked():
                prioridade = 1
            else:
                prioridade = 0
            
            if self.maincadastrartarefashorariotimeEdit.time().hour() < 10:
                hora = f'0{self.maincadastrartarefashorariotimeEdit.time().hour()}'
            else:
                hora = self.maincadastrartarefashorariotimeEdit.time().hour()
            try:
                self.bd.insere_Tarefa([(f'{self.maincadastrartarefalbdia.text()} {hora}:00',texto,prioridade,0)])
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Cadastrar uma tarefa em um horário válido!")
                msg.exec()

            self.maincadastrartarefarbnormal.setChecked(True)
            self.maincadastrartarefatextedit.setText("")
            self.tarefas(self.maincadastrartarefalbdia.text())
    
    def alterar_tarefa(self) -> None:
        
        self.maincadastrartarefatextedit.selectAll()
        self.maincadastrartarefatextedit.copy()
        texto = pc.paste()
        
        if not texto:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Necessário descrever a tarefa!")
            msg.exec()
        else:
            if self.maincadastrartarefarbessencial.isChecked():
                prioridade = 2
            elif self.maincadastrartarefarbsecudaria.isChecked():
                prioridade = 1
            else:
                prioridade = 0
            
            if self.maincadastrartarefashorariotimeEdit.time().hour() < 10:
                hora = f'0{self.maincadastrartarefashorariotimeEdit.time().hour()}'
            else:
                hora = self.maincadastrartarefashorariotimeEdit.time().hour()
            try:
                self.bd.alterar_Tarefa([f'{self.maincadastrartarefalbdia.text()} {hora}:00',texto,prioridade,0])
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Cadastrar uma tarefa em um horário válido!")
                msg.exec()
            self.maincadastrartarefarbnormal.setChecked(True)
            self.maincadastrartarefatextedit.setText("")
            self.tarefas(self.maincadastrartarefalbdia.text())

    def exclui_tarefa(self) -> None:
        
        data = self.data_format_sql(self.maincalendariocalendario.selectedDate())
        tabela = self.maintarefastab
        self.bd.excluir_Tarefa(data+" "+str(tabela.verticalHeaderItem(tabela.currentRow()).text()))
        self.tarefas(self.data_format_sql(self.maincalendariocalendario.selectedDate()))

    def calendario(self) -> None:
      self.tarefas(self.data_format_sql(self.maincalendariocalendario.selectedDate()))

    def data_format_sql(self,data) -> None:
        if data.day() < 10:
            dia = f'0{str(data.day())}'
        else:
            dia = data.day()
        
        if data.month() < 10:
            mes = f'0{str(data.month())}'
        else:
            mes = data.month()

        return f"{str(data.year())}-{mes}-{dia}"

    def gastos(self) -> None:
        self.mainpages.setCurrentWidget(self.mainpggastos)

        tabela = self.maingastostab
        gastos = self.bd.listar_Gastos()

        self.maingastosframepb.close()

        tabela.setRowCount(len(gastos))
        tabela.setColumnCount(3)
        tabela.setHorizontalHeaderItem(0,QTableWidgetItem('Gasto'))
        tabela.setHorizontalHeaderItem(1,QTableWidgetItem('Valor'))
        tabela.setHorizontalHeaderItem(2,QTableWidgetItem('Vencimento'))

        valortotal=0
        for i in range(len(gastos)):
            tabela.setItem(i,0,QTableWidgetItem(str(gastos[i][0])))
            tabela.setItem(i,1,QTableWidgetItem(str(gastos[i][1])))
            tabela.setItem(i,2,QTableWidgetItem(str(gastos[i][2])))
            valortotal += int(gastos[i][1])            

        self.maingastoslblquantidadedegastos.setText(str(len(gastos)))
        self.maingastoslbltotalgastos.setText(str(valortotal)+" R$")

    def mostrar_botao_gastos(self) -> None:
        self.maingastosframepb.show()

    def mostar_cadastro_gasto(self) -> None:
        
        self.mainpages.setCurrentWidget(self.mainpgcadastrargasto)
        self.maincadastrargastolegasto.setText("")
        self.maincadastrargastoslevalor.setText("")
        self.maincadastrargastoframepb.close()

    def mostrar_botao_gasto_salvar(self) -> None:
        if self.maincadastrargastolegasto.text():
            self.maincadastrargastoframepb.show()
        else:
            self.maincadastrargastoframepb.close()

    def insere_gasto(self) -> None:
        data = str(self.maincadastrargastodata.date().day())+"-"+str(self.maincadastrargastodata.date().month())+"-"+str(self.maincadastrargastodata.date().year())
        self.bd.insere_Gasto([self.maincadastrargastolegasto.text(),self.maincadastrargastoslevalor.text(),data])
        
        self.gastos()

    def deletar_gasto(self) -> None:
        tabela= self.maingastostab
        gasto = tabela.item(tabela.row(tabela.currentItem()),0).text()

        self.bd.excluir_Gasto(gasto)
        self.gastos()




if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainJanela()
    window.show()
    app.exec()

    