from clases.estado import Estado


class Demorado(Estado):

    def __init__(self):
        self.id_estado = 4
        self.nombre = "Demorado"
        self.contexto = None


    def get_nombre(self):
        return self.nombre

    def cambiar_estado_disponible(self):
        return False

    def cambiar_estado_prestado(self):
        pass

    def cambiar_estado_extraviado(self):
        return "Un libro extraviado no puede pasar a estado Extraviado"

    def cambiar_estado_demorado(self):
        return False