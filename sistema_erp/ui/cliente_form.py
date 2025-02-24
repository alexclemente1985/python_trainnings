# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente_form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import ui.icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(496, 274)
        self.lbl_nome = QLabel(Form)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(50, 40, 58, 16))
        self.txt_nome = QLineEdit(Form)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(140, 40, 301, 21))
        self.txt_cidade = QLineEdit(Form)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setGeometry(QRect(140, 120, 301, 21))
        self.lbl_cidade = QLabel(Form)
        self.lbl_cidade.setObjectName(u"lbl_cidade")
        self.lbl_cidade.setGeometry(QRect(50, 120, 58, 16))
        self.txt_telefone = QLineEdit(Form)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(140, 80, 301, 21))
        self.lbl_telefone = QLabel(Form)
        self.lbl_telefone.setObjectName(u"lbl_telefone")
        self.lbl_telefone.setGeometry(QRect(50, 80, 58, 16))
        self.btn_cliente_cadastrar = QPushButton(Form)
        self.btn_cliente_cadastrar.setObjectName(u"btn_cliente_cadastrar")
        self.btn_cliente_cadastrar.setGeometry(QRect(290, 170, 81, 81))
        self.btn_cliente_cadastrar.setStyleSheet(u"image: url(:/icons_cliente/cadastrar.png)")
        self.btn_cliente_cancelar = QPushButton(Form)
        self.btn_cliente_cancelar.setObjectName(u"btn_cliente_cancelar")
        self.btn_cliente_cancelar.setGeometry(QRect(200, 170, 81, 81))
        self.btn_cliente_cancelar.setStyleSheet(u"image: url(:/icons_cliente/cancelar.png)")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_nome.setText(QCoreApplication.translate("Form", u"Nome", None))
        self.lbl_cidade.setText(QCoreApplication.translate("Form", u"Cidade", None))
        self.lbl_telefone.setText(QCoreApplication.translate("Form", u"Telefone", None))
        self.btn_cliente_cadastrar.setText("")
        self.btn_cliente_cancelar.setText("")
    # retranslateUi

