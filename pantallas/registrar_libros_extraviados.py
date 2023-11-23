import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from tipo_mensajes import ID_MENSAJE_EXITO

class ExtravioManager:
    def __init__(self, gestor):
        self.gestor = gestor
        self.fecha_actual = datetime.now()

    def obtener_prestamos_demorados(self):
        return self.gestor.obtener_prestamos_demorados()

    def registrar_extravio(self, libros):
        return self.gestor.registrar_extravio(libros)
        

class InterfazRegistrarExtravios:
    def __init__(self, root, extravio_manager):
        self.root = root
        self.root.title("Registro de extravíos")

        self.extravio_manager = extravio_manager

        # Crear el frame de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=10)

        self.registrar_extravio_button = tk.Button(self.input_frame, text="Registrar extravíos", command=self.registrar_extravio)
        self.registrar_extravio_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Frame para la grilla
        self.extravios_treeview = ttk.Treeview(self.root, columns=("ID", "Título libro", "Fecha pactada de devolucion"), show="headings")

        self.extravios_treeview.heading("ID", text="ID")
        self.extravios_treeview.heading("Título libro", text="Título libro")
        self.extravios_treeview.heading("Fecha pactada de devolucion", text="Fecha pactada de devolucion")

        # Mostrar la grilla en la interfaz
        self.extravios_treeview.pack(padx=10, pady=10)

        self.actualizar_grilla_libros()

    def actualizar_grilla_libros(self):
        # Limpiar la grilla antes de actualizarla
        for item in self.extravios_treeview.get_children():
            self.extravios_treeview.delete(item)

        # Obtener los datos de los libros disponibles y agregarlos a la grilla
        prestamos = self.extravio_manager.obtener_prestamos_demorados()
        for prestamo in prestamos:
            self.extravios_treeview.insert("", "end", values=(prestamo.libro.id, prestamo.libro.titulo, datetime.strptime(prestamo.fechaPactadaDevolucion, "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%Y")))

    def registrar_extravio(self):
        libros = []
    
        for i in self.extravios_treeview.get_children():
            id = self.extravios_treeview.item(i, "values")[0]
            libros.append(id)

        tipoMensaje, mensaje = self.extravio_manager.registrar_extravio(libros)

        if tipoMensaje == ID_MENSAJE_EXITO: 
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_grilla_libros()
        else:
            messagebox.showerror("Error", mensaje)

