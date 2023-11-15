import sqlite3



class Gestor:
    def __init__(self):
        self.conexion = None



    conexion = sqlite3.connect("biblioteca.db")

