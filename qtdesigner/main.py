from PySide6.QtCore import Qt
from ui_main import Ui_Form
from ui_main_teste import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QWidget,
    QFrame,
    QMessageBox
)
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Login")

        self.btn_login.clicked.connect(self.login)

    def login(self):
        
        if self.txt_user.text().upper() == 'ADMIN':
            self.msg('OK','Usuário valido')
        else:
            self.msg('ERRO','Usuário não cadastrado')
            

        if self.txt_password.text() == '123':
            self.msg('OK', 'Usuário logado com sucesso!')
            
            
    
    def msg(self,tipo, texto):
        msg = QMessageBox()
        if tipo == 'OK':
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setIcon(QMessageBox.Critical)
        msg.setText(texto)
        msg.exec()

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()