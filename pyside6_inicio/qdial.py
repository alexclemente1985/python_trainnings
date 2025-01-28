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
    QAbstractSpinBox,
    QSlider,
    QDial)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDial")

        self.qdial = QDial()

        #self.qdial.setMinimum(-10)
        #self.qdial.setMaximum(10)
        self.qdial.setRange(-10,10)

        self.qdial.valueChanged.connect(self.value_changed)
        self.qdial.sliderMoved.connect(self.slider_position)
        self.qdial.sliderPressed.connect(self.slider_pressed)
        self.qdial.sliderReleased.connect(self.slider_released)

        # Slider horizontal
        self.qhslider = QSlider(Qt.Horizontal, self)

        self.qhslider.setRange(-10,10)

        self.qhslider.valueChanged.connect(lambda x: self.value_changed(x, True))
        self.qhslider.sliderMoved.connect(lambda x: self.slider_position(x, True))
        self.qhslider.sliderPressed.connect(lambda : self.slider_pressed(True))
        self.qhslider.sliderReleased.connect(lambda : self.slider_released(True))



        self.layout = QVBoxLayout()
        self.layout.addWidget(self.qdial)
        self.layout.addWidget(self.qhslider)

        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

    def value_changed(self,i, isHorizontal: bool = False):
        if not isHorizontal:
            print(f'valor alterado: {i}')
        else:
            print(f'valor alterado (horizontal): {i}')

    def slider_position(self,p, isHorizontal: bool = False):
        if not isHorizontal:
            print(f'posição atual: {p}')
        else:
            print(f'posição atual (horizontal): {p}')

    def slider_pressed(self, isHorizontal: bool = False):
        if not isHorizontal:
            print('slider pressionado')
        else:
            print('slider horizontal pressionado')

    def slider_released(self, isHorizontal: bool = False):
        if not isHorizontal:
            print('slider liberado')
        else:
            print('slider horizontal liberado')


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()

    window.show()

    app.exec()