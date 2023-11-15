import sqlite3
from libro import Libro



class Gestor:
    def __init__(self,):
        self.conexion = sqlite3.connect("biblioteca.db")

    def agregar_libro(self, libro):
        libro.insertar_libro(self.conexion)

        
    


