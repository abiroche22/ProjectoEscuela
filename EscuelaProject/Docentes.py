import tkinter as tk
from tkinter import Tk
from RegistrarDocente import RegistrarDocente
from ActualizarDocente import ActualizarDocente
from EliminarDocente import EliminarDocente

class Docentes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Docentes')
        self.geometry('400x220+450+180')
        self.resizable(0,0)
        self.config(bg='black')
        self.widgets_principales()

    def widgets_principales(self):
        self.boton_registrar = tk.Button(self, text='Registrar Datos', bg='pink',
                                             width=40, height=3, font=('arial',10), 
                                             cursor='hand2', command=self.registrar)
        self.boton_registrar.grid(row=0, column=0, padx=30, pady=10)

        self.boton_actualizar = tk.Button(self, text='Actualizar Datos', bg='pink',
                                             width=40, height=3, font=('arial',10), 
                                             cursor='hand2', command=self.actulizar)
        self.boton_actualizar.grid(row=1, column=0, padx=30)

        self.boton_eliminar = tk.Button(self, text='Eliminar Datos', bg='pink',
                                             width=40, height=3, font=('arial',10), 
                                             cursor='hand2', command=self.eliminar)
        self.boton_eliminar.grid(row=2, column=0, padx=30, pady=10)

    def registrar(self):
        self.destroy()
        RegistrarDocente()

    def actulizar(self):
        self.destroy()
        ActualizarDocente()

    def eliminar(self):
        self.destroy()
        EliminarDocente()

        

if __name__ == '__main__':
    ventana = Docentes()
    ventana.mainloop()
