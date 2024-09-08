"""Archivo que tiene como funcionalidad actualizar los datos de tipo estudiante"""

import tkinter as tk
from tkinter import Tk, ttk, messagebox
from Conexion import Conexion

class ActualizarEstudiante(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Actualizar Estudiante')
        self.geometry('420x500+500+150')
        self.resizable(0,0)
        self.config(bg='black')
        self.widgets_principales()

    def widgets_principales(self):
        etiqueta_cedula = tk.Label(self, text='Cedula', bg='black', fg='white', 
                                   font=('arial',15, 'bold'), width=8, height=2)
        etiqueta_cedula.grid(row=0, column=0, pady=10, sticky='w', padx=15)

        self.etiqueta_id = tk.Label(self, text='Id            ', bg='black', fg='white', 
                                   font=('arial',15, 'bold'), width=8, height=2)
        self.etiqueta_id.grid(row=1, column=0, padx=20)

        self.etiqueta_nombre = tk.Label(self, text='Nombres', bg='black', fg='white', 
                                   font=('arial',15, 'bold'), width=8, height=2)
        self.etiqueta_nombre.grid(row=2, column=0, padx=20)

        self.etiqueta_apellido = tk.Label(self, text='Apellidos', bg='black', fg='white', 
                                   font=('arial',15, 'bold'), width=8, height=2)
        self.etiqueta_apellido.grid(row=3, column=0, padx=20)

        self.etiqueta_cedula = tk.Label(self, text='Cedula   ', bg='black', fg='white', 
                                   font=('arial',15, 'bold'), width=8, height=2)
        self.etiqueta_cedula.grid(row=4, column=0, padx=20)

        self.etiqueta_edad = tk.Label(self, text='Edad      ', bg='black', fg='white', 
                                   font=('arial',15, 'bold'), width=8, height=2)
        self.etiqueta_edad.grid(row=5, column=0, padx=20)

        self.etiqueta_grado = tk.Label(self, text='Grado     ', bg='black', fg='white', 
                                   font=('arial',15, 'bold'), width=8, height=2)
        self.etiqueta_grado.grid(row=6, column=0, padx=20)

        self.etiqueta_seccion = tk.Label(self, text='Seccion ', bg='black', fg='white', 
                                   font=('arial',15, 'bold'), width=8, height=2)
        self.etiqueta_seccion.grid(row=7, column=0, padx=20)


        estilo = ttk.Style()
        estilo.configure('MyEntry.TEntry', padding=3)

        entrada_cedula = ttk.Entry(self, width=15, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10))
        entrada_cedula.grid(row=0, column=1, sticky='w')

        self.entrada_id = ttk.Entry(self, width=18, justify=tk.CENTER, 
                                    cursor='hand2', font=('arial',10), 
                                    style='MyEntry.TEntry')
        self.entrada_id.grid(row=1, column=1)

        self.entrada_nombre = ttk.Entry(self, width=18, justify=tk.CENTER, 
                                        cursor='hand2', font=('arial',10), 
                                        style='MyEntry.TEntry')
        self.entrada_nombre.grid(row=2, column=1)

        self.entrada_apellido = ttk.Entry(self, width=18, justify=tk.CENTER, 
                                          cursor='hand2', font=('arial',10), 
                                          style='MyEntry.TEntry')
        self.entrada_apellido.grid(row=3, column=1)

        self.entrada_cedula = ttk.Entry(self, width=18, justify=tk.CENTER, 
                                        cursor='hand2', font=('arial',10), 
                                        style='MyEntry.TEntry')
        self.entrada_cedula.grid(row=4, column=1)

        self.entrada_edad = ttk.Entry(self, width=18, justify=tk.CENTER, 
                                      cursor='hand2', font=('arial',10), 
                                      style='MyEntry.TEntry')
        self.entrada_edad.grid(row=5, column=1)

        self.combo_grado = ttk.Combobox(self, state='readonly', width=19,
                                        values=['Grado 1',
                                                'Grado 2',
                                                'Grado 3', 
                                                'Grado 4',
                                                'Grado 5',
                                                'Grado 6'])
        self.combo_grado.grid(row=6, column=1)

        self.combo_seccion = ttk.Combobox(self, state='readonly', width=19,
                                          values=['A','B'])
        self.combo_seccion.grid(row=7, column=1)

        self.boton_buscar = tk.Button(self, text='Buscar', bg='pink',
                                             width=10, height=1, font=('arial',10), 
                                             cursor='hand2', command=lambda: 
                                             self.recuperar_datos(entrada_cedula.get()))
        self.boton_buscar.grid(row=0, column=2, sticky='w')

        self.boton_actualizar = tk.Button(self, text='Actualizar', bg='pink',
                                             width=35, height=1, font=('arial',10), 
                                             cursor='hand2', command=lambda:
                                             self.actualizar_datos(
                                                self.entrada_nombre.get(),
                                                self.entrada_apellido.get(),
                                                self.entrada_cedula.get(),
                                                self.entrada_edad.get(),
                                                self.combo_grado.get(),
                                                self.combo_seccion.get(),
                                                self.entrada_id.get()))
        self.boton_actualizar.grid(row=8, column=0, columnspan=3, padx=30, pady=10,
                                   sticky='e')
        
    
    def recuperar_datos(self, cedula):
        try:
            if Conexion.CONEXION:
                self.cursor = Conexion.CONEXION.cursor()
                query = 'SELECT * FROM estudiantes WHERE cedula=%s'
                valores = (cedula,)
                self.cursor.execute(query, valores)
                datos = self.cursor.fetchone()
                if datos:
                    self.entrada_id.insert(0, datos[0])
                    self.entrada_nombre.insert(0, datos[1])
                    self.entrada_apellido.insert(0, datos[2])
                    self.entrada_cedula.insert(0, datos[3])
                    self.entrada_edad.insert(0, datos[4])
                    self.combo_grado.set(datos[5])
                    self.combo_seccion.set(datos[6])
                Conexion.CONEXION.commit()
        except Exception:
            messagebox.showerror(title='Mensaje', message='Ocurrió un error al recuperar datos')

    
    def actualizar_datos(self, nombres, apellidos, cedula, edad, grado, seccion, id):
        try:
            query = 'UPDATE estudiantes SET nombres=%s, apellidos=%s, cedula=%s, edad=%s, grado=%s, seccion=%s WHERE id=%s'
            valores = (nombres, apellidos, cedula, edad, grado, seccion, id)
            self.cursor.execute(query, valores)
            messagebox.showinfo(title='Mensaje', message='Datos actualizados con éxito')
            Conexion.CONEXION.commit()
            self.destroy()
        except Exception:
            messagebox.showerror(title='Mensaje', message='Ocurrió un error al actualizar los datos')


if __name__ == '__main__':
    ventana = ActualizarEstudiante()
    ventana.mainloop()
