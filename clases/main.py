from libro import Libro
from socio import Socio
from disponible import Disponible
from prestado import Prestado
from extraviado import Extraviado
from datetime import datetime, timedelta
import sqlite3
from gestor import Gestor


conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

libro = Libro(1,11,11111,1355)
libro.insertar_libro(conexion)

# libros = Libro.obtener_libros()


print()



















#libro1 = Libro(123,"asd","desc",200)
#print(libro1.get_estado())


#a = datetime.now()
#nuevafecha = a + timedelta(days=90)
#print(nuevafecha)


#Ejemplo insertar un socio nuevo
'''
def insertar_socio(conexion, socio):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO socios (nro_socio, nombre, apellido) VALUES (?, ?, ?)",
               (socio.get_nro_socio(), socio.get_nombre(), socio.get_apellido()))

    conexion.commit()

def actualizar_socio(conexion, socio):
    cursor = conexion.cursor()
    cursor.execute("UPDATE socios SET nombre = ?, apellido = ? WHERE nro_socio = ?",
                    (socio.get_nombre(), socio.get_apellido(), socio.get_nro_socio()))
    conexion.commit()
    print(f"Información del socio con número {socio.get_nro_socio()} actualizada correctamente.")


def eliminar_socio(conexion, nro_socio):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM socios WHERE nro_socio = ?", (nro_socio,))
    conexion.commit()
    print(f"Socio con número {nro_socio} eliminado correctamente.")


conexion = sqlite3.connect("biblioteca.db")
'''

#nro = int(input("Ingrese numero socio: "))
#nombre = input("Ingrese nombre socio: ")
#apellido = input("Ingrese apellido socio: ")
#nro_eliminado = int(input("Ingrese el nro de socio que desea eliminar: "))

#socio_actualizado = Socio(60, "Diego", "Maradona")

#socio1 = Socio(nro, nombre, apellido)
#insertar_socio(conexion, socio1)
#eliminar_socio(conexion, nro_eliminado)
#actualizar_socio(conexion, socio_actualizado)

#conexion.close()