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
                self.form_data[field_name]['value'] = BooleanVar()
            elif obj_type == 'radiobutton':
                default = self.form_data[field_name].get('default', StringVar())
                self.form_data[field_name]['value'].set(default)
            elif obj_type == 'optionmenu':
                default = self.form_data[field_name].get('default', StringVar())
                self.form_data[field_name]['value'].set(default)

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

    def add_radiobutton(self, label, name, values, default_value=None):
        self.form_data[name] = {}
        self.form_data[name]['type'] = 'radiobutton'
        self.form_data[name]['field'] = name
        self.form_data[name]['label'] = label
        self.form_data[name]['value'] = StringVar()
        if default_value:
            default = default_value
        else:
            default = list(values.keys())[0]
        self.form_data[name]['default'] = default
        self.form_data[name]['value'].set(default)
        self.form_data[name]['form_object'] = []

        data_frame = self.form_frames[1]

        radio_frame = LabelFrame(data_frame, text=label, bd=2, relief='groove')
        radio_frame.grid(row=self.data_frame_row, column=0)
        frame_row = 0
        for key, val in values.items():
            radiobutton = Radiobutton(radio_frame,
                                      text=val,
                                      variable=self.form_data[name]['value'],
                                      value=key
                                      )
            radiobutton.grid(row=frame_row, column=0, sticky="w")
            self.form_data[name]['form_object'].append(radiobutton)
            frame_row += 1

        self.data_frame_row += 1

    def add_optionmenu(self, label, name, values, default_value=None):
        """
        Agrega un OptionMenu a un Frame.

        :param label: El texto para el Label que se coloca junto al OptionMenu.
        :param name: El nombre del campo en el formulario.
        :param values: Una lista de opciones para el OptionMenu.
        :param default_value: Valor inicial del OptionMenu (opcional).
        """
        # Inicializar la estructura de datos en form_data
        self.form_data[name] = {}
        self.form_data[name]['type'] = 'optionmenu'
        self.form_data[name]['field'] = name
        self.form_data[name]['label'] = label
        self.form_data[name]['value'] = StringVar()

        # Establecer el valor inicial del OptionMenu
        if default_value:
            default = values.get(default_value)
            self.form_data[name]['value'].set(default)
            self.form_data[name]['default'] = default
        else:
            default = values.get(list(values.keys())[0])
            self.form_data[name]['value'].set(default)  # Seleccionar la primera opción como predeterminada
            self.form_data[name]['default'] = default


        # Obtener el Frame en el que se colocará el OptionMenu
        data_frame = self.form_frames[1]

        option_frame = Frame(data_frame)
        option_frame.grid(row=self.data_frame_row, column=0, padx=10)

        # Crear un Label para el OptionMenu
        label_widget = Label(option_frame, text=label)
        label_widget.grid(row=0, column=0, padx=5, pady=5)

        # Crear el OptionMenu
        optionmenu = OptionMenu(option_frame, self.form_data[name]['value'], *values.values())
        optionmenu.grid(row=0, column=1, padx=5, pady=5)

        # Almacenar el OptionMenu en form_object
        self.form_data[name]['form_object'] = optionmenu

        # Incrementar el contador de filas para la siguiente entrada en el formulario
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
            field_type = self.form_data[field_name]['type']
            if field_type == 'entry':
                value = self.form_data[field_name]['value'].get()
            elif field_type == 'checkbox':
                value = self.form_data[field_name]['value'].get()
            elif field_type == 'radiobutton':
                value = self.form_data[field_name]['value'].get()
            elif field_type == 'optionmenu':
                value = self.form_data[field_name]['value']
            else:
                value = self.form_data[field_name]['value']
            if required and not value:
                MessageBox.showerror(title='Error de Validación',
                                     message=f"El campo {label} es obligatorio.")
                error = True
                break
            vals[field_name] = value
        if not error:
            MessageBox.showinfo("Validación de datos", "Los datos se han cargado correctamente.")

            res = MessageBox.askyesno(title="Salir", message="¿Desea salir?")
            if res:
                self.main_window.destroy()
            else:
                self.reset_fields()
                self.form_fields[0].focus_set()
        print("Valores Capturados", vals)
        return vals

    def button_close(self):
        self.main_window.destroy()


# end content management -----


app = MyApplication("Mi Primera Aplicación")
app.set_icon()
app.set_form_title("Usuarios")
app.add_field_entry(label="Nombre", name="name", required=True)
app.add_field_entry(label="Apellido", name="lastname")
app.add_field_entry(label="Correo Electrónico", name="email", required=True)
app.add_checkbox(label="Activo", name="active")
app.add_radiobutton(label="Tipo de Usuario", name='user_type',
                    values={'internal': 'Interno',
                            'portal'  : 'Portal',
                            'public'  : 'Public'})
app.add_optionmenu(label="Grupo de Acceso", name='access_group',
                   values={'user'      : 'Usuario',
                           'supervisor': 'Supervisor',
                           'admin'     : 'Administrador del Sistema'},
                   default_value='user')
app.add_action_button("Enviar", special="send")
app.add_action_button("Cerrar", special="close")
app.start()
