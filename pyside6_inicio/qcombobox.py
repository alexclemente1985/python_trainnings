from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel, QComboBox
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('QComboBox')
        self.cb = QComboBox()

        self.cb.addItem("item 01")
        self.cb.addItem("item 02")

        self.cb.addItems([f"item 0{i}" for i in range(3,16)])

        self.cb.currentIndexChanged.connect(self.mudanca_index)
        self.cb.currentTextChanged.connect(self.mudanca_texto)

        #combobox editável
        self.cb.setEditable(True)

        # Número de elementos (limita)
        self.cb.setMaxCount(10)

        self.setCentralWidget(self.cb)

    def mudanca_index(self,i):
        print(i)

    def mudanca_texto(self, t):
        print(f'Conecta ao banco e traz informações do {t}.')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    app.exec()