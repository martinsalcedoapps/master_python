import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Múltiples Grids")

# Primer Frame con su propio grid
frame1 = tk.Frame(root, bd=2, relief="groove")
frame1.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame1, text="Grid 1 - Label 1").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame1, text="Grid 1 - Label 2").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame1).grid(row=0, column=1, padx=5, pady=5)
tk.Entry(frame1).grid(row=1, column=1, padx=5, pady=5)

# Segundo Frame con su propio grid
frame2 = tk.Frame(root, bd=2, relief="groove")
frame2.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame2, text="Grid 2 - Label 1").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame2, text="Grid 2 - Label 2").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame2).grid(row=0, column=1, padx=5, pady=5)
tk.Entry(frame2).grid(row=1, column=1, padx=5, pady=5)

# Tercer Frame con su propio grid
frame3 = tk.LabelFrame(root, text="Grid 3", bd=2, relief="groove")
frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

tk.Label(frame3, text="Grid 3 - Label 1").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame3, text="Grid 3 - Label 2").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame3).grid(row=0, column=1, padx=5, pady=5)
tk.Entry(frame3).grid(row=1, column=1, padx=5, pady=5)

# Configuración de la expansión de los frames
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

# Iniciar el bucle principal de Tkinter
root.mainloop()
