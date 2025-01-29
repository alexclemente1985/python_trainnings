from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QWidget,
    QTableWidgetItem, QHeaderView)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabelas - QTableWidget")
        self.setFixedSize(QSize(600,400))

        self.tb = QTableWidget()
        self.tb.setRowCount(3)
        self.tb.setColumnCount(3)

        self.tb.setHorizontalHeaderLabels(["Nome","Endereço","Email"])

        '''self.tb.setItem(0,0,QTableWidgetItem("Nome"))
        self.tb.setItem(0,1,QTableWidgetItem("Endereço"))
        self.tb.setItem(0,2,QTableWidgetItem("Email"))'''

        self.tb.setItem(0,0,QTableWidgetItem("Sicrano"))
        self.tb.setItem(0,1,QTableWidgetItem("Rua das Camélias"))
        self.tb.setItem(0,2,QTableWidgetItem("sicrano@gmail.com"))

        self.tb.setItem(1,0,QTableWidgetItem("Fulano"))
        self.tb.setItem(1,1,QTableWidgetItem("Rua das Acácias"))
        self.tb.setItem(1,2,QTableWidgetItem("fulano@gmail.com"))

        self.tb.cellChanged.connect(self.result)
        self.tb.itemChanged.connect(self.item_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.tb)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def result(self, r, c):
        print("Alteração na célula: ", r, c)

    def item_changed(self, item):
        print("Item alterado: ", item.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()