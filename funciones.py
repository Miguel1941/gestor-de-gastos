
from conexion import conectar

def insertar_gasto():
    categoria = input("Categoría: ")
    cantidad = float(input("Cantidad: "))
    descripcion = input("Descripción: ")
    fecha = input("Fecha (YYYY-MM-DD): ")

    conn = None
    cursor = None

    try:
        conn = conectar()          
        cursor = conn.cursor()     

        sql = """
        INSERT INTO tipo_gasto (categoria, cantidad, descripcion, fecha)
        VALUES (%s, %s, %s, %s)
        """

        valores = (categoria, cantidad, descripcion, fecha)

        cursor.execute(sql, valores)
        conn.commit()               

        print("Gasto insertado correctamente.")

    except Exception as e:
        print("Error al insertar el gasto:", e)

    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    insertar_gasto()

