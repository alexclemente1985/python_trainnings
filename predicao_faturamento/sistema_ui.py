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

        self.bt_arquivo.clicked.connect(self.openfile)
        self.bt_predicao.clicked.connect(self.predicao)

    # setupUi

    def openfile(self):
        #Localizando o caminho do arquivo
        Tk().withdraw()
        path = askopenfilename(title='Escolha o arquivo csv')
        self.all_data = pd.read_csv(path)

        #Carregando o arquivo na tabela tb_faturamento
        numColumns = self.sp_colunas.value()

        if numColumns == 0:
            numRows = len(self.all_data.index)
        else:
            numRows = numColumns

        # Setando o número de linhas e colunas
        self.tb_faturamento.setColumnCount(len(self.all_data.columns))
        self.tb_faturamento.setRowCount(numRows)

        # Setando o cabeçalho da tabela
        self.tb_faturamento.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                #adicionando informações em cada célula da tabela
                self.tb_faturamento.setItem(i,j,QTableWidgetItem(str(self.all_data.iat[i,j])))

        #Redimensionando a tabela de maneira correta
        self.tb_faturamento.resizeColumnToContents
        self.tb_faturamento.resizeRowsToContents

        # Soma do faturamento
        ## % permite inserir o valor dentro da string, com duas casas decimais
        soma_faturamento = str('R$%0.02f' %sum(self.all_data['Faturamento']))

        self.txt_tfaturado.setText(soma_faturamento)

    def predicao(self):
        df = self.all_data

        ## Média ##
        if self.rb_media.isChecked() == True:
            media = df['Faturamento'].mean()
            #predicao = 'Nos próximos meses será faturado R$ '+str('%0.02f' %media)+'/mês em média'
            predicao = f'Nos próximos meses será faturado R$ {str(round(media,2))}/mês em média'
            self.txt_predicao.setText(predicao)

        ## Desvio Padrão ##
        elif self.rb_dpadrao.isChecked() == True:
            media = df['Faturamento'].mean()
            desvpad = df['Faturamento'].std()
            coe_var = (desvpad/media)*100
            
            predicao = f'Predição de R$ {str(round(media,2))}/mês podendo variar em torno de {str(round(coe_var,2))}%'
            self.txt_predicao.setText(predicao)
        
        ## Média Ponderada ##
        elif self.rb_mediap.isChecked() == True:
            lista = np.transpose((np.array([df['Faturamento'].tail(), np.arange(1,6)])))
            
            df_ult = pd.DataFrame(lista, columns=['Ultimos','Pesos'])

            df_ult['Ponderado'] = df_ult['Ultimos']*df_ult['Pesos']

            med_pond = df_ult['Ponderado'].sum()/df_ult['Pesos'].sum()

            predicao = f'Predição ponderada de R$ {str(round(med_pond,2))} para os próximos meses.'
            self.txt_predicao.setText(predicao)
        
        ## Segregação de dados ##
        elif self.rb_segdados.isChecked() == True:
            df_janeiro = df.loc[df['Mes'] == 1]
            med_seg = df_janeiro['Faturamento'].mean()
            predicao = 'Predição segregada de R$ ' + str('%0.02f' %med_seg) + ' para janeiro.'
            self.txt_predicao.setText(predicao)
        
        ## Regressão Linear ##
        elif self.rb_reglin.isChecked() == True:
            coefficients = np.polyfit(df.index, df['Faturamento'], 1)
            a = coefficients[0]
            b = coefficients[1]

            jan_reta = a * 36 + b
            predicao = 'Predição por regressão de R$ ' + str('%0.02f' %jan_reta) + ' para janeiro.'
            self.txt_predicao.setText(predicao)
        
        ## Séries Temporais ##
        elif self.rb_seriestp.isChecked() == True:
            ### Criação do modelo de regressão linear ###
            model = AutoReg(df['Faturamento'], lags=1) #old_names só foi utilizado por conta de um aviso da próxima versão
            ### Treinando o modelo ###
            model_fit = model.fit()
            ### Predição dos dados (2 novos valores após o final da lista) ###
            yhat = model_fit.predict(len(df['Faturamento']), len(df['Faturamento'])+2)
            pred = np.array(yhat)
            predicao = 'Predição por serie temporal de R$ ' + str('%0.02f' %pred[0]) + ' para janeiro e R$ ' + str('%0.02f' %pred[1]) + ' para fevereiro.'
            self.txt_predicao.setText(predicao)



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

