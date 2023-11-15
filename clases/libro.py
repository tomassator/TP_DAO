from disponible import Disponible
from prestado import Prestado
from extraviado import Extraviado


class Libro:
    def __init__(self, codigo, titulo, descripcion, preciorep, estado=Disponible()):
        self.codigo = codigo    #ISBN, codigo que identifica cada titulo       
        self.titulo = titulo
        self.descripcion = descripcion
        self.precioReposicion = preciorep
        self.estado = estado

    #ABM
    def insertar_libro(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO libros (codigo, titulo, descripcion, precioReposicion, id_estado) VALUES (?, ?, ?, ?, ?)",
                       (self.get_codigo(), self.get_titulo(), self.get_descripcion(), self.get_precioReposicion(), self.estado.get_id_estado()))
        conexion.commit()
        conexion.close()

    def actualizar_libro(self,conexion):
        cursor = conexion.cursor()
        cursor.execute("UPDATE libros SET codigo = ?, titulo = ?, descripcion = ?,precioReposicion = ?,id_estado = ? WHERE id = ?",
                       (self.get_codigo(), self.get_titulo(), self.get_descripcion(), self.get_precioReposicion(), self.estado.get_id_estado(), self.get_id()))
        conexion.commit()
        conexion.close()


    def eliminar_libro(self,conexion):
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", (self.get_id()))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_libros(conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM libros")
        resultados = cursor.fetchall()

        libros = []
        for fila in resultados:
            libro = Libro(fila[0], fila[1],fila[2],fila[3],fila[4], fila[5])
            libros.append(libro)
        return libros





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
        self.estado = nuevo_estado