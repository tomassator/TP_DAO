from clases.estado import Estado, ID_DISPONIBLE
from tipo_mensajes import ID_MENSAJE_ERROR, ID_MENSAJE_EXITO

class Disponible(Estado):
    
    def __init__(self, libro):
        self._id = ID_DISPONIBLE
        self._nombre = "DISPONIBLE"
        self._libro = libro

    def prestar(self):
        from clases.estados.prestado import Prestado
        self._libro.estado = Prestado(self._libro)
        return ID_MENSAJE_EXITO, "Préstamo registrado correctamente."

    def devolver(self):
        return ID_MENSAJE_ERROR, "No se puede devolver un libro disponible."

    def extraviado(self):
        return ID_MENSAJE_ERROR, "No se puede registrar como extraviado un libro disponible."

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
    

    

