# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_teste.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(424, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"}\n"
"QLineEdit{\n"
"	border-radius:4px;\n"
"	border: 1px solid rgb(233,233,233);\n"
"	border-bottom: 3px solid rgb(233,233,233);\n"
"}\n"
"\n"                                         
"QLabel{\n"
"	color: rgb(150,150,150);\n"
"	font-size: 16px;\n"
"	font-family:  \"Cooper\";\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(51, 99, 255);\n"
"	border-radius: 4px;\n"
"	border: 1px solid rgb(51, 99, 255);\n"
"	border-bottom: 3px solid  rgb(0, 11, 213);\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"		\n"
"	background-color: rgb(42, 42, 42);\n"
"\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lbl_user = QLabel(self.frame)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.lbl_user.setScaledContents(False)
        self.lbl_user.setAlignment(Qt.AlignCenter)
        self.lbl_user.setMargin(55)

        self.verticalLayout.addWidget(self.lbl_user)

        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        font = QFont()
        font.setPointSize(11)
        self.txt_user.setFont(font)
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_user)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_password = QLabel(self.frame_2)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setStyleSheet(u"background-color: rgb(244, 244, 244);")

        self.verticalLayout_2.addWidget(self.lbl_password)

        self.txt_password = QLineEdit(self.frame_2)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setFont(font)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_password)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.btn_login = QPushButton(self.centralwidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(160, 29))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_login, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">TELA DE LOGIN</span></p></body></html>", None))
        self.lbl_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/user.png\"/></p></body></html>", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o usu\u00e1rio...", None))
        self.lbl_password.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/password.png\"/></p></body></html>", None))
        self.txt_password.setInputMask("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe a sua senha...", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi

