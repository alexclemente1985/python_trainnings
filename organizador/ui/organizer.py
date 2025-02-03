# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'organizer.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from qrc import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 561)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(83, 27, 147, 255), stop:1 rgba(215, 131, 255, 255));\n"
"\n"
"border: 0;\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	min-height: 30px;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"QPushButton{\n"
"	min-height: 30px;\n"
"	min-width: 100px;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,109,159);\n"
"}\n"
"QPushButton::hover{\n"
"	color: #fff;\n"
"	background-color: rgb(0,157,235);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lbl_title = QLabel(self.frame)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.lbl_title)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_path = QLineEdit(self.frame_2)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_path)

        self.btn_open = QPushButton(self.frame_2)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(100, 30))
        self.btn_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_open)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_organize = QPushButton(self.frame)
        self.btn_organize.setObjectName(u"btn_organize")
        self.btn_organize.setMinimumSize(QSize(100, 30))
        self.btn_organize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_organize, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/_imgs/folder.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">ORGANIZADOR DE ARQUIVOS</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta --->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btn_organize.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
    # retranslateUi

