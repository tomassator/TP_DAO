from clases.socio import Socio
from clases.singleton import ConexionSingleton
from clases.estado import ID_DISPONIBLE, ID_PRESTADO
from clases.libro import Libro
from clases.prestamo import Prestamo
from datetime import datetime
from tipo_mensajes import ID_MENSAJE_ERROR, ID_MENSAJE_EXITO

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
    
    def obtener_socio(self, nroSocio):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT * FROM socios WHERE nro_socio = ?", [nroSocio])
        fila = cursor.fetchone()
        self.conexion.cerrar_cursor()
        return Socio(fila[0], fila[1], fila[2])
    
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

    def obtener_prestamo(self, idPrestamo):
        cursor = self.conexion.obtener_cursor()
        cursor.execute(f"SELECT * FROM prestamo WHERE id = {idPrestamo}")
        resultado = cursor.fetchone()

        socio = self.obtener_socio(resultado[5])
        libro = self.obtener_libro(resultado[6])
        prestamo = Prestamo(resultado[0], socio,resultado[1],resultado[2],resultado[3],resultado[4], libro)

        self.conexion.cerrar_cursor()
        return prestamo     
    
    def obtener_prestamos_activos(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute(f"SELECT * FROM prestamo p INNER JOIN libros l ON p.id_libro = l.id \
                       WHERE fecha_devolucion IS NULL and l.id_estado = {ID_PRESTADO}")
        resultados = cursor.fetchall()

        prestamos = []
        for fila in resultados:
            socio = self.obtener_socio(fila[5])
            libro = self.obtener_libro(fila[6])
            prestamo = Prestamo(fila[0], socio,fila[1],fila[2],fila[3],fila[4], libro)
            prestamos.append(prestamo)
        self.conexion.cerrar_cursor()
        return prestamos        

    def prestar_libro(self, idLibro, nroSocio, tiempoPrestamo, fechaPactada):
        if self.verificar_prestamo(nroSocio):
            libro = self.obtener_libro(idLibro)
            tipoMensaje, mensaje = libro.prestar()

            if (tipoMensaje == ID_MENSAJE_EXITO):
                self.actualizar_estado_libro(idLibro, libro.estado.id)
                self.registrar_prestamo(idLibro, nroSocio, datetime.now(), tiempoPrestamo, fechaPactada)
        else:
            tipoMensaje, mensaje = ID_MENSAJE_ERROR, "No se puede registrar un prestamo para este socio."
        return tipoMensaje, mensaje

    def registrar_prestamo(self, idLibro, nroSocio, fechaActual, tiempoPrestamo, fechaPactada):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("INSERT INTO prestamo (tiempoPrestamo, fecha_prestamo, fecha_pactada_devolucion, id_socio, id_libro) VALUES (?, ?, ?, ?,?)",
                       (tiempoPrestamo, fechaActual, fechaPactada, nroSocio, idLibro))

        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()

    #Chequear que al solicitar un prestamo el socio no tenga mas de 3 libros prestados y de tener menos
    #que ninguno de ellos este demorado en su devolucion
    #No se consideran los extraviados
    def verificar_prestamo(self, nro_socio):

        #Validacion de no mas de 3 libros prestados
        cursor = self.conexion.obtener_cursor()
        cursor.execute(
            "select COUNT(*) from prestamo p\
                INNER JOIN libros l ON p.id_libro = l.id \
                WHERE p.id_socio = ? AND l.id_estado = 2", [nro_socio])
        cantidad_libros = int(cursor.fetchone()[0])
        #Validacion ningun libro demorado

        cursor.execute(
            "select COUNT(*) from prestamo p \
                INNER JOIN libros l ON p.id_libro = l.id \
                WHERE l.id_estado = 2 AND  julianday(?) - julianday(p.fecha_pactada_devolucion) > 0 AND p.id_socio = ?",
            (datetime.now(),nro_socio))
        cantidad_libros_demorados = int(cursor.fetchone()[0])

        return cantidad_libros < 3 and cantidad_libros_demorados == 0
    
    def actualizar_fecha_devolucion_prestamo(self, idPrestamo, fechaDevolucion):
        cursor = self.conexion.obtener_cursor()
        fechaDevolucion = fechaDevolucion.strftime("%Y-%m-%d %H:%M:%S") 
        cursor.execute(f"UPDATE prestamo SET fecha_devolucion = '{fechaDevolucion}' WHERE id = {idPrestamo}")
        self.conexion.conexion_commit()
        self.conexion.cerrar_cursor()
    
    #Devoluciones

    def devolver_libro(self, idPrestamo, fechaDevolucion):
        libro = self.obtener_prestamo(idPrestamo).libro
        tipoMensaje, mensaje = libro.devolver()

        if tipoMensaje == ID_MENSAJE_EXITO:
            self.actualizar_estado_libro(libro.id, libro.estado.id)
            self.actualizar_fecha_devolucion_prestamo(idPrestamo, fechaDevolucion)
        
        return tipoMensaje, mensaje
    
    # Extravio

    def registrar_extravio(self, libros):
        mensajePantalla = None
        for idLibro in libros:
            libro = self.obtener_libro(idLibro)
            tipoMensaje, mensaje = libro.extraviado()

            if tipoMensaje == ID_MENSAJE_EXITO:
                mensajePantalla =  mensaje
                self.actualizar_estado_libro(libro.id, libro.estado.id)

        return ID_MENSAJE_EXITO, mensajePantalla
            
    #Reportes

    #Reporte que indica la sumatoria del precio de reposicion de todos los libros que se encuentren en estado extraviado
    def generar_reporte_precio_extraviados(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT SUM(precioReposicion) FROM libros WHERE id_estado = 3")
        resultados = cursor.fetchone()[0]
        cursor.close()
        return resultados

    #Reporque que indica en cuantos libros estan en cada uno de los tres estados posibles
    def generar_reporte_cant_librosxestado(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT e.nombre, COUNT(*) FROM libros l \
                       INNER JOIN estado e ON e.id = l.id_estado\
                       GROUP BY e.nombre")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados


    #Reporte que muestra todos los socios que solicitaron un determinado libro filtrado por su titulo
    def generar_reporte_nombre_socios_libro(self, titulo):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT DISTINCT s.nro_socio, s.nombre, s.apellido from prestamo p \
                        INNER JOIN libros l ON p.id_libro = l.id \
                        INNER JOIN socios s ON s.nro_socio = p.id_socio\
                        where titulo = ?",
                       (titulo,))  # Cambiar el 4334 por el titulo del libro que viene como dato de la interfaz
        resultados = cursor.fetchall()
        cursor.close()

        socios = []
        for fila in resultados:
            socio = Socio(fila[0], fila[1], fila[2])
            socios.append(socio)
        return socios


    #Reporte que muestra prestamos dado un determinado socio
    def generar_reporte_prestamos_socio(self,socio):
        cursor = self.conexion.obtener_cursor()
        cursor.execute("SELECT p.* , s.* from prestamo p \
                       INNER JOIN socios s ON s.nro_socio = p.id_socio \
                       where id_socio = ?",(socio,))

        resultados = cursor.fetchall()

        cursor.close()

        prestamos = []
        for fila in resultados:
            prestamo = Prestamo(fila[0],Socio(fila[7], fila[8], fila[9]),fila[1],datetime.strptime(fila[2], "%Y-%m-%d %H:%M:%S.%f"),fila[3],fila[4],fila[6])

            prestamos.append(prestamo)
        return prestamos

    #Reporte que muestra y mapea los prestamos con demora en su devolucion para mostrar en pantalla
    def generar_reporte_prestamos_demorados(self):

        cursor = self.conexion.obtener_cursor()
        cursor.execute(
            "SELECT p.*,s.* from prestamo p INNER JOIN socios s ON s.nro_socio = p.id_socio \
            where julianday(date('now')) - julianday(fecha_pactada_devolucion) > 0")
        resultados = cursor.fetchall()
        print(resultados)
        cursor.close()

        prestamos = []
        for fila in resultados:
            prestamo = Prestamo(fila[0], Socio(fila[7], fila[8], fila[9]), fila[1], datetime.strptime(fila[2], "%Y-%m-%d %H:%M:%S.%f"), fila[3],fila[4], fila[6])
            prestamos.append(prestamo)
        return prestamos

    
    #Otras funcionalidades
    
    #Libros que no se devolvieron y ya paso la fecha pactada
    def obtener_prestamos_demorados(self):
        cursor = self.conexion.obtener_cursor()
        cursor.execute(
            "select l.*, p.* from prestamo p \
                INNER JOIN libros l ON p.id_libro = l.id \
                WHERE l.id_estado = 2 AND  julianday(date('now')) - julianday(p.fecha_pactada_devolucion) > 30")
        resultados = cursor.fetchall()
        cursor.close()

        prestamos = []
        for fila in resultados:
            prestamo = Prestamo(fila[6],fila[11],fila[7],fila[8],fila[9],fila[10],Libro(fila[12],fila[1],fila[2],fila[3],fila[4],fila[5]))
            prestamos.append(prestamo)
        return prestamos
    
    #Esta funcionalidad se deberia ejecutar cuando en la ventana el usuario haga click en actualizar estado de libro
    #Dados una lista de libros con mas de 30 dias de demora en la fecha de devolucion pactada
    def actualizar_libros_extraviados(self, libros):
        for libro in libros:
            libro.set_estado(3)
            libro.actualizar_libro()
