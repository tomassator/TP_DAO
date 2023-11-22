from clases.estado import Estado
from clases.estado import Estado, ID_PRESTADO
from tipo_mensajes import ID_MENSAJE_EXITO

class Prestado(Estado):
    
    def __init__(self, libro):
        self._id = ID_PRESTADO
        self._nombre = "PRESTADO"
        self._libro = libro

    def prestar(self):
        pass

    def devolver(self):
        from clases.estados.disponible import Disponible
        self._libro.estado = Disponible(self._libro)
        return ID_MENSAJE_EXITO, "Devolución registrada correctamente."

    @property
    def libro(self):
        return self._libro
    
    @libro.setter
    def libro(self, libro):
        self._libro = libro

    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre