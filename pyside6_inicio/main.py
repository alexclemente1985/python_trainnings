from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout
import sys
from PySide6.QtCore import QSize # Aula 4

## Aula 3
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Programa inicial em PySide6")

        self.button = QPushButton("Ligue o botão!")
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.imprimir)

        ## Aula 4
        self.button.setCheckable(True) ### Atualiza a marcação, alternando entre os cliques
        self.button.clicked.connect(self.clicado)

        self.setFixedSize(QSize(300,200)) ## Aula 4



    def imprimir(self):
        print("Teste do botão...")

    ## Aula 4
    def clicado(self,s):
        print("Clicado: ",s)

        if s:
            self.button.setStyleSheet(u"background-color:green")
            self.button.setText("Ligado!")
        else:
            self.button.setStyleSheet(u"background-color:red")
            self.button.setText("Desligado!")

        ## Desabilitando o button após o primeiro clique
        #self.button.setEnabled(False)

app = QApplication(sys.argv)

#win = QWidget() ## Aula 1
#win = QMainWindow() ## Aula 2
win = MainWindow() ## Aula 3

win.show()
app.exec()