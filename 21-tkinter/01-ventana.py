from tkinter import *
from tkinter import messagebox as MessageBox
import tkinter as tk
import os
from PIL import Image, ImageTk


class MyApplication(object):
    form_window = Tk()
    form_row = 0
    form_data = {}
    form_frames = []
    form_fields = []

    def __init__(self, title):
        self.form_window.title(title)
        self.form_window.geometry('500x500')
        self.set_icon()

    def set_icon(self):
        ico_path = os.path.abspath("./imagenes/icon.ico")
        xbm_path = os.path.abspath("./imagenes/icon.xbm")
        png_path = os.path.abspath("./imagenes/icon16.png")
        jpg_path = os.path.abspath("./imagenes/icon.jpg")
        self.form_window.title("Interfaz gráfica con Python")
        try:
            self.form_window.iconbitmap(ico_path)
        except BaseException as errstr:
            try:
                images = PhotoImage(file=png_path)
                self.form_window.iconphoto(True, images)
            except BaseException as errstr:
                print("Icon can not be set")

    def set_form_title(self, form_title):
        form_title = Label(self.form_window,
                           text=form_title,
                           cnf={'fg'    : "blue",
                                'bg'    : 'gray',
                                'height': 1}
                           )
        form_title.pack(anchor=N, fill=X)

    def start(self):
        self.form_window.mainloop()

    def add_field_entry(self, label, field_name, required=False):
        entry_config = {'bg': 'white'}
        label_config = {'width': 15}

        self.form_data[field_name] = {}
        self.form_data[field_name]['field'] = field_name
        self.form_data[field_name]['label'] = label
        self.form_data[field_name]['value'] = StringVar()
        self.form_data[field_name]['required'] = required

        field_frame = Frame(self.form_window, cnf={'height': '2'})
        label = Label(field_frame,
                      text=f"{label}:",
                      padx=10,
                      cnf=label_config)
        entry = Entry(field_frame,
                      textvariable=self.form_data[field_name]['value'],
                      cnf=entry_config)
        label.grid(row=self.form_row, column=0)
        entry.grid(row=self.form_row, column=1)
        field_frame.pack(anchor=W)
        self.form_data[field_name]['form_label'] = label
        self.form_data[field_name]['form_entry'] = entry
        self.form_frames.append(field_frame)
        self.form_fields.append(entry)
        self.form_row += 1

    def button_command(self):
        vals = {}
        error = False
        for field_name in self.form_data:
            print(field_name, self.form_data[field_name])
            label = self.form_data[field_name]['label']
            required = self.form_data[field_name]['required']
            value = self.form_data[field_name]['value'].get()
            if required and not value:
                mbox = MessageBox.showerror(title='Error de Validación',
                                            message=f"El campo {label} es obligatorio.")
                error = True
            vals[field_name] = value
        if not error:
            MessageBox.showinfo("Validación de datos", "Los datos se han cargado correctamente.")
        res = MessageBox.askyesno(title="Salir", message="¿Desea salir?")
        print(res, type(res))
        if res:
            self.form_window.destroy()
        else:
            for field_name in self.form_data:
                self.form_data[field_name]['form_entry'].delete(0, tk.END)
            self.form_fields[0].focus_set()
        print(vals)

        return vals

    def add_buttom(self, label):
        button = Button(self.form_frames[-1], text=label, command=self.button_command)
        button.grid(row=self.form_row, column=1)
        self.form_row += 1


app = MyApplication("Mi Primera Aplicación")
app.set_icon()
app.set_form_title("Datos Personales")
app.add_field_entry(label="Nombre", field_name="name", required=True)
app.add_field_entry(label="Apellido", field_name="lastname")
app.add_field_entry(label="Correo Electrónico", field_name="email", required=True)
app.add_buttom("Enviar")
app.start()
