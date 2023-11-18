from estado import Estado
from extraviado import Extraviado
from disponible import Disponible


class Prestado(Estado):
    def __init__(self):
        self.id_estado = 2
        self.nombre = "Prestado"
        self.contexto = None

    def get_nombre(self):
        return self.nombre

    def cambiar_estado_disponible(self):
        return Disponible()

    def cambiar_estado_prestado(self):
        return Prestado()

    def cambiar_estado_extraviado(self):
        return Extraviado()

