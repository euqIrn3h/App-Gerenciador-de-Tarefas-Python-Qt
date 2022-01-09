# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)

class Ui_ToDo(object):
    def setupUi(self, ToDo):
        if not ToDo.objectName():
            ToDo.setObjectName(u"ToDo")
        ToDo.resize(530, 520)
        ToDo.setMinimumSize(QSize(0, 520))
        ToDo.setStyleSheet(u"*{\n"
"background-color:rgb(0,0,0);\n"
"color:rgb(255,255,255);\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(ToDo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lcontainer = QFrame(self.centralwidget)
        self.lcontainer.setObjectName(u"lcontainer")
        self.lcontainer.setMaximumSize(QSize(130, 16777215))
        self.lcontainer.setFrameShape(QFrame.StyledPanel)
        self.lcontainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.lcontainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pbhome = QPushButton(self.lcontainer)
        self.pbhome.setObjectName(u"pbhome")
        font = QFont()
        font.setBold(True)
        self.pbhome.setFont(font)
        self.pbhome.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pbhome)

        self.pbtarefas = QPushButton(self.lcontainer)
        self.pbtarefas.setObjectName(u"pbtarefas")
        self.pbtarefas.setFont(font)
        self.pbtarefas.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pbtarefas)

        self.pbgastos = QPushButton(self.lcontainer)
        self.pbgastos.setObjectName(u"pbgastos")
        self.pbgastos.setFont(font)

        self.verticalLayout.addWidget(self.pbgastos)

        self.pbcalendario = QPushButton(self.lcontainer)
        self.pbcalendario.setObjectName(u"pbcalendario")
        self.pbcalendario.setFont(font)

        self.verticalLayout.addWidget(self.pbcalendario)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.lcontainer)

        self.maincontainer = QFrame(self.centralwidget)
        self.maincontainer.setObjectName(u"maincontainer")
        self.maincontainer.setFrameShape(QFrame.StyledPanel)
        self.maincontainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.maincontainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.header = QFrame(self.maincontainer)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 30))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pbtoogle = QPushButton(self.header)
        self.pbtoogle.setObjectName(u"pbtoogle")
        self.pbtoogle.setMinimumSize(QSize(0, 20))
        self.pbtoogle.setMaximumSize(QSize(30, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.pbtoogle.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pbtoogle)

        self.headerlblhorario = QLabel(self.header)
        self.headerlblhorario.setObjectName(u"headerlblhorario")
        self.headerlblhorario.setMinimumSize(QSize(0, 15))
        self.headerlblhorario.setFont(font)
        self.headerlblhorario.setStyleSheet(u"border:solid;\n"
"border-width:1px;\n"
"border-color:grey;")
        self.headerlblhorario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.headerlblhorario)

        self.headerlbldia = QLabel(self.header)
        self.headerlbldia.setObjectName(u"headerlbldia")
        self.headerlbldia.setMinimumSize(QSize(0, 15))
        self.headerlbldia.setFont(font)
        self.headerlbldia.setStyleSheet(u"border:solid;\n"
"border-width:1px;\n"
"border-color:grey;")
        self.headerlbldia.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.headerlbldia)

        self.headerlbltemperatura = QLabel(self.header)
        self.headerlbltemperatura.setObjectName(u"headerlbltemperatura")
        self.headerlbltemperatura.setMinimumSize(QSize(0, 15))
        self.headerlbltemperatura.setFont(font)
        self.headerlbltemperatura.setStyleSheet(u"border:solid;\n"
"border-width:1px;\n"
"border-color:grey;")
        self.headerlbltemperatura.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.headerlbltemperatura)


        self.verticalLayout_2.addWidget(self.header)

        self.main = QFrame(self.maincontainer)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mainpages = QStackedWidget(self.main)
        self.mainpages.setObjectName(u"mainpages")
        self.mainpages.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.mainpghome = QWidget()
        self.mainpghome.setObjectName(u"mainpghome")
        self.mainpghome.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.mainpghome)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.mainpghome)
        self.frame.setObjectName(u"frame")
        font2 = QFont()
        font2.setBold(False)
        self.frame.setFont(font2)
        self.frame.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_4.addWidget(self.label_11)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_4.addWidget(self.label_10)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_4.addWidget(self.label)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_4.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_4.addWidget(self.label_8)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.mainpghome)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.mainhomecidade = QLabel(self.frame_2)
        self.mainhomecidade.setObjectName(u"mainhomecidade")
        self.mainhomecidade.setFont(font)
        self.mainhomecidade.setStyleSheet(u"background-color: rgb(190, 190, 200);\n"
"")

        self.verticalLayout_8.addWidget(self.mainhomecidade)

        self.mainhomedata = QLabel(self.frame_2)
        self.mainhomedata.setObjectName(u"mainhomedata")
        self.mainhomedata.setFont(font)

        self.verticalLayout_8.addWidget(self.mainhomedata)

        self.mainhometemperatura = QLabel(self.frame_2)
        self.mainhometemperatura.setObjectName(u"mainhometemperatura")
        self.mainhometemperatura.setFont(font)
        self.mainhometemperatura.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_8.addWidget(self.mainhometemperatura)

        self.mainhomeclima = QLabel(self.frame_2)
        self.mainhomeclima.setObjectName(u"mainhomeclima")
        self.mainhomeclima.setFont(font)

        self.verticalLayout_8.addWidget(self.mainhomeclima)

        self.mainhomemaxmin = QLabel(self.frame_2)
        self.mainhomemaxmin.setObjectName(u"mainhomemaxmin")
        self.mainhomemaxmin.setFont(font)
        self.mainhomemaxmin.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_8.addWidget(self.mainhomemaxmin)

        self.verticalSpacer_3 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.mainhometarconcluida = QLabel(self.frame_2)
        self.mainhometarconcluida.setObjectName(u"mainhometarconcluida")
        self.mainhometarconcluida.setFont(font)
        self.mainhometarconcluida.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_8.addWidget(self.mainhometarconcluida)

        self.mainhometarfaltando = QLabel(self.frame_2)
        self.mainhometarfaltando.setObjectName(u"mainhometarfaltando")
        self.mainhometarfaltando.setFont(font)

        self.verticalLayout_8.addWidget(self.mainhometarfaltando)

        self.mainhometaressencial = QLabel(self.frame_2)
        self.mainhometaressencial.setObjectName(u"mainhometaressencial")
        self.mainhometaressencial.setFont(font)
        self.mainhometaressencial.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_8.addWidget(self.mainhometaressencial)

        self.mainhometaressencialconluida = QLabel(self.frame_2)
        self.mainhometaressencialconluida.setObjectName(u"mainhometaressencialconluida")
        self.mainhometaressencialconluida.setFont(font)

        self.verticalLayout_8.addWidget(self.mainhometaressencialconluida)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.mainpghome)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(190, 190, 200);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font)
        self.progressBar.setValue(50)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat(u"%p%")

        self.horizontalLayout_4.addWidget(self.progressBar)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 2)

        self.mainpages.addWidget(self.mainpghome)
        self.mainpgtarefasdiarias = QWidget()
        self.mainpgtarefasdiarias.setObjectName(u"mainpgtarefasdiarias")
        self.mainpgtarefasdiarias.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.mainpgtarefasdiarias)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.maintarefasdiariasframetarefa = QFrame(self.mainpgtarefasdiarias)
        self.maintarefasdiariasframetarefa.setObjectName(u"maintarefasdiariasframetarefa")
        self.maintarefasdiariasframetarefa.setFrameShape(QFrame.StyledPanel)
        self.maintarefasdiariasframetarefa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.maintarefasdiariasframetarefa)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.maintarefasdiariaslbl = QLabel(self.maintarefasdiariasframetarefa)
        self.maintarefasdiariaslbl.setObjectName(u"maintarefasdiariaslbl")
        self.maintarefasdiariaslbl.setMinimumSize(QSize(25, 20))
        self.maintarefasdiariaslbl.setFont(font)
        self.maintarefasdiariaslbl.setStyleSheet(u"background-color: rgba(190, 190, 190, 234);\n"
"border:solid;\n"
"border-width:1px;\n"
"")
        self.maintarefasdiariaslbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.maintarefasdiariaslbl)

        self.maintarefasdiariastab = QTableWidget(self.maintarefasdiariasframetarefa)
        self.maintarefasdiariastab.setObjectName(u"maintarefasdiariastab")
        self.maintarefasdiariastab.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.maintarefasdiariastab)

        self.maintarefasdiariaspbtarefaconcluida = QPushButton(self.maintarefasdiariasframetarefa)
        self.maintarefasdiariaspbtarefaconcluida.setObjectName(u"maintarefasdiariaspbtarefaconcluida")

        self.verticalLayout_5.addWidget(self.maintarefasdiariaspbtarefaconcluida)


        self.horizontalLayout_5.addWidget(self.maintarefasdiariasframetarefa)

        self.mainpages.addWidget(self.mainpgtarefasdiarias)
        self.mainpggastos = QWidget()
        self.mainpggastos.setObjectName(u"mainpggastos")
        self.mainpggastos.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}\n"
