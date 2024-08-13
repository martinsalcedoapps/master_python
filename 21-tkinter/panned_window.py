import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de PanedWindow")

# Crear el PanedWindow
paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Crear dos frames para los paneles
left_frame = ttk.Frame(paned_window, width=200, height=300, relief=tk.SUNKEN)
right_frame = ttk.Frame(paned_window, width=400, height=300, relief=tk.SUNKEN)

# Agregar los frames al PanedWindow
paned_window.add(left_frame, weight=1)
paned_window.add(right_frame, weight=3)

# Agregar contenido a los frames
tk.Label(left_frame, text="Panel Izquierdo", padx=10, pady=10).pack()
tk.Label(right_frame, text="Panel Derecho", padx=10, pady=10).pack()

# Iniciar el loop de eventos
root.mainloop()
