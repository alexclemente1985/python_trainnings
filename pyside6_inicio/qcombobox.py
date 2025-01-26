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

        self.cb.addItems([f"item 0{i}" for i in range(3,5)])

        self.setCentralWidget(self.cb)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    app.exec()