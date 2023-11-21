import sqlite3

conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

# Tabla Libros
cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo INTEGER,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                precioReposicion REAL NOT NULL,
                id_estado INTEGER,
                FOREIGN KEY (id_estado) REFERENCES estado (id))
               ''')


#Tabla Socios
cursor.execute('''
                CREATE TABLE IF NOT EXISTS socios (
                nro_socio INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL)
            ''')


#Tabla Prestamo
cursor.execute('''
                CREATE TABLE IF NOT EXISTS prestamo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tiempoPrestamo INTEGER NOT NULL,
                fecha_prestamo DATETIME,
                fecha_pactada_devolucion DATETIME,
                fecha_devolucion DATETIME,
                id_socio INTEGER NOT NULL,
                id_libro INTEGER NOT NULL,
                FOREIGN KEY (id_socio) REFERENCES socios (nro_socio),
                FOREIGN KEY (id_libro) REFERENCES libros (id))
            ''')


#Tabla Estado 
cursor.execute('''
                CREATE TABLE IF NOT EXISTS estado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL)
            ''')


conexion.commit()
cursor.close()
conexion.close()

