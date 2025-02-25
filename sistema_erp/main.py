from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from pathlib import Path
from ui.erp import Ui_MainWindow
import sys
from ui.cliente_form import Ui_Form as Ui_CustomerForm
from ui.cliente_widget import Ui_Form as Ui_CustomerScreen
from database import Database_ERP
from classes.Customer import Customer
from controlVariables import customerDataScreenType



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        ### Conexão com banco de dados
        self.database = Database_ERP()

        ### Botões sistema
        self.btn_sair.clicked.connect(self.exitSystem)
        self.btn_cliente.clicked.connect(self.customerScreen)

        ## Botões tela cliente
        self.btn_cliente

        ### Menu bar ###
        self.actionCliente.triggered.connect(self.customerScreen)

    ### Funções sistema
    ## Fechar sistema ##
    def exitSystem(self):
        sys.exit()

    ## Abrir tela cliente ##
    def customerScreen(self):
        self.customerScreen = QWidget()
        self.ui_customerScreen = Ui_CustomerScreen()
        self.ui_customerScreen.setupUi(self.customerScreen)

        self.ui_customerScreen.btn_cliente_retornar.clicked.connect(lambda: self.exitScreen(self.customerScreen))
        self.ui_customerScreen.btn_cliente_pesquisar.clicked.connect(lambda: self.searchCustomer(self.ui_customerScreen.txt_cliente_nome.text(), self.ui_customerScreen.tb_cliente))
        self.ui_customerScreen.btn_cliente_adicionar.clicked.connect(self.customerFormScreen)

        self.customerScreen.show()

    ## Fechar telas secundárias ##
    def exitScreen(self, screen: QWidget):
        screen.close()

    ## Busca de clientes por nome (todos se nome não for fornecido)
    def searchCustomer(self, name: str, table: QTableWidget):
        results = self.database.search_customer(name)
        table.clearContents()

        if results and (len(results) > 0):
            table.setRowCount(len(results))

        for row, customer in enumerate(results):
            for column, data in enumerate(vars(customer).values()):
                table.setItem(row,column, QTableWidgetItem(data))

        table.resizeColumnsToContents()
        table.resizeRowsToContents()

    def customerFormScreen(self):
        self.customerForm = QWidget()
        self.ui_customerForm = Ui_CustomerForm()
        self.ui_customerForm.setupUi(self.customerForm)

        self.ui_customerForm.btn_cliente_cancelar.clicked.connect(lambda: self.exitScreen(self.customerForm))
        
        if customerDataScreenType == 'add':
            self.ui_customerForm.btn_cliente_cadastrar.clicked.connect(lambda: self.addCustomer(
                Customer(
                    name=self.ui_customerForm.txt_nome.text(),
                    phone=self.ui_customerForm.txt_telefone.text(),
                    city=self.ui_customerForm.txt_cidade.text()
                )
            ))

        self.customerForm.show()

    # implementar sistema de mensagens
    def addCustomer(self, customer: Customer):
        customerDataScreenType = 'add'
        result = self.database.register_customer(customer)
        if result.type == 'OK':
            self.exitScreen(self.customerForm)
        else:
            print('erro registro (implementar alerta de mensagem)')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
