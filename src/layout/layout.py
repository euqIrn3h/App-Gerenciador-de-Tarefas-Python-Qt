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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_ToDo(object):
    def setupUi(self, ToDo):
        if not ToDo.objectName():
            ToDo.setObjectName(u"ToDo")
        ToDo.resize(573, 520)
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

        self.verticalLayout.addWidget(self.pbhome)

        self.pbtarefas = QPushButton(self.lcontainer)
        self.pbtarefas.setObjectName(u"pbtarefas")
        self.pbtarefas.setFont(font)

        self.verticalLayout.addWidget(self.pbtarefas)

        self.pbcontas = QPushButton(self.lcontainer)
        self.pbcontas.setObjectName(u"pbcontas")
        self.pbcontas.setFont(font)

        self.verticalLayout.addWidget(self.pbcontas)

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
        self.mainpghome.setStyleSheet(u"color: rgb(0, 0, 0);\n"
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
        self.horizontalLayout_5 = QHBoxLayout(self.mainpgtarefas)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.maintarefasframehorario = QFrame(self.mainpgtarefas)
        self.maintarefasframehorario.setObjectName(u"maintarefasframehorario")
        self.maintarefasframehorario.setMinimumSize(QSize(80, 0))
        self.maintarefasframehorario.setMaximumSize(QSize(80, 16777215))
        self.maintarefasframehorario.setFrameShape(QFrame.StyledPanel)
        self.maintarefasframehorario.setFrameShadow(QFrame.Raised)
        self.maintarefaspb00_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb00_00.setObjectName(u"maintarefaspb00_00")
        self.maintarefaspb00_00.setGeometry(QRect(0, 24, 80, 16))
        self.maintarefaspb00_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb00_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb02_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb02_00.setObjectName(u"maintarefaspb02_00")
        self.maintarefaspb02_00.setGeometry(QRect(0, 53, 80, 16))
        self.maintarefaspb02_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb02_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb04_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb04_00.setObjectName(u"maintarefaspb04_00")
        self.maintarefaspb04_00.setGeometry(QRect(0, 82, 80, 16))
        self.maintarefaspb04_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb04_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb06_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb06_00.setObjectName(u"maintarefaspb06_00")
        self.maintarefaspb06_00.setGeometry(QRect(0, 111, 80, 16))
        self.maintarefaspb06_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb06_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb07_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb07_00.setObjectName(u"maintarefaspb07_00")
        self.maintarefaspb07_00.setGeometry(QRect(0, 126, 80, 16))
        self.maintarefaspb07_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb07_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb10_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb10_00.setObjectName(u"maintarefaspb10_00")
        self.maintarefaspb10_00.setGeometry(QRect(0, 170, 80, 16))
        self.maintarefaspb10_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb10_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb12_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb12_00.setObjectName(u"maintarefaspb12_00")
        self.maintarefaspb12_00.setGeometry(QRect(0, 199, 80, 16))
        self.maintarefaspb12_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb12_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb14_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb14_00.setObjectName(u"maintarefaspb14_00")
        self.maintarefaspb14_00.setGeometry(QRect(0, 228, 80, 16))
        self.maintarefaspb14_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb14_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb16_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb16_00.setObjectName(u"maintarefaspb16_00")
        self.maintarefaspb16_00.setGeometry(QRect(0, 257, 80, 16))
        self.maintarefaspb16_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb16_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb17_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb17_00.setObjectName(u"maintarefaspb17_00")
        self.maintarefaspb17_00.setGeometry(QRect(0, 272, 80, 16))
        self.maintarefaspb17_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb17_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb18_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb18_00.setObjectName(u"maintarefaspb18_00")
        self.maintarefaspb18_00.setGeometry(QRect(0, 286, 80, 16))
        self.maintarefaspb18_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb18_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb20_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb20_00.setObjectName(u"maintarefaspb20_00")
        self.maintarefaspb20_00.setGeometry(QRect(0, 315, 80, 16))
        self.maintarefaspb20_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb20_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb23_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb23_00.setObjectName(u"maintarefaspb23_00")
        self.maintarefaspb23_00.setGeometry(QRect(0, 359, 80, 16))
        self.maintarefaspb23_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb23_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb21_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb21_00.setObjectName(u"maintarefaspb21_00")
        self.maintarefaspb21_00.setGeometry(QRect(0, 330, 80, 16))
        self.maintarefaspb21_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb21_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb19_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb19_00.setObjectName(u"maintarefaspb19_00")
        self.maintarefaspb19_00.setGeometry(QRect(0, 301, 80, 16))
        self.maintarefaspb19_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb19_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb15_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb15_00.setObjectName(u"maintarefaspb15_00")
        self.maintarefaspb15_00.setGeometry(QRect(0, 242, 80, 16))
        self.maintarefaspb15_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb15_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb05_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb05_00.setObjectName(u"maintarefaspb05_00")
        self.maintarefaspb05_00.setGeometry(QRect(0, 97, 80, 16))
        self.maintarefaspb05_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb05_00.setMaximumSize(QSize(80, 16777215))
        self.mainpgtarefaspb03_00 = QPushButton(self.maintarefasframehorario)
        self.mainpgtarefaspb03_00.setObjectName(u"mainpgtarefaspb03_00")
        self.mainpgtarefaspb03_00.setGeometry(QRect(0, 68, 80, 16))
        self.mainpgtarefaspb03_00.setMinimumSize(QSize(0, 16))
        self.mainpgtarefaspb03_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb01_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb01_00.setObjectName(u"maintarefaspb01_00")
        self.maintarefaspb01_00.setGeometry(QRect(0, 39, 80, 16))
        self.maintarefaspb01_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb01_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb13_1 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb13_1.setObjectName(u"maintarefaspb13_1")
        self.maintarefaspb13_1.setGeometry(QRect(0, 213, 80, 16))
        self.maintarefaspb13_1.setMinimumSize(QSize(0, 16))
        self.maintarefaspb13_1.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb11_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb11_00.setObjectName(u"maintarefaspb11_00")
        self.maintarefaspb11_00.setGeometry(QRect(0, 184, 80, 16))
        self.maintarefaspb11_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb11_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb09_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb09_00.setObjectName(u"maintarefaspb09_00")
        self.maintarefaspb09_00.setGeometry(QRect(0, 155, 80, 16))
        self.maintarefaspb09_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb09_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb08_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb08_00.setObjectName(u"maintarefaspb08_00")
        self.maintarefaspb08_00.setGeometry(QRect(0, 141, 80, 16))
        self.maintarefaspb08_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb08_00.setMaximumSize(QSize(80, 16777215))
        self.maintarefaspb22_00 = QPushButton(self.maintarefasframehorario)
        self.maintarefaspb22_00.setObjectName(u"maintarefaspb22_00")
        self.maintarefaspb22_00.setGeometry(QRect(0, 344, 80, 16))
        self.maintarefaspb22_00.setMinimumSize(QSize(0, 16))
        self.maintarefaspb22_00.setMaximumSize(QSize(80, 16777215))
        self.label_12 = QLabel(self.maintarefasframehorario)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 80, 20))
        self.label_12.setMinimumSize(QSize(0, 20))
        self.label_12.setMaximumSize(QSize(80, 20))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.maintarefasframehorario)

        self.maintarefasframetarefa = QFrame(self.mainpgtarefas)
        self.maintarefasframetarefa.setObjectName(u"maintarefasframetarefa")
        self.maintarefasframetarefa.setFrameShape(QFrame.StyledPanel)
        self.maintarefasframetarefa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.maintarefasframetarefa)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.maintarefastextedit = QTextEdit(self.maintarefasframetarefa)
        self.maintarefastextedit.setObjectName(u"maintarefastextedit")
        self.maintarefastextedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.maintarefastextedit)

        self.maintarefaspbtarefaconcluida = QPushButton(self.maintarefasframetarefa)
        self.maintarefaspbtarefaconcluida.setObjectName(u"maintarefaspbtarefaconcluida")

        self.verticalLayout_5.addWidget(self.maintarefaspbtarefaconcluida)


        self.horizontalLayout_5.addWidget(self.maintarefasframetarefa)

        self.mainpages.addWidget(self.mainpgtarefas)
        self.mainpgcontas = QWidget()
        self.mainpgcontas.setObjectName(u"mainpgcontas")
        self.tableWidget = QTableWidget(self.mainpgcontas)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 70, 256, 192))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mainpages.addWidget(self.mainpgcontas)
        self.mainpgcalendario = QWidget()
        self.mainpgcalendario.setObjectName(u"mainpgcalendario")
        self.mainpgcalendario.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.mainpgcalendario)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.calendarWidget = QCalendarWidget(self.mainpgcalendario)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"\n"
