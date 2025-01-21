# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sistema.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

import sys
from os.path import dirname, realpath, join
import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AutoReg

from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(879, 676)
        font = QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_arquivo = QPushButton(self.centralwidget)
        self.bt_arquivo.setObjectName(u"bt_arquivo")
        self.bt_arquivo.setGeometry(QRect(700, 40, 141, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setStrikeOut(False)
        self.bt_arquivo.setFont(font1)
        self.bt_predicao = QPushButton(self.centralwidget)
        self.bt_predicao.setObjectName(u"bt_predicao")
        self.bt_predicao.setGeometry(QRect(700, 550, 141, 51))
        self.bt_predicao.setFont(font1)
        self.txt_predicao = QLineEdit(self.centralwidget)
        self.txt_predicao.setObjectName(u"txt_predicao")
        self.txt_predicao.setGeometry(QRect(30, 550, 641, 51))
        self.lb_titulo = QLabel(self.centralwidget)
        self.lb_titulo.setObjectName(u"lb_titulo")
        self.lb_titulo.setGeometry(QRect(30, 30, 371, 51))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.lb_titulo.setFont(font2)
        self.txt_tfaturado = QLineEdit(self.centralwidget)
        self.txt_tfaturado.setObjectName(u"txt_tfaturado")
        self.txt_tfaturado.setGeometry(QRect(410, 50, 181, 31))
        self.lb_tfaturado = QLabel(self.centralwidget)
        self.lb_tfaturado.setObjectName(u"lb_tfaturado")
        self.lb_tfaturado.setGeometry(QRect(410, 30, 181, 16))
        self.sp_colunas = QSpinBox(self.centralwidget)
        self.sp_colunas.setObjectName(u"sp_colunas")
        self.sp_colunas.setGeometry(QRect(631, 51, 41, 31))
        self.lb_tipopred = QLabel(self.centralwidget)
        self.lb_tipopred.setObjectName(u"lb_tipopred")
        self.lb_tipopred.setGeometry(QRect(700, 100, 131, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.lb_tipopred.setFont(font3)
        self.tb_faturamento = QTableWidget(self.centralwidget)
        if (self.tb_faturamento.columnCount() < 3):
            self.tb_faturamento.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_faturamento.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_faturamento.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_faturamento.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tb_faturamento.setObjectName(u"tb_faturamento")
        self.tb_faturamento.setGeometry(QRect(30, 100, 641, 421))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(700, 140, 141, 381))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rb_media = QRadioButton(self.widget)
        self.rb_media.setObjectName(u"rb_media")
        self.rb_media.setChecked(True)

        self.verticalLayout.addWidget(self.rb_media)

        self.rb_dpadrao = QRadioButton(self.widget)
        self.rb_dpadrao.setObjectName(u"rb_dpadrao")

        self.verticalLayout.addWidget(self.rb_dpadrao)

        self.rb_mediap = QRadioButton(self.widget)
        self.rb_mediap.setObjectName(u"rb_mediap")

        self.verticalLayout.addWidget(self.rb_mediap)

        self.rb_segdados = QRadioButton(self.widget)
        self.rb_segdados.setObjectName(u"rb_segdados")

        self.verticalLayout.addWidget(self.rb_segdados)

        self.rb_reglin = QRadioButton(self.widget)
        self.rb_reglin.setObjectName(u"rb_reglin")

        self.verticalLayout.addWidget(self.rb_reglin)

        self.rb_seriestp = QRadioButton(self.widget)
        self.rb_seriestp.setObjectName(u"rb_seriestp")

        self.verticalLayout.addWidget(self.rb_seriestp)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 879, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_arquivo.setText(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.bt_predicao.setText(QCoreApplication.translate("MainWindow", u"Predizer", None))
        self.lb_titulo.setText(QCoreApplication.translate("MainWindow", u"Predi\u00e7\u00e3o de Faturamento", None))
        self.lb_tfaturado.setText(QCoreApplication.translate("MainWindow", u"Total Faturado", None))
        self.lb_tipopred.setText(QCoreApplication.translate("MainWindow", u"Tipo de Predi\u00e7\u00e3o", None))
        ___qtablewidgetitem = self.tb_faturamento.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ano", None));
        ___qtablewidgetitem1 = self.tb_faturamento.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mes", None));
        ___qtablewidgetitem2 = self.tb_faturamento.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Faturamento", None));
        self.rb_media.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia", None))
        self.rb_dpadrao.setText(QCoreApplication.translate("MainWindow", u"Desvio Padr\u00e3o", None))
        self.rb_mediap.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia Ponderada", None))
        self.rb_segdados.setText(QCoreApplication.translate("MainWindow", u"Segrega\u00e7\u00e3o de dados", None))
        self.rb_reglin.setText(QCoreApplication.translate("MainWindow", u"Regress\u00e3o Linear", None))
        self.rb_seriestp.setText(QCoreApplication.translate("MainWindow", u"S\u00e9ries Temporais", None))
    # retranslateUi

