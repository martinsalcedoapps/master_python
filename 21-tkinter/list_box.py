import tkinter as tk


# Crear la clase principal de la aplicación
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de Listbox")
        self.root.geometry("300x200")

        # Crear un Frame para contener los widgets
        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Crear el Listbox
        self.listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Insertar elementos en el Listbox
        items = ["Manzana", "Banana", "Cereza", "Dátil", "Elderberry"]
        for item in items:
            self.listbox.insert(tk.END, item)

        # Crear un botón para mostrar el elemento seleccionado
        show_button = tk.Button(frame, text="Mostrar Selección", command=self.show_selection)
        show_button.pack(pady=10)

        # Crear una etiqueta para mostrar la selección
        self.selection_label = tk.Label(frame, text="Selecciona un elemento")
        self.selection_label.pack(pady=10)

    def show_selection(self):
        # Obtener el índice del elemento seleccionado
        selected_index = self.listbox.curselection()

        if selected_index:
            # Obtener el valor del elemento seleccionado
            selected_value = self.listbox.get(selected_index)
            self.selection_label.config(text=f"Seleccionaste: {selected_value}")
        else:
            self.selection_label.config(text="No se ha seleccionado ningún elemento")


# Crear la ventana principal
root = tk.Tk()
app = App(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()
