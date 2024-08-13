import tkinter as tk
from tkinter import ttk


def create_notebook_example():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Ejemplo de Notebook")

    # Crear un widget Notebook
    notebook = ttk.Notebook(root)
    notebook.pack(padx=10, pady=10, expand=True, fill='both')

    # Crear las pestañas (tabs)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)

    # Agregar las pestañas al Notebook
    notebook.add(tab1, text="Pestaña 1")
    notebook.add(tab2, text="Pestaña 2")
    notebook.add(tab3, text="Pestaña 3")

    # Contenido para la primera pestaña
    label1 = tk.Label(tab1, text="Contenido de la Pestaña 1")
    label1.pack(padx=10, pady=10)
    button1 = tk.Button(tab1, text="Botón en Pestaña 1")
    button1.pack(padx=10, pady=10)

    # Contenido para la segunda pestaña
    label2 = tk.Label(tab2, text="Contenido de la Pestaña 2")
    label2.pack(padx=10, pady=10)
    entry2 = tk.Entry(tab2)
    entry2.pack(padx=10, pady=10)

    # Contenido para la tercera pestaña
    label3 = tk.Label(tab3, text="Contenido de la Pestaña 3")
    label3.pack(padx=10, pady=10)
    button3 = tk.Button(tab3, text="Botón en Pestaña 3")
    button3.pack(padx=10, pady=10)

    # Iniciar el bucle principal de Tkinter
    root.mainloop()


# Llamar a la función para ejecutar el ejemplo
create_notebook_example()
