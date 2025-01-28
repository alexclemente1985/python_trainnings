from PySide6.QtWidgets import (
    QDoubleSpinBox,
    QListWidget,
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QFrame,
    QVBoxLayout,
    QLabel,
    QCheckBox,
    QAbstractSpinBox)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox")

        self.qdsb = QDoubleSpinBox()
        self.qdsb.setMinimum(-5)
        self.qdsb.setMaximum(50)

        self.qdsb.setPrefix('R$ ')

        # pulando de 3 em 3
        self.qdsb.setSingleStep(3)

        self.qdsb.valueChanged.connect(self.value_brl) # mostra valor com prefixo e sufixo
        self.qdsb.textChanged.connect(self.value_brl) #só mostra o valor

        #Removendo os botões de acrescentar/remover
        self.qdsb.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.qdsb)

        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)


    def value_brl(self, i):
        print('Quantidade de marrecos: ',i)



if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()

    window.show()

    app.exec()