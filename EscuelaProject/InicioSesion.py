"""Archivo que tiene como funcionalidad iniciar la sesion del administrador"""

import tkinter as tk
from tkinter import Tk, ttk, messagebox
from Conexion import Conexion
from Administrador import Administrador
from RegistrarAdmin import RegistrarAdmin

class InicioSesion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Iniciar Sesion')
        self.geometry('400x150+500+250')
        self.resizable(0,0)
        self.config(bg='black')
        self.widgets_principales()

    def widgets_principales(self):
        etiqueta_usuario = tk.Label(self, text='Usuario', bg='black', width=8,
                            font=('arial', 20, 'bold'), fg='white')
        etiqueta_usuario.grid(row=0, column=0, pady=10)

        etiqueta_clave = tk.Label(self, text='Clave   ', bg='black', width=8,
                            font=('arial', 20, 'bold'), fg='white')
        etiqueta_clave.grid(row=1, column=0)

        estilo = ttk.Style()
        estilo.configure('MyEntry.TEntry', padding=3)
        self.entrada_usuario = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_usuario.grid(row=0, column=1)

        self.entrada_clave = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                  font=('arial', 10), style="MyEntry.TEntry", 
                                  show='*')
        self.entrada_clave.grid(row=1, column=1)

        self.boton_registrar = tk.Button(self, text='Registrar', bg='pink', fg='black',
                                        font=('arial', 10), cursor='hand2', width=20,
                                        height=1, command=RegistrarAdmin)
        self.boton_registrar.grid(row=2, column=0, pady=20, padx=10) 

        self.boton_iniciar = tk.Button(self, text='Iniciar Sesion', bg='pink', fg='black',
                                  font=('arial', 10), cursor='hand2', width=20,
                                  height=1, command=lambda: self.validar_datos(
                                      self.entrada_usuario.get(),
                                      self.entrada_clave.get()))
        self.boton_iniciar.grid(row=2, column=1, pady=20, padx=10)


    def validar_datos(self, usuario, clave):
        try:
            if Conexion.CONEXION:
                print('hay conexion')
                self.cursor = Conexion.CONEXION.cursor()
                query = 'SELECT usuario, clave FROM administradores WHERE usuario=%s AND clave=%s'
                valores = (usuario, clave)
                self.cursor.execute(query, valores)
                usuario, clave = self.cursor.fetchone()
                Conexion.CONEXION.commit()
                print('Se hizo commit')
                if usuario and clave:
                    self.destroy()
                    print('Se inició Sesión.')
                    Administrador(usuario, clave)
            else:
                print('No hay conexión a la base de datos.')
        except Exception:
            print("Error:", Exception)
            messagebox.showerror(title='Mensaje', message='Datos invalidos')


if __name__ == '__main__':
    ventana = InicioSesion()
    ventana.mainloop()
