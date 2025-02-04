from PySide6.QtCore import Qt, QSize
from ui.cad_emp_screen import Ui_Cad_Emp_Screen
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
import sys
from pathlib import Path
import shutil
import os

class MainWindow(QMainWindow, Ui_Cad_Emp_Screen):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ACP - Cadastro de Empresas")
        iconPath = Path.joinpath(Path(__file__).parent, "imgs", "imagem3.png")
        appIcon = QIcon(iconPath.as_posix())
        self.setWindowIcon(appIcon)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()