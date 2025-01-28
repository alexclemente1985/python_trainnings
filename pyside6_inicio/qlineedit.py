from PySide6.QtWidgets import QListWidget, QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel, QCheckBox
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit")

        self.le = QLineEdit()

        # Propriedades
        ## Limitando até 10 caracteres
        self.le.setMaxLength(10)
        ## Adição de placeholder
        self.le.setPlaceholderText('Digite o seu texto aqui...')
        ## Criação de máscara (colocar ";_" após o padrão é necessário)
        self.le.setInputMask("00/0000;_")

        self.label = QLabel()



        self.layout = QVBoxLayout()
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.label)
        self.label.setVisible(False)

        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

        ## Recursos
        self.le.editingFinished.connect(self.edit_finished)
        self.le.returnPressed.connect(self.return_pressed)
        self.le.selectionChanged.connect(self.selection_changed)
        self.le.textEdited.connect(self.text_changed)

    def edit_finished(self):
        print("Edição terminada")

    def return_pressed(self):
        print("Botão Enter pressionado")

        self.label.setText(f'Texto digitado: {self.le.text()}')
        self.label.setVisible(True)

    def selection_changed(self):
        print("Selection changed",self.le.selectedText())

    def text_changed(self,s):
        print("Texto alterado...")
        print(s)




if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()

    window.show()

    app.exec()