class Cliente:

<<<<<<< HEAD

   def __init__(self, nombreCompleto,
               usuario,
               password,
               documento,
               correo,
               pregunta1,
               respuesta1,
               pregunta2,
               respuesta2,
               pregunta3,
               respuesta3,
               ):
       self.nombreCompleto = nombreCompleto
       self.usuario = usuario
       self.password = password
       self.documento = documento
       self.correo = correo
       self.pregunta1 = pregunta1
       self.respuesta1 = respuesta1
       self.pregunta2 = pregunta2
       self.respuesta2 = respuesta2
       self.pregunta3 = pregunta3
       self.respuesta3 = respuesta3


   def __str__(self):
       return f"Nombre: {self.nombreCompleto} Documento: {self.documento}"
=======
    def __init__(self, nombreCompleto,
                 usuario,
                 password,
                 documento,
                 correo,
                 pregunta1,
                 respuesta1,
                 pregunta2,
                 respuesta2,
                 pregunta3,
                 respuesta3,
                 ):
        self.nombreCompleto = nombreCompleto
        self.usuario = usuario
        self.password = password
        self.documento = documento
        self.correo = correo
        self.pregunta1 = pregunta1
        self.respuesta1 = respuesta1
        self.pregunta2 = pregunta2
        self.respuesta2 = respuesta2
        self.pregunta3 = pregunta3
        self.respuesta3 = respuesta3

    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Documento: {self.documento}"
>>>>>>> 8e129cff53de6231446064b162917196048f79bf
