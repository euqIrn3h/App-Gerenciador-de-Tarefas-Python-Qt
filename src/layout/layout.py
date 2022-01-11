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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_ToDo(object):
    def setupUi(self, ToDo):
        if not ToDo.objectName():
            ToDo.setObjectName(u"ToDo")
        ToDo.resize(550, 531)
        ToDo.setMinimumSize(QSize(0, 0))
        ToDo.setStyleSheet(u"*{\n"
"background-color:rgb(0,0,0);\n"
"color:rgb(255,255,255);\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(190, 190, 200);\n"
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

        self.pbtarefasdiarias = QPushButton(self.lcontainer)
        self.pbtarefasdiarias.setObjectName(u"pbtarefasdiarias")
        self.pbtarefasdiarias.setFont(font)
        self.pbtarefasdiarias.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pbtarefasdiarias)

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
        self.header.setStyleSheet(u"")
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
        self.headerlblhorario.setStyleSheet(u"QLabel{\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"background-color: rgb(190, 190, 200);\n"
"color:black;\n"
"}")
        self.headerlblhorario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.headerlblhorario)

        self.headerlbldia = QLabel(self.header)
        self.headerlbldia.setObjectName(u"headerlbldia")
        self.headerlbldia.setMinimumSize(QSize(0, 15))
        self.headerlbldia.setFont(font)
        self.headerlbldia.setStyleSheet(u"QLabel{\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"background-color: rgb(190, 190, 200);\n"
"color:black;\n"
"}")
        self.headerlbldia.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.headerlbldia)

        self.headerlbltemperatura = QLabel(self.header)
        self.headerlbltemperatura.setObjectName(u"headerlbltemperatura")
        self.headerlbltemperatura.setMinimumSize(QSize(0, 15))
        self.headerlbltemperatura.setFont(font)
        self.headerlbltemperatura.setStyleSheet(u"QLabel{\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"background-color: rgb(190, 190, 200);\n"
"color:black;\n"
"}")
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

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: rgb(190, 190, 200);")

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

        self.mainhometarefasdiarias = QLabel(self.frame_2)
        self.mainhometarefasdiarias.setObjectName(u"mainhometarefasdiarias")
        self.mainhometarefasdiarias.setFont(font)
        self.mainhometarefasdiarias.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_8.addWidget(self.mainhometarefasdiarias)

        self.mainhometarconcluida = QLabel(self.frame_2)
        self.mainhometarconcluida.setObjectName(u"mainhometarconcluida")
        self.mainhometarconcluida.setFont(font)
        self.mainhometarconcluida.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.mainhometarconcluida)

        self.mainhometarfaltando = QLabel(self.frame_2)
        self.mainhometarfaltando.setObjectName(u"mainhometarfaltando")
        self.mainhometarfaltando.setFont(font)
        self.mainhometarfaltando.setStyleSheet(u"background-color: rgb(190, 190, 200);")

        self.verticalLayout_8.addWidget(self.mainhometarfaltando)

        self.mainhometaressencial = QLabel(self.frame_2)
        self.mainhometaressencial.setObjectName(u"mainhometaressencial")
        self.mainhometaressencial.setFont(font)
        self.mainhometaressencial.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.mainhometaressencial)

        self.mainhometaressencialconluida = QLabel(self.frame_2)
        self.mainhometaressencialconluida.setObjectName(u"mainhometaressencialconluida")
        self.mainhometaressencialconluida.setFont(font)
        self.mainhometaressencialconluida.setStyleSheet(u"background-color: rgb(190, 190, 200);")

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

        self.mainhomeprogressbar = QProgressBar(self.frame_3)
        self.mainhomeprogressbar.setObjectName(u"mainhomeprogressbar")
        self.mainhomeprogressbar.setFont(font)
        self.mainhomeprogressbar.setValue(50)
        self.mainhomeprogressbar.setAlignment(Qt.AlignCenter)
        self.mainhomeprogressbar.setTextVisible(True)
        self.mainhomeprogressbar.setOrientation(Qt.Horizontal)
        self.mainhomeprogressbar.setInvertedAppearance(False)
        self.mainhomeprogressbar.setFormat(u"%p%")

        self.horizontalLayout_4.addWidget(self.mainhomeprogressbar)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 2)

        self.mainpages.addWidget(self.mainpghome)
        self.mainpgtarefasdiarias = QWidget()
        self.mainpgtarefasdiarias.setObjectName(u"mainpgtarefasdiarias")
        self.mainpgtarefasdiarias.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(190, 190, 200);\n"
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
        self.maintarefasdiariasframe = QFrame(self.mainpgtarefasdiarias)
        self.maintarefasdiariasframe.setObjectName(u"maintarefasdiariasframe")
        self.maintarefasdiariasframe.setFrameShape(QFrame.StyledPanel)
        self.maintarefasdiariasframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.maintarefasdiariasframe)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.maintarefasdiariastab = QTableWidget(self.maintarefasdiariasframe)
        self.maintarefasdiariastab.setObjectName(u"maintarefasdiariastab")
        self.maintarefasdiariastab.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.maintarefasdiariastab)

        self.maintarefasdiariasframepb = QFrame(self.maintarefasdiariasframe)
        self.maintarefasdiariasframepb.setObjectName(u"maintarefasdiariasframepb")
        self.maintarefasdiariasframepb.setMinimumSize(QSize(0, 30))
        self.maintarefasdiariasframepb.setFrameShape(QFrame.StyledPanel)
        self.maintarefasdiariasframepb.setFrameShadow(QFrame.Raised)
        self.maintarefasdiariaspbtarefaconcluida = QPushButton(self.maintarefasdiariasframepb)
        self.maintarefasdiariaspbtarefaconcluida.setObjectName(u"maintarefasdiariaspbtarefaconcluida")
        self.maintarefasdiariaspbtarefaconcluida.setGeometry(QRect(0, 10, 312, 15))

        self.verticalLayout_5.addWidget(self.maintarefasdiariasframepb)


        self.horizontalLayout_5.addWidget(self.maintarefasdiariasframe)

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
        self.maincalendarioframe = QFrame(self.mainpgcalendario)
        self.maincalendarioframe.setObjectName(u"maincalendarioframe")
        self.maincalendarioframe.setFrameShape(QFrame.StyledPanel)
        self.maincalendarioframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.maincalendarioframe)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.maincalendariocalendario = QCalendarWidget(self.maincalendarioframe)
        self.maincalendariocalendario.setObjectName(u"maincalendariocalendario")
        self.maincalendariocalendario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:black;")

        self.verticalLayout_9.addWidget(self.maincalendariocalendario)


        self.verticalLayout_7.addWidget(self.maincalendarioframe)

        self.mainpages.addWidget(self.mainpgcalendario)
        self.mainpgtarefas = QWidget()
        self.mainpgtarefas.setObjectName(u"mainpgtarefas")
        self.mainpgtarefas.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(190, 190, 200);\n"
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
        self.maintarefasframeheader = QFrame(self.maintarefasframe)
        self.maintarefasframeheader.setObjectName(u"maintarefasframeheader")
        self.maintarefasframeheader.setMinimumSize(QSize(0, 30))
        self.maintarefasframeheader.setStyleSheet(u"QLabe {\n"
"background-color: rgb(190, 190, 200);\n"
"}l")
        self.maintarefasframeheader.setFrameShape(QFrame.StyledPanel)
        self.maintarefasframeheader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.maintarefasframeheader)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.maintarefaslbldia = QLabel(self.maintarefasframeheader)
        self.maintarefaslbldia.setObjectName(u"maintarefaslbldia")
        self.maintarefaslbldia.setFont(font)
        self.maintarefaslbldia.setStyleSheet(u"QLabel{\n"
"border:solid;\n"
"border-width:1px;\n"
"}")
        self.maintarefaslbldia.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.maintarefaslbldia)

        self.maintarefaslblmaxmin = QLabel(self.maintarefasframeheader)
        self.maintarefaslblmaxmin.setObjectName(u"maintarefaslblmaxmin")
        self.maintarefaslblmaxmin.setFont(font)
        self.maintarefaslblmaxmin.setStyleSheet(u"QLabel{\n"
"border:solid;\n"
"border-width:1px;\n"
"}")
        self.maintarefaslblmaxmin.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.maintarefaslblmaxmin)

        self.maintarefaslbldescricao = QLabel(self.maintarefasframeheader)
        self.maintarefaslbldescricao.setObjectName(u"maintarefaslbldescricao")
        self.maintarefaslbldescricao.setFont(font)
        self.maintarefaslbldescricao.setStyleSheet(u"QLabel{\n"
"border:solid;\n"
"border-width:1px;\n"
"}")
        self.maintarefaslbldescricao.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.maintarefaslbldescricao)


        self.verticalLayout_12.addWidget(self.maintarefasframeheader)

        self.maintarefastab = QTableWidget(self.maintarefasframe)
        self.maintarefastab.setObjectName(u"maintarefastab")
        self.maintarefastab.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.maintarefastab)

        self.maintarefasframepb = QFrame(self.maintarefasframe)
        self.maintarefasframepb.setObjectName(u"maintarefasframepb")
        self.maintarefasframepb.setMinimumSize(QSize(0, 0))
        self.maintarefasframepb.setMaximumSize(QSize(16777215, 16777215))
        self.maintarefasframepb.setFrameShape(QFrame.StyledPanel)
        self.maintarefasframepb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.maintarefasframepb)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.maintarefaspbalterar = QPushButton(self.maintarefasframepb)
        self.maintarefaspbalterar.setObjectName(u"maintarefaspbalterar")
        self.maintarefaspbalterar.setFont(font)

        self.verticalLayout_13.addWidget(self.maintarefaspbalterar)

        self.maintarefaspbdeletar = QPushButton(self.maintarefasframepb)
        self.maintarefaspbdeletar.setObjectName(u"maintarefaspbdeletar")
        self.maintarefaspbdeletar.setFont(font)

        self.verticalLayout_13.addWidget(self.maintarefaspbdeletar)


        self.verticalLayout_12.addWidget(self.maintarefasframepb)

        self.maintarefasframepbcadastrar = QFrame(self.maintarefasframe)
        self.maintarefasframepbcadastrar.setObjectName(u"maintarefasframepbcadastrar")
        self.maintarefasframepbcadastrar.setMinimumSize(QSize(0, 0))
        self.maintarefasframepbcadastrar.setFrameShape(QFrame.StyledPanel)
        self.maintarefasframepbcadastrar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.maintarefasframepbcadastrar)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.maintarefaspbcadastrar = QPushButton(self.maintarefasframepbcadastrar)
        self.maintarefaspbcadastrar.setObjectName(u"maintarefaspbcadastrar")
        self.maintarefaspbcadastrar.setFont(font)

        self.verticalLayout_14.addWidget(self.maintarefaspbcadastrar)


        self.verticalLayout_12.addWidget(self.maintarefasframepbcadastrar)


        self.verticalLayout_11.addWidget(self.maintarefasframe)

        self.mainpages.addWidget(self.mainpgtarefas)
        self.mainpgcadastrartarefa = QWidget()
        self.mainpgcadastrartarefa.setObjectName(u"mainpgcadastrartarefa")
        self.mainpgcadastrartarefa.setStyleSheet(u"*{\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(190, 190, 200);\n"
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
        self.verticalLayout_10 = QVBoxLayout(self.mainpgcadastrartarefa)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.mainctarefasframecadastrar = QFrame(self.mainpgcadastrartarefa)
        self.mainctarefasframecadastrar.setObjectName(u"mainctarefasframecadastrar")
        self.mainctarefasframecadastrar.setFrameShape(QFrame.StyledPanel)
        self.mainctarefasframecadastrar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.mainctarefasframecadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.maincadastrartarefalbdia = QLabel(self.mainctarefasframecadastrar)
        self.maincadastrartarefalbdia.setObjectName(u"maincadastrartarefalbdia")
        self.maincadastrartarefalbdia.setFont(font)
        self.maincadastrartarefalbdia.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.maincadastrartarefalbdia)

        self.mainctarefasframehorario_2 = QFrame(self.mainctarefasframecadastrar)
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

        self.maincadastrartarefashorariotimeEdit = QTimeEdit(self.mainctarefasframehorario_2)
        self.maincadastrartarefashorariotimeEdit.setObjectName(u"maincadastrartarefashorariotimeEdit")
        self.maincadastrartarefashorariotimeEdit.setFont(font)
        self.maincadastrartarefashorariotimeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.maincadastrartarefashorariotimeEdit.setCurrentSection(QDateTimeEdit.HourSection)

        self.horizontalLayout_6.addWidget(self.maincadastrartarefashorariotimeEdit)


        self.verticalLayout_6.addWidget(self.mainctarefasframehorario_2)

        self.maincadastrartarefatextedit = QTextEdit(self.mainctarefasframecadastrar)
        self.maincadastrartarefatextedit.setObjectName(u"maincadastrartarefatextedit")
        self.maincadastrartarefatextedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.maincadastrartarefatextedit)

        self.maincadastrartarefarbessencial = QRadioButton(self.mainctarefasframecadastrar)
        self.maincadastrartarefarbessencial.setObjectName(u"maincadastrartarefarbessencial")
        self.maincadastrartarefarbessencial.setFont(font)
        self.maincadastrartarefarbessencial.setStyleSheet(u"background-color: rgb(255, 155, 155);")

        self.verticalLayout_6.addWidget(self.maincadastrartarefarbessencial)

        self.maincadastrartarefarbsecudaria = QRadioButton(self.mainctarefasframecadastrar)
        self.maincadastrartarefarbsecudaria.setObjectName(u"maincadastrartarefarbsecudaria")
        self.maincadastrartarefarbsecudaria.setFont(font)
        self.maincadastrartarefarbsecudaria.setStyleSheet(u"background-color:rgb(255, 200, 155);")

        self.verticalLayout_6.addWidget(self.maincadastrartarefarbsecudaria)

        self.maincadastrartarefarbnormal = QRadioButton(self.mainctarefasframecadastrar)
        self.maincadastrartarefarbnormal.setObjectName(u"maincadastrartarefarbnormal")
        self.maincadastrartarefarbnormal.setFont(font)
        self.maincadastrartarefarbnormal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.maincadastrartarefarbnormal.setChecked(True)

        self.verticalLayout_6.addWidget(self.maincadastrartarefarbnormal)

        self.maincadastrartarefafrapbalterar = QFrame(self.mainctarefasframecadastrar)
        self.maincadastrartarefafrapbalterar.setObjectName(u"maincadastrartarefafrapbalterar")
        self.maincadastrartarefafrapbalterar.setMinimumSize(QSize(0, 30))
        self.maincadastrartarefafrapbalterar.setFrameShape(QFrame.StyledPanel)
        self.maincadastrartarefafrapbalterar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.maincadastrartarefafrapbalterar)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.maincadastrartarefapbalterar = QPushButton(self.maincadastrartarefafrapbalterar)
        self.maincadastrartarefapbalterar.setObjectName(u"maincadastrartarefapbalterar")
        self.maincadastrartarefapbalterar.setFont(font)

        self.verticalLayout_16.addWidget(self.maincadastrartarefapbalterar)


        self.verticalLayout_6.addWidget(self.maincadastrartarefafrapbalterar)

        self.maincadastrartarefafrapbsalvar = QFrame(self.mainctarefasframecadastrar)
        self.maincadastrartarefafrapbsalvar.setObjectName(u"maincadastrartarefafrapbsalvar")
        self.maincadastrartarefafrapbsalvar.setMinimumSize(QSize(0, 30))
        self.maincadastrartarefafrapbsalvar.setFrameShape(QFrame.StyledPanel)
        self.maincadastrartarefafrapbsalvar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.maincadastrartarefafrapbsalvar)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.maincadastrartarefapbsalvar = QPushButton(self.maincadastrartarefafrapbsalvar)
        self.maincadastrartarefapbsalvar.setObjectName(u"maincadastrartarefapbsalvar")
        self.maincadastrartarefapbsalvar.setFont(font)

        self.verticalLayout_15.addWidget(self.maincadastrartarefapbsalvar)


        self.verticalLayout_6.addWidget(self.maincadastrartarefafrapbsalvar)


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
        self.footerlblassinatura = QLabel(self.footer)
        self.footerlblassinatura.setObjectName(u"footerlblassinatura")
        self.footerlblassinatura.setMinimumSize(QSize(0, 20))
        self.footerlblassinatura.setFont(font)
        self.footerlblassinatura.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.footerlblassinatura)


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
        self.pbtarefasdiarias.setText(QCoreApplication.translate("ToDo", u"TAREFAS DI\u00c1RIAS", None))
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
        self.label_12.setText(QCoreApplication.translate("ToDo", u"Tarefas di\u00e1rias :", None))
        self.label_5.setText(QCoreApplication.translate("ToDo", u"Tarefas conclu\u00eddas :", None))
        self.label_6.setText(QCoreApplication.translate("ToDo", u"Tarefas faltando :", None))
        self.label_7.setText(QCoreApplication.translate("ToDo", u"Tarefas essenciais :", None))
        self.label_8.setText(QCoreApplication.translate("ToDo", u"Tarefas essencias conclu\u00eddas :", None))
        self.mainhomecidade.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhomedata.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometemperatura.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhomeclima.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhomemaxmin.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometarefasdiarias.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometarconcluida.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometarfaltando.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometaressencial.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.mainhometaressencialconluida.setText(QCoreApplication.translate("ToDo", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("ToDo", u"Percentual de conclus\u00e3o :", None))
        self.maintarefasdiariaspbtarefaconcluida.setText(QCoreApplication.translate("ToDo", u"Tarefa conclu\u00edda", None))
        self.maintarefaslbldia.setText(QCoreApplication.translate("ToDo", u"Data", None))
        self.maintarefaslblmaxmin.setText(QCoreApplication.translate("ToDo", u"M\u00e1x - M\u00edn", None))
        self.maintarefaslbldescricao.setText(QCoreApplication.translate("ToDo", u"Clima", None))
        self.maintarefaspbalterar.setText(QCoreApplication.translate("ToDo", u"Alterar", None))
        self.maintarefaspbdeletar.setText(QCoreApplication.translate("ToDo", u"Deletar", None))
        self.maintarefaspbcadastrar.setText(QCoreApplication.translate("ToDo", u"Cadastrar", None))
        self.maincadastrartarefalbdia.setText(QCoreApplication.translate("ToDo", u"DIA", None))
        self.mainctarefaslblhorario.setText(QCoreApplication.translate("ToDo", u"Hor\u00e1rio", None))
        self.maincadastrartarefarbessencial.setText(QCoreApplication.translate("ToDo", u"Essencial", None))
        self.maincadastrartarefarbsecudaria.setText(QCoreApplication.translate("ToDo", u"Secund\u00e1ria", None))
        self.maincadastrartarefarbnormal.setText(QCoreApplication.translate("ToDo", u"Normal", None))
        self.maincadastrartarefapbalterar.setText(QCoreApplication.translate("ToDo", u"Alterar", None))
        self.maincadastrartarefapbsalvar.setText(QCoreApplication.translate("ToDo", u"Salvar", None))
        self.footerlblassinatura.setText(QCoreApplication.translate("ToDo", u"(C) HENRIQUE - 2022", None))
    # retranslateUi

