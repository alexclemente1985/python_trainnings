from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel
import sys
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercício 1: Cálculo de área")
        self.setFixedSize(QSize(300,200))

        ## Elementos da janela
        self.lblWidth = QLabel()
        self.lblWidth.setText("Informe a largura em metros:")
        self.inputWidth = QLineEdit()

        self.lblHeight = QLabel()
        self.lblHeight.setText("Informe a altura em metros:")
        self.inputHeight = QLineEdit()

        self.btnResult = QPushButton()
        self.btnResult.setText("Calcular área")

        self.lblResult = QLabel()

        ## Layout
        layout = QVBoxLayout()

        layout.addWidget(self.lblWidth)
        layout.addWidget(self.inputWidth)

        layout.addWidget(self.lblHeight)
        layout.addWidget(self.inputHeight)

        layout.addWidget(self.btnResult)
        layout.addWidget(self.lblResult)

        ## Container
        container = QFrame()
        container.setLayout(layout)
        self.setCentralWidget(container)

        ## Ações
        self.btnResult.clicked.connect(self.result)

    def result(self):
        try:
            width = float(self.inputWidth.text())
            height = float(self.inputHeight.text())

            area = round(width*height,2)

            self.lblResult.setText(f"Valor da área: {area}m²")

        except Exception as e:
            print("Erro: ", e)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()

