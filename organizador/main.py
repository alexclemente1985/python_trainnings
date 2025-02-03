from PySide6.QtCore import Qt, QSize
from ui.organizer import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
import sys
from pathlib import Path
import shutil
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ACP - Organizador de Arquivos")
        self.setMaximumSize(QSize(600,400))
        iconPath = Path.joinpath(Path(__file__).parent, "imgs", "folder.png")
        appIcon = QIcon(iconPath.as_posix())
        self.setWindowIcon(appIcon)

        self.path = ''
        self.txt_path.textChanged.connect(self.text_change)
        self.btn_open.clicked.connect(self.open_path)
        self.btn_organize.clicked.connect(self.organizer)

    def text_change(self,t):
        self.path = t
        print(self.path)

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str("pasta com arquivos"),
                                                     self.check_folder(),
                                                     QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
                                                     )
        self.txt_path.setText(self.path)

    def organizer(self):
        path = Path(self.path)
        files = os.listdir(path)


        for file in files:
            filename, extension = os.path.splitext(file)
            #pegando valor da posição 1 até a final
            extension = extension[1:]

            if Path.joinpath(path, extension).exists():
                shutil.move(Path.joinpath(path, file), Path.joinpath(path,extension,file))
            else:
                os.makedirs(Path.joinpath(path,extension))
                shutil.move(Path.joinpath(path, file), Path.joinpath(path,extension))

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Arquivos organizados com sucesso")
        msg.exec()

    def check_folder(self):
        if (len(self.path) > 0) and (Path(self.path).exists()):
            return self.path
        else:
            return str(Path.home())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()