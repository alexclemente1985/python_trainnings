
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, QTableView, QVBoxLayout, QWidget)
from PySide6.QtCore import QSize, Qt
from pathlib import Path
import pandas as pd


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
        self.setWindowTitle("Tabelas - QTableView com Pandas")

        self.tb = QTableView()

        data= pd.DataFrame([
            ['001', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['002', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['003', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['004', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['005', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['006', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['007', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['008', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['009', 'R$100,00','R$ 18,00','R$ 5,00'],
        ], columns=['Notas','Valor','ICMS','IPI'])

        self.model = TableModel(data)
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