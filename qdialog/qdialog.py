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
    QLineEdit)
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from pathlib import Path

icons = Path.joinpath(Path(__file__).parent,'icons','fugue-icons-3.5.6','icons')

class Meu_Dialog(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Meu Dialog")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        """
        QDialogButtonBox.Ok
        QDialogButtonBox.Open
        QDialogButtonBox.Save
        QDialogButtonBox.Cancel
        QDialogButtonBox.Close
        QDialogButtonBox.Discard
        QDialogButtonBox.Apply
        QDialogButtonBox.Reset
        QDialogButtonBox.RestoreDefaults
        QDialogButtonBox.Help
        QDialogButtonBox.SaveAll
        QDialogButtonBox.Yes
        QDialogButtonBox.YesToAll
        QDialogButtonBox.No
        QDialogButtonBox.NoToAll
        QDialogButtonBox.Abort
        QDialogButtonBox.Retry
        QDialogButtonBox.Ignore
        QDialogButtonBox.NoButton
            
        """

        self.btn_box = QDialogButtonBox(buttons)
        self.btn_box.accepted.connect(self.accept)
        self.btn_box.rejected.connect(self.reject)

        #Traduzindo os nomes nos botões
        self.btn_box.button(QDialogButtonBox.Ok).setText("Sim")
        self.btn_box.button(QDialogButtonBox.Cancel).setText("Cancelar")

        #self.btn_box.addButton("Executar", QDialogButtonBox.ActionRole)

        #self.btn_box.clicked.connect(self.run)

        msg = QLabel("Você deseja continuar?")
        self.txt_nome = QLineEdit()
        self.texto = ""

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.txt_nome)
        self.layout.addWidget(msg)
        self.layout.addWidget(self.btn_box)


        '''container = QFrame()
        container.setLayout(self.layout)'''

        self.setLayout(self.layout)

        #self.texto = self.txt_nome.text() ##Não funciona... tem que ter a função accept, que atualiza no momento em que se aceita na qdialog
    
    # Função ativada ao se pressionar o botão de aceite
    def accept(self) -> None:
        self.texto = self.txt_nome.text()
        return super().accept()
    
    def run(self):
        print ("Executando...")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDialog")

        btn = QPushButton("Clique para abrir uma caixa de dialogo")
        btn.clicked.connect(self.button_clicked)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(btn)

        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)
        
        
    def button_clicked(self, s):
        print("clicado ",s)

        '''dlg = QDialog(self)
        dlg.setWindowTitle("Minha caixa de diálogo")
        dlg.exec()'''

        dlg = Meu_Dialog()

        if dlg.exec():
            print("Sucesso!")
            print(dlg.texto)
        else:
            print("Cancelar!")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()