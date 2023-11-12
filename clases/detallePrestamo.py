

class DetallePrestamo:
    def __init__(self, libro):
        self.libro = libro

    # Getters y Setters
    def get_libro(self):
        return self.libro

    def set_libro(self, nuevo_libro):
        self.libro = nuevo_libro