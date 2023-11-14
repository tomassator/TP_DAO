import tkinter as tk
from tkinter import ttk, messagebox

class Libro:
    def __init__(self, codigo, titulo, descripcion, precio_reposicion):
        self.codigo = codigo
        self.titulo = titulo
        self.descripcion = descripcion
        self.precio_reposicion = precio_reposicion

class LibroManager:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        existing_libro = self.buscar_libro(libro.codigo)
        if existing_libro:
            # Modificar el libro existente
            existing_libro.titulo = libro.titulo
            existing_libro.descripcion = libro.descripcion
            existing_libro.precio_reposicion = libro.precio_reposicion
        else:
            # Agregar un nuevo libro
            self.libros.append(libro)

    def buscar_libro(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro:
            self.libros.remove(libro)
            return True
        return False

class InterfazABM:
    def __init__(self, root, libro_manager):
        self.root = root
        self.libro_manager = libro_manager

        self.root.title("ABM de Libros")

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

        self.precio_reposicion_label = tk.Label(self.input_frame, text="Precio Reposición:")
        self.precio_reposicion_label.grid(row=3, column=0, padx=10, pady=5)
        self.precio_reposicion_entry = tk.Entry(self.input_frame)
        self.precio_reposicion_entry.grid(row=3, column=1, padx=10, pady=5)

        self.agregar_button = tk.Button(self.input_frame, text="Agregar/Modificar Libro", command=self.agregar_libro)
        self.agregar_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.eliminar_button = tk.Button(self.input_frame, text="Eliminar Libro", command=self.eliminar_libro)
        self.eliminar_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Frame para la grilla
        self.grid_frame = tk.Frame(root)
        self.grid_frame.grid(row=1, column=0, padx=10, pady=5)

        self.libros_treeview = ttk.Treeview(self.grid_frame, columns=("Código", "Título", "Descripción", "Precio Reposición"))
        self.libros_treeview.heading("#0", text="ID")
        self.libros_treeview.heading("Código", text="Código")
        self.libros_treeview.heading("Título", text="Título")
        self.libros_treeview.heading("Descripción", text="Descripción")
        self.libros_treeview.heading("Precio Reposición", text="Precio Reposición")
        self.libros_treeview.bind("<ButtonRelease-1>", self.cargar_datos_seleccionados)
        self.libros_treeview.grid(row=0, column=0, padx=10, pady=5)

        # Datos de libros hardcodeados para prueba
        libro_manager.agregar_libro(Libro("1234567890", "Libro 1", "Descripción 1", 19.99))
        libro_manager.agregar_libro(Libro("9876543210", "Libro 2", "Descripción 2", 29.99))
        libro_manager.agregar_libro(Libro("1112223334", "Libro 3", "Descripción 3", 39.99))

        # Actualizar la grilla con los libros hardcodeados
        self.cargar_libros_en_grilla()

    def agregar_libro(self):
        codigo = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        descripcion = self.descripcion_entry.get()
        precio_reposicion = self.precio_reposicion_entry.get()

        if codigo and titulo and descripcion and precio_reposicion:
            nuevo_libro = Libro(codigo, titulo, descripcion, precio_reposicion)
            self.libro_manager.agregar_libro(nuevo_libro)
            self.cargar_libros_en_grilla()
            messagebox.showinfo("Éxito", "Libro agregado/modificado correctamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_libro(self):
        item = self.libros_treeview.selection()
        if item:
            libro_seleccionado = self.libros_treeview.item(item[0], "values")
            if libro_seleccionado:
                codigo_libro = libro_seleccionado[0]
                if self.libro_manager.eliminar_libro(codigo_libro):
                    self.cargar_libros_en_grilla()
                    messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
                    self.limpiar_campos()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el libro.")
            else:
                messagebox.showerror("Error", "No se ha seleccionado un libro.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado un libro.")

    def cargar_libros_en_grilla(self):
        # Limpiar la grilla
        for item in self.libros_treeview.get_children():
            self.libros_treeview.delete(item)

        # Cargar libros en la grilla
        for i, libro in enumerate(self.libro_manager.libros):
            self.libros_treeview.insert("", i, text=str(i + 1), values=(libro.codigo, libro.titulo, libro.descripcion, libro.precio_reposicion))

    def cargar_datos_seleccionados(self, event):
        item = self.libros_treeview.selection()
        if item:
            libro_seleccionado = self.libros_treeview.item(item[0], "values")

            if libro_seleccionado:
                self.codigo_entry.delete(0, tk.END)
                self.titulo_entry.delete(0, tk.END)
                self.descripcion_entry.delete(0, tk.END)
                self.precio_reposicion_entry.delete(0, tk.END)

                self.codigo_entry.insert(0, libro_seleccionado[0])
                self.titulo_entry.insert(0, libro_seleccionado[1])
                self.descripcion_entry.insert(0, libro_seleccionado[2])
                self.precio_reposicion_entry.insert(0, libro_seleccionado[3])

    def limpiar_campos(self):
        self.codigo_entry.delete(0, tk.END)
        self.titulo_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.precio_reposicion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    libro_manager = LibroManager()
    interfaz = InterfazABM(root, libro_manager)
    root.mainloop()
