from clases.estado import Estado

class Prestado(Estado):
    
    def __init__(self, libro):
        self._id = 2
        self._nombre = "PRESTADO"
        self._libro = libro

    def prestar(self):
        pass

    def devolver(self):
        pass

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