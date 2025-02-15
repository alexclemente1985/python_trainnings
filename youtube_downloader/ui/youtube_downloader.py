# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'youtube_downloader.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)
from qrc import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.VideoDisplay))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 49, 20, 255), stop:1 rgba(112, 23, 10, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border-radius: 8px;\n"
"	color: rgb(198, 40, 17);\n"
"	font-size: 16px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-size: 18px;\n"
"	color: rgb(198, 40, 17);\n"
"	font-weight: 600;\n"
"	border-radius: 8px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: #fff;\n"
"	background-color: rgb(198, 40, 17);\n"
"}\n"
"\n"
"#btn_converter{\n"
"	min-width: 200px;\n"
"}")
        self.tab_download = QWidget()
        self.tab_download.setObjectName(u"tab_download")
        self.verticalLayout_4 = QVBoxLayout(self.tab_download)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_logo = QFrame(self.tab_download)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setStyleSheet(u"#frame_logo{\n"
"	background-color: rgba(255,255,255,0.3);\n"
"	border-radius: 8px;\n"
"}")
        self.frame_logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_logo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img_logo = QLabel(self.frame_logo)
        self.img_logo.setObjectName(u"img_logo")

        self.verticalLayout.addWidget(self.img_logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lbl_logo = QLabel(self.frame_logo)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setStyleSheet(u"")
        self.lbl_logo.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout.addWidget(self.lbl_logo)


        self.verticalLayout_4.addWidget(self.frame_logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_radiobtns = QFrame(self.tab_download)
        self.frame_radiobtns.setObjectName(u"frame_radiobtns")
        self.frame_radiobtns.setStyleSheet(u"QRadioButton{\n"
"	background-color: white;\n"
"	border-radius: 8px;\n"
"	font-size: 16px;\n"
"	color: rgb(198, 40, 17);\n"
"	font-weight: 500;\n"
"	min-width: 75px;\n"
"}")
        self.frame_radiobtns.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_radiobtns.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_radiobtns)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rdb_audio = QRadioButton(self.frame_radiobtns)
        self.rdb_audio.setObjectName(u"rdb_audio")
        self.rdb_audio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rdb_audio.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.rdb_audio.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.rdb_audio)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.rdb_video = QRadioButton(self.frame_radiobtns)
        self.rdb_video.setObjectName(u"rdb_video")

        self.horizontalLayout.addWidget(self.rdb_video)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.rdb_playlist = QRadioButton(self.frame_radiobtns)
        self.rdb_playlist.setObjectName(u"rdb_playlist")

        self.horizontalLayout.addWidget(self.rdb_playlist)


        self.verticalLayout_4.addWidget(self.frame_radiobtns, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.frame_link = QFrame(self.tab_download)
        self.frame_link.setObjectName(u"frame_link")
        self.frame_link.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_link.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_link)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_info = QLabel(self.frame_link)
        self.lbl_info.setObjectName(u"lbl_info")

        self.verticalLayout_2.addWidget(self.lbl_info)

        self.txt_link = QLineEdit(self.frame_link)
        self.txt_link.setObjectName(u"txt_link")
        self.txt_link.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(198, 40, 17);\n"
"font-size: 14px;\n"
"border-radius: 8px;\n"
"min-height: 25px;")

        self.verticalLayout_2.addWidget(self.txt_link)


        self.verticalLayout_4.addWidget(self.frame_link)

        self.btn_download = QPushButton(self.tab_download)
        self.btn_download.setObjectName(u"btn_download")
        self.btn_download.setMinimumSize(QSize(200, 30))
        self.btn_download.setStyleSheet(u"#btn_download{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-size: 18px;\n"
"	color: rgb(198, 40, 17);\n"
"	font-weight: 600;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"#btn_download::hover{\n"
"	color: #fff;\n"
"	background-color: rgb(198, 40, 17);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_download, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_download, "")
        self.tab_video = QWidget()
        self.tab_video.setObjectName(u"tab_video")
        self.verticalLayout_8 = QVBoxLayout(self.tab_video)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_logo2 = QFrame(self.tab_video)
        self.frame_logo2.setObjectName(u"frame_logo2")
        self.frame_logo2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255,255,255,0.3);\n"
"	border-radius: 8px;\n"
"}")
        self.frame_logo2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_logo2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_logo2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.img_logo_3 = QLabel(self.frame_logo2)
        self.img_logo_3.setObjectName(u"img_logo_3")

        self.verticalLayout_6.addWidget(self.img_logo_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lbl_logo_3 = QLabel(self.frame_logo2)
        self.lbl_logo_3.setObjectName(u"lbl_logo_3")
        self.lbl_logo_3.setStyleSheet(u"background-color: transparent;")
        self.lbl_logo_3.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_6.addWidget(self.lbl_logo_3)


        self.verticalLayout_8.addWidget(self.frame_logo2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_video = QFrame(self.tab_video)
        self.frame_video.setObjectName(u"frame_video")
        self.frame_video.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_video.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_video)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_video = QLabel(self.frame_video)
        self.lbl_video.setObjectName(u"lbl_video")

        self.verticalLayout_7.addWidget(self.lbl_video)

        self.frame_2 = QFrame(self.frame_video)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"min-width: 100px;\n"
"min-height: 30px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_video = QLineEdit(self.frame_2)
        self.txt_video.setObjectName(u"txt_video")

        self.horizontalLayout_2.addWidget(self.txt_video)

        self.btn_video_open = QPushButton(self.frame_2)
        self.btn_video_open.setObjectName(u"btn_video_open")
        self.btn_video_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_video_open.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_video_open)


        self.verticalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_8.addWidget(self.frame_video)

        self.frame_time = QFrame(self.tab_video)
        self.frame_time.setObjectName(u"frame_time")
        self.frame_time.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 600;\n"
"	\n"
"}")
        self.frame_time.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_time.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_time)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_start = QLabel(self.frame_time)
        self.lbl_start.setObjectName(u"lbl_start")

        self.gridLayout.addWidget(self.lbl_start, 0, 0, 1, 1)

        self.lbl_end = QLabel(self.frame_time)
        self.lbl_end.setObjectName(u"lbl_end")

        self.gridLayout.addWidget(self.lbl_end, 0, 1, 1, 1)

        self.txt_start = QLineEdit(self.frame_time)
        self.txt_start.setObjectName(u"txt_start")

        self.gridLayout.addWidget(self.txt_start, 1, 0, 1, 1)

        self.txt_end = QLineEdit(self.frame_time)
        self.txt_end.setObjectName(u"txt_end")

        self.gridLayout.addWidget(self.txt_end, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_time)

        self.btn_converter = QPushButton(self.tab_video)
        self.btn_converter.setObjectName(u"btn_converter")
        self.btn_converter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_converter.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.btn_converter, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab_video, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Youtube Downloader", None))
        self.img_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/youtube_logo.png\"/></p></body></html>", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Downloader</span></p></body></html>", None))
        self.rdb_audio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.rdb_video.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.rdb_playlist.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.lbl_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Cole o link do v\u00eddeo na caixa abaixo</span></p></body></html>", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_download), QCoreApplication.translate("MainWindow", u"Download", None))
        self.img_logo_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/youtube_logo.png\"/></p></body></html>", None))
        self.lbl_logo_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Downloader</span></p></body></html>", None))
        self.lbl_video.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Cortar partes de um v\u00eddeo</span></p></body></html>", None))
        self.btn_video_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.lbl_start.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Tempo inicial</span></p></body></html>", None))
        self.lbl_end.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Tempo final</span></p></body></html>", None))
        self.btn_converter.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_video), QCoreApplication.translate("MainWindow", u"V\u00eddeo", None))
    # retranslateUi

