# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(907, 644)
        Form.setStyleSheet(u"QWidget{\n"
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
"}")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_user_2 = QLabel(self.frame_6)
        self.lbl_user_2.setObjectName(u"lbl_user_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_user_2.sizePolicy().hasHeightForWidth())
        self.lbl_user_2.setSizePolicy(sizePolicy)
        self.lbl_user_2.setPixmap(QPixmap(u":/imgs/user.png"))
        self.lbl_user_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.lbl_user_2)

        self.le_user_2 = QLineEdit(self.frame_6)
        self.le_user_2.setObjectName(u"le_user_2")
        sizePolicy.setHeightForWidth(self.le_user_2.sizePolicy().hasHeightForWidth())
        self.le_user_2.setSizePolicy(sizePolicy)
        self.le_user_2.setMinimumSize(QSize(0, 49))
        self.le_user_2.setMaximumSize(QSize(16777215, 49))
        self.le_user_2.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.le_user_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.le_user_2)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_pass_2 = QLabel(self.frame_3)
        self.lbl_pass_2.setObjectName(u"lbl_pass_2")
        sizePolicy.setHeightForWidth(self.lbl_pass_2.sizePolicy().hasHeightForWidth())
        self.lbl_pass_2.setSizePolicy(sizePolicy)
        self.lbl_pass_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.lbl_pass_2)

        self.le_pass_2 = QLineEdit(self.frame_3)
        self.le_pass_2.setObjectName(u"le_pass_2")
        sizePolicy.setHeightForWidth(self.le_pass_2.sizePolicy().hasHeightForWidth())
        self.le_pass_2.setSizePolicy(sizePolicy)
        self.le_pass_2.setMinimumSize(QSize(0, 49))
        self.le_pass_2.setMaximumSize(QSize(16777215, 49))
        self.le_pass_2.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.le_pass_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.le_pass_2)

        self.btn_login_2 = QPushButton(self.frame_3)
        self.btn_login_2.setObjectName(u"btn_login_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_login_2.sizePolicy().hasHeightForWidth())
        self.btn_login_2.setSizePolicy(sizePolicy1)
        self.btn_login_2.setMinimumSize(QSize(200, 40))
        self.btn_login_2.setBaseSize(QSize(200, 200))
        self.btn_login_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_login_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_user_2.setText("")
        self.le_user_2.setPlaceholderText(QCoreApplication.translate("Form", u"Informe o nome de usu\u00e1rio...", None))
        self.lbl_pass_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/password.png\"/></p></body></html>", None))
        self.le_pass_2.setPlaceholderText(QCoreApplication.translate("Form", u"Informe a sua senha...", None))
        self.btn_login_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

