import tkinter as tk
from tkinter import Toplevel


# Crear la clase principal de la aplicación
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")

        # Crear la barra de menú
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Crear un menú desplegable "Archivo"
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)

        # Añadir opción para abrir la ventana secundaria
        file_menu.add_command(label="Abrir Ventana Secundaria", command=self.open_secondary_window)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

    # Método para abrir la ventana secundaria
    def open_secondary_window(self):
        secondary_window = Toplevel(self.root)
        secondary_window.title("Ventana Secundaria")
        secondary_window.geometry("300x200")

        label = tk.Label(secondary_window, text="Esta es la ventana secundaria")
        label.pack(padx=20, pady=20)

        close_button = tk.Button(secondary_window, text="Cerrar", command=secondary_window.destroy)
        close_button.pack(pady=10)


# Crear la ventana principal
root = tk.Tk()
app = App(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()
