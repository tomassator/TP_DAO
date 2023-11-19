import tkinter as tk
from tkinter import ttk, messagebox

class LibroManager:
    def __init__(self, gestor):
        self.gestor = gestor

    def agregar_libro(self, codigo, titulo, descripcion, precioReposicion):
        self.gestor.agregar_libro(codigo, titulo, descripcion, precioReposicion)

    def eliminar_libro(self, id):
        self.gestor.eliminar_libro(id)
    
    def actualizar_libro(self, id, codigo, titulo, descripcion, precioReposicion):
        self.gestor.actualizar_libro(id, codigo, titulo, descripcion, precioReposicion)
    
    def consultar_libros(self):
        return self.gestor.obtener_libros()
    
class InterfazAdministrarLibros:
    def __init__(self, root, libro_manager):
        self.root = root
        self.libro_manager = libro_manager

        self.root.title("Libros")

        # Frame para los campos de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.codigo_label = tk.Label(self.input_frame, text="Código (ISBN):")
        self.codigo_label.grid(row=0, column=0, padx=10, pady=5)
        self.codigo_entry = tk.Entry(self.input_frame)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=5)

        self.titulo_label = tk.Label(self.input_frame, text="Título:")
        self.titulo_label.grid(row=1, column=0, padx=10, pady=5)
        self.titulo_entry = tk.Entry(self.input_frame)
        self.titulo_entry.grid(row=1, column=1, padx=10, pady=5)

        self.descripcion_label = tk.Label(self.input_frame, text="Descripción:")
        self.descripcion_label.grid(row=2, column=0, padx=10, pady=5)
        self.descripcion_entry = tk.Entry(self.input_frame)
        self.descripcion_entry.grid(row=2, column=1, padx=10, pady=5)

        self.precio_reposicion_label = tk.Label(self.input_frame, text="Precio reposición:")
        self.precio_reposicion_label.grid(row=3, column=0, padx=10, pady=5)
        self.precio_reposicion_entry = tk.Entry(self.input_frame)
        self.precio_reposicion_entry.grid(row=3, column=1, padx=10, pady=5)

        self.agregar_button = tk.Button(self.input_frame, text="Agregar libro", command=self.agregar_libro)
        self.agregar_button.grid(row=4, column=0, columnspan=1, pady=10)

        self.eliminar_button = tk.Button(self.input_frame, text="Eliminar libro", command=self.eliminar_libro)
        self.eliminar_button.grid(row=4, column=1, columnspan=1, pady=10)

        self.actualizar_button = tk.Button(self.input_frame, text="Actualizar libro", command=self.actualizar_libro)
        self.actualizar_button.grid(row=4, column=2, columnspan=1, pady=10)

        # Frame para la grilla
        self.grid_frame = tk.Frame(root)
        self.grid_frame.grid(row=1, column=0, padx=10, pady=5)

        self.libros_treeview = ttk.Treeview(self.grid_frame, columns=("ID","Código", "Título", "Descripción", "Precio reposición", "Estado"))
        self.libros_treeview.heading("ID", text="ID")
        self.libros_treeview.heading("Código", text="Código")
        self.libros_treeview.heading("Título", text="Título")
        self.libros_treeview.heading("Descripción", text="Descripción")
        self.libros_treeview.heading("Precio reposición", text="Precio reposición")
        self.libros_treeview.heading("Estado", text="Estado")
        self.libros_treeview.bind("<ButtonRelease-1>", self.cargar_datos_seleccionados)
        self.libros_treeview.grid(row=0, column=0, padx=10, pady=5)

        self.cargar_libros_en_grilla()

    def agregar_libro(self):
        codigo = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        descripcion = self.descripcion_entry.get()
        precioReposicion = self.precio_reposicion_entry.get()

        if codigo and titulo and descripcion and precioReposicion:
            self.libro_manager.agregar_libro(codigo, titulo, descripcion, precioReposicion)
            self.cargar_libros_en_grilla()
            messagebox.showinfo("Éxito", "Libro agregado correctamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_libro(self):
        item = self.libros_treeview.selection()
        if item:
            libro_seleccionado = self.libros_treeview.item(item[0], "values")
            if libro_seleccionado:
                id = libro_seleccionado[0]
                self.libro_manager.eliminar_libro(id)

                self.cargar_libros_en_grilla()
                messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", "No se ha seleccionado un libro.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado un libro.")

    def actualizar_libro(self):
        item = self.libros_treeview.selection()
        if item:
            libro_seleccionado = self.libros_treeview.item(item[0], "values")
            if libro_seleccionado:
                id = libro_seleccionado[0]
                codigo = self.codigo_entry.get()
                titulo = self.titulo_entry.get()
                descripcion = self.descripcion_entry.get()
                precioReposicion = self.precio_reposicion_entry.get()

                if codigo and titulo and descripcion and precioReposicion:

                    self.libro_manager.actualizar_libro(id, codigo, titulo, descripcion, precioReposicion)

                    self.cargar_libros_en_grilla()
                    messagebox.showinfo("Éxito", "Libro actualizado correctamente.")

                    self.limpiar_campos()
                else:
                    messagebox.showerror("Error", "Por favor, complete todos los campos.")
            else:
                messagebox.showerror("Error", "No se ha seleccionado un libro.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado un libro.")


    def cargar_libros_en_grilla(self):
        # Limpiar la grilla
        for item in self.libros_treeview.get_children():
            self.libros_treeview.delete(item)

        # Cargar libros en la grilla
        for i, libro in enumerate(self.libro_manager.consultar_libros()):
            self.libros_treeview.insert("", i, values=(libro.id, libro.codigo, libro.titulo, libro.descripcion, libro.precioReposicion, libro.estado.nombre))

    def cargar_datos_seleccionados(self, event):
        item = self.libros_treeview.selection()
        if item:
            libro_seleccionado = self.libros_treeview.item(item[0], "values")
            if libro_seleccionado:
                self.codigo_entry.delete(0, tk.END)
                self.titulo_entry.delete(0, tk.END)
                self.descripcion_entry.delete(0, tk.END)
                self.precio_reposicion_entry.delete(0, tk.END)

                self.codigo_entry.insert(0, libro_seleccionado[1])
                self.titulo_entry.insert(0, libro_seleccionado[2])
                self.descripcion_entry.insert(0, libro_seleccionado[3])
                self.precio_reposicion_entry.insert(0, libro_seleccionado[4])

    def limpiar_campos(self):
        self.codigo_entry.delete(0, tk.END)
        self.titulo_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.precio_reposicion_entry.delete(0, tk.END)
