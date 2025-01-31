import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, QTableView, QVBoxLayout, QWidget, QTreeWidget,QTreeWidgetItem)
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTreeWidget")

        self.trw = QTreeWidget()
        self.trw.setHeaderLabels(["Nome", "Valor"])
        self.trw.setAlternatingRowColors(True)
        candy = QTreeWidgetItem(self.trw, ["Doce", '2,00'])

        # Adição de caixa de seleção (checkbox)
        candy.setCheckState(0,Qt.CheckState.Checked)

        # Reaproveitamento da variável já inserida para inserção de subvalores
        QTreeWidgetItem(candy, ['brigadeiro','1,00'])
        QTreeWidgetItem(candy, ['beijinho','1,00'])

        # Criação de valores desativados
        other = QTreeWidgetItem(self.trw, ['outro','5,00'])
        other.setDisabled(True)

        layout = QVBoxLayout()
        layout.addWidget(self.trw)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()

    app.exec()

