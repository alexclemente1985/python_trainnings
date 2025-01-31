import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, QTableView, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit, QTreeWidget, QTreeWidgetItem)
from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlTableModel, QSqlQuery
from database import Database
from pathlib import Path
import re

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        database = Database()
        self.db = database.qsqlDatabase()
        self.db.open()

        self.setFixedSize(QSize(600,400))

        self.table = QTreeWidget()

        # Obtenção dos nomes das colunas da tabela no banco de dados
        query = QSqlQuery(self.db)
        ## SQLITE
        query.exec("PRAGMA table_info('notas')")

        # Extração dos nomes das colunas
        headerNames = []
        while query.next():
            ## value(0) pega o valor do índice
            headerNames.append(query.value(1))

        ## a partir do valor 1 para não pegar o nome "index"
        self.table.setHeaderLabels(headerNames[1::])

        # Extração dos valores da tabela no banco de dados
        query.exec("SELECT * FROM notas")
        rows = []

        while query.next():
            columns = []
            #a partir do 1 para não pegar o índice
            for i in range(1,len(headerNames)):
                columns.append(query.value(i))

            rows.append(columns)

        # Preenchendo a QTreeWidget
        aux = ''
        for row in rows:
            if not row[0] == aux:
                parent = QTreeWidgetItem(self.table, row)
                parent.setCheckState(0, Qt.CheckState.Checked)
            else:
                child = QTreeWidgetItem(parent, row)
            aux = row[0]


        # Criação do layout e container
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()