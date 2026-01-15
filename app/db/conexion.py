

import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # contraseña de tu servidor local
        database="gestor_gastos"
    )
    return conexion


