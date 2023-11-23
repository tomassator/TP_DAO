from clases.estado import Estado, ID_EXTRAVIADO
from tipo_mensajes import ID_MENSAJE_ERROR

class Extraviado(Estado):
    
    def __init__(self, libro):
        self._id = ID_EXTRAVIADO
        self._nombre = "EXTRAVIADO"
        self._libro = libro

    def prestar(self):
        return ID_MENSAJE_ERROR, "No se puede prestar un libro extraviado."

    def devolver(self):
        return ID_MENSAJE_ERROR, "No se puede devolver un libro extraviado."

    def extraviado(self):
        return ID_MENSAJE_ERROR, "El libro ya se encuentra extraviado"

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