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

#Insert libros
#cursor.execute("INSERT INTO libros (id, codigo, titulo, descripcion, precioReposicion, id_estado) VALUES (?, ?, ?, ?, ?, ?)",
#               (2, 1233, "Libro 2", "Descripción del Libro 1", 19.99, 1))


#Tabla Socios
cursor.execute('''
                CREATE TABLE IF NOT EXISTS socios (
                nro_socio INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL)
            ''')

#Insert socios
#cursor.execute("INSERT INTO socios (nro_socio, nombre, apellido) VALUES (?, ?, ?)",
#               (1, "Juan", "Pérez"))


#Tabla Prestamo
cursor.execute('''
                CREATE TABLE IF NOT EXISTS prestamo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tiempoPrestamo INTEGER NOT NULL,
                fecha_prestamo DATETIME,
                fecha_pactada_devolucion DATETIME,
                fecha_devolucion DATETIME,
                id_socio INTEGER NOT NULL,
                FOREIGN KEY (id_socio) REFERENCES socios (nro_socio))
            ''')

#Insert Prestamo
#cursor.execute("INSERT INTO prestamo (id, tiempoPrestamo, fecha_prestamo, fecha_pactada_devolucion, fecha_devolucion, id_socio) VALUES (?, ?, ?, ?, ?, ?, ?)", 
#               (14, "2023-11-01 00:00:00", "2023-12-01 00:00:00", 1))


#Tabla Detalle Prestamo
cursor.execute('''
                CREATE TABLE IF NOT EXISTS detalle_prestamo (
                id_detalle_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
                id_prestamo INTEGER,
                id_libro INTEGER,
                FOREIGN KEY (id_prestamo) REFERENCES prestamo (id),
                FOREIGN KEY (id_libro) REFERENCES libros (id))
            ''')

#Insert DetallePrestamo
#cursor.execute("INSERT INTO detalle_prestamo (id_detalle_prestamo, id_prestamo, id_libro) VALUES (?, ?, ?)",
#              (1, 1, 1))  


#Tabla Estado 
cursor.execute('''
                CREATE TABLE IF NOT EXISTS estado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL)
            ''')

#Insert Estado
#cursor.execute("INSERT INTO estado (id, nombre) VALUES (?,?)", (1,"Disponible",))

conexion.commit()
cursor.close()
conexion.close()

