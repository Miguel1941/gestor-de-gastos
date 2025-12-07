

import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root1234!",   # si tienes contraseña, colócala aquí
        database="gestor_gastos"
    )

    if conexion.is_connected():
        print("Conexión exitosa a MySQL!")

except Exception as e:
    print("Error al conectar:", e)
