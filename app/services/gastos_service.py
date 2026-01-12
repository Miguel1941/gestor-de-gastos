
# este arhcivo solo tendra las funciones base sin pedirle al usuario nada

from app.db.conexion import conectar

def crear_gasto(categoria, cantidad, descripcion, fecha):
    conn = conectar()   # funcion de conexion.py conecta el codigo con el database
    cursor = conn.cursor() # este linea es el intermedario de conectar el codigo con el database
    
    # comando de mysql
    sql = """
    INSERT INTO tipo_gasto (categoria, cantidad, descripcion, fecha)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (categoria, cantidad, descripcion, fecha))  # ejecuta comando de mysql usando los valores validos
    conn.commit()   # se encarga de guardar los cambios echos en la consulta 

    cursor.close()  # se cierra el cursor
    conn.close()   # se cierra la coneccion con el database


def mostrar_gastos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tipo_gasto") # comando de mysql
    gastos = cursor.fetchall()

    cursor.close()
    conn.close()

    return gastos


def eliminar_gasto(gasto_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tipo_gasto WHERE id = %s", (gasto_id,)) # comando de mysql
    conn.commit()

    cursor.close()
    conn.close()


def obtener_gastos_por_categoria(categoria):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "select * from tipo_gasto WHERE categoria = %s", #comando de mysql
        (categoria,)
    )
    gastos = cursor.fetchall()

    cursor.close()
    conn.close()

    return gastos


def actualizar_gasto(gasto_id, categoria, cantidad, descripcion, fecha):
    conn = conectar()
    cursor = conn.cursor()
    
    # comando de mysql
    sql = """
    UPDATE tipo_gasto
    SET categoria=%s, cantidad=%s, descripcion=%s, fecha=%s
    WHERE id=%s
    """
    cursor.execute(sql, (categoria, cantidad, descripcion, fecha, gasto_id))
    conn.commit()

    cursor.close()
    conn.close()
