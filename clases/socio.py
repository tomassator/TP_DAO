class Socio:
    def __init__(self, nroSocio, nombre, apellido):
        self._nroSocio = nroSocio
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nroSocio(self):
        return self._nroSocio

    @nroSocio.setter
    def nro_socio(self, value):
        self._nroSocio = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value