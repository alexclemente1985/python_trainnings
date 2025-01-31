import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, QTableView, QVBoxLayout, QWidget, QHeaderView)
from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlTableModel
from database import Database
from pathlib import Path


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
    
        self.model.select()

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        app.exec()
    except Exception as e:
        print("Erro: ",e)

    
