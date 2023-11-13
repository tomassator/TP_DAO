from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, id, socio, dias):
        self.id = id
        self.socio = socio
        self.tiempoPrestamo = dias
        self.detallePrestamo = [] #Listas con objetos detalle de prestamos
        self.fecha_prestamo = datetime.now()
        self.fecha_pactada_devolucion = self.fecha_prestamo + timedelta(days=self.tiempoPrestamo)


    #Cargamos todos los libros prestados al prestamo
    def cargar_prestamo(self, detalles):
        for det in detalles:
            self.detallePrestamo.append(det)


    #Getters y Setters
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
