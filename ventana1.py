import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication
from PyQt5 import QtGui

class Ventana1(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        self.setWindowTitle("Formulario de registro")

        #Poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/cat.jpg'))

        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenfondo = QPixmap('imagenes/beach-sunset.jpg')
        self.fondo.setPixmap(self.imagenfondo)
        self.fondo.setScaledContents(True)

        # hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenfondo.width(), self.imagenfondo.height())

        self.setCentralWidget(self.fondo)

        #distribucion layaout horizontal
        self.horizontal = QHBoxLayout()
        # margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)



        # ---------- FINAL---------
        #el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())