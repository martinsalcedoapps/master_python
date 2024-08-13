from tkinter import *
from tkinter import messagebox as MessageBox
import tkinter as tk
import os
from PIL import Image, ImageTk


class MyApplication(object):
    main_window = Tk()
    data_frame_row = 0
    form_data = {}
    form_frames = []
    form_fields = []
    action_buttons = 0

    def __init__(self, title):
        self.main_window.title(title)
        # self.main_window.geometry('500x500')
        self.set_icon()

    def set_icon(self):
        ico_path = os.path.abspath("./imagenes/icon.ico")
        xbm_path = os.path.abspath("./imagenes/icon.xbm")
        png_path = os.path.abspath("./imagenes/icon16.png")
        jpg_path = os.path.abspath("./imagenes/icon.jpg")
        self.main_window.title("Interfaz gráfica con Python")
        try:
            self.main_window.iconbitmap(ico_path)
        except BaseException as errstr:
            try:
                images = PhotoImage(file=png_path)
                self.main_window.iconphoto(True, images)
            except BaseException as errstr:
                print("Icon can not be set")

    def start(self):
        self.main_window.mainloop()

    # Helper methods

    def reset_fields(self):
        for field_name in self.form_data:
            obj_type = self.form_data[field_name].get('type')
            obj_widget = self.form_data[field_name].get('form_object')
            if obj_type == 'entry':
                obj_widget.delete(0, tk.END)
                # self.form_data[field_name]['value'] = StringVar()
            elif obj_type == 'checkbox':
                self.form_data[field_name]['value'] = False

    # Content management
    def set_form_title(self, title_label):

        title_frame = Frame(self.main_window, bd=2, relief='groove')
        title_frame.grid(row=0, column=0, padx=10, pady=10)

        back_color = '#e6f7ff'

        title_label = Label(title_frame, text=title_label, cnf={'bg': back_color}, width=50,
                            font=('Ubuntu', 12, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2)
        self.form_frames.append(title_frame)

        data_frame = LabelFrame(self.main_window, text="Introduzca los siguientes campos", bd=2, relief='groove')
        data_frame.grid(row=1, column=0, padx=10, ipady=5, ipadx=5)

        self.form_frames.append(data_frame)

        action_frame = Frame(self.main_window, bd=2, relief='groove', pady=5, padx=10)
        action_frame.grid(row=2, column=0, columnspan=2)

        self.form_frames.append(action_frame)

    def add_field_entry(self, label, name, required=False):
        entry_config = {'bg': 'white'}
        label_config = {'width': 20}

        self.form_data[name] = {}
        self.form_data[name]['type'] = 'entry'
        self.form_data[name]['field'] = name
        self.form_data[name]['label'] = label
        self.form_data[name]['value'] = StringVar()
        self.form_data[name]['required'] = required

        data_frame = self.form_frames[1]

        field_frame = Frame(data_frame, cnf={'height': '2'})
        field_frame.grid(row=self.data_frame_row, column=0, padx=10)

        field_label = Label(field_frame,
                            text=label,
                            cnf=label_config,
                            anchor='e',
                            font=('Arial', 11, 'bold' if required else ''))
        field_label.grid(row=0, column=0)
        field_entry = Entry(field_frame, textvariable=self.form_data[name]['value'], cnf=entry_config)
        field_entry.grid(row=0, column=1)

        self.form_data[name]['form_label'] = field_label
        self.form_data[name]['form_object'] = field_entry

        self.data_frame_row += 1

        self.form_fields.append(field_entry)

    def add_checkbox(self, label, name):
        self.form_data[name] = {}
        self.form_data[name]['type'] = 'checkbox'
        self.form_data[name]['field'] = name
        self.form_data[name]['label'] = label
        self.form_data[name]['value'] = IntVar()

        data_frame = self.form_frames[1]
        checkbox = Checkbutton(data_frame,
                               text=label,
                               variable=self.form_data[name]['value'],
                               onvalue=True, offvalue=False)
        checkbox.grid(row=self.data_frame_row, column=0)
        self.form_data[name]['form_object'] = checkbox
        self.data_frame_row += 1

    def add_action_button(self, label, special):
        action_frame = self.form_frames[2]
        attr = getattr(self, f"button_{special}")
        button = Button(action_frame, text=label, command=attr)
        button.grid(row=0, column=self.action_buttons)
        self.action_buttons += 1

    def button_send(self):
        vals = {}
        error = False
        for field_name in self.form_data:
            print(field_name, self.form_data[field_name])
            label = self.form_data[field_name]['label']
            required = self.form_data[field_name].get('required', False)
            value = self.form_data[field_name]['value'].get()
            if required and not value:
                mbox = MessageBox.showerror(title='Error de Validación',
                                            message=f"El campo {label} es obligatorio.")
                error = True
                break
            vals[field_name] = value
        if not error:
            MessageBox.showinfo("Validación de datos", "Los datos se han cargado correctamente.")

            res = MessageBox.askyesno(title="Salir", message="¿Desea salir?")
            print(res, type(res))
            if res:
                self.main_window.destroy()
            else:
                self.reset_fields()
                self.form_fields[0].focus_set()
        print(vals)
        return vals

    def button_close(self):
        self.main_window.destroy()


# end content management -----


app = MyApplication("Mi Primera Aplicación")
app.set_icon()
app.set_form_title("Datos Personales")
app.add_field_entry(label="Nombre", name="name", required=True)
app.add_field_entry(label="Apellido", name="lastname")
app.add_field_entry(label="Correo Electrónico", name="email", required=True)
app.add_checkbox(label="Activo", name="active")
app.add_action_button("Enviar", special="send")
app.add_action_button("Cerrar", special="close")
app.start()
