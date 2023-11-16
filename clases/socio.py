class Socio:
    def __init__(self, nro_socio, nombre, apellido):
        self.nro_socio = nro_socio
        self.nombre = nombre
        self.apellido = apellido


    #ABM
    def insertar_socio(self, conexion):
        cursor = conexion.obtener_cursor()
        cursor.execute("INSERT INTO socios (nro_socio, nombre, apellido) VALUES (?, ?, ?)",
                       (self.get_nro_socio(), self.get_nombre(), self.get_apellido()))
        conexion.conexion_commit()
        conexion.cerrar_cursor()

    def actualizar_socio(self,conexion):
        cursor = conexion.obtener_cursor()
        cursor.execute("UPDATE socios SET nombre = ?, apellido = ? WHERE nro_socio = ?",
                       (self.get_nombre(), self.get_apellido(), self.get_nro_socio()))
        conexion.conexion_commit()
        conexion.cerrar_cursor()
        print(f"Información del socio con número {self.get_nro_socio()} actualizada correctamente.")

    def eliminar_socio(self,conexion):
        cursor = conexion.obtener_cursor()
        cursor.execute("DELETE FROM socios WHERE nro_socio = ?", (self.get_nro_socio()))
        conexion.conexion_commit()
        conexion.cerrar_cursor()
        print(f"Socio con número {self.get_nro_socio()} eliminado correctamente.")


    # Getters y Setters
    def get_nro_socio(self):
        return self.nro_socio
    
    def set_nro_socio(self, nuevo_nro):
        self.nro_socio = nuevo_nro
        
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido