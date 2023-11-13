from disponible import Disponible
from prestado import Prestado
from extraviado import Extraviado


class Libro:
    def __init__(self, id, codigo, titulo, descripcion, preciorep):
        self.id = id            #id de cada libro por separado
        self.codigo = codigo    #ISBN, codigo que identifica cada titulo       
        self.titulo = titulo
        self.descripcion = descripcion
        self.precioReposicion = preciorep
        self.estado = Disponible()


    #Definimos un metodo para cada cambio de estado

    def cambiar_a_disponible(self):
        if not isinstance(self.estado, Disponible):
            pass
        else:
            return "El libro esta en estado Disponible"

    def cambiar_a_prestado(self):
        if not isinstance(self.estado, Prestado):
            pass
        else:
            return "El libro esta en estado Prestado"

    def cambiar_a_extraviado(self):
        if not isinstance(self.estado, Extraviado):
            pass
        else:
            return "El libro esta en estado Extraviado"

    def cambiar_a_demorado(self):
        if not isinstance(self.estado, Extraviado):
            pass
        else:
            return "El libro esta en estado Extraviado"


    #Getters y setters
    def get_codigo(self):
        return self.codigo

    def set_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def get_precioReposicion(self):
        return self.precioReposicion

    def set_precioReposicion(self, nuevo_precio):
        self.precioReposicion = nuevo_precio

    def get_estado(self):
        return self.estado.get_nombre()

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado