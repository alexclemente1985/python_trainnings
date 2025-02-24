# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import ui.icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(653, 495)
        self.btn_cliente_adicionar = QPushButton(Form)
        self.btn_cliente_adicionar.setObjectName(u"btn_cliente_adicionar")
        self.btn_cliente_adicionar.setGeometry(QRect(10, 10, 81, 81))
        self.btn_cliente_adicionar.setStyleSheet(u"image: url(:/icons_cliente/adicionar.png);")
        self.btn_cliente_alterar = QPushButton(Form)
        self.btn_cliente_alterar.setObjectName(u"btn_cliente_alterar")
        self.btn_cliente_alterar.setGeometry(QRect(100, 10, 81, 81))
        self.btn_cliente_alterar.setStyleSheet(u"image: url(:/icons_cliente/alterar.png)")
        self.btn_cliente_consultar = QPushButton(Form)
        self.btn_cliente_consultar.setObjectName(u"btn_cliente_consultar")
        self.btn_cliente_consultar.setGeometry(QRect(190, 10, 81, 81))
        self.btn_cliente_consultar.setStyleSheet(u"image: url(:/icons_cliente/consultar.png)")
        self.btn_cliente_excluir = QPushButton(Form)
        self.btn_cliente_excluir.setObjectName(u"btn_cliente_excluir")
        self.btn_cliente_excluir.setGeometry(QRect(280, 10, 81, 81))
        self.btn_cliente_excluir.setStyleSheet(u"image: url(:/icons_cliente/excluir.png)")
        self.btn_cliente_retornar = QPushButton(Form)
        self.btn_cliente_retornar.setObjectName(u"btn_cliente_retornar")
        self.btn_cliente_retornar.setGeometry(QRect(560, 10, 81, 81))
        self.btn_cliente_retornar.setStyleSheet(u"image: url(:/icons_cliente/retornar.png)")
        self.lbl_cliente_nome = QLabel(Form)
        self.lbl_cliente_nome.setObjectName(u"lbl_cliente_nome")
        self.lbl_cliente_nome.setGeometry(QRect(70, 100, 91, 16))
        self.txt_cliente_nome = QLineEdit(Form)
        self.txt_cliente_nome.setObjectName(u"txt_cliente_nome")
        self.txt_cliente_nome.setGeometry(QRect(190, 100, 241, 21))
        self.btn_cliente_pesquisar = QPushButton(Form)
        self.btn_cliente_pesquisar.setObjectName(u"btn_cliente_pesquisar")
        self.btn_cliente_pesquisar.setGeometry(QRect(450, 90, 31, 41))
        self.btn_cliente_pesquisar.setStyleSheet(u"image: url(:/icons_cliente/pesquisar.png)")
        self.tb_cliente = QTableWidget(Form)
        if (self.tb_cliente.columnCount() < 4):
            self.tb_cliente.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_cliente.setObjectName(u"tb_cliente")
        self.tb_cliente.setGeometry(QRect(10, 150, 631, 331))
        self.btn_cliente_filtrar = QPushButton(Form)
        self.btn_cliente_filtrar.setObjectName(u"btn_cliente_filtrar")
        self.btn_cliente_filtrar.setGeometry(QRect(490, 90, 31, 41))
        self.btn_cliente_filtrar.setStyleSheet(u"image: url(:/icons_cliente/filtro.png)")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_cliente_adicionar.setText("")
        self.btn_cliente_alterar.setText("")
        self.btn_cliente_consultar.setText("")
        self.btn_cliente_excluir.setText("")
        self.btn_cliente_retornar.setText("")
        self.lbl_cliente_nome.setText(QCoreApplication.translate("Form", u"Nome cliente:", None))
        self.btn_cliente_pesquisar.setText("")
        ___qtablewidgetitem = self.tb_cliente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tb_cliente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nome", None));
        ___qtablewidgetitem2 = self.tb_cliente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Telefone", None));
        ___qtablewidgetitem3 = self.tb_cliente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Cidade", None));
        self.btn_cliente_filtrar.setText("")
    # retranslateUi

