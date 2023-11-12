


class Socio:
    def __init__(self, nombre, apellido, nro_socio):
        self.nro_socio = nro_socio
        self.nombre = nombre
        self.apellido = apellido


    # Getters y Setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def get_dni(self):
        return self.dni

    def set_dni(self, nuevo_dni):
        self.dni = nuevo_dni