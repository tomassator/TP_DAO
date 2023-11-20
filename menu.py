import tkinter as tk
from gestor import Gestor
from pantallas.administrar_socios import SocioManager, InterfazAdministrarSocios
from pantallas.administrar_libros import LibroManager, InterfazAdministrarLibros
from pantallas.registrar_prestamos import PrestamoManager, InterfazRegistrarPrestamos
from pantallas.menu_reportes import ReportesManager,InterfazMenuReportes

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú")

        # Se obtienen las dimensiones de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Centrar la pantalla
        ancho_ventana = 400
        alto_ventana = 300
        x_ventana = (ancho_pantalla - ancho_ventana) // 2
        y_ventana = (alto_pantalla - alto_ventana) // 2

        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

        # Botones
        btn_socios = tk.Button(root, text="Administración de socios", command=self.administracion_socios)
        btn_libros = tk.Button(root, text="Administración de libros", command=self.administracion_libros)
        btn_prestamos = tk.Button(root, text="Registro de préstamos", command=self.registro_prestamos)
        btn_extraviados = tk.Button(root, text="Registro de libros extraviados", command=self.registro_libros_extraviados)
        btn_reportes = tk.Button(root, text="Generar reportes", command=self.generar_reportes)

        btn_socios.pack(pady=10)
        btn_libros.pack(pady=10)
        btn_prestamos.pack(pady=10)
        btn_extraviados.pack(pady=10)
        btn_reportes.pack(pady=10)

    def administracion_socios(self):
        root_socios = tk.Tk()
        gestor = Gestor()
        socio_manager = SocioManager(gestor)
        interfaz_socios = InterfazAdministrarSocios(root_socios, socio_manager)
        root_socios.mainloop()

    def administracion_libros(self):
        root_libros = tk.Tk()
        gestor = Gestor()
        libro_manager = LibroManager(gestor)
        interfaz_libros = InterfazAdministrarLibros(root_libros, libro_manager)
        root_libros.mainloop()
        
    def registro_prestamos(self):
        root_prestamo = tk.Tk()
        gestor = Gestor()
        prestamo_manager = PrestamoManager(gestor)
        interfaz_prestamos = InterfazRegistrarPrestamos(root_prestamo, prestamo_manager)
        root_prestamo.mainloop()
        
    def registro_libros_extraviados(self):
        pass

    def generar_reportes(self):
        root_reportes = tk.Tk()
        gestor = Gestor()
        reporte_manager = ReportesManager(gestor)
        interfaz_prestamos = InterfazMenuReportes(root_reportes, reporte_manager)
        root_reportes.mainloop()

if __name__ == "__main__":
    root_menu = tk.Tk()
    menu_principal = Menu(root_menu)
    root_menu.mainloop()