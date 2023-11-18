from disponible import Disponible
from prestado import Prestado
from extraviado import Extraviado


class Libro:
    def __init__(self, codigo, titulo, descripcion, preciorep, id=None, estado=1):
        self.codigo = codigo    #ISBN, codigo que identifica cada titulo       
        self.titulo = titulo
        self.descripcion = descripcion
        self.precioReposicion = preciorep
        self.id = id
        self.estado = None
        self.set_estado(estado)
    

    #ABM
    def insertar_libro(self, conexion):
        cursor = conexion.obtener_cursor()
        cursor.execute("INSERT INTO libros (codigo, titulo, descripcion, precioReposicion, id_estado) VALUES (?, ?, ?, ?, ?)",
                       (self.get_codigo(), self.get_titulo(), self.get_descripcion(), self.get_precioReposicion(), self.estado.get_id_estado()))
        conexion.conexion_commit()
        conexion.cerrar_cursor()

    def actualizar_libro(self,conexion):
        cursor = conexion.obtener_cursor()
        cursor.execute("UPDATE libros SET codigo = ?, titulo = ?, descripcion = ?,precioReposicion = ?,id_estado = ? WHERE id = ?",
                       (self.get_codigo(), self.get_titulo(), self.get_descripcion(), self.get_precioReposicion(), self.estado.get_id_estado(), self.get_id()))
        conexion.conexion_commit()
        conexion.cerrar_cursor()

    def eliminar_libro(self,conexion):
        cursor = conexion.obtener_cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", (self.get_id()))
        conexion.conexion_commit()
        conexion.cerrar_cursor()


    #Definimos un metodo para cada cambio de estado
    def cambiar_a_disponible(self):
        if not isinstance(self.estado, Disponible):
            self.estado.cambiar_estado_disponible()
        else:
            return "El libro esta en estado Disponible"

    def cambiar_a_prestado(self):
        if not isinstance(self.estado, Prestado):
            self.estado.cambiar_estado_prestado()
        else:
            return "El libro esta en estado Prestado"

    def cambiar_a_extraviado(self):
        if not isinstance(self.estado, Extraviado):
            self.estado.cambiar_estado_extraviado()
        else:
            return "El libro esta en estado Extraviado"

    def cambiar_a_demorado(self):
        if not isinstance(self.estado, Extraviado):
            pass
        else:
            return "El libro esta en estado Extraviado"


    #Getters y setters
    def get_id(self):
        return self.id

    def set_id(self, nuevo_id):
        self.id = nuevo_id
        
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
        if nuevo_estado == 1:
            self.estado = Disponible()
        elif nuevo_estado == 2:
            self.estado = Prestado()
        elif nuevo_estado == 3:
            self.estado = Extraviado()