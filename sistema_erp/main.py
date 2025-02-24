from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from pathlib import Path
from ui.erp import Ui_MainWindow
import sys
from ui.cliente_form import Ui_Form as Ui_ClienteForm
from ui.cliente_widget import Ui_Form as Ui_ClienteScreen
from database import Database_ERP



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        ### Botões sistema
        self.btn_sair.clicked.connect(self.exitSystem)
        self.btn_cliente.clicked.connect(self.openClienteScreen)

        ## Botões tela cliente
        self.btn_cliente

        ### Menu bar ###
        self.actionCliente.triggered.connect(self.openClienteScreen)

    ### Funções sistema
    ## Fechar sistema ##
    def exitSystem(self):
        sys.exit()

    ## Abrir tela cliente ##
    def openClienteScreen(self):
        self.clienteScreen = QWidget()
        self.ui_clienteScreen = Ui_ClienteScreen()
        self.ui_clienteScreen.setupUi(self.clienteScreen)

        self.ui_clienteScreen.btn_cliente_retornar.clicked.connect(lambda: self.exitScreen(self.clienteScreen))
        self.ui_clienteScreen.btn_cliente_pesquisar.clicked.connect(self.searchAll)
        
        self.clienteScreen.show() 

    ## Fechar telas secundárias ##
    def exitScreen(self, screen: QWidget):
        screen.close()
    
    ## Busca geral clientes
    def searchAll(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
