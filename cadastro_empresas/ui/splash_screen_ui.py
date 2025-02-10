# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)

class Ui_splash_screen(object):
    def setupUi(self, splash_screen):
        if not splash_screen.objectName():
            splash_screen.setObjectName(u"splash_screen")
        splash_screen.resize(358, 352)
        self.centralwidget = QWidget(splash_screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.circular_progressBar = QFrame(self.centralwidget)
        self.circular_progressBar.setObjectName(u"circular_progressBar")
        self.circular_progressBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.circular_progressBar.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBg = QFrame(self.circular_progressBar)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(20, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgb(255,255,255)\n"
"}")
        self.circularBg.setFrameShape(QFrame.Shape.StyledPanel)
        self.circularBg.setFrameShadow(QFrame.Shadow.Raised)
        self.circularProgress = QFrame(self.circularBg)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(0, 0, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255,0,127,0), stop:0.750 rgba(85,170,255,255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.Shape.StyledPanel)
        self.circularProgress.setFrameShadow(QFrame.Shadow.Raised)
        self.container = QFrame(self.circularProgress)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(15, 15, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(0,84,126)\n"
"}")
        self.container.setFrameShape(QFrame.Shape.StyledPanel)
        self.container.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 30, 151, 201))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.widget)
        self.lbl_title.setObjectName(u"lbl_title")

        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)

        self.lbl_percentual = QLabel(self.widget)
        self.lbl_percentual.setObjectName(u"lbl_percentual")
        font = QFont()
        font.setPointSize(75)
        self.lbl_percentual.setFont(font)
        self.lbl_percentual.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.lbl_percentual, 1, 0, 1, 1)

        self.lbl_loading = QLabel(self.widget)
        self.lbl_loading.setObjectName(u"lbl_loading")
        self.lbl_loading.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(0,170,255);\n"
"	color: rgb(255,255,255);\n"
"}")

        self.gridLayout.addWidget(self.lbl_loading, 2, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(255,255,255)\n"
"}")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.circular_progressBar)

        splash_screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splash_screen)

        QMetaObject.connectSlotsByName(splash_screen)
    # setupUi

    def retranslateUi(self, splash_screen):
        splash_screen.setWindowTitle(QCoreApplication.translate("splash_screen", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("splash_screen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">CADASTRO DE EMPRESAS</span></p></body></html>", None))
        self.lbl_percentual.setText(QCoreApplication.translate("splash_screen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">0%</span></p></body></html>", None))
        self.lbl_loading.setText(QCoreApplication.translate("splash_screen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Loading...</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("splash_screen", u"<html><head/><body><p align=\"center\">ACP Projects</p></body></html>", None))
    # retranslateUi

