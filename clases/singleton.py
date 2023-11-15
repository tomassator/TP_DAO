import sqlite3

class ConexionSingleton:
    instancia = None

    def __new__(cls, database_path):
        if not cls.instancia:
            cls.instancia = super(ConexionSingleton, cls).__new__(cls)
            cls.instancia.conexion = sqlite3.connect(database_path)
        return cls.instancia

    def obtener_cursor(self):
        return self.conexion.cursor()
    
    def conexion_commit(self):
        self.conexion.commit()
        
    def cerrar_conexion(self):
        self.conexion.close()


    

