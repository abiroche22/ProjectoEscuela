"""Archivo que tiene como funcionalidad recuperar datos estudiantiles de grado"""

import tkinter as tk
from tkinter import Tk, ttk, messagebox
from Conexion import Conexion

class ObtenerGrado(tk.Tk):
    def __init__(self, etiqueta, query):
        self.etiqueta = etiqueta
        self.query = query
        super().__init__()
        self.title('Grado 1')
        self.geometry('680x300+350+180')
        self.resizable(0,0)
        self.config(bg='black')
        self.widgets_principales()
        self.obtener_registros()

    def widgets_principales(self):
        self.etiqueta_grado = tk.Label(self, text=self.etiqueta, bg='black', 
                                       fg='white', font=('arial',15, 'bold'), 
                                       width=20,)
        self.etiqueta_grado.grid(row=0, column=0, pady=10)

        self.frame = tk.Frame(self, bg='black')
        self.frame.grid(row=1, column=0, sticky='nswe', padx=23)

        self.vista = ttk.Treeview(self.frame, columns=('nombres', 'apellidos', 'cedula',
                                                'edad', 'seccion'))
        
        self.vista.column("#0", width=100)
        self.vista.column("nombres", width=100)
        self.vista.column("apellidos", width=100)
        self.vista.column("cedula", width=100)
        self.vista.column("edad", width=100)
        self.vista.column("seccion", width=100)

        self.vista.heading("#0", text="ID")
        self.vista.heading("nombres", text="Nombres")
        self.vista.heading("apellidos", text="Apellidos")
        self.vista.heading("cedula", text="Cédula")
        self.vista.heading("edad", text="Edad")
        self.vista.heading("seccion", text="Sección")
        self.vista.grid(row=0, column=0)

        self.scroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.vista.yview)
        self.scroll.grid(row=0, column=1, sticky='ns')

        self.vista.configure(yscrollcommand=self.scroll.set)

        
    def obtener_registros(self):
        try:
            if Conexion.CONEXION:
                self.cursor = Conexion.CONEXION.cursor()
                self.cursor.execute(self.query)
                registros = self.cursor.fetchall()
                for registro in registros:
                    self.vista.insert("", tk.END, text=registro[0], 
                                      values=(registro[1],
                                              registro[2],
                                              registro[3],
                                              registro[4],
                                              registro[5]))
        except Exception:
            messagebox.showerror(title='Mensaje', message='Error al obtener datos')
        


if __name__ == '__main__':
    ventana = ObtenerGrado()
    ventana.mainloop()
