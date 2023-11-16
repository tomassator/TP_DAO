import tkinter as tk
from tkinter import ttk, messagebox
from gestor import Gestor

class PrestamoManager:
    def __init__(self, gestor=Gestor()):
        self.gestor = gestor

    def consultar_socios(self):
        return self.gestor.obtener_socios()

class InterfazRegistrarPrestamos:
    def __init__(self, root, prestamo_manager):
        self.root = root
        self.root.title("Registro de Préstamos")

        self.prestamo_manager = prestamo_manager

        # Crear el frame de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=10)

        # Elementos en el input_frame
        self.socio_label = tk.Label(self.input_frame, text="Socio:")
        self.socio_label.grid(row=0, column=0, padx=10, pady=5)
        socios = prestamo_manager.consultar_socios()
        nombres_socios = [socio.nombre + " " + socio.apellido for socio in socios]
        self.socio_combobox = ttk.Combobox(self.input_frame, values=nombres_socios)
        self.socio_combobox.grid(row=0, column=1, padx=10, pady=5)

        self.libro_label = tk.Label(self.input_frame, text="Libro:")
        self.libro_label.grid(row=1, column=0, padx=10, pady=5)
        self.libro_combobox = ttk.Combobox(self.input_frame, values=["Libro1", "Libro2", "Libro3"])
        self.libro_combobox.grid(row=1, column=1, padx=10, pady=5)

        self.dias_label = tk.Label(self.input_frame, text="Días para devolución:")
        self.dias_label.grid(row=2, column=0, padx=10, pady=5)
        self.dias_entry = tk.Entry(self.input_frame)
        self.dias_entry.grid(row=2, column=1, padx=10, pady=5)

        self.prestamo_button = tk.Button(self.input_frame, text="Registrar Préstamo", command=self.registrar_prestamo)
        self.prestamo_button.grid(row=3, column=0, columnspan=2, pady=10)

    def registrar_prestamo(self):
        socio = self.socio_combobox.get()
        libro = self.libro_combobox.get()
        dias = self.dias_entry.get()

        if socio and libro and dias:
            #Logica para registrar prestamo
            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Préstamo registrado correctamente.")

            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def limpiar_campos(self):
        self.socio_combobox.set("")  # Limpiar el combobox de Socio
        self.libro_combobox.set("")  # Limpiar el combobox de Libro
        self.dias_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazRegistrarPrestamos(root, None)
    root.mainloop()