"")
        self.tableWidget = QTableWidget(self.mainpggastos)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 70, 256, 192))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mainpages.addWidget(self.mainpggastos)
        self.mainpgcalendario = QWidget()
        self.mainpgcalendario.setObjectName(u"mainpgcalendario")
        self.mainpgcalendario.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.mainpgcalendario)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.mainpgcalendario)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.calendarWidget = QCalendarWidget(self.frame_4)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:black;")

        self.verticalLayout_9.addWidget(self.calendarWidget)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.mainpages.addWidget(self.mainpgcalendario)
        self.mainpgtarefas = QWidget()
        self.mainpgtarefas.setObjectName(u"mainpgtarefas")
        self.mainpgtarefas.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.mainpgtarefas)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.maintarefasframe = QFrame(self.mainpgtarefas)
        self.maintarefasframe.setObjectName(u"maintarefasframe")
        self.maintarefasframe.setFrameShape(QFrame.StyledPanel)
        self.maintarefasframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.maintarefasframe)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.maintarefaslbl = QLabel(self.maintarefasframe)
        self.maintarefaslbl.setObjectName(u"maintarefaslbl")
        self.maintarefaslbl.setMinimumSize(QSize(25, 20))
        self.maintarefaslbl.setFont(font)
        self.maintarefaslbl.setStyleSheet(u"background-color: rgba(190, 190, 190, 234);\n"
"color: rgb(0, 0, 0);\n"
"border:solid;\n"
"border-width:1px;\n"
"")
        self.maintarefaslbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.maintarefaslbl)

        self.maintarefastab = QTableWidget(self.maintarefasframe)
        self.maintarefastab.setObjectName(u"maintarefastab")
        self.maintarefastab.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.maintarefastab)

        self.maintarefaspbcadastrar = QPushButton(self.maintarefasframe)
        self.maintarefaspbcadastrar.setObjectName(u"maintarefaspbcadastrar")

        self.verticalLayout_12.addWidget(self.maintarefaspbcadastrar)


        self.verticalLayout_11.addWidget(self.maintarefasframe)

        self.mainpages.addWidget(self.mainpgtarefas)
        self.mainpgcadastrartarefa = QWidget()
        self.mainpgcadastrartarefa.setObjectName(u"mainpgcadastrartarefa")
        self.mainpgcadastrartarefa.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}\n"
"\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.mainpgcadastrartarefa)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.mainctarefasframehorario_2 = QFrame(self.mainpgcadastrartarefa)
        self.mainctarefasframehorario_2.setObjectName(u"mainctarefasframehorario_2")
        self.mainctarefasframehorario_2.setMinimumSize(QSize(0, 30))
        self.mainctarefasframehorario_2.setMaximumSize(QSize(10000000, 16777215))
        self.mainctarefasframehorario_2.setFrameShape(QFrame.StyledPanel)
        self.mainctarefasframehorario_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.mainctarefasframehorario_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mainctarefaslblhorario = QLabel(self.mainctarefasframehorario_2)
        self.mainctarefaslblhorario.setObjectName(u"mainctarefaslblhorario")
        self.mainctarefaslblhorario.setMinimumSize(QSize(0, 20))
        self.mainctarefaslblhorario.setMaximumSize(QSize(80, 20))
        self.mainctarefaslblhorario.setFont(font)
        self.mainctarefaslblhorario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.mainctarefaslblhorario)

        self.mainctarefaslblhorariotimeEdit = QTimeEdit(self.mainctarefasframehorario_2)
        self.mainctarefaslblhorariotimeEdit.setObjectName(u"mainctarefaslblhorariotimeEdit")
        self.mainctarefaslblhorariotimeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.mainctarefaslblhorariotimeEdit)


        self.verticalLayout_10.addWidget(self.mainctarefasframehorario_2)

        self.mainctarefasframecadastrar = QFrame(self.mainpgcadastrartarefa)
        self.mainctarefasframecadastrar.setObjectName(u"mainctarefasframecadastrar")
        self.mainctarefasframecadastrar.setFrameShape(QFrame.StyledPanel)
        self.mainctarefasframecadastrar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.mainctarefasframecadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.maincadastrartarefatextedit = QTextEdit(self.mainctarefasframecadastrar)
        self.maincadastrartarefatextedit.setObjectName(u"maincadastrartarefatextedit")
        self.maincadastrartarefatextedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.maincadastrartarefatextedit)

        self.maincadastrartarefarbessencial = QRadioButton(self.mainctarefasframecadastrar)
        self.maincadastrartarefarbessencial.setObjectName(u"maincadastrartarefarbessencial")
        self.maincadastrartarefarbessencial.setFont(font)
        self.maincadastrartarefarbessencial.setStyleSheet(u"background-color: rgb(255, 155, 155);")

        self.verticalLayout_6.addWidget(self.maincadastrartarefarbessencial)

        self.maincadastrartarefarbimportante = QRadioButton(self.mainctarefasframecadastrar)
        self.maincadastrartarefarbimportante.setObjectName(u"maincadastrartarefarbimportante")
        self.maincadastrartarefarbimportante.setFont(font)
        self.maincadastrartarefarbimportante.setStyleSheet(u"background-color:rgb(255, 200, 155);")

        self.verticalLayout_6.addWidget(self.maincadastrartarefarbimportante)

        self.maincadastrartarefarbsecudaria = QRadioButton(self.mainctarefasframecadastrar)
        self.maincadastrartarefarbsecudaria.setObjectName(u"maincadastrartarefarbsecudaria")
        self.maincadastrartarefarbsecudaria.setFont(font)
        self.maincadastrartarefarbsecudaria.setStyleSheet(u"background-color: rgb(255, 255, 155);")

        self.verticalLayout_6.addWidget(self.maincadastrartarefarbsecudaria)

        self.maincadastrartarefapbsalvar = QPushButton(self.mainctarefasframecadastrar)
        self.maincadastrartarefapbsalvar.setObjectName(u"maincadastrartarefapbsalvar")
        self.maincadastrartarefapbsalvar.setFont(font)

        self.verticalLayout_6.addWidget(self.maincadastrartarefapbsalvar)


        self.verticalLayout_10.addWidget(self.mainctarefasframecadastrar)

        self.mainpages.addWidget(self.mainpgcadastrartarefa)

        self.verticalLayout_3.addWidget(self.mainpages)


        self.verticalLayout_2.addWidget(self.main)

        self.footer = QFrame(self.maincontainer)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 30))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.maincontainer)

        ToDo.setCentralWidget(self.centralwidget)

        self.retranslateUi(ToDo)

        self.mainpages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ToDo)
    # setupUi

    def retranslateUi(self, ToDo):
        ToDo.setWindowTitle(QCoreApplication.translate("ToDo", u"ToDo", None))
        self.pbhome.setText(QCoreApplication.translate("ToDo", u"HOME", None))
        self.pbtarefas.setText(QCoreApplication.translate("ToDo", u"TAREFAS DI\u00c1RIAS", None))
        self.pbgastos.setText(QCoreApplication.translate("ToDo", u"GASTOS", None))
        self.pbcalendario.setText(QCoreApplication.translate("ToDo", u"CALENDARIO", None))
        self.pbtoogle.setText(QCoreApplication.translate("ToDo", u">>>", None))
        self.headerlblhorario.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.headerlbldia.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.headerlbltemperatura.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("ToDo", u"Cidade :", None))
        self.label_10.setText(QCoreApplication.translate("ToDo", u"Data :", None))
        self.label.setText(QCoreApplication.translate("ToDo", u"Temperatura :", None))
        self.label_3.setText(QCoreApplication.translate("ToDo", u"Cilma :", None))
        self.label_4.setText(QCoreApplication.translate("ToDo", u"Max / Min :", None))
        self.label_5.setText(QCoreApplication.translate("ToDo", u"Tarefas conclu\u00eddas :", None))
        self.label_6.setText(QCoreApplication.translate("ToDo", u"Tarefas faltando :", None))
        self.label_7.setText(QCoreApplication.translate("ToDo", u"Tarefas essenciais :", None))
        self.label_8.setText(QCoreApplication.translate("ToDo", u"Tarefas essencias conclu\u00eddas :", None))
        self.mainhomecidade.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhomedata.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometemperatura.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhomeclima.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhomemaxmin.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometarconcluida.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometarfaltando.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometaressencial.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometaressencialconluida.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("ToDo", u"Percentual de conclus\u00e3o :", None))
        self.maintarefasdiariaslbl.setText(QCoreApplication.translate("ToDo", u"20", None))
        self.maintarefasdiariaspbtarefaconcluida.setText(QCoreApplication.translate("ToDo", u"Tarefa conclu\u00edda", None))
        self.maintarefaslbl.setText(QCoreApplication.translate("ToDo", u"DIA", None))
        self.maintarefaspbcadastrar.setText(QCoreApplication.translate("ToDo", u"PushButton", None))
        self.mainctarefaslblhorario.setText(QCoreApplication.translate("ToDo", u"Hor\u00e1rio", None))
        self.maincadastrartarefarbessencial.setText(QCoreApplication.translate("ToDo", u"Essencial", None))
        self.maincadastrartarefarbimportante.setText(QCoreApplication.translate("ToDo", u"Importante", None))
        self.maincadastrartarefarbsecudaria.setText(QCoreApplication.translate("ToDo", u"Secund\u00e1ria", None))
        self.maincadastrartarefapbsalvar.setText(QCoreApplication.translate("ToDo", u"Salvar", None))
        self.label_2.setText(QCoreApplication.translate("ToDo", u"(C) HENRIQUE - 2022", None))
    # retranslateUi

