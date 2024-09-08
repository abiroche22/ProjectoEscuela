"""Archivo que tiene como funcionalidad registrar datos estudiantiles
en la base de datos."""

import tkinter as tk
from tkinter import Tk, ttk, messagebox
from Conexion import Conexion

class RegistrarEstudiantes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Registrar Estudiantes')
        self.geometry('300x450+550+180')
        self.resizable(0,0)
        self.config(bg='black')
        self.widgets_principales()

    def widgets_principales(self):
        self.etiqueta_nombre = tk.Label(self, text='Nombres', bg='black', 
                                        fg='white', font=('arial',18, 'bold'), 
                                        width=8, height=2)
        self.etiqueta_nombre.grid(row=0, column=0)

        self.etiqueta_apellido = tk.Label(self, text='Apellidos', bg='black', 
                                          fg='white',  font=('arial',18, 'bold'), 
                                          width=8, height=2)
        self.etiqueta_apellido.grid(row=1, column=0)

        self.etiqueta_cedula = tk.Label(self, text='Cedula  ', bg='black', 
                                        fg='white', font=('arial',18, 'bold'), 
                                        width=8, height=2)
        self.etiqueta_cedula.grid(row=2, column=0)

        self.etiqueta_edad = tk.Label(self, text='Edad     ', bg='black', 
                                      fg='white', font=('arial',18, 'bold'), 
                                      width=8, height=2)
        self.etiqueta_edad.grid(row=3, column=0)

        self.etiqueta_grado = tk.Label(self, text='Grado    ', bg='black', 
                                       fg='white', font=('arial',18, 'bold'), 
                                       width=8, height=2)
        self.etiqueta_grado.grid(row=4, column=0)

        self.etiqueta_seccion = tk.Label(self, text='Seccion', bg='black', 
                                         fg='white', font=('arial',18, 'bold'), 
                                         width=8, height=2)
        self.etiqueta_seccion.grid(row=5, column=0)


        estilo = ttk.Style()
        estilo.configure('MyEntry.TEntry', padding=3)
        self.entrada_nombre = ttk.Entry(self, width=20, justify=tk.CENTER, 
                                        cursor='hand2', font=('arial',10), 
                                        style='MyEntry.TEntry')
        self.entrada_nombre.grid(row=0, column=1)

        self.entrada_apellido = ttk.Entry(self, width=20, justify=tk.CENTER, 
                                          cursor='hand2', font=('arial',10), 
                                          style='MyEntry.TEntry')
        self.entrada_apellido.grid(row=1, column=1)

        self.entrada_cedula = ttk.Entry(self, width=20, justify=tk.CENTER, 
                                        cursor='hand2', font=('arial',10), 
                                        style='MyEntry.TEntry')
        self.entrada_cedula.grid(row=2, column=1)

        self.entrada_edad = ttk.Entry(self, width=20, justify=tk.CENTER, 
                                      cursor='hand2', font=('arial',10), 
                                      style='MyEntry.TEntry')
        self.entrada_edad.grid(row=3, column=1)

        self.combo_grado = ttk.Combobox(self, state='readonly', values=['Grado 1',
                                                                        'Grado 2',
                                                                        'Grado 3', 
                                                                        'Grado 4',
                                                                        'Grado 5',
                                                                        'Grado 6'])
        self.combo_grado.grid(row=4, column=1)

        self.combo_seccion = ttk.Combobox(self, state='readonly', values=['A','B'])
        self.combo_seccion.grid(row=5, column=1)

        self.boton_registrar = tk.Button(self, text='Registrar', bg='pink',
                                             width=20, height=2, font=('arial',10), 
                                             cursor='hand2', command=lambda: 
                                             self.validar_datos(
                                                 self.entrada_nombre.get(),
                                                 self.entrada_apellido.get(),
                                                 self.entrada_cedula.get(),
                                                 self.entrada_edad.get(),
                                                 self.combo_grado.get(),
                                                 self.combo_seccion.get()))
        self.boton_registrar.grid(row=6, column=0, columnspan=2, pady=10)

    
    def validar_datos(self, nombre, apellido, cedula, edad, grado, seccion):
        try:
            if Conexion.CONEXION:
                print('Hay conexion')
                self.cursor = Conexion.CONEXION.cursor()
                query = "INSERT INTO estudiantes(nombres, apellidos, cedula, edad, grado, seccion) VALUES(%s,%s,%s,%s,%s,%s)"
                valores = (nombre, apellido, cedula, edad, grado, seccion)
                self.cursor.execute(query, valores)
                print('Hemos llegado hasta aqui')
                Conexion.CONEXION.commit()
                messagebox.showinfo(title='Mensaje', message='Estudiante registrado con éxito')
                self.destroy()
        except Exception:
            print('Error:', Exception)
            messagebox.showerror(title='Mensaje', message='No se registraron datos, ocurrió un error.')



if __name__ == '__main__':
    ventana = RegistrarEstudiantes()
    ventana.mainloop()
