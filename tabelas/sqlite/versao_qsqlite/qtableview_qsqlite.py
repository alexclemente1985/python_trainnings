import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, QTableView, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit)
from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlTableModel
from database import Database
from pathlib import Path
import re


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        database = Database()
        self.db = database.qsqlDatabase()
        self.db.open()

        self.setFixedSize(QSize(600,400))

        self.table = QTableView()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.model = QSqlTableModel(db=self.db)

        self.table.setModel(self.model)

        self.model.setTable("notas")

        # Alterando a ordem dos dados

        ## Ordenação pela coluna ICMS decrescente
        #self.model.setSort(3, Qt.DescendingOrder)

        ## Ordenação pela coluna "valor" ascendente
        #self.model.setSort(2, Qt.AscendingOrder)

        # Remoção de colunas
        ## remoção da primeira coluna (index)
        #self.model.removeColumns(0,1)

        ## remoção das duas últimas (Valor e ICMS -> antiga coluna 2 virou coluna 1 agora)
        #self.model.removeColumns(1,2)

        ## remoção de colunas pelo nome
        '''
        colunas = ['Notas', "IPI"]
        for c in colunas:
            id = self.model.fieldIndex(c)
            self.model.removeColumns(id,1)
        '''

        ## Aplicação de filtros na tabela


        self.model.select()

        #Alterando o tipo de edição
        #self.model.setEditStrategy(QSqlTableModel.OnRowChange)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.filtro = QLineEdit()
        self.filtro.setPlaceholderText("Filtro de notas")

        self.btn_alterar = QPushButton("Salvar alteração")
        self.btn_reset = QPushButton("Resetar alterações")

        layout = QVBoxLayout()
        layout.addWidget(self.filtro)
        layout.addWidget(self.table)
        layout.addWidget(self.btn_alterar)
        layout.addWidget(self.btn_reset)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.btn_alterar.clicked.connect(self.alterar_dados)
        self.btn_reset.clicked.connect(self.reverter_alterações)
        self.filtro.textChanged.connect(self.filtrar_nota)

    def alterar_dados(self):
        self.model.submitAll()

    def reverter_alterações(self):
        self.model.revertAll()

    def filtrar_nota(self,s):
        #re.sub(regex,texto_substituto,texto_original) -> reconhece um padrão e o substitui no texto, retornando a cópia com alteração
        s = re.sub('[\W_]+','',s)
        filter_str = f'Notas LIKE "%{s}%"'
        self.model.setFilter(filter_str)


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        app.exec()
    except Exception as e:
        print("Erro: ",e)


