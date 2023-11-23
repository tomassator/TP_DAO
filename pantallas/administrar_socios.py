import tkinter as tk
from tkinter import ttk, messagebox
from tipo_mensajes import ID_MENSAJE_EXITO

class SocioManager:
    def __init__(self, gestor):
        self.gestor = gestor

    def agregar_socio(self, nombre, apellido):
        self.gestor.agregar_socio(nombre, apellido)

    def eliminar_socio(self, nro_socio):
        return self.gestor.eliminar_socio(nro_socio)
        
    def actualizar_socio(self, nro_socio, nombre, apellido):
        self.gestor.actualizar_socio(nro_socio, nombre, apellido)
    
    def consultar_socios(self):
        return self.gestor.obtener_socios()
    
class InterfazAdministrarSocios:
    def __init__(self, root, socio_manager):
        self.root = root
        self.socio_manager = socio_manager
        self.socio_seleccionado = None 

        self.root.title("Socios")

        # Frame para los campos de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.nombre_label = tk.Label(self.input_frame, text="Nombre:")
        self.nombre_label.grid(row=1, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(self.input_frame)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        self.apellido_label = tk.Label(self.input_frame, text="Apellido:")
        self.apellido_label.grid(row=2, column=0, padx=10, pady=5)
        self.apellido_entry = tk.Entry(self.input_frame)
        self.apellido_entry.grid(row=2, column=1, padx=10, pady=5)

        self.agregar_button = tk.Button(self.input_frame, text="Agregar socio", command=self.agregar_socio)
        self.agregar_button.grid(row=3, column=0, columnspan=1, pady=10)

        self.eliminar_button = tk.Button(self.input_frame, text="Eliminar socio", command=self.eliminar_socio)
        self.eliminar_button.grid(row=3, column=1, columnspan=1, pady=10)

        self.actualizar_button = tk.Button(self.input_frame, text="Actualizar socio", command=self.actualizar_socio)
        self.actualizar_button.grid(row=3, column=2, columnspan=1, pady=10)

        # Frame para la grilla
        self.grid_frame = tk.Frame(root)
        self.grid_frame.grid(row=1, column=0, padx=10, pady=5)

    
        self.socios_treeview = ttk.Treeview(self.grid_frame, columns=("Número de socio", "Nombre", "Apellido"))
        self.socios_treeview.heading("Número de socio", text="Número de socio")
        self.socios_treeview.heading("Nombre", text="Nombre")
        self.socios_treeview.heading("Apellido", text="Apellido")
        self.socios_treeview.bind("<ButtonRelease-1>", self.cargar_datos_seleccionados)
        self.socios_treeview.grid(row=0, column=0, padx=10, pady=5)

        self.cargar_socios_en_grilla()

    def agregar_socio(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()

        if nombre and apellido:
            self.socio_manager.agregar_socio(nombre, apellido)
            self.cargar_socios_en_grilla()
            messagebox.showinfo("Éxito", "Socio agregado correctamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_socio(self):
        if self.socio_seleccionado:
            nro_socio = self.socio_seleccionado[0]
            tipo_mensaje, mensaje = self.socio_manager.eliminar_socio(nro_socio)
            if tipo_mensaje == ID_MENSAJE_EXITO:
                self.cargar_socios_en_grilla()
                self.limpiar_campos()
                return messagebox.showinfo("Éxito", mensaje)
            else:
                return messagebox.showerror("Error", mensaje)
            
        else:
            messagebox.showerror("Error", "No se ha seleccionado un socio.")

    def actualizar_socio(self):
        if self.socio_seleccionado:
            nro_socio = self.socio_seleccionado[0]
            nombre = self.nombre_entry.get()
            apellido = self.apellido_entry.get()

            if nombre and apellido:
                self.socio_manager.actualizar_socio(nro_socio, nombre, apellido)
                self.cargar_socios_en_grilla()
                messagebox.showinfo("Éxito", "Socio actualizado correctamente.")
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado un socio.")

    def cargar_socios_en_grilla(self):
        # Limpiar la grilla
        for item in self.socios_treeview.get_children():
            self.socios_treeview.delete(item)

        # Cargar socios en la grilla
        for i, socio in enumerate(self.socio_manager.consultar_socios()):
            self.socios_treeview.insert("", i, values=(socio.nroSocio, socio.nombre, socio.apellido))

    def cargar_datos_seleccionados(self, event):
        item = self.socios_treeview.selection()
        if item:
            socio_seleccionado = self.socios_treeview.item(item[0], "values")
            if socio_seleccionado:
                self.socio_seleccionado = socio_seleccionado
                self.nombre_entry.delete(0, tk.END)
                self.apellido_entry.delete(0, tk.END)

                # Ajustar para usar socio_seleccionado[0]
                self.nombre_entry.insert(0, socio_seleccionado[1])
                self.apellido_entry.insert(0, socio_seleccionado[2])

    def limpiar_campos(self):
        self.socio_seleccionado = None
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)

    

