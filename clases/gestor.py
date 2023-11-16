import sqlite3
from libro import Libro
from socio import Socio
from singleton import ConexionSingleton

class Gestor:
    def __init__(self):
        
        self.conexion = ConexionSingleton("biblioteca.db")

    #LIBRO

    def agregar_libro(self, codigo, titulo, descripcion, precioReposicion):
        libro = Libro(codigo, titulo, descripcion, precioReposicion)
        libro.insertar_libro(self.conexion)

    def obtener_libros(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT * FROM libros")
        resultados = cursor.fetchall()

        libros = []
        for fila in resultados:
            libro = Libro(fila[1], fila[2],fila[3],fila[4], id=fila[0], estado=fila[5])
            libros.append(libro)
        self.conexion.cerrar_cursor()
        return libros        
    
    def eliminar_libro(self, id):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", [id])
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

    def actualizar_libro(self, id, codigo, titulo, descripcion, precioReposicion):
        libro = Libro(codigo, titulo, descripcion, precioReposicion, id=id)
        libro.actualizar_libro(self.conexion)

    
    #SOCIOS

    def agregar_socio(self, numeroSocio, nombre, apellido):
        socio = Socio(numeroSocio, nombre, apellido)
        socio.insertar_socio(self.conexion)

    def obtener_socios(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT * FROM socios")
        resultados = cursor.fetchall()

        socios = []
        for fila in resultados:
            socio = Socio(fila[0], fila[1], fila[2])
            socios.append(socio)
        return socios
    
    def eliminar_socio(self, nro_socio):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("DELETE FROM socios WHERE nro_socio = ?", [nro_socio])
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

    def actualizar_socio(self, nro_socio, nombre, apellido):
        socio = Socio(nro_socio, nombre, apellido)
        socio.actualizar_socio(self.conexion)



    

        
    


