# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)
from pathlib import Path

## ---- Importação da imagem convertida para .py
import imgs.Youtube #Youtube_rc

## ---- Importação da lib para download de vídeos Youtube
#from mhyt import yt_download

## Correção do problema do mhyt (não consegue baixar mais nada)
import pytube
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(659, 368)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 278, 131, 41))
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 178, 49, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 218, 49, 16))
        self.txt_link = QLineEdit(Dialog)
        self.txt_link.setObjectName(u"txt_link")
        self.txt_link.setGeometry(QRect(80, 178, 491, 21))
        self.txt_title = QLineEdit(Dialog)
        self.txt_title.setObjectName(u"txt_title")
        self.txt_title.setGeometry(QRect(80, 218, 491, 21))
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(70, 268, 55, 26))
        self.radioButton.setFont(font)
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(70, 300, 55, 26))
        self.radioButton_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 110, 141, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 10, 281, 140))
        self.label_4.setMaximumSize(QSize(1800, 140))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        # Ação do botão de download
        self.pushButton.clicked.connect(self.download)
    # setupUi

    ## -- Função de download
    def download(self):
        url = self.txt_link.text()
        #title = self.txt_title.text()
        yt = pytube.YouTube(url)

        if self.radioButton.isChecked() == True:
            try:
                #title_mp3 = title+".mp3"
                #yt_download(url, title_mp3, ismusic=True, codec="mp3")

                audio = yt.streams.filter(only_audio=True).first()
                out_file = audio.download()

                #salvando no formato .mp3 (lib pytube sempre salva como .mp4)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
            except Exception as error:
                print(f'Falha no download: ', repr(error))


        elif self.radioButton_2.isChecked() == True:
            #title_mp4 = title+".mp4"
            #yt_download(url,title_mp4)
            video = yt.streams.get_highest_resolution()
            video.download()




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Download", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Link: ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"T\u00edtulo", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"MP3", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"MP4", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Downloads", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/youtube/ytube.png\"/></p></body></html>", None))
    # retranslateUi

