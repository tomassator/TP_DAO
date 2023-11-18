from estado import Estado
from extraviado import Extraviado
from prestado import Prestado

class Disponible(Estado):

    def __init__(self):
        self.id_estado = 1
        self.nombre = "Disponible"
        self.contexto = None

    def get_id_estado(self):
        return self.id_estado

    def set_id_estado(self,id):
        self.id_estado = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def cambiar_estado_disponible(self):
        return Disponible()

    def cambiar_estado_prestado(self):
        return Prestado()

    def cambiar_estado_extraviado(self):
        return None


