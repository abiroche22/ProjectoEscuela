"""Archivo que tiene como funcionalidad recuperar datos del perfil del Administrador"""

import tkinter as tk
from tkinter import Tk, ttk, messagebox
from Conexion import Conexion

class Perfil(tk.Tk):
    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        super().__init__()
        self.title('Perfil del Administrador')
        self.geometry('320x400+550+180')
        self.resizable(0,0)
        self.config(bg='black')
        self.widgets_principales()
        self.obtener_registro()

    def widgets_principales(self):
        self.etiqueta_id = tk.Label(self, text='ID        ', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_id.grid(row=0, column=0)

        self.etiqueta_nombre = tk.Label(self, text='Nombre', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_nombre.grid(row=1, column=0)

        self.etiqueta_apellido = tk.Label(self, text='Apellido', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_apellido.grid(row=2, column=0)

        self.etiqueta_usuario = tk.Label(self, text='Usuario ', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_usuario.grid(row=3, column=0)

        self.etiqueta_clave = tk.Label(self, text='Clave    ', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_clave.grid(row=4, column=0)
 
        self.etiqueta_email = tk.Label(self, text='Email    ', bg='black', fg='white', 
                                   font=('arial',18, 'bold'), width=10, height=2)
        self.etiqueta_email.grid(row=5, column=0)

        estilo = ttk.Style()
        estilo.configure('MyEntry.TEntry', padding=3)
        self.entrada_id = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_id.grid(row=0, column=1)
        
        self.entrada_nombre = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_nombre.grid(row=1, column=1)

        self.entrada_apellido = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_apellido.grid(row=2, column=1)

        self.entrada_usuario = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_usuario.grid(row=3, column=1)

        self.entrada_clave = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_clave.grid(row=4, column=1)

        self.entrada_email = ttk.Entry(self, width=20, justify=tk.CENTER, cursor='hand2',
                                    font=('arial',10), style='MyEntry.TEntry')
        self.entrada_email.grid(row=5, column=1)

    
    def obtener_registro(self):
        try:
            if Conexion.CONEXION:
                self.cursor = Conexion.CONEXION.cursor()
                query = 'SELECT * FROM administradores WHERE usuario=%s AND clave=%s'
                valores = (self.usuario, self.clave)
                self.cursor.execute(query, valores)
                registro = self.cursor.fetchone()
                if registro:
                    self.entrada_id.insert(0, registro[0])
                    self.entrada_nombre.insert(0, registro[1])
                    self.entrada_apellido.insert(0, registro[2])
                    self.entrada_usuario.insert(0, registro[3])
                    self.entrada_clave.insert(0, registro[4])
                    self.entrada_email.insert(0, registro[5])
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error al recuperar los datos')

if __name__ == '__main__':
    ventana = Perfil()
    ventana.mainloop()