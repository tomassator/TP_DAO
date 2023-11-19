import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from tipo_mensajes import ID_MENSAJE_ERROR, ID_MENSAJE_EXITO

class PrestamoManager:
    def __init__(self, gestor):
        self.gestor = gestor
        self.fecha_actual = datetime.now()

    def consultar_socios(self):
        return self.gestor.obtener_socios()
    
    def consultar_libros(self):
        return self.gestor.obtener_libros_disponibles()
    
    def registrar_prestamo(self, idLibro, nroSocio, tiempoPrestamo, fechaPactada):
        tipoMensaje, mensaje = self.gestor.prestar_libro(idLibro, nroSocio)
        if tipoMensaje == ID_MENSAJE_EXITO:
            self.gestor.registrar_prestamo(idLibro, nroSocio, self.fecha_actual, tiempoPrestamo, fechaPactada)
        return tipoMensaje, mensaje
        
    
class InterfazRegistrarPrestamos:
    def __init__(self, root, prestamo_manager):
        self.root = root
        self.root.title("Registro de préstamos")

        self.prestamo_manager = prestamo_manager

        # Crear el frame de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=10)

        # Elementos en el input_frame
        self.socio_label = tk.Label(self.input_frame, text="Socio:")
        self.socio_label.grid(row=0, column=0, padx=10, pady=5)
        socios = prestamo_manager.consultar_socios()
        nombres_socios = [str(socio.nro_socio) + " - " + socio.nombre + " " + socio.apellido for socio in socios]
        self.socio_combobox = ttk.Combobox(self.input_frame, values=nombres_socios)
        self.socio_combobox.grid(row=0, column=1, padx=10, pady=5)

        self.dias_label = tk.Label(self.input_frame, text="Días para devolución:")
        self.dias_label.grid(row=1, column=0, padx=10, pady=5)
        self.dias_entry = tk.Entry(self.input_frame)
        self.dias_entry.grid(row=1, column=1, padx=10, pady=5)

        self.fecha_pactada_label = tk.Label(self.input_frame, text="Fecha pactada:")
        self.fecha_pactada_label.grid(row=2, column=0, padx=10, pady=5)
        self.fecha_pactada_entry = tk.Entry(self.input_frame, state=tk.DISABLED)  # Deshabilitar la edición
        self.fecha_pactada_entry.grid(row=2, column=1, padx=10, pady=5)

        self.prestamo_button = tk.Button(self.input_frame, text="Registrar préstamo", command=self.registrar_prestamo)
        self.prestamo_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Actualizacion dinamica de la fecha
        self.dias_entry.bind("<KeyRelease>", self.actualizar_fecha_pactada)

        #Frame para la grilla
        self.libros_treeview = ttk.Treeview(self.root, columns=("ID", "Codigo", "Titulo", "Descripcion"), show="headings")

        self.libros_treeview.heading("ID", text="ID")
        self.libros_treeview.heading("Codigo", text="Código")
        self.libros_treeview.heading("Titulo", text="Título")
        self.libros_treeview.heading("Descripcion", text="Descripción")

        # Mostrar la grilla en la interfaz
        self.libros_treeview.pack(padx=10, pady=10)

        self.actualizar_grilla_libros()
        
    def actualizar_grilla_libros(self):
        # Limpiar la grilla antes de actualizarla
        for item in self.libros_treeview.get_children():
            self.libros_treeview.delete(item)

        # Obtener los datos de los libros y agregarlos a la grilla
        libros = self.prestamo_manager.consultar_libros()
        for libro in libros:
            self.libros_treeview.insert("", "end", values=(libro.id, libro.codigo, libro.titulo, libro.descripcion))

    def registrar_prestamo(self):
        item = self.libros_treeview.selection()
        if item:
            libro_seleccionado = self.libros_treeview.item(item[0], "values")

            idLibro = int(libro_seleccionado[0])
            nroSocio = int(self.socio_combobox.get().split("-")[0].strip())
            tiempoPrestamo = int(self.dias_entry.get())
            fechaPactada =  self.prestamo_manager.fecha_actual + timedelta(days=tiempoPrestamo)

            if nroSocio and fechaPactada:
                tipoMensaje, mensaje = self.prestamo_manager.registrar_prestamo(idLibro, nroSocio, tiempoPrestamo, fechaPactada)
                if tipoMensaje == ID_MENSAJE_EXITO: 
                    messagebox.showinfo("Éxito", mensaje)
                else:
                    messagebox.showerror("Error", mensaje)

                self.limpiar_campos()
                self.actualizar_grilla_libros()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
        else:
            messagebox.showerror("Error", "Por favor, seleccione un libro")

    def actualizar_fecha_pactada(self, event):
        # Obtener los días ingresados
        dias = self.dias_entry.get() or 0

        # Se calcula la nueva fecha pactada sumando los días
        dias_a_agregar = int(dias)
        fecha_pactada = self.prestamo_manager.fecha_actual + timedelta(days=dias_a_agregar)

        # Actualizar la fecha pactada en el campo correspondiente
        self.fecha_pactada_entry.config(state=tk.NORMAL) 
        self.fecha_pactada_entry.delete(0, tk.END)
        self.fecha_pactada_entry.insert(0, fecha_pactada.strftime("%d/%m/%Y"))
        self.fecha_pactada_entry.config(state=tk.DISABLED)

    def limpiar_campos(self):
        self.socio_combobox.set("")
        self.dias_entry.delete(0, tk.END)
        self.fecha_pactada_entry.config(state=tk.NORMAL)
        self.fecha_pactada_entry.delete(0, tk.END)
        self.fecha_pactada_entry.config(state=tk.DISABLED)