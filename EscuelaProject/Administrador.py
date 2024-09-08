""" Archivo del Administrador. Estan definidas todas las caracteristicas y 
funcionalidades que podrá realizar el administrador. """

import tkinter as tk
from tkinter import Tk, messagebox
from Conexion import Conexion
from Estudiantes import Estudiantes
from Docentes import Docentes
from Perfil import Perfil

class Administrador(tk.Tk):
    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        super().__init__()
        self.title('Administrador')
        self.geometry('500x300+450+200')
        self.resizable(0,0)
        self.config(bg='black')
        self.botones_principales()
        self.botones_secundarios()

    def botones_principales(self):
        etiqueta = tk.Label(self, text='Bienvenido', bg='black', width=10,
                            font=('arial', 25, 'bold'), fg='white')
        etiqueta.grid(row=0, column=1, padx=50, pady=10)
        self.boton_estudiantes = tk.Button(self, text='Datos Estudiantiles',
                                            font=('arial', 12), bg='pink',
                                            cursor='hand2', border=2, width=33, 
                                            height=5, command=Estudiantes)
        self.boton_estudiantes.grid(row=1, column=1, padx=12, pady=10) 

        self.boton_docentes = tk.Button(self, text='Datos Profesores', 
                                          font=('arial', 12), bg='pink', 
                                          cursor='hand2', border=2, width=33,
                                          height=5, command=Docentes)
        self.boton_docentes.grid(row=3, column=1, padx=12)

    def botones_secundarios(self):
        frame = tk.Frame(self, bg='grey', width=160, bd=2, height=350)
        frame.grid(row=0, rowspan=4, column=0, sticky='nswe')

        self.boton_perfil = tk.Button(frame, text='Perfil', font=('arial', 10), 
                                     bg='pink', cursor='hand2', border=2, width=20,
                                     height=2, command=self.perfil)
        self.boton_perfil.grid(row=0, column=0)

        self.boton_salir = tk.Button(frame, text='Salir', font=('arial', 10), 
                                     bg='pink', cursor='hand2', border=2, width=20,
                                     height=2, command=self.accion_salir)
        self.boton_salir.grid(row=4, column=0)

    
    def perfil(self):
        try:
            Perfil(self.usuario, self.clave)
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error')

    def accion_salir(self):
        self.destroy()
        Conexion.CONEXION.close()
        print('Se cerró la conexión.')


if __name__ == '__main__':
    ventana = Administrador()
    ventana.mainloop()
