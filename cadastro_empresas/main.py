from PySide6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve
from ui.cad_emp_screen import Ui_Cad_Emp_Screen
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
import sys
from pathlib import Path
import shutil
import os
from qt_material import apply_stylesheet
from functions import *
from database import Database_cadEmp
from classes.Company import Company

class MainWindow(QMainWindow, Ui_Cad_Emp_Screen):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ACP - Cadastro de Empresas")
        self.setMinimumSize(QSize(970,670))
        iconPath = Path.joinpath(Path(__file__).parent, "imgs", "imagem3.png")
        appIcon = QIcon(iconPath.as_posix())
        self.setWindowIcon(appIcon)

        #######
        # variável que irá receber os dados da consulta
        self.fullDataSet: Company = None
        #######

        #######
        # Instância do banco de dados

        self.banco = Database_cadEmp()
        #######

        #######
        # Botão MENU
        self.btn_menu.clicked.connect(self.leftMenu)
        #######

        #######
        # Páginas do sistema
        self.btn_menu_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_menu_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_menu_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
        self.btn_menu_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))

        #######

        #######
        # Preenchimento automático dos dados do CNPJ consultado
        self.txt_cnpj.editingFinished.connect(self.consult_api)
        #######

        #######
        # Cadastro de empresa
        self.btn_cadastrar.clicked.connect(self.register_company)
        #######

    ######
    # Animação do menu lateral
    def leftMenu(self):
        width = self.left_frame.width()

        if width == 0:
            newWidth = 400
        else:
            newWidth = 0

        self.animation =QPropertyAnimation(self.left_frame, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    ######

    ######
    # Consulta CNPJ API pública (criar message box informando excesso de consulta)
    def consult_api(self):
        consulta = consulta_cnpj(self.txt_cnpj.text())

        if (consulta.status_ok) and ('company' in consulta.__dict__.keys()) and (consulta.company != None):
            self.fullDataSet = consulta.company
            self.txt_nome.setText(self.fullDataSet.nome)
            self.txt_logradouro.setText(self.fullDataSet.logradouro)
            self.txt_num.setText(self.fullDataSet.numero)
            self.txt_complemento.setText(self.fullDataSet.complemento)
            self.txt_bairro.setText(self.fullDataSet.bairro)
            self.txt_municipio.setText(self.fullDataSet.municipio)
            self.txt_uf.setText(self.fullDataSet.uf)
            self.txt_cep.setText(self.fullDataSet.cep)
            self.txt_telefone.setText(self.fullDataSet.telefone)
            self.txt_email.setText(self.fullDataSet.email)

        ## Alterar para usar função msg()
        elif ('company' in consulta.__dict__.keys()) and (consulta.company == None):
            '''msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("CNPJ não encontrado na base da Receita.")
            msg.exec()'''
            self.msg('aviso','CNPJ não encontrado na base da Receita.')

        else:
            '''msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(consulta.message )
            msg.exec()'''
            self.msg('erro',consulta.message)



    ######

    def register_company(self):
        result = self.banco.register_company(self.fullDataSet)
        self.msg(result, None, 'registro')


    def msg(self, tipo,msg = None, tipo_funcao = None ):
        msgbox = QMessageBox()

        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
            if (tipo_funcao) and (tipo_funcao.lower()) == 'registro':
                msg = 'Empresa cadastrada com sucesso'
        elif tipo.lower() == 'erro':
            msgbox.setIcon(QMessageBox.Critical)
            if (tipo_funcao) and (tipo_funcao.lower()) == 'registro':
                msg = 'Falha no cadastro da empresa'
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)

        msgbox.setText(msg)
        msgbox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow()
    window.show()
    app.exec()