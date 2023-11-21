from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, id, socio, dias, fecha_prestamo, fecha_devolucion, id_libro):
        self.id = id
        self.socio = socio
        self.tiempoPrestamo = dias
        self.fecha_prestamo = fecha_prestamo
        self.fecha_pactada_devolucion = self.fecha_prestamo + timedelta(days=self.tiempoPrestamo)
        self.fecha_devolucion = fecha_devolucion
        self.id_libro = id_libro


    #Registracion de prestamos y devoluciones
    def insertar_prestamo(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO prestamo (id, tiempoPrestamo, fecha_prestamo, fecha_pactada_devolucion, fecha_devolucion, id_socio) VALUES (?, ?, ?)",
                       (self.get_id(), self.get_tiempoPrestamo(), self.get_fecha_prestamo(), self.get_fecha_pactada_devolucion(), self.get_fecha_devolucion(), self.socio.get_nro_socio()))
        conexion.commit()
        conexion.close()

    def actualizar_prestamo(self,conexion):
        cursor = conexion.cursor()
        cursor.execute("UPDATE prestamo  SET tiempoPrestamo = ?, fecha_prestamo = ?, fecha_pactada_devolucion = ?, fecha_devolucion = ?, id_socio = ? WHERE id = ?",
                       (self.get_tiempoPrestamo(), self.get_fecha_prestamo(), self.get_fecha_pactada_devolucion(), self.get_fecha_devolucion(), self.socio.get_nro_socio(), self.get_id()))
        conexion.commit()
        conexion.close()



    #Getters y Setters
    def get_id(self):
        return self.id

    def set_id(self, nuevo_id):
        self.id = nuevo_id
    
    def get_socio(self):
        return self.socio

    def set_socio(self, nuevo_socio):
        self.socio = nuevo_socio

    def get_tiempoPrestamo(self):
        return self.tiempoPrestamo

    def set_tiempoPrestamo(self, nuevos_dias):
        self.tiempoPrestamo = nuevos_dias

    def get_detallePrestamo(self):
        return self.detallePrestamo

    def set_detallePrestamo(self, nuevo_detalle):
        self.detallePrestamo = nuevo_detalle

    def get_fecha_prestamo(self):
        return self.fecha_prestamo

    def set_fecha_prestamo(self, nueva_fecha):
        self.fecha_prestamo = nueva_fecha
        
    def get_fecha_devolucion(self):
        return self.fecha_devolucion
    
    def set_fecha_devolucion(self, nueva_fecha):
        self.fecha_devolucion = nueva_fecha

    def get_fecha_pactada_devolucion(self):
        return self.fecha_pactada_devolucion

    def set_fecha_pactada_devolucion(self, fecha):
        self.fecha_pactada_devolucion = fecha