"background-color:rgb(255,255,255);\n"
"color:black;\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.calendarWidget)

        self.mainpages.addWidget(self.mainpgcalendario)
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
        self.horizontalLayout_6 = QHBoxLayout(self.mainpgcadastrartarefa)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mainctarefasframehorario_2 = QFrame(self.mainpgcadastrartarefa)
        self.mainctarefasframehorario_2.setObjectName(u"mainctarefasframehorario_2")
        self.mainctarefasframehorario_2.setMinimumSize(QSize(80, 0))
        self.mainctarefasframehorario_2.setMaximumSize(QSize(80, 16777215))
        self.mainctarefasframehorario_2.setFrameShape(QFrame.StyledPanel)
        self.mainctarefasframehorario_2.setFrameShadow(QFrame.Raised)
        self.mainctarefaspb00_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb00_1.setObjectName(u"mainctarefaspb00_1")
        self.mainctarefaspb00_1.setGeometry(QRect(0, 24, 80, 16))
        self.mainctarefaspb00_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb00_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb02_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb02_1.setObjectName(u"mainctarefaspb02_1")
        self.mainctarefaspb02_1.setGeometry(QRect(0, 53, 80, 16))
        self.mainctarefaspb02_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb02_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb04_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb04_1.setObjectName(u"mainctarefaspb04_1")
        self.mainctarefaspb04_1.setGeometry(QRect(0, 82, 80, 16))
        self.mainctarefaspb04_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb04_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb06_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb06_1.setObjectName(u"mainctarefaspb06_1")
        self.mainctarefaspb06_1.setGeometry(QRect(0, 111, 80, 16))
        self.mainctarefaspb06_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb06_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb07_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb07_1.setObjectName(u"mainctarefaspb07_1")
        self.mainctarefaspb07_1.setGeometry(QRect(0, 126, 80, 16))
        self.mainctarefaspb07_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb07_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb10_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb10_1.setObjectName(u"mainctarefaspb10_1")
        self.mainctarefaspb10_1.setGeometry(QRect(0, 170, 80, 16))
        self.mainctarefaspb10_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb10_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb12_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb12_1.setObjectName(u"mainctarefaspb12_1")
        self.mainctarefaspb12_1.setGeometry(QRect(0, 199, 80, 16))
        self.mainctarefaspb12_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb12_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb14_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb14_1.setObjectName(u"mainctarefaspb14_1")
        self.mainctarefaspb14_1.setGeometry(QRect(0, 228, 80, 16))
        self.mainctarefaspb14_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb14_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb16_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb16_1.setObjectName(u"mainctarefaspb16_1")
        self.mainctarefaspb16_1.setGeometry(QRect(0, 257, 80, 16))
        self.mainctarefaspb16_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb16_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb17_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb17_1.setObjectName(u"mainctarefaspb17_1")
        self.mainctarefaspb17_1.setGeometry(QRect(0, 272, 80, 16))
        self.mainctarefaspb17_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb17_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb18_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb18_1.setObjectName(u"mainctarefaspb18_1")
        self.mainctarefaspb18_1.setGeometry(QRect(0, 286, 80, 16))
        self.mainctarefaspb18_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb18_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb20_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb20_1.setObjectName(u"mainctarefaspb20_1")
        self.mainctarefaspb20_1.setGeometry(QRect(0, 315, 80, 16))
        self.mainctarefaspb20_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb20_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb23_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb23_1.setObjectName(u"mainctarefaspb23_1")
        self.mainctarefaspb23_1.setGeometry(QRect(0, 359, 80, 16))
        self.mainctarefaspb23_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb23_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb21_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb21_1.setObjectName(u"mainctarefaspb21_1")
        self.mainctarefaspb21_1.setGeometry(QRect(0, 330, 80, 16))
        self.mainctarefaspb21_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb21_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb19_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb19_1.setObjectName(u"mainctarefaspb19_1")
        self.mainctarefaspb19_1.setGeometry(QRect(0, 301, 80, 16))
        self.mainctarefaspb19_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb19_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb15_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb15_1.setObjectName(u"mainctarefaspb15_1")
        self.mainctarefaspb15_1.setGeometry(QRect(0, 242, 80, 16))
        self.mainctarefaspb15_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb15_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb05_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb05_1.setObjectName(u"mainctarefaspb05_1")
        self.mainctarefaspb05_1.setGeometry(QRect(0, 97, 80, 16))
        self.mainctarefaspb05_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb05_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb03_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb03_1.setObjectName(u"mainctarefaspb03_1")
        self.mainctarefaspb03_1.setGeometry(QRect(0, 68, 80, 16))
        self.mainctarefaspb03_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb03_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb01_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb01_1.setObjectName(u"mainctarefaspb01_1")
        self.mainctarefaspb01_1.setGeometry(QRect(0, 39, 80, 16))
        self.mainctarefaspb01_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb01_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb13_2 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb13_2.setObjectName(u"mainctarefaspb13_2")
        self.mainctarefaspb13_2.setGeometry(QRect(0, 213, 80, 16))
        self.mainctarefaspb13_2.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb13_2.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb11_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb11_1.setObjectName(u"mainctarefaspb11_1")
        self.mainctarefaspb11_1.setGeometry(QRect(0, 184, 80, 16))
        self.mainctarefaspb11_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb11_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb09_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb09_1.setObjectName(u"mainctarefaspb09_1")
        self.mainctarefaspb09_1.setGeometry(QRect(0, 155, 80, 16))
        self.mainctarefaspb09_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb09_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb08_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb08_1.setObjectName(u"mainctarefaspb08_1")
        self.mainctarefaspb08_1.setGeometry(QRect(0, 141, 80, 16))
        self.mainctarefaspb08_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb08_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaspb22_1 = QPushButton(self.mainctarefasframehorario_2)
        self.mainctarefaspb22_1.setObjectName(u"mainctarefaspb22_1")
        self.mainctarefaspb22_1.setGeometry(QRect(0, 344, 80, 16))
        self.mainctarefaspb22_1.setMinimumSize(QSize(0, 16))
        self.mainctarefaspb22_1.setMaximumSize(QSize(80, 16777215))
        self.mainctarefaslblhorario = QLabel(self.mainctarefasframehorario_2)
        self.mainctarefaslblhorario.setObjectName(u"mainctarefaslblhorario")
        self.mainctarefaslblhorario.setGeometry(QRect(0, 0, 80, 20))
        self.mainctarefaslblhorario.setMinimumSize(QSize(0, 20))
        self.mainctarefaslblhorario.setMaximumSize(QSize(80, 20))
        self.mainctarefaslblhorario.setFont(font)
        self.mainctarefaslblhorario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.mainctarefasframehorario_2)

        self.mainctarefasframecadastrar = QFrame(self.mainpgcadastrartarefa)
        self.mainctarefasframecadastrar.setObjectName(u"mainctarefasframecadastrar")
        self.mainctarefasframecadastrar.setFrameShape(QFrame.StyledPanel)
        self.mainctarefasframecadastrar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.mainctarefasframecadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.maincadastrartarefatextedit = QPlainTextEdit(self.mainctarefasframecadastrar)
        self.maincadastrartarefatextedit.setObjectName(u"maincadastrartarefatextedit")
        self.maincadastrartarefatextedit.setStyleSheet(u"\n"
"background-color:rgb(255,255,255);\n"
"color:black;\n"
"\n"
"")

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

        self.maincadastrartarefacombob = QComboBox(self.mainctarefasframecadastrar)
        self.maincadastrartarefacombob.setObjectName(u"maincadastrartarefacombob")
        self.maincadastrartarefacombob.setFont(font)

        self.verticalLayout_6.addWidget(self.maincadastrartarefacombob)

        self.maincadastrartarefapbsalvar = QPushButton(self.mainctarefasframecadastrar)
        self.maincadastrartarefapbsalvar.setObjectName(u"maincadastrartarefapbsalvar")
        self.maincadastrartarefapbsalvar.setFont(font)

        self.verticalLayout_6.addWidget(self.maincadastrartarefapbsalvar)


        self.horizontalLayout_6.addWidget(self.mainctarefasframecadastrar)

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
        self.pbcontas.setText(QCoreApplication.translate("ToDo", u"GASTOS", None))
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
        self.maintarefaspb00_00.setText(QCoreApplication.translate("ToDo", u"00:00", None))
        self.maintarefaspb02_00.setText(QCoreApplication.translate("ToDo", u"02:00", None))
        self.maintarefaspb04_00.setText(QCoreApplication.translate("ToDo", u"04:00", None))
        self.maintarefaspb06_00.setText(QCoreApplication.translate("ToDo", u"06:00", None))
        self.maintarefaspb07_00.setText(QCoreApplication.translate("ToDo", u"07:00", None))
        self.maintarefaspb10_00.setText(QCoreApplication.translate("ToDo", u"10:00", None))
        self.maintarefaspb12_00.setText(QCoreApplication.translate("ToDo", u"12:00", None))
        self.maintarefaspb14_00.setText(QCoreApplication.translate("ToDo", u"14:00", None))
        self.maintarefaspb16_00.setText(QCoreApplication.translate("ToDo", u"16:00", None))
        self.maintarefaspb17_00.setText(QCoreApplication.translate("ToDo", u"17:00", None))
        self.maintarefaspb18_00.setText(QCoreApplication.translate("ToDo", u"18:00", None))
        self.maintarefaspb20_00.setText(QCoreApplication.translate("ToDo", u"20:00", None))
        self.maintarefaspb23_00.setText(QCoreApplication.translate("ToDo", u"23:00", None))
        self.maintarefaspb21_00.setText(QCoreApplication.translate("ToDo", u"21:00", None))
        self.maintarefaspb19_00.setText(QCoreApplication.translate("ToDo", u"19:00", None))
        self.maintarefaspb15_00.setText(QCoreApplication.translate("ToDo", u"15:00", None))
        self.maintarefaspb05_00.setText(QCoreApplication.translate("ToDo", u"05:00", None))
        self.mainpgtarefaspb03_00.setText(QCoreApplication.translate("ToDo", u"03:00", None))
        self.maintarefaspb01_00.setText(QCoreApplication.translate("ToDo", u"01:00", None))
        self.maintarefaspb13_1.setText(QCoreApplication.translate("ToDo", u"13:00", None))
        self.maintarefaspb11_00.setText(QCoreApplication.translate("ToDo", u"11;00", None))
        self.maintarefaspb09_00.setText(QCoreApplication.translate("ToDo", u"09:00", None))
        self.maintarefaspb08_00.setText(QCoreApplication.translate("ToDo", u"08:00", None))
        self.maintarefaspb22_00.setText(QCoreApplication.translate("ToDo", u"22:00", None))
        self.label_12.setText(QCoreApplication.translate("ToDo", u"Hor\u00e1rio", None))
        self.maintarefaspbtarefaconcluida.setText(QCoreApplication.translate("ToDo", u"Tarefa conclu\u00edda", None))
        self.mainctarefaspb00_1.setText(QCoreApplication.translate("ToDo", u"00:00", None))
        self.mainctarefaspb02_1.setText(QCoreApplication.translate("ToDo", u"02:00", None))
        self.mainctarefaspb04_1.setText(QCoreApplication.translate("ToDo", u"04:00", None))
        self.mainctarefaspb06_1.setText(QCoreApplication.translate("ToDo", u"06:00", None))
        self.mainctarefaspb07_1.setText(QCoreApplication.translate("ToDo", u"07:00", None))
        self.mainctarefaspb10_1.setText(QCoreApplication.translate("ToDo", u"10:00", None))
        self.mainctarefaspb12_1.setText(QCoreApplication.translate("ToDo", u"12:00", None))
        self.mainctarefaspb14_1.setText(QCoreApplication.translate("ToDo", u"14:00", None))
        self.mainctarefaspb16_1.setText(QCoreApplication.translate("ToDo", u"16:00", None))
        self.mainctarefaspb17_1.setText(QCoreApplication.translate("ToDo", u"17:00", None))
        self.mainctarefaspb18_1.setText(QCoreApplication.translate("ToDo", u"18:00", None))
        self.mainctarefaspb20_1.setText(QCoreApplication.translate("ToDo", u"20:00", None))
        self.mainctarefaspb23_1.setText(QCoreApplication.translate("ToDo", u"23:00", None))
        self.mainctarefaspb21_1.setText(QCoreApplication.translate("ToDo", u"21:00", None))
        self.mainctarefaspb19_1.setText(QCoreApplication.translate("ToDo", u"19:00", None))
        self.mainctarefaspb15_1.setText(QCoreApplication.translate("ToDo", u"15:00", None))
        self.mainctarefaspb05_1.setText(QCoreApplication.translate("ToDo", u"05:00", None))
        self.mainctarefaspb03_1.setText(QCoreApplication.translate("ToDo", u"03:00", None))
        self.mainctarefaspb01_1.setText(QCoreApplication.translate("ToDo", u"01:00", None))
        self.mainctarefaspb13_2.setText(QCoreApplication.translate("ToDo", u"13:00", None))
        self.mainctarefaspb11_1.setText(QCoreApplication.translate("ToDo", u"11;00", None))
        self.mainctarefaspb09_1.setText(QCoreApplication.translate("ToDo", u"09:00", None))
        self.mainctarefaspb08_1.setText(QCoreApplication.translate("ToDo", u"08:00", None))
        self.mainctarefaspb22_1.setText(QCoreApplication.translate("ToDo", u"22:00", None))
        self.mainctarefaslblhorario.setText(QCoreApplication.translate("ToDo", u"Hor\u00e1rio", None))
        self.maincadastrartarefarbessencial.setText(QCoreApplication.translate("ToDo", u"Essencial", None))
        self.maincadastrartarefarbimportante.setText(QCoreApplication.translate("ToDo", u"Importante", None))
        self.maincadastrartarefarbsecudaria.setText(QCoreApplication.translate("ToDo", u"Secund\u00e1ria", None))
        self.maincadastrartarefapbsalvar.setText(QCoreApplication.translate("ToDo", u"Salvar", None))
        self.label_2.setText(QCoreApplication.translate("ToDo", u"(C) HENRIQUE - 2022", None))
    # retranslateUi

