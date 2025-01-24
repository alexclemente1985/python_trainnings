from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel, QCheckBox
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox")

        self.lbl = QLabel("Você fuma?")
        self.ck = QCheckBox("Marque caso positivo")
        ## Para obter valor parcialmente marcado (valor 1)
        self.ck.setTristate(True)

        self.lbl2 = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.ck)
        layout.addWidget(self.lbl2)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.ck.stateChanged.connect(self.state)

    def state(self,s):
        #if s == Qt.Checked:
        if s == 2:
            self.lbl2.setText("Fumante")
        elif s == 1:
            self.lbl2.setText("Fuma parcialmente")
        else:
            self.lbl2.setText('Não fumante')


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()

    window.show()

    app.exec()