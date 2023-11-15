from estado import Estado


class Prestado(Estado):
    def __init__(self):
        self.id_estado = 2
        self.nombre = "Prestado"
        self.contexto = None

    def get_nombre(self):
        return self.nombre

    def cambiar_estado_disponible(self):
        pass

    def cambiar_estado_prestado(self):
        pass

    def cambiar_estado_extraviado(self):
        pass

    def cambiar_estado_demorado(self):
        return False
