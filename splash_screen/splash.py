from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QColor
import sys
from ui.splash_screen_ui import Ui_splash_screen

#Variáveis globais do contador(acesso será dado pelo "global" na frente da variável)
counter  = 0
jumper = 10

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_splash_screen()
        self.ui.setupUi(self)

        #Iniciando progress bar
        self.progressBarValue(0)

        #remove o titlebar para que não se possa redimensionar ou fechar a janela antes do fim do load
        #tela não terá barra de títulos com borda padrão
        self.setWindowFlags(Qt.FramelessWindowHint)

        #permite que a janela tenha fundo translúcido; útil quando se cria janelas personalizadas com formas não retangulares
        #utilizado geralmente junto com a flag Qt.FramelessWindowHint para criar janelas sem borda
        self.setAttribute(Qt.WA_TranslucentBackground)

        #aplicação de efeito drop shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        # criação do timer

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)

        self.show()

    def progress(self):
        global counter
        global jumper
        value = counter

        #texto com porcentagem no HTML
        htmlText = """
                    <p align="center"><span style=" font-size:72pt;">{VALUE}</span>
                    <span style=" font-size:62pt; vertical-align:super;">%</span></p>
                   """
        #substituição do valor
        newHtml = htmlText.replace("{VALUE}", str(jumper))


        if(value > jumper):
            self.ui.lbl_percentual.setText(newHtml)
            jumper += 10


        #definição do timer
        if value >= 100:
            value = 1.000


        self.progressBarValue(value)

        if counter > 100:
            self.timer.stop()

            #chamando a tela principal do programa (no caso, ainda vai ser criado - CADASTRO EMPRESAS)
            ## NOTA: Liberar quando classe MainWindow do projeto principal estiver pronta
            #self.main = MainWindow()
            #self.main.show()
            self.close()

        counter += 0.5


    #cx, cy: define o centro do grandiente (no meio do quadro)
    #gconicalgradiente: define o gradiente cônico
    #STOP: define os pontos de parada no gradiente com uma cor RGBA

    #A ideia é a cor azul de fundo ir completando o círculo do fundo
    def progressBarValue(self, value):
        stylesheet = """
                        QFrame{
                            border-radius: 150px;
	                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255,0,127,0), stop:{STOP_2} rgba(85,170,255,255));
                        }
                     """

        progress = (100 - value)/100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStylesheet = stylesheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)


        self.ui.circularProgress.setStyleSheet(newStylesheet)


#Remover ou alterar quando projeto estiver pronto ou acessível
if __name__ == "__main__":
    app =QApplication(sys.argv)
    #self.main = MainWindow()
    #apply_stylesheet(self.main, theme='dart_teal.xml') ## para não aplicar estilo no loader
    window = SplashScreen()
    window.show()

    app.exec()