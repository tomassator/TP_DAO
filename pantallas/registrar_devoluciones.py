import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from tipo_mensajes import ID_MENSAJE_ERROR, ID_MENSAJE_EXITO

class DevolucionManager:
    def __init__(self, gestor):
        self.gestor = gestor
        self.fecha_actual = datetime.now()

    def obtener_prestamos_activos(self):
        return self.gestor.obtener_prestamos_activos()

    def registrar_devolucion(self, idPrestamo):
        tipoMensaje, mensaje = self.gestor.devolver_libro(idPrestamo)
        return tipoMensaje, mensaje

class InterfazRegistrarDevoluciones:
    def __init__(self, root, devolucion_manager):
        self.root = root
        self.root.title("Registro de devoluciones")

        self.devolucion_manager = devolucion_manager

        # Crear el frame de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=10)

        # Elementos en el input_frame
        self.fecha_devolucion_label = tk.Label(self.input_frame, text="Fecha de devolución:")
        self.fecha_devolucion_label.grid(row=0, column=0, padx=10, pady=5)
        self.fecha_devolucion_entry = tk.Entry(self.input_frame)
        self.fecha_devolucion_entry.grid(row=0, column=1, padx=10, pady=5)

        # Obtener la fecha actual
        fecha_actual = devolucion_manager.fecha_actual.strftime("%d/%m/%Y")
        self.fecha_devolucion_entry.insert(0, fecha_actual)
        self.fecha_devolucion_entry.config(state=tk.DISABLED)

        self.registrar_devolucion_button = tk.Button(self.input_frame, text="Registrar devolución", command=self.registrar_devolucion)
        self.registrar_devolucion_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Frame para la grilla
        self.devoluciones_treeview = ttk.Treeview(self.root, columns=("ID", "Titulo libro", "Nombre del socio", "Fecha pactada de devolución"), show="headings")

        self.devoluciones_treeview.heading("ID", text="ID")
        self.devoluciones_treeview.heading("Titulo libro", text="Título libro")
        self.devoluciones_treeview.heading("Nombre del socio", text="Nombre del socio")
        self.devoluciones_treeview.heading("Fecha pactada de devolución", text="Fecha pactada de devolución")

        # Mostrar la grilla en la interfaz
        self.devoluciones_treeview.pack(padx=10, pady=10)

        self.actualizar_grilla_prestamos()

    def actualizar_grilla_prestamos(self):
        # Limpiar la grilla antes de actualizarla
        for item in self.devoluciones_treeview.get_children():
            self.devoluciones_treeview.delete(item)

        # Obtener los datos de las devoluciones y agregarlos a la grilla
        prestamos = self.devolucion_manager.obtener_prestamos_activos()
        for prestamo in prestamos:
            self.devoluciones_treeview.insert("", "end", values=(prestamo.id, prestamo.libro.titulo, f'{prestamo.socio.nombre} {prestamo.socio.apellido}' , datetime.strptime(prestamo.fechaPactadaDevolucion, "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%Y")))

    def registrar_devolucion(self):
        item = self.devoluciones_treeview.selection()
        if item:
            prestamo_seleccionado = self.devoluciones_treeview.item(item[0], "values")
            idPrestamo = prestamo_seleccionado[0]

            if idPrestamo:
                tipoMensaje, mensaje = self.devolucion_manager.registrar_devolucion(idPrestamo)
                if tipoMensaje == ID_MENSAJE_EXITO:
                    messagebox.showinfo("Éxito", mensaje)
                else:
                    messagebox.showerror("Error", mensaje)

                self.actualizar_grilla_prestamos()
            else:
                messagebox.showerror("Error", "Por favor, seleccione una devolución")
        else:
            messagebox.showerror("Error", "Por favor, seleccione una devolución")