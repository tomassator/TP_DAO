from clases.estado import Estado


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
        return False

    def cambiar_estado_prestado(self):
        pass

    def cambiar_estado_extraviado(self):
        return "Un libro disponible no puede pasar a estado Extraviado"

    def cambiar_estado_demorado(self):
        return "Un libro disponible no puede pasar a estado Demorado"

