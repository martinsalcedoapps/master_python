import tkinter as tk
from tkinter import ttk


# Crear la clase principal de la aplicación
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de Treeview")
        self.root.geometry("600x400")

        # Crear un Frame para el Treeview
        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear el Treeview
        self.tree = ttk.Treeview(frame, columns=("Name", "Age", "City"), show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Definir las columnas
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("City", text="City")

        self.tree.column("Name", width=150)
        self.tree.column("Age", width=100)
        self.tree.column("City", width=150)

        # Insertar algunos datos
        self.insert_data()

    def insert_data(self):
        # Insertar datos en el Treeview
        self.tree.insert("", tk.END, values=("Alice", 30, "New York"))
        self.tree.insert("", tk.END, values=("Bob", 25, "Los Angeles"))
        self.tree.insert("", tk.END, values=("Charlie", 35, "Chicago"))

        # Insertar datos con una estructura jerárquica
        parent_id = self.tree.insert("", tk.END, text="Parent", values=("Parent", "", ""))
        self.tree.insert(parent_id, tk.END, values=("Child 1", 10, "Location A"))
        self.tree.insert(parent_id, tk.END, values=("Child 2", 20, "Location B"))


# Crear la ventana principal
root = tk.Tk()
app = App(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()
