# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cad_emp_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import qrc.icons_rc

class Ui_Cad_Emp_Screen(object):
    def setupUi(self, Cad_Emp_Screen):
        if not Cad_Emp_Screen.objectName():
            Cad_Emp_Screen.setObjectName(u"Cad_Emp_Screen")
        Cad_Emp_Screen.resize(899, 639)
        self.centralwidget = QWidget(Cad_Emp_Screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMaximumSize(QSize(0, 16777215))
        self.left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_frame = QFrame(self.left_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.logo_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.logo_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.logo_frame)

        self.buttons_frame = QFrame(self.left_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.buttons_frame)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tbxPage_menu = QWidget()
        self.tbxPage_menu.setObjectName(u"tbxPage_menu")
        self.tbxPage_menu.setGeometry(QRect(0, 0, 113, 416))
        self.verticalLayout_7 = QVBoxLayout(self.tbxPage_menu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_menu_home = QPushButton(self.tbxPage_menu)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        self.btn_menu_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_menu_home)

        self.btn_menu_cadastrar = QPushButton(self.tbxPage_menu)
        self.btn_menu_cadastrar.setObjectName(u"btn_menu_cadastrar")
        self.btn_menu_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_menu_cadastrar)

        self.btn_menu_contatos = QPushButton(self.tbxPage_menu)
        self.btn_menu_contatos.setObjectName(u"btn_menu_contatos")
        self.btn_menu_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_menu_contatos)

        self.btn_menu_sobre = QPushButton(self.tbxPage_menu)
        self.btn_menu_sobre.setObjectName(u"btn_menu_sobre")
        self.btn_menu_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_menu_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.tbxPage_menu, u"Menu")
        self.tbxPage_info = QWidget()
        self.tbxPage_info.setObjectName(u"tbxPage_info")
        self.tbxPage_info.setGeometry(QRect(0, 0, 103, 416))
        self.verticalLayout_6 = QVBoxLayout(self.tbxPage_info)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_usuario = QLabel(self.tbxPage_info)
        self.lbl_usuario.setObjectName(u"lbl_usuario")

        self.verticalLayout_6.addWidget(self.lbl_usuario)

        self.toolBox.addItem(self.tbxPage_info, u"Informa\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.buttons_frame)


        self.horizontalLayout.addWidget(self.left_frame)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu = QPushButton(self.top_frame)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(0, 0))
        self.btn_menu.setMaximumSize(QSize(40, 16777215))
        self.btn_menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"#btn_menu{\n"
