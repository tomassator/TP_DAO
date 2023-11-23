from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

class ReportesPrestamoDemoradosManager:
    def __init__(self, gestor):
        self.gestor = gestor

    def obtener_prestamos(self):
        return self.gestor.generar_reporte_prestamos_demorados()

class InterfazPrestamoDemorados:
    def __init__(self, root, reporte_manager):
        self.root = root
        self.reporte_manager = reporte_manager
        self.reporte_seleccionado = None

        # Frame para la grilla
        self.grid_frame = tk.Frame(root)
        self.grid_frame.grid(row=1, column=0, padx=10, pady=5)

        self.prestamos_treeview = ttk.Treeview(self.grid_frame, columns=("ID", "Tiempo prestamo", "Fecha prestamo", "Fecha pactada devolucion"))
        self.prestamos_treeview.heading("ID", text="ID")
        self.prestamos_treeview.heading("Tiempo prestamo", text="Tiempo prestamo")
        self.prestamos_treeview.heading("Fecha prestamo", text="Fecha prestamo")
        self.prestamos_treeview.heading("Fecha pactada devolucion", text="Fecha pactada devolucion")
        self.prestamos_treeview.grid(row=0, column=0, padx=10, pady=5)

        self.cargar_prestamos_en_grilla()

    def cargar_prestamos_en_grilla(self):
        # Limpiar la grilla
        for item in self.prestamos_treeview.get_children():
            self.prestamos_treeview.delete(item)

        # Cargar socios en la grilla
        for i, prestamo in enumerate(self.reporte_manager.obtener_prestamos()):
            self.prestamos_treeview.insert("", i, values=(prestamo.id, prestamo.tiempoPrestamo, prestamo.fechaPrestamo.strftime("%d/%m/%Y"), datetime.strptime(prestamo.fechaPactadaDevolucion, "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%Y")))
