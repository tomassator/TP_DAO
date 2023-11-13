


class Socio:
    def __init__(self, nro_socio, nombre, apellido):
        self.nro_socio = nro_socio
        self.nombre = nombre
        self.apellido = apellido


    # Getters y Setters
    def get_nro_socio(self):
        return self.nro_socio
    
    def set_nro_socio(self, nuevo_nro):
        self.nro_socio = nuevo_nro
        
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido