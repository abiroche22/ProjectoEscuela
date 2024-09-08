"""Archivo principal del programa. Están definidas todas las caracteristicas
y funcionalidades del programa."""

import tkinter as tk
from tkinter import Tk, ttk, messagebox
from InicioSesion import InicioSesion
from ObtenerGrado import ObtenerGrado

class VenPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bienvenidos')
        self.geometry('800x400+300+150')
        self.resizable(0,0)
        self.config(bg='black')
        self.botones_principales()
        self.botones_secundarios()

    def botones_principales(self):
        etiqueta = tk.Label(self, text='Bienvenidos', bg='black', fg='white',
                            font=('arial', 30, 'bold'), width=15, height=1)
        etiqueta.grid(row=0, column=0, columnspan=3, padx=10, pady=18)

        self.boton_grado1 = tk.Button(self, text='Grado 1', bg='pink', 
                                       width=30, height=6, font=('arial', 10),
                                       cursor='hand2', command=self.grado1)
        self.boton_grado1.grid(row=1, column=0, padx=10, sticky='nw')

        self.boton_grado2 = tk.Button(self, text='Grado 2', bg='pink',
                                       width=30, height=6, font=('arial',10),
                                       cursor='hand2', command=self.grado2)
        self.boton_grado2.grid(row=1, column=1)

        self.boton_grado3 = tk.Button(self, text='Grado 3', bg='pink',
                                      width=30, height=6, font=('arial',10),
                                      cursor='hand2', command=self.grado3)
        self.boton_grado3.grid(row=1, column=2, padx=10, sticky='nw')

        self.boton_grado4 = tk.Button(self, text='Grado 4', bg='pink',
                                      width=30, height=6,  font=('arial',10),
                                      cursor='hand2', command=self.grado4)
        self.boton_grado4.grid(row=2, column=0, padx=10, pady=10, sticky='nw')

        self.boton_grado5 = tk.Button(self, text='Grado 5', bg='pink',
                                      width=30, height=6, font=('arial',10),
                                      cursor='hand2', command=self.grado5)
        self.boton_grado5.grid(row=2, column=1, pady=10)

        self.boton_grado6 = tk.Button(self, text='Grado 6', bg='pink',
                                      width=30, height=6, font=('arial',10),
                                      cursor='hand2', command=self.grado6)
        self.boton_grado6.grid(row=2, column=2, padx=10, pady=10, sticky='nw')

    
    def botones_secundarios(self):
        self.boton_inicio_sesion = tk.Button(self, text='Iniciar Sesion', bg='pink',
                                             width=25, height=3, font=('arial',8), 
                                             cursor='hand2', command=self.iniciar_sesion)
        self.boton_inicio_sesion.grid(row=3, column=0, columnspan=2, padx=10, 
                                      pady=10, sticky='nswe')
        
    
    def grado1(self):
        try:
            etiqueta = 'Estudiantes: Grado 1'
            query = 'SELECT id, nombres, apellidos, cedula, edad, seccion FROM estudiantes WHERE grado="Grado 1"'
            ObtenerGrado(etiqueta, query)
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error')

    
    def grado2(self):
        try:
            etiqueta = 'Estudiantes: Grado 2'
            query = 'SELECT id, nombres, apellidos, cedula, edad, seccion FROM estudiantes WHERE grado="Grado 2"'
            ObtenerGrado(etiqueta, query)
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error')

    
    def grado3(self):
        try:
            etiqueta = 'Estudiantes: Grado 3'
            query = 'SELECT id, nombres, apellidos, cedula, edad, seccion FROM estudiantes WHERE grado="Grado 3"'
            ObtenerGrado(etiqueta, query)
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error')

    
    def grado4(self):
        try:
            etiqueta = 'Estudiantes: Grado 4'
            query = 'SELECT id, nombres, apellidos, cedula, edad, seccion FROM estudiantes WHERE grado="Grado 4"'
            ObtenerGrado(etiqueta, query)
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error')

    
    def grado5(self):
        try:
            etiqueta = 'Estudiantes: Grado 5'
            query = 'SELECT id, nombres, apellidos, cedula, edad, seccion FROM estudiantes WHERE grado="Grado 5"'
            ObtenerGrado(etiqueta, query)
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error')

    
    def grado6(self):
        try:
            etiqueta = 'Estudiantes: Grado 6'
            query = 'SELECT id, nombres, apellidos, cedula, edad, seccion FROM estudiantes WHERE grado="Grado 6"'
            ObtenerGrado(etiqueta, query)
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error')

        
    def iniciar_sesion(self):
        self.destroy()
        InicioSesion()
            

if __name__ == '__main__':
    ventana = VenPrincipal()
    ventana.mainloop()