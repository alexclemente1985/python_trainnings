from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QVBoxLayout,
    QLabel,
    QToolBar,
    QStatusBar)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from pathlib import Path

icons = Path.joinpath(Path(__file__).parent,'icons','fugue-icons-3.5.6','icons')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QToolbar")

        self.lbl = QLabel('QToolBar')

        self.lbl.setAlignment(Qt.AlignCenter)

        toolbar = QToolBar("Minha ToolBar")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)
        self.addToolBar(toolbar)

        # Inserindo botões na toolbar
        #btn_action = QAction("Botão de teste", self)
        #btn_action = QAction("Botão teste", self)

        # Adicionando ícones no QToolBar
        toolbar.setIconSize(QSize(24,24))

        self.home = Path.joinpath(icons, 'home.png')
        btn_action = QAction(QIcon(self.home.as_posix()),"Botão teste com ícone", self)
        btn_action.setStatusTip("Este é um botão para testes")
        btn_action.triggered.connect(self.funcao)

        #Deixar o botão como marcado ou desmarcado
        btn_action.setCheckable(True)

        toolbar.addAction(btn_action)

        # Adição de segundo botão
        toolbar.addSeparator()

        self.fire = Path.joinpath(icons, 'fire.png')
        btn_action2 = QAction(QIcon(self.fire.as_posix()),"Botão teste com ícone 2", self)
        btn_action2.setStatusTip("Este é um segundo botão para testes")
        btn_action2.triggered.connect(self.funcao)

        btn_action2.setCheckable(True)
        toolbar.addAction(btn_action2)

        # Estilização
        #toolbar.setToolButtonStyle(Qt.ToolButtonTextOnly)
        #toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)


        self.setStatusBar(QStatusBar(self))





    def funcao(self, s):
        print("clicado ",s)
        print(self.home.as_posix())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()