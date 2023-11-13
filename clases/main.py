from libro import Libro
from socio import Socio
from disponible import Disponible
from prestado import Prestado
from extraviado import Extraviado
from datetime import datetime, timedelta
import sqlite3

libro1 = Libro(123,"asd","desc",200)
print(libro1.get_estado())


a = datetime.now()
nuevafecha = a + timedelta(days=90)
print(nuevafecha)


#Ejemplo insertar un socio nuevo, seria una funcion agregar_socio() dentro de la clase Socio

conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()


nro = int(input("Ingrese numero socio: "))
nombre = input("Ingrese nombre socio: ")
apellido = input("Ingrese apellido socio: ")


socio = Socio(nro, nombre, apellido)

cursor.execute("INSERT INTO socios (nro_socio, nombre, apellido) VALUES (?, ?, ?)",
               (socio.get_nro_socio(), socio.get_nombre(), socio.get_apellido()))

conexion.commit()
cursor.close()
conexion.close()