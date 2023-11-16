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


    # REPORTES

    def generar_reporte_precio_extraviados(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT SUM(precioReposicion) FROM libros WHERE id_estado = 3")
        resultados = cursor.fetchall()

    def generar_reporte_cant_librosxestado(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT id_estado, COUNT(*) FROM libros GROUP BY id_estado")
        resultados = cursor.fetchall()

    def generar_reporte_nombre_socios_libro(self, titulo):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT s.*, l.titulo from prestamo p \
                        INNER JOIN detalle_prestamo dp ON p.id = dp.id_prestamo \
                        INNER JOIN libros l ON dp.id_libro = l.id \
                        INNER JOIN socios s ON s.nro_socio = p.id_socio\
                        where titulo = ?",
                       (titulo,))  # Cambiar el 4334 por el titulo del libro que viene como dato de la interfaz
        resultados = cursor.fetchall()

    def generar_reporte_prestamos_socio(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT p.*, s.nombre, s.apellido from prestamo p \
                       INNER JOIN socios s ON s.nro_socio = p.id_socio \
                       where id_socio = 1")
        resultados = cursor.fetchall()

    def generar_reporte_prestamos_demorados(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute(
            "SELECT julianday(fecha_pactada_devolucion) - julianday(fecha_prestamo) as ASD from prestamo")
        resultados = cursor.fetchall()
        print(resultados)


    

        
    


