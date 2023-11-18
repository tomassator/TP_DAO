from estado import Estado
from prestado import Prestado
from disponible import Disponible

class Extraviado(Estado):
    def __init__(self):
        self.id_estado = 3
        self.nombre = "Extraviado"
        self.contexto = None

    def get_nombre(self):
        return self.nombre

    def cambiar_estado_disponible(self):
        return Disponible()

    def cambiar_estado_prestado(self):
        return None

    def cambiar_estado_extraviado(self):
        return Extraviado()

