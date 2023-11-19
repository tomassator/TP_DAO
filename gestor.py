from clases.socio import Socio
from clases.singleton import ConexionSingleton
from clases.estado import ID_DISPONIBLE
from clases.libro import Libro
from datetime import datetime
from tipo_mensajes import ID_MENSAJE_ERROR

class Gestor:
    def __init__(self):
        self.conexion = ConexionSingleton("biblioteca.db")

    # Socios
    def agregar_socio(self, nombre, apellido):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("INSERT INTO socios (nombre, apellido) VALUES (?, ?)",
                       (nombre, apellido))
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

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
        cursor = self.conexion.obtener_cursor()
        cursor.execute("UPDATE socios SET nombre = ?, apellido = ? WHERE nro_socio = ?",
                       (nombre, apellido, nro_socio))
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()
        print(f"Información del socio con número {nro_socio} actualizada correctamente.")

    # Libros

    def agregar_libro(self, codigo, titulo, descripcion, precioReposicion):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("INSERT INTO libros (codigo, titulo, descripcion, precioReposicion, id_estado) VALUES (?, ?, ?, ?, ?)",
                       (codigo, titulo, descripcion, precioReposicion, ID_DISPONIBLE))
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

    def obtener_libros(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT * FROM libros")
        resultados = cursor.fetchall()

        libros = []
        for fila in resultados:
            libro = Libro(fila[0], fila[1], fila[2],fila[3],fila[4], fila[5])
            libros.append(libro)
        self.conexion.cerrar_cursor()
        return libros        
    
    def eliminar_libro(self, id):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", [id])
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

    def actualizar_libro(self, id, codigo, titulo, descripcion, precioReposicion):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("UPDATE libros SET codigo = ?, titulo = ?, descripcion = ?, precioReposicion = ? WHERE id = ?",
                       (codigo, titulo, descripcion, precioReposicion, id))
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

    def obtener_libro(self, id):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT * FROM libros WHERE id = ?", [id])
        fila = cursor.fetchone()
        self.conexion.cerrar_cursor()
        return Libro(fila[0], fila[1], fila[2],fila[3],fila[4], fila[5])
    
    def actualizar_estado_libro(self, id, idEstado):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("UPDATE libros SET id_estado = ? WHERE id = ?",
                       (idEstado, id))
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

    def obtener_libros_disponibles(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute(f"SELECT * FROM libros WHERE id_estado = {ID_DISPONIBLE}")
        resultados = cursor.fetchall()

        libros = []
        for fila in resultados:
            libro = Libro(fila[0], fila[1], fila[2],fila[3],fila[4], fila[5])
            libros.append(libro)
        self.conexion.cerrar_cursor()
        return libros   
    
    # Prestamos

    def prestar_libro(self, idLibro, nro_socio):
        if self.verificar_prestamo(nro_socio):
            libro = self.obtener_libro(idLibro)
            tipoMensaje, mensaje = libro.prestar()
            self.actualizar_estado_libro(idLibro, libro.estado.id)
        else:
            tipoMensaje, mensaje = ID_MENSAJE_ERROR, "No se puede registrar un prestamo para este socio."
        return tipoMensaje, mensaje

    def registrar_prestamo(self, idLibro, nroSocio, fechaActual, tiempoPrestamo, fechaPactada):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("INSERT INTO prestamo (tiempoPrestamo, fecha_prestamo, fecha_pactada_devolucion, id_socio) VALUES (?, ?, ?, ?)",
                       (tiempoPrestamo, fechaActual, fechaPactada, nroSocio))
        
        id_prestamo = cursor.lastrowid

        cursor.execute("INSERT INTO detalle_prestamo (id_prestamo, id_libro) VALUES (?, ?)",
                       (id_prestamo, idLibro))

        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

    #Chequear que al solicitar un prestamo el socio no tenga mas de 3 libros prestados y de tener menos
    #que ninguno de ellos este demorado en su devolucion
    #No se consideran los extraviados
    def verificar_prestamo(self, nro_socio):

        #Validacion de no mas de 3 libros prestados
        cursor = self.conexion.obtener_cursor()
        cursor.execute(
            "select COUNT(*) from detalle_prestamo dp \
                INNER JOIN prestamo p ON p.id=dp.id_prestamo \
                INNER JOIN libros l ON dp.id_libro = l.id \
                WHERE p.id_socio = ? AND l.id_estado = 2", [nro_socio])
        cantidad_libros = int(cursor.fetchone()[0])

        #Validacion ningun libro demorado

        cursor.execute(
            "select COUNT(*) from detalle_prestamo dp \
                INNER JOIN prestamo p ON p.id=dp.id_prestamo \
                INNER JOIN libros l ON dp.id_libro = l.id \
                WHERE l.id_estado = 2 AND  julianday(?) - julianday(p.fecha_pactada_devolucion) > 0 AND p.id_socio = ?",
            (datetime.now(),nro_socio))
        cantidad_libros_demorados = int(cursor.fetchone()[0])

        return cantidad_libros <= 3 and cantidad_libros_demorados == 0
    
    #Reportes

    #Reporte que indica la sumatoria del precio de reposicion de todos los libros que se encuentren en estado extraviado
    def generar_reporte_precio_extraviados(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT SUM(precioReposicion) FROM libros WHERE id_estado = 3")
        resultados = cursor.fetchall()
        cursor.close()

    #Reporque que indica en cuantos libros estan en cada uno de los tres estados posibles
    def generar_reporte_cant_librosxestado(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT id_estado, COUNT(*) FROM libros GROUP BY id_estado")
        resultados = cursor.fetchall()
        cursor.close()

    #Reporte que muestra todos los socios que solicitaron un determinado libro filtrado por su titulo
    def generar_reporte_nombre_socios_libro(self, titulo):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT s.*, l.titulo from prestamo p \
                        INNER JOIN detalle_prestamo dp ON p.id = dp.id_prestamo \
                        INNER JOIN libros l ON dp.id_libro = l.id \
                        INNER JOIN socios s ON s.nro_socio = p.id_socio\
                        where titulo = ?",
                       (titulo,))  # Cambiar el 4334 por el titulo del libro que viene como dato de la interfaz
        resultados = cursor.fetchall()
        cursor.close()

    #Reporte que muestra prestamos dado un determinado socio
    def generar_reporte_prestamos_socio(self,socio):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT p.*, s.nombre, s.apellido from prestamo p \
                       INNER JOIN socios s ON s.nro_socio = p.id_socio \
                       where id_socio = ?",(socio,))

        resultados = cursor.fetchall()
        cursor.close()

    #Reporte que muestra y mapea los prestamos con demora en su devolucion para mostrar en pantalla
    def generar_reporte_prestamos_demorados(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute(
            "SELECT * from prestamo \
            where julianday(?) - julianday(fecha_pactada_devolucion) > 0", (datetime.now(),))
        resultados = cursor.fetchall()
        cursor.close()
        print(resultados)
    
    #Otras funcionalidades
    
    #Libros que no se devolvieron y ya paso la fecha pactada
    def obtener_libros_demorados(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute(
            "select l.* from detalle_prestamo dp \
                INNER JOIN prestamo p ON p.id=dp.id_prestamo \
                INNER JOIN libro l ON dp.id_libros = l.id \
                WHERE l.id_estado = 2 AND  julianday(?) - julianday(p.fecha_pactada_devolucion) > 0", (datetime.now(),))
        resultados = cursor.fetchall()
        cursor.close()

        print(resultados)

        libros = []
        for fila in resultados:
            libro = Libro(fila[1], fila[2], fila[3],fila[4], id=fila[0], estado=fila[5])
            libros.append(libro)
        return libros
    
    #Esta funcionalidad se deberia ejecutar cuando en la ventana el usuario haga click en actualizar estado de libro
    #Dados una lista de libros con mas de 30 dias de demora en la fecha de devolucion pactada
    def actualizar_libros_extraviados(self, libros):
        for libro in libros:
            libro.set_estado(3)
            libro.actualizar_libro()
