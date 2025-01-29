from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QVBoxLayout,
    QLabel,
    QToolBar,
    QStatusBar,
    QDialog,
    QPushButton,
    QDialogButtonBox,
    QWidget,
    QLineEdit)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from pathlib import Path

icons = Path.joinpath(Path(__file__).parent,'icons','fugue-icons-3.5.6','icons')

class Another_window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()
        self.lbl = QLabel("Outra janela")

        layout.addWidget(self.lbl)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDialog")

        self.btn = QPushButton("Clique para abrir uma nova janela")
        self.btn.clicked.connect(self.show_new_window)

        #self.w = None
        self.w = Another_window() # janela persistente

        # Conectando informações entre janelas
        self.txt = QLineEdit()
        self.txt.textChanged.connect(self.w.lbl.setText)
        
        self.layout = QVBoxLayout()        
        self.layout.addWidget(self.txt)
        self.layout.addWidget(self.btn)

        container = QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)
        

    def show_new_window(self):
        #Para janela não persistente
        #NOTA: tem que adicionar o "self"
        '''
        if self.w is None:
            self.w = Another_window()
            self.w.show()
        else:
            #Permite fechar a janela no clique do mesmo botão de acionamento
            self.w = None
        '''
        # Para ter uma janela persistente e que possa ser escondida ou mostrada por meio do clique do botão
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
  


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()