import tkinter as tk
from tkinter import ttk, messagebox
from gestor import Gestor
from socio import Socio

class SocioManager:
    def __init__(self, gestor=Gestor()):
        self.gestor = gestor

    def agregar_socio(self, nro_socio, nombre, apellido):
        self.gestor.agregar_socio(nro_socio, nombre, apellido)

    def buscar_socio(self, nro_socio):
        for socio in self.gestor.obtener_socios():
            if socio.nro_socio == nro_socio:
                return socio
        return None

    def eliminar_socio(self, nro_socio):
        self.gestor.eliminar_socio(nro_socio)
        return True
    
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

        self.nro_socio_label = tk.Label(self.input_frame, text="Número de Socio:")
        self.nro_socio_label.grid(row=0, column=0, padx=10, pady=5)
        self.nro_socio_entry = tk.Entry(self.input_frame, state=tk.NORMAL) 
        self.nro_socio_entry.grid(row=0, column=1, padx=10, pady=5)

        self.nombre_label = tk.Label(self.input_frame, text="Nombre:")
        self.nombre_label.grid(row=1, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(self.input_frame)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        self.apellido_label = tk.Label(self.input_frame, text="Apellido:")
        self.apellido_label.grid(row=2, column=0, padx=10, pady=5)
        self.apellido_entry = tk.Entry(self.input_frame)
        self.apellido_entry.grid(row=2, column=1, padx=10, pady=5)

        self.agregar_button = tk.Button(self.input_frame, text="Agregar Socio", command=self.agregar_socio)
        self.agregar_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.eliminar_button = tk.Button(self.input_frame, text="Eliminar Socio", command=self.eliminar_socio)
        self.eliminar_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.actualizar_button = tk.Button(self.input_frame, text="Actualizar Socio", command=self.actualizar_socio)
        self.actualizar_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Frame para la grilla
        self.grid_frame = tk.Frame(root)
        self.grid_frame.grid(row=1, column=0, padx=10, pady=5)

    
        self.socios_treeview = ttk.Treeview(self.grid_frame, columns=("Número de Socio", "Nombre", "Apellido"))
        self.socios_treeview.heading("Número de Socio", text="Número de Socio")
        self.socios_treeview.heading("Nombre", text="Nombre")
        self.socios_treeview.heading("Apellido", text="Apellido")
        self.socios_treeview.bind("<ButtonRelease-1>", self.cargar_datos_seleccionados)
        self.socios_treeview.grid(row=0, column=0, padx=10, pady=5)

        self.cargar_socios_en_grilla()

    def agregar_socio(self):
        nro_socio = self.nro_socio_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()

        if nro_socio and nombre and apellido:
            self.socio_manager.agregar_socio(nro_socio, nombre, apellido)
            self.cargar_socios_en_grilla()
            messagebox.showinfo("Éxito", "Socio agregado correctamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_socio(self):
        if self.socio_seleccionado:
            nro_socio = self.socio_seleccionado[0]
            if self.socio_manager.eliminar_socio(nro_socio):
                self.cargar_socios_en_grilla()
                messagebox.showinfo("Éxito", "Socio eliminado correctamente.")
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el socio.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado un socio.")

    def actualizar_socio(self):
        if self.socio_seleccionado:
            nro_socio = self.socio_seleccionado[0]
            nombre = self.nombre_entry.get()
            apellido = self.apellido_entry.get()

            if nro_socio and nombre and apellido:
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
            self.socios_treeview.insert("", i, values=(socio.nro_socio, socio.nombre, socio.apellido))

    def cargar_datos_seleccionados(self, event):
        item = self.socios_treeview.selection()
        if item:
            socio_seleccionado = self.socios_treeview.item(item[0], "values")
            if socio_seleccionado:
                self.socio_seleccionado = socio_seleccionado
                self.nro_socio_entry.delete(0, tk.END)
                self.nombre_entry.delete(0, tk.END)
                self.apellido_entry.delete(0, tk.END)

                # Ajustar para usar socio_seleccionado[0]
                self.nro_socio_entry.insert(0, socio_seleccionado[0])
                self.nombre_entry.insert(0, socio_seleccionado[1])
                self.apellido_entry.insert(0, socio_seleccionado[2])

                # Deshabilitar el campo nro_socio_entry
                self.nro_socio_entry.config(state=tk.DISABLED)

    def limpiar_campos(self):
        self.socio_seleccionado = None
        self.nro_socio_entry.config(state=tk.NORMAL)  # Habilitar el campo nro_socio_entry
        self.nro_socio_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    socio_manager = SocioManager()
    interfaz = InterfazAdministrarSocios(root, socio_manager)
    root.mainloop()
