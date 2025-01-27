from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel, QComboBox
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path
#import pycep_correios ## lib foi renomeada para o nome abaixo
import brazilcep
import sys

# Programa consulta CEP
## 1) Informar nome
## 2) Informar sexo (combobox) -> Iniciar sem marcação (colocar placeholder)
## 3) Informar CEP
## 4) Criar os seguintes campos line edit que se preenchem automaticamente após inserção do CEP
### 4.1) Logradouro
### 4.2) Bairro
### 4.3) Cidade

### Desafio: Tentar criar como texto não editável, e somente mostrar após retorno da lib de cep

class Consulta_CEP(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Consultar Endereço por CEP")

        self.lbl_nome = QLabel("Informe o nome:")
        self.led_nome = QLineEdit()

        self.lbl_sexo = QLabel("Informe o sexo:")
        self.cb_sexo = QComboBox()
        self.cb_sexo.setPlaceholderText("Selecione...")
        self.cb_sexo.addItems(['Masculino', 'Feminino'])

        self.lbl_cep = QLabel("Informe o CEP:")
        self.led_cep = QLineEdit()

        # Componentes dependentes do retorno da consulta de CEP

        self.txt_error = QLineEdit()
        self.txt_lograd = QLineEdit()
        self.txt_bairro = QLineEdit()
        self.txt_cidade = QLineEdit()


        # Layout e Container
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_nome)
        self.layout.addWidget(self.led_nome)

        self.layout.addWidget(self.lbl_sexo)
        self.layout.addWidget(self.cb_sexo)

        self.layout.addWidget(self.lbl_cep)
        self.layout.addWidget(self.led_cep)

        container = QFrame()
        container.setLayout(self.layout)


        self.led_cep.editingFinished.connect(self.consulta_cep)

        self.setCentralWidget(container)



    def consulta_cep(self):
        try:
            endereco = brazilcep.get_address_from_cep(self.led_cep.text())

            self.lbl_lograd = QLabel("Logradouro:")
            self.txt_lograd.setText(endereco['street'])
            self.lbl_bairro = QLabel("Bairro:")
            self.txt_bairro.setText(endereco['district'])
            self.lbl_cidade = QLabel("Cidade:")
            self.txt_cidade.setText(endereco['city'])

            self.layout.addWidget(self.lbl_lograd)
            self.layout.addWidget(self.txt_lograd)
            self.layout.addWidget(self.lbl_bairro)
            self.layout.addWidget(self.txt_bairro)
            self.layout.addWidget(self.lbl_cidade)
            self.layout.addWidget(self.txt_cidade)

        # Caso não haja retorno na busca (ou aconteca algum erro)
        except Exception as e:
            print(f"Erro na consulta de CEP ou CEP não encontrado.")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Consulta_CEP()
    window.show()

    app.exec()