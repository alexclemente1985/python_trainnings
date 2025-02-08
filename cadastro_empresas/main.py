from typing import List
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
from PySide6.QtSql import QSqlTableModel

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
        # Inicialização da tabela caso já exista
        self.feed_table()
        #######

        #######
        # Preenchimento automático dos dados do CNPJ consultado
        self.txt_cnpj.editingFinished.connect(self.consult_api)
        #######

        #######
        # Cadastro de empresa
        self.btn_cadastrar.clicked.connect(self.register_company)
        #######

        #######
        # Alteração de dados de empresa
        self.btn_alterar.clicked.connect(self.update_company)

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
            self.msg('aviso','CNPJ não encontrado na base da Receita.')

        else:
            self.msg('erro',consulta.message)


    ######

    def register_company(self):
        result = self.banco.register_company(self.fullDataSet)
        self.msg(result.type, result.msg)
        self.feed_table()

    def feed_table(self):
        results = self.banco.select_all_companies()
        # Limpeza da tabela para evitar concatenações indevidas de dados
        self.tb_empresas.clearContents()

        if results and (len(results) > 0):
            self.tb_empresas.setRowCount(len(results))

            # Não é necessário pois já foi feito lá no QT Designer
            #self.tb_empresas.setColumnCount(len(vars(results[0])))

            for row, company in enumerate(results):
                for column, data in enumerate(vars(company).values()):
                    self.tb_empresas.setItem(row,column, QTableWidgetItem(data))
    
    def update_company(self):
        data = []
        updated_data: List[Company] = []
        

        for row in range(self.tb_empresas.rowCount()):
            for column in range(self.tb_empresas.columnCount()):
                data.append(self.tb_empresas.item(row, column).text())

            company = Company(
                cnpj=data[0],
                nome=data[1],
                logradouro=data[2],
                numero=data[3],
                complemento=data[4],
                bairro=data[5],
                municipio=data[6],
                uf=data[7],
                cep=data[8],
                telefone=data[9],
                email=data[10]
            )
            updated_data.append(company)
            data = []

       
        result = self.banco.update_company(updated_data)
        self.msg(result.type, result.msg)
        self.feed_table()

        


    def msg(self, tipo,msg):
        msgbox = QMessageBox()

        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)

        elif tipo.lower() == 'erro':
            msgbox.setIcon(QMessageBox.Critical)

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