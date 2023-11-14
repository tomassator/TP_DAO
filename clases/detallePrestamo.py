

class DetallePrestamo:
    def __init__(self, id, libro):
        self.id = id
        self.id_prestamo = None
        self.libro = libro


    # Getters y Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id


    def get_id_prestamo(self):
        return self.libro

    def set_id_prestamo(self, id_prestamo):
        self.id_prestamo = id_prestamo


    def get_libro(self):
        return self.libro

    def set_libro(self, nuevo_libro):
        self.libro = nuevo_libro