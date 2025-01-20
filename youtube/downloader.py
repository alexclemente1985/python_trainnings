from PySide6.QtCore import Qt
from ui_frame_principal import Ui_Dialog
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
import sys

class Downloader(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = Downloader()
    win.show()

    app.exec()