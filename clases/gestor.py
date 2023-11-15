import sqlite3
from libro import Libro

class Gestor:
    def __init__(self):
        self.conexion = sqlite3.connect("biblioteca.db")

    def agregar_libro(self, codigo, titulo, descripcion, precioReposicion):
        libro = Libro(codigo, titulo, descripcion, precioReposicion)
        libro.insertar_libro(self.conexion)

    def obtener_libros(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM libros")
        resultados = cursor.fetchall()

        libros = []
        for fila in resultados:
            libro = Libro(fila[1], fila[2],fila[3],fila[4], id=fila[0], estado=fila[5])
            libros.append(libro)
        return libros
    
    def eliminar_libro(self, id):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", (id))
        self.conexion.commit()
        cursor.close()



    

        
    


