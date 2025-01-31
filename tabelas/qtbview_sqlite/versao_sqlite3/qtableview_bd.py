
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, QTableView, QVBoxLayout, QWidget, QHeaderView)
from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

from database import Database



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    # As funções abaixo são herdadas de QtCore.QAbstractTableModel e servem para construir a tabela
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
    
    def rowCount(self, index):
        return self._data.shape[0] #shape: retorna estrutura da matriz - 0 -> nº de linhas 1-> nº de colunas
    
    def columnCount(self, index):
        return self._data.shape[1]
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
            

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabelas - QTableView com Pandas e SQLite3")
        self.setFixedSize(QSize(600,400))
        
        database = Database()
        
        self.tb = QTableView()
        self.tb.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.model = TableModel(database.data)
        self.tb.setModel(self.model)
        

        layout = QVBoxLayout()
        layout.addWidget(self.tb)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        print("acionando programa...")

        window = MainWindow()
        window.show()

        app.exec()
    except Exception as e:
        print("Erro: ",e)