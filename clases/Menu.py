import tkinter as tk
from gestor import Gestor
from tkinter import messagebox
from AdministrarLibros import LibroManager, InterfazAdministrarLibros
from AdministrarSocios import SocioManager, InterfazAdministrarSocios
from RegistrarPrestamos import PrestamoManager, InterfazRegistrarPrestamos

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")

        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Definir el tamaño de la ventana y centrarla
        ancho_ventana = 400
        alto_ventana = 300
        x_ventana = (ancho_pantalla - ancho_ventana) // 2
        y_ventana = (alto_pantalla - alto_ventana) // 2

        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

        # Crear botones para cada opción
        btn_socios = tk.Button(root, text="Administración de Socios", command=self.administracion_socios)
        btn_libros = tk.Button(root, text="Administración de Libros", command=self.administracion_libros)
        btn_prestamos = tk.Button(root, text="Registro de Préstamos", command=self.registro_prestamos)
        btn_extraviados = tk.Button(root, text="Registro de Libros Extraviados", command=self.registro_libros_extraviados)
        btn_reportes = tk.Button(root, text="Generar Reportes", command=self.generar_reportes)

        # Colocar los botones en la ventana con espacio entre ellos
        btn_socios.pack(pady=10)
        btn_libros.pack(pady=10)
        btn_prestamos.pack(pady=10)
        btn_extraviados.pack(pady=10)
        btn_reportes.pack(pady=10)

    def administracion_socios(self):
        root_socios = tk.Tk()
        gestor = Gestor()
        socio_manager = SocioManager(gestor)
        interfaz_socio = InterfazAdministrarSocios(root_socios, socio_manager)
        root_socios.mainloop()

    def administracion_libros(self):
        root_libros = tk.Tk()
        gestor = Gestor()
        libro_manager = LibroManager(gestor)
        interfaz_libros = InterfazAdministrarLibros(root_libros, libro_manager)
        root_libros.mainloop()

    def registro_prestamos(self):
        root_prestamos = tk.Tk()
        gestor = Gestor()
        prestamo_manager = PrestamoManager(gestor)
        interfaz_prestamo = InterfazRegistrarPrestamos(root_prestamos, prestamo_manager)
        root_prestamos.mainloop()

    def registro_libros_extraviados(self):
        # Lógica para la registración de libros extraviados
        print("Registración de libros extraviados")

    def generar_reportes(self):
        # Lógica para la generación de reportes
        print("Generar reportes")

if __name__ == "__main__":
    root_menu = tk.Tk()
    menu_principal = MenuPrincipal(root_menu)
    root_menu.mainloop()
