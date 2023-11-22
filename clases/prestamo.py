from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, id, socio,tiempoPrestamo, fechaPrestamo, fechaPactadaDevolucion, fechaDevolucion, libro):
        self._id = id
        self._socio = socio
        self._tiempoPrestamo = tiempoPrestamo
        self._fechaPrestamo = fechaPrestamo
        self._fechaPactadaDevolucion = fechaPactadaDevolucion
        self._fechaDevolucion = fechaDevolucion
        self._libro = libro

    @property
    def id(self):
        return self._id

    @property
    def socio(self):
        return self._socio
    
    @socio.setter
    def nroSocio(self, socio):
        self._socio = socio

    @property
    def tiempoPrestamo(self):
        return self._tiempoPrestamo
    
    @tiempoPrestamo.setter
    def tiempoPrestamo(self, tiempoPrestamo):
        self._tiempoPrestamo = tiempoPrestamo

    @property
    def fechaPrestamo(self):
        return self._fechaPrestamo
    
    @fechaPrestamo.setter
    def fechaPrestamo(self, fechaPrestamo):
        self._fechaPrestamo = fechaPrestamo

    @property
    def fechaPactadaDevolucion(self):
        return self._fechaPactadaDevolucion

    @fechaPactadaDevolucion.setter
    def fechaPactadaDevolucion(self, fecha):
        self._fechaPactadaDevolucion = fecha

    @property
    def fechaDevolucion(self):
        return self._fechaDevolucion

    @fechaDevolucion.setter
    def fechaDevolucion(self, fecha):
        self._fechaDevolucion = fecha

    @property
    def libro(self):
        return self._libro

    @libro.setter
    def libro(self, libro):
        self._libro = libro