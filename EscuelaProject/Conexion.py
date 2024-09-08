"""Archivo que tendrá funcionalidad conectarse a la base de datos."""

import mysql.connector

class Conexion:
        CONEXION = mysql.connector.connect(user='admin', password='admin',
                                        host='localhost', database='escuela_bd')
        
        print(f'Conexion exitosa: {CONEXION}')

if __name__ == '__main__':
    conexion = Conexion()
    