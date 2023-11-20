import tkinter as tk
from tkinter import ttk, messagebox


class ReportesSociosLibroManager:
    def __init__(self, gestor):
        self.gestor = gestor

    def obtener_socios(self, titulo):
        return self.gestor.generar_reporte_nombre_socios_libro(titulo)

class InterfazReporteSociosLibro:
    def __init__(self, root, reporte_manager):
        self.root = root
        self.reporte_manager = reporte_manager
        self.reporte_seleccionado = None

        # Frame para los campos de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.titulo_label = tk.Label(self.input_frame, text="Titulo del libro:")
        self.titulo_label.grid(row=1, column=0, padx=10, pady=5)
        self.titulo_entry = tk.Entry(self.input_frame)
        self.titulo_entry.grid(row=1, column=1, padx=10, pady=5)

        self.buscar_button = tk.Button(self.input_frame, text="Buscar socios", command=self.cargar_socios_en_grilla)
        self.buscar_button.grid(row=3, column=1, columnspan=1, pady=10)

        # Frame para la grilla
        self.grid_frame = tk.Frame(root)
        self.grid_frame.grid(row=1, column=0, padx=10, pady=5)

        self.socios_treeview = ttk.Treeview(self.grid_frame, columns=("Número de socio", "Nombre", "Apellido"))
        self.socios_treeview.heading("Número de socio", text="Número de socio")
        self.socios_treeview.heading("Nombre", text="Nombre")
        self.socios_treeview.heading("Apellido", text="Apellido")
        self.socios_treeview.grid(row=0, column=0, padx=10, pady=5)


    def cargar_socios_en_grilla(self):
        # Limpiar la grilla
        for item in self.socios_treeview.get_children():
            self.socios_treeview.delete(item)

        # Cargar socios en la grilla
        for i, socio in enumerate(self.reporte_manager.obtener_socios(self.titulo_entry.get())):
            self.socios_treeview.insert("", i, values=(socio.nroSocio, socio.nombre, socio.apellido))