"	background-color: none;\n"
"	border: 0;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/imgs/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_menu, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        sizePolicy.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_5 = QVBoxLayout(self.pg_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_logo = QLabel(self.pg_home)
        self.lbl_logo.setObjectName(u"lbl_logo")

        self.verticalLayout_5.addWidget(self.lbl_logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.pg_contatos)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)

        self.frame_3 = QFrame(self.pg_contatos)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_11.addWidget(self.label_11)


        self.verticalLayout_12.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_13 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_12 = QLabel(self.pg_sobre)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.label_12)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.label_13 = QLabel(self.pg_sobre)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(400, 200))
        self.label_13.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_14 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tabWidget = QTabWidget(self.pg_cadastro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideRight)
        self.tab_cadastro = QWidget()
        self.tab_cadastro.setObjectName(u"tab_cadastro")
        self.verticalLayout_8 = QVBoxLayout(self.tab_cadastro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.tab_cadastro)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.frame = QFrame(self.tab_cadastro)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_cnpj = QLineEdit(self.frame)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 0, 0, 1, 3)

        self.txt_nome = QLineEdit(self.frame)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 0, 3, 1, 4)

        self.txt_logradouro = QLineEdit(self.frame)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 1, 0, 1, 7)

        self.txt_num = QLineEdit(self.frame)
        self.txt_num.setObjectName(u"txt_num")
        self.txt_num.setMaximumSize(QSize(100, 16777215))
        self.txt_num.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_num, 2, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setMinimumSize(QSize(200, 0))
        self.txt_complemento.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 2, 1, 1, 3)

        self.txt_bairro = QLineEdit(self.frame)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 2, 4, 1, 3)

        self.txt_municipio = QLineEdit(self.frame)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 3, 0, 1, 5)

        self.txt_uf = QLineEdit(self.frame)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 3, 5, 1, 1)

        self.txt_cep = QLineEdit(self.frame)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 3, 6, 1, 1)

        self.txt_telefone = QLineEdit(self.frame)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 4, 0, 1, 2)

        self.txt_email = QLineEdit(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 4, 2, 1, 5)


        self.verticalLayout_8.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.btn_cadastrar = QPushButton(self.tab_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_cadastrar, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab_cadastro, "")
        self.tab_empresas = QWidget()
        self.tab_empresas.setObjectName(u"tab_empresas")
        self.verticalLayout_10 = QVBoxLayout(self.tab_empresas)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.title_empresas = QLabel(self.tab_empresas)
        self.title_empresas.setObjectName(u"title_empresas")

        self.verticalLayout_10.addWidget(self.title_empresas)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_empresas = QTableWidget(self.tab_empresas)
        if (self.tb_empresas.columnCount() < 11):
            self.tb_empresas.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tb_empresas.setObjectName(u"tb_empresas")

        self.horizontalLayout_5.addWidget(self.tb_empresas)

        self.frame_2 = QFrame(self.tab_empresas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_excel = QPushButton(self.frame_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_excluir)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_empresas, "")

        self.verticalLayout_14.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastro)

        self.verticalLayout_4.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.footer_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        Cad_Emp_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cad_Emp_Screen)

        self.toolBox.setCurrentIndex(1)
        self.Pages.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Cad_Emp_Screen)
    # setupUi

    def retranslateUi(self, Cad_Emp_Screen):
        Cad_Emp_Screen.setWindowTitle(QCoreApplication.translate("Cad_Emp_Screen", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">LOGO</span></p></body></html>", None))
        self.btn_menu_home.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Home", None))
        self.btn_menu_cadastrar.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Cadastrar", None))
        self.btn_menu_contatos.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Contatos", None))
        self.btn_menu_sobre.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tbxPage_menu), QCoreApplication.translate("Cad_Emp_Screen", u"Menu", None))
        self.lbl_usuario.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Usu\u00e1rio: Alex", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tbxPage_info), QCoreApplication.translate("Cad_Emp_Screen", u"Informa\u00e7\u00f5es", None))
        self.btn_menu.setText("")
        self.label.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p><span style=\" font-size:18pt;\">SISTEMA DE CADASTRO</span></p></body></html>", None))
        self.lbl_logo.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/Imagem3.png\"/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">CONTATOS</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p><img src=\":/imgs/whats.png\"/><span style=\" font-size:18pt; vertical-align:super;\">(21) 99999-9999</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p><img src=\":/imgs/email.png\"/><span style=\" font-size:18pt; vertical-align:super;\"> teste@teste.com</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p><img src=\":/imgs/instagram.png\"/><span style=\" font-size:18pt; vertical-align:super;\"> @instagram</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p><img src=\":/imgs/youtube.png\"/><span style=\" font-size:18pt; vertical-align:super;\"> youtube</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">SOBRE</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p>Este sistema realiza consulta do CNPJ utilizando a API da Receita Federal, fazendo o cadastro da empresa em um banco de dados SQLite3. </p><p>Possui objetivo did\u00e1tico, com \u00eanfase no ensino do uso do Python e QT para desenvolvimento de aplica\u00e7\u00f5es modernas e funcionais.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p align=\"center\">Empresa</p></body></html>", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"CNPJ", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"Nome empresarial", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"Logradouro", None))
        self.txt_num.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"N\u00famero", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"Complemento", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"Bairro", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"Munic\u00edpio", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"UF", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"CEP", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"Telefone", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("Cad_Emp_Screen", u"Email", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cadastro), QCoreApplication.translate("Cad_Emp_Screen", u"Cadastro", None))
        self.title_empresas.setText(QCoreApplication.translate("Cad_Emp_Screen", u"<html><head/><body><p align=\"center\">Empresas</p></body></html>", None))
        ___qtablewidgetitem = self.tb_empresas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Cad_Emp_Screen", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_empresas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Cad_Emp_Screen", u"NOME EMPRESARIAL", None));
        ___qtablewidgetitem2 = self.tb_empresas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Cad_Emp_Screen", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tb_empresas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Cad_Emp_Screen", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tb_empresas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Cad_Emp_Screen", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tb_empresas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Cad_Emp_Screen", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tb_empresas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Cad_Emp_Screen", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tb_empresas.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Cad_Emp_Screen", u"UF", None));
        ___qtablewidgetitem8 = self.tb_empresas.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Cad_Emp_Screen", u"CEP", None));
        ___qtablewidgetitem9 = self.tb_empresas.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Cad_Emp_Screen", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tb_empresas.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Cad_Emp_Screen", u"EMAIL", None));
        self.btn_excel.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("Cad_Emp_Screen", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_empresas), QCoreApplication.translate("Cad_Emp_Screen", u"Empresas", None))
        self.label_3.setText(QCoreApplication.translate("Cad_Emp_Screen", u"CopyRight ACP Projects 2025", None))
    # retranslateUi

