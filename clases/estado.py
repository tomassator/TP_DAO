from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def prestar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass

# Constantes
ID_DISPONIBLE = 1
ID_PRESTADO = 2
ID_EXTRAVIADO = 3



