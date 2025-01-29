from PySide6.QtWidgets import (QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider, QVBoxLayout, QFrame, QPlainTextEdit)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QPalette, QColor
from pathlib import Path
from qt_material import apply_stylesheet

icons = Path.joinpath(Path(__file__).parent,'icons','fugue-icons-3.5.6','icons')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStyleSheet")

        formulario = QFormLayout()

        formulario.addRow(QCheckBox('Checkbox'))
        formulario.addRow(QRadioButton('Radio Button'))
        formulario.addRow("QLabel", QLabel("QLabel"))
        formulario.addRow("QPushButton", QPushButton("QPushButton"))
        formulario.addRow("QLineEdit", QLineEdit("QLineEdit"))
        formulario.addRow("QDateEdit", QDateEdit())
        formulario.addRow("QDateTimeEdit", QDateTimeEdit())
        formulario.addRow("QSpinBox", QSpinBox())
        formulario.addRow("QDoubleSpinBox", QDoubleSpinBox())
        formulario.addRow("QComboBox", QComboBox())
        formulario.addRow("QFontComboBox", QFontComboBox())
        formulario.addRow("QProgressBar", QProgressBar())
        formulario.addRow("QLCDNumber", QLCDNumber())
        formulario.addRow("QSlider", QSlider(Qt.Horizontal))
        formulario.addRow("QDial", QDial())



        container = QFrame()
        container.setLayout(formulario)

        self.setCentralWidget(container)
        self.aplicar_estilo()


    def aplicar_estilo(self):
        stylesheet = Path.joinpath(Path(__file__).parent, 'resources','style_01.css')

        try:
            with open(stylesheet) as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print("Erro: ",e)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # estilo fusion
    app.setStyle("Fusion")


    window = MainWindow()
    window.show()

    app.exec()