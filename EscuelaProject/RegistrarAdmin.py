"""Archivo que tiene como funcionalidad registrar nuevos adminisradores."""

import tkinter as tk
from tkinter import Tk, ttk, messagebox
from Conexion import Conexion

class RegistrarAdmin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Registrar Administrador')
        self.geometry('320x400+550+180')
        self.resizable(0,0)
        self.config(bg='black')
        self.widgets_principales()

    def widgets_principales(self):
        self.etiqueta_nombre = tk.Label(self, text='Nombre', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_nombre.grid(row=0, column=0)

        self.etiqueta_apellido = tk.Label(self, text='Apellido', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_apellido.grid(row=1, column=0)

        self.etiqueta_usuario = tk.Label(self, text='Usuario ', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_usuario.grid(row=2, column=0)

        self.etiqueta_clave = tk.Label(self, text='Clave    ', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_clave.grid(row=3, column=0)
 
        self.etiqueta_email = tk.Label(self, text='Email    ', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_email.grid(row=4, column=0)

        estilo = ttk.Style()
        estilo.configure('MyEntry.TEntry', padding=3)
        self.entrada_nombre = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_nombre.grid(row=0, column=1)

        self.entrada_apellido = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_apellido.grid(row=1, column=1)

        self.entrada_usuario = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_usuario.grid(row=2, column=1)

        self.entrada_clave = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_clave.grid(row=3, column=1)

        self.entrada_email = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_email.grid(row=4, column=1)

        self.boton_registrar = tk.Button(self, text='Registrar', bg='pink',
                                             width=25, height=2, font=('arial',8), 
                                             cursor='hand2', 
                                             command=lambda: self.enviar_datos(
                                                 self.entrada_nombre.get(),
                                                 self.entrada_apellido.get(),
                                                 self.entrada_usuario.get(),
                                                 self.entrada_clave.get(),
                                                 self.entrada_email.get()
                                             ))
        self.boton_registrar.grid(row=5, column=0, columnspan=2, pady=10)

    def enviar_datos(self, nombre, apellido, usuario, clave, email):
        try:
            if Conexion.CONEXION:
                print('Hay conexion')
                self.cursor = Conexion.CONEXION.cursor()
                query = "INSERT INTO administradores(nombre, apellido, usuario, clave, email) VALUES(%s,%s,%s,%s,%s)"
                valores = (nombre, apellido, usuario, clave, email)
                print(self.cursor.execute(query, valores))
                Conexion.CONEXION.commit()
                Conexion.CONEXION.close()
                messagebox.showinfo(title='Mensaje', message='Administrador registrado con éxito')
                self.destroy()
        except Exception:
            print(f'Error: {Exception}')


if __name__ == '__main__':
    ventana = RegistrarAdmin()
    ventana.mainloop()
    