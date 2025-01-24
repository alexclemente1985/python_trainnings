from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel
import sys
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit")
        self.input = QLineEdit()
        self.lbl = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.input.textChanged.connect(self.texto)

    def texto(self):
        self.lbl.setText(f"Valor alterado: {self.input.text()}")

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()