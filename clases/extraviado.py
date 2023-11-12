from estado import Estado

class Extraviado(Estado):
    def __init__(self):
        self.id_estado = 3
        self.nombre = "Extraviado"
        self.contexto = None

    def get_nombre(self):
        return self.nombre

    def cambiar_estado_disponible(self):
        pass

    def cambiar_estado_prestado(self):
        return "Un libro extraviado no puede pasar a estado Prestado"

    def cambiar_estado_extraviado(self):
        pass

    def cambiar_estado_demorado(self):
        return "Un libro extraviado no puede pasar a estado Demorado"
