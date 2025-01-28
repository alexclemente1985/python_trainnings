from PySide6.QtWidgets import QSpinBox,QListWidget, QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel, QCheckBox
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox")

        self.qsb = QSpinBox()
        self.qsb.setMinimum(-5)
        self.qsb.setMaximum(50)

        self.qsb.setPrefix('Quantidade ')

        self.qsb.setSuffix(' marrecos')

        # pulando de 3 em 3
        self.qsb.setSingleStep(3)

        self.qsb.valueChanged.connect(self.value_marreco) # mostra valor com prefixo e sufixo
        self.qsb.textChanged.connect(self.value_marreco) #só mostra o valor


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.qsb)

        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)


    def value_marreco(self, i):
        print('Quantidade de marrecos: ',i)



if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()

    window.show()

    app.exec()