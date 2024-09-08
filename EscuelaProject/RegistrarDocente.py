"""Archivo que tiene como funcionalidad registrar datos tipo docentes"""

import tkinter as tk
from tkinter import Tk, ttk, messagebox
from Conexion import Conexion

class RegistrarDocente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Registrar Estudiantes')
        self.geometry('320x400+550+180')
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
        self.etiqueta_apellido.grid(row=1, column=0, padx=10)

        self.etiqueta_cedula = tk.Label(self, text='Cedula  ', bg='black', 
                                        fg='white', font=('arial',18, 'bold'), 
                                        width=8, height=2)
        self.etiqueta_cedula.grid(row=2, column=0)

        self.etiqueta_edad = tk.Label(self, text='Edad     ', bg='black', 
                                      fg='white', font=('arial',18, 'bold'), 
                                      width=8, height=2)
        self.etiqueta_edad.grid(row=3, column=0)

        self.etiqueta_materia = tk.Label(self, text='Materia  ', bg='black', 
                                      fg='white', font=('arial',18, 'bold'), 
                                      width=8, height=2)
        self.etiqueta_materia.grid(row=4, column=0)


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

        self.combo_materias = ttk.Combobox(self, state='readonly', values=['Lengua y Literatura',
                                                                        'Inglés',
                                                                        'Historia', 
                                                                        'Matemática',
                                                                        'Física',
                                                                        'Química',
                                                                        'Biología',
                                                                        'Arte',
                                                                        'Deporte',
                                                                        'Cs Sociales'])
        self.combo_materias.grid(row=4, column=1)

        self.boton_registrar = tk.Button(self, text='Registrar', bg='pink',
                                             width=25, height=1, font=('arial',10), 
                                             cursor='hand2', command=lambda: 
                                             self.validar_datos(
                                                self.entrada_nombre.get(),
                                                self.entrada_apellido.get(),
                                                self.entrada_cedula.get(),
                                                self.entrada_edad.get(),
                                                self.combo_materias.get()))
        self.boton_registrar.grid(row=5, column=0, columnspan=2, pady=10)

    
    def validar_datos(self, nombre, apellido, cedula, edad, materia):
        try:
            if Conexion.CONEXION:
                print('Hay conexion')
                self.cursor = Conexion.CONEXION.cursor()
                query = "INSERT INTO docentes(nombres, apellidos, cedula, edad, materia) VALUES(%s,%s,%s,%s,%s)"
                valores = (nombre, apellido, cedula, edad, materia)
                self.cursor.execute(query, valores)
                Conexion.CONEXION.commit()
                messagebox.showinfo(title='Mensaje', message='Docente registrado con éxito')
                self.destroy()
        except Exception:
            print('Error:', Exception)
            messagebox.showerror(title='Mensaje', message='No se registraron datos, ocurrió un error.')



if __name__ == '__main__':
    ventana = RegistrarDocente()
    ventana.mainloop()
