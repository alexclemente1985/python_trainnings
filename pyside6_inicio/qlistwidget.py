from PySide6.QtWidgets import QListWidget, QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel, QCheckBox
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget")

        self.lw = QListWidget()
        self.lw.addItems([f'ITEM 0{i}' for i in range(1,4)])

        self.lw.itemDoubleClicked.connect(self.abrir_janela)
        self.lw.currentItemChanged.connect(self.indice)
        self.lw.currentTextChanged.connect(self.texto_alterado)



        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lw)

        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

    def abrir_janela(self, i):
        print(f'abrindo janela do item {i.text()}')

    def texto_alterado(self,t):
        print(t)

    def indice(self, i):
        print(i.text())



if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()

    window.show()

    app.exec()