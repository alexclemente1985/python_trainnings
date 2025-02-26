from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from pathlib import Path
from ui.erp import Ui_MainWindow
import sys
from ui.cliente_form import Ui_Form as Ui_CustomerForm
from ui.cliente_widget import Ui_Form as Ui_CustomerScreen
from database import Database_ERP
from classes.Customer import Customer



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        ### Conexão com banco de dados
        self.database = Database_ERP()

        ### Botões sistema
        self.btn_sair.clicked.connect(self.exitSystem)
        self.btn_cliente.clicked.connect(self.callCustomerScreen)

        ## Botões tela cliente
        self.btn_cliente

        ### Menu bar ###
        self.actionCliente.triggered.connect(self.callCustomerScreen)


    ### Funções sistema
    ## Fechar sistema ##
    def exitSystem(self):
        sys.exit()

    ## Abrir tela cliente ##
    def callCustomerScreen(self):
        self.customerScreen = QWidget()

        self.ui_customerScreen = Ui_CustomerScreen()
        self.ui_customerScreen.setupUi(self.customerScreen)

        self.ui_customerScreen.btn_cliente_retornar.clicked.connect(lambda: self.exitScreen(self.customerScreen))
        self.ui_customerScreen.btn_cliente_pesquisar.clicked.connect(lambda: self.searchCustomer(self.ui_customerScreen.txt_cliente_nome.text()))
        self.ui_customerScreen.btn_cliente_adicionar.clicked.connect(lambda: self.customerFormScreen(formType = 'add'))
        self.ui_customerScreen.btn_cliente_consultar.clicked.connect(lambda: self.customerFormScreen(formType='consult'))
        self.ui_customerScreen.btn_cliente_alterar.clicked.connect(lambda: self.customerFormScreen(formType='update'))
        self.ui_customerScreen.btn_cliente_excluir.clicked.connect(self.deleteCustomer)

        self.customerScreen.show()
        self.searchCustomer('')

    ## Fechar telas secundárias ##
    def exitScreen(self, screen: QWidget):
        screen.close()

    ## Busca de clientes por nome (todos se nome não for fornecido)
    def searchCustomer(self, name: str):
        results = self.database.search_customer(name)
        self.ui_customerScreen.tb_cliente.clearContents()

        if results and (len(results) > 0):
            self.ui_customerScreen.tb_cliente.setRowCount(len(results))
        for row, customer in enumerate(results):
            for column, data in enumerate(vars(customer).values()):
                self.ui_customerScreen.tb_cliente.setItem(row,column, QTableWidgetItem(str(data)))

        self.ui_customerScreen.tb_cliente.resizeColumnsToContents()
        self.ui_customerScreen.tb_cliente.resizeRowsToContents()

    def customerFormScreen(self, formType: str):
        self.customerForm = QWidget()
        self.ui_customerForm = Ui_CustomerForm()
        self.ui_customerForm.setupUi(self.customerForm)

        self.ui_customerForm.btn_cliente_cancelar.clicked.connect(lambda: self.exitScreen(self.customerForm))

        if formType == 'add':
            self.ui_customerForm.btn_cliente_cadastrar.clicked.connect(lambda: self.addCustomer(
                Customer(
                    id_customer= None,
                    name=self.ui_customerForm.txt_nome.text(),
                    phone=self.ui_customerForm.txt_telefone.text(),
                    city=self.ui_customerForm.txt_cidade.text()
                )
            ))
        elif (formType == 'consult') or (formType =='update'):
            line = self.ui_customerScreen.tb_cliente.currentRow()
            id_customer = self.ui_customerScreen.tb_cliente.item(line, 0).text()
            name = self.ui_customerScreen.tb_cliente.item(line, 1).text()
            phone = self.ui_customerScreen.tb_cliente.item(line, 2).text()
            city = self.ui_customerScreen.tb_cliente.item(line, 3).text()

            if formType == 'consult':
                self.ui_customerForm.txt_nome.setEnabled(False)
                self.ui_customerForm.txt_telefone.setEnabled(False)
                self.ui_customerForm.txt_cidade.setEnabled(False)
                self.ui_customerForm.btn_cliente_cadastrar.setEnabled(False)


            self.ui_customerForm.txt_nome.setText(name)
            self.ui_customerForm.txt_telefone.setText(phone)
            self.ui_customerForm.txt_cidade.setText(city)

            if formType == 'update':
                self.ui_customerForm.btn_cliente_cadastrar.clicked.connect(lambda: self.updateCustomer(
                    Customer(
                        id_customer= id_customer,
                        name=self.ui_customerForm.txt_nome.text(),
                        phone=self.ui_customerForm.txt_telefone.text(),
                        city=self.ui_customerForm.txt_cidade.text()
                    )
            ))

        self.customerForm.show()


    # implementar sistema de mensagens
    def addCustomer(self, customer: Customer):
        result = self.database.register_customer(customer)
        if result.type == 'OK':
            self.exitScreen(self.customerForm)
            self.searchCustomer('')

        self.msg(result.type, result.msg)

    def updateCustomer(self, customer: Customer):
        result = self.database.update_customer(customer)

        if result.type == 'OK':
            self.exitScreen(self.customerForm)
            self.searchCustomer('')

        self.msg(result.type, result.msg)

    def deleteCustomer(self):

        line = self.ui_customerScreen.tb_cliente.currentRow()
        id_customer = self.ui_customerScreen.tb_cliente.item(line, 0).text()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        resp = msg.exec()

        if resp == QMessageBox.Yes:
            result = self.database.delete_customer(id_customer)
            if result.type == 'OK':
                self.searchCustomer('')
                self.msg(result.type, result.msg)


        else:
            print(f'erro na atualização dos dados: {result.msg}')

    def msg(self, type, msg):
        msgBox = QMessageBox()

        if type.lower() == 'ok':
            msgBox.setIcon(QMessageBox.Information)
        elif type.lower() == 'error':
            msgBox.setIcon(QMessageBox.Critical)
        elif type.lower() == 'warning':
            msgBox.setIcon(QMessageBox.Warning)

        msgBox.setText(msg)
        msgBox.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
