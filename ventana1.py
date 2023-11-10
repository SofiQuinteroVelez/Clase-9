import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog
from PyQt5 import QtGui, QtCore


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


        # --------LAYOUT IZQUIERDO-----------

        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Información del cliente")
        self.letrero1.setFont(QFont("Candara", 20))
        self.letrero1.setStyleSheet("color: #000080;")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(340)
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Century", 10))
        self.letrero2.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "martgin top: 20px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Ususario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        self.horizontal.addLayout(self.ladoIzquierdo)

        # ---------LAYOUT DERECHO-------

        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel()
        self.letrero3.setText("Recuperar contraseña")
        self.letrero3.setFont(QFont("Candara", 20))
        self.letrero3.setStyleSheet("color: #000080;")

        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la informarción para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        self.letrero4.setFont(QFont("Century", 10))

        self.letrero4.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "martgin top: 20px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoDerecho.addRow(self.letrero4)

        # ------1
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta1)

        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

        # ------2
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        # ------3
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)

        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(90)
        self.botonBuscar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")

        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(90)
        self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                            "color: #FFFFFF;"
                                            "padding: 10px;"
                                            "margin-top: 40px;")

        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)

        self.horizontal.addLayout(self.ladoDerecho)

        self.horizontal.addLayout(self.ladoDerecho)

        # ---------- FINAL---------
        #el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        self.nombreCompleto.setText(' ')
        self.usuario.setText(' ')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText(' ')
        self.correo.setText(' ')
        self.pregunta1.setText(' ')
        self.respuesta1.setText(' ')
        self.pregunta2.setText(' ')
        self.respuesta2.setText(' ')
        self.pregunta3.setText(' ')
        self.respuesta3.setText(' ')


    def accion_botonRegistrar(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())