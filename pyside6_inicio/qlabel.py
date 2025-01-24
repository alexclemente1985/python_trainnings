from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel")

        self.lbl = QLabel('Programa para QLabel')

        ## Imagens
        self.lblImg = QLabel()
        img = Path.joinpath(Path(__file__).parent, 'resources','jake_dog.png')
        self.lblImg.setPixmap(QPixmap(img))

        font = self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)

        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #self.lblImg.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.lblImg.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.lblImg)


        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()