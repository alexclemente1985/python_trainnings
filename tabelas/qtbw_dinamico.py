from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QWidget,
    QTableWidgetItem, QHeaderView, QPushButton)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabelas - QTableWidget Dinâmico")
        self.setFixedSize(QSize(600,400))

        self.btn_print = QPushButton("Imprimir")

        lista= [
            ['001', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['002', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['003', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['004', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['005', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['006', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['007', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['008', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['009', 'R$100,00','R$ 18,00','R$ 5,00'],
        ]

        self.tb = QTableWidget()

        self.tb.setRowCount(len(lista))
        self.tb.setColumnCount(len(lista[0]))
        self.tb.setHorizontalHeaderLabels(["NOTA","VALOR TOTAL", "ICMS", "IPI"])

        # O reajuste da largura do header já implica no reajuste do restante (padronizado)
        self.tb.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for row, text in enumerate(lista):
            for column, data in enumerate(text):
                self.tb.setItem(row, column, QTableWidgetItem(str(data)))
       
        layout = QVBoxLayout()
        layout.addWidget(self.tb)
        layout.addWidget(self.btn_print)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btn_print.clicked.connect(self.imprimir_table)

    
    def imprimir_table(self):

        dados = []
        table_data = []

        for row in range(self.tb.rowCount()):
            for column in range(self.tb.columnCount()):
                dados.append(self.tb.item(row,column).text())
            table_data.append(dados)
            dados = []
        
        print(table_data)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()