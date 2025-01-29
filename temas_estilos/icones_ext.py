from PySide6.QtWidgets import (QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider, QVBoxLayout, QFrame, QStyle, QGridLayout)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QPalette, QColor
from pathlib import Path
from qt_material import apply_stylesheet

icons = Path.joinpath(Path(__file__).parents[1],'icons','fugue-icons-3.5.6','icons')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ícones de terceiros")

        self.setFixedSize(QSize(600,400))

        money = Path.joinpath(icons, 'money-coin.png')
        icon = QIcon(money.as_posix())
        button = QPushButton(icon, "Bufunfa")
        #button.setIconSize(QSize(200,200))

        layout = QVBoxLayout()
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    #estilo
    apply_stylesheet(app, theme='dark_amber.xml')


    window = MainWindow()

    window.show()

    app.exec()