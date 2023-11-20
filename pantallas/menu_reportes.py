import tkinter as tk
from tkinter import ttk, messagebox
from pantallas.reporte_socio_libro import ReportesSociosLibroManager, InterfazReporteSociosLibro
from pantallas.reporte_prestamos_demorados import ReportesPrestamoDemoradosManager, InterfazPrestamoDemorados
from pantallas.reporte_prestamo_socio import ReportesPrestamoSocioManager, InterfazPrestamoSocio

class ReportesManager:
    def __init__(self, gestor):
        self.gestor = gestor

    def generarReportePrecioReposicion(self):
        return self.gestor.generar_reporte_precio_extraviados()

    def generarReporteLibrosEstado(self):
        return self.gestor.generar_reporte_cant_librosxestado()

    def get_gestor(self):
        return self.gestor

class InterfazMenuReportes:
    def __init__(self, root, reporte_manager):
        self.root = root
        self.reporte_manager = reporte_manager
        self.reporte_seleccionado = None

        self.root.title("Reportes")

        # Frame para los campos de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.reporte_precio_extraviados_button = tk.Button(self.input_frame, text="Generar reporte sumatoria de precios de reposicion de libros extraviados", width=60, command=self.mostrarPrecioReposicion)
        self.reporte_precio_extraviados_button.grid(row=0, column=0, columnspan=1, pady=10)

        self.librosxestado_button = tk.Button(self.input_frame, text="Cantidad de libros por estado", width=60, command=self.mostrarLibrosXEstado)
        self.librosxestado_button.grid(row=1, column=0, columnspan=1, pady=10)

        self.sociosxlibro_button = tk.Button(self.input_frame, text="Socios que solicitaron determinado libro", width=60, command=self.ventana_reporte_socios_libro)
        self.sociosxlibro_button.grid(row=2, column=0, columnspan=1, pady=10)

        self.prestamosxsocio_button = tk.Button(self.input_frame, text="Prestamos para un determinado socio", width=60, command = self.ventana_reporte_prestamos_socio)
        self.prestamosxsocio_button.grid(row=3, column=0, columnspan=1, pady=10)

        self.prestamosdemorados_button = tk.Button(self.input_frame, text="Prestamos demorados", width=60, command= self.ventana_prestamos_demorados)
        self.prestamosdemorados_button.grid(row=4, column=0, columnspan=1, pady=10)

    def mostrarPrecioReposicion(self):
        resultado = self.reporte_manager.generarReportePrecioReposicion()
        mensaje = f"La sumatoria de precios de reposicion para los libros extraviados es: {resultado}"
        if resultado != None:
            messagebox.showinfo("Reporte", mensaje)
        else:
            messagebox.showinfo("Reporte" , "No hay libros extraviados en este momento")



    def mostrarLibrosXEstado(self):
        resultado = self.reporte_manager.generarReporteLibrosEstado()
        mensaje = ""
        for res in resultado:
            mensaje += f"La cantidad de libros en estado {res[0]} son: {res[1]} \n"

        messagebox.showinfo("Reporte", mensaje)


    def ventana_reporte_socios_libro(self):
        root_reporte_socio_libro = tk.Tk()
        reporte_manager = ReportesSociosLibroManager(self.reporte_manager.get_gestor())
        interfaz_prestamos = InterfazReporteSociosLibro(root_reporte_socio_libro, reporte_manager)
        root_reporte_socio_libro.mainloop()


    def ventana_reporte_prestamos_socio(self):
        root_reporte_prestamo_socio = tk.Tk()
        reporte_manager = ReportesPrestamoSocioManager(self.reporte_manager.get_gestor())
        interfaz_prestamos = InterfazPrestamoSocio(root_reporte_prestamo_socio, reporte_manager)
        root_reporte_prestamo_socio.mainloop()


    def ventana_prestamos_demorados(self):
        root_reporte_prestamos_demorados = tk.Tk()
        reporte_manager = ReportesPrestamoDemoradosManager(self.reporte_manager.get_gestor())
        interfaz_prestamos = InterfazPrestamoDemorados(root_reporte_prestamos_demorados, reporte_manager)
        root_reporte_prestamos_demorados.mainloop()