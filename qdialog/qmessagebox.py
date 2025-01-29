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
    QLineEdit,
    QMessageBox)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")

        self.setFixedSize(QSize(600,600))

        button_msg = QPushButton("Mostrar Message Box")
        button_qst = QPushButton("Mostrar Message Box de Question")

        layout = QVBoxLayout()
        layout.addWidget(button_msg)
        layout.addWidget(button_qst)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        button_msg.clicked.connect(self.show_message)
        button_qst.clicked.connect(self.show_question)

    def show_question(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Question")
        self.msg.setText("Responda Yes ou No:")
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        self.msg.setIcon(QMessageBox.Question)

        resposta = self.msg.exec()

        if resposta == QMessageBox.Yes:
            print("O programa será executado...")
        elif resposta == QMessageBox.No:
            print("A execução do programa foi recusada...")
        else:
            print("Operação cancelada...")

        self.msg.exec()

    def show_message(self,s):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)

        """_
        QMessageBox.NoIcon
        QMessageBox.Question 
        QMessageBox.Information 
        QMessageBox.Warning 
        QMessageBox.Critical
        """

        self.msg.setWindowTitle("Message")
        self.msg.setText("Operação concluída com sucesso!")
        self.msg.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()