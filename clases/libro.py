from clases.estados.disponible import Disponible
from clases.estados.prestado import Prestado
from clases.estados.extraviado import Extraviado
from clases.estado import ID_DISPONIBLE, ID_EXTRAVIADO, ID_PRESTADO

class Libro:
    def __init__(self, id, codigo, titulo, descripcion, precioReposicion, estado):
        self._id = id
        self._codigo = codigo    # ISBN, codigo que identifica cada titulo       
        self._titulo = titulo
        self._descripcion = descripcion
        self._precioReposicion = precioReposicion
        self.set_estado(estado)

    def prestar(self):
        return self._estado.prestar()

    def devolver(self):
        return self._estado.devolver() 

    def set_estado(self, idEstado):
        if idEstado == ID_DISPONIBLE:
            self._estado = Disponible(self)
        elif idEstado == ID_PRESTADO:
            self._estado = Prestado(self)
        elif idEstado == ID_EXTRAVIADO:
            self._estado = Extraviado(self)

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def precioReposicion(self):
        return self._precioReposicion

    @precioReposicion.setter
    def precioReposicion(self, precioReposicion):
        self._precioReposicion = precioReposicion

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado


