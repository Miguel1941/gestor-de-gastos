
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

def mostrar_gastos():

    conn = None
    cursor = None

    try:
        conn = conectar()          
        cursor = conn.cursor()

        cursor.execute("select * from tipo_gasto;")
        resultados = cursor.fetchall()
        print(resultados)


    except Exception as e:
        print("Error al mostrar los gastos:", e)

    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def eliminar_gasto():

    conn = None
    cursor = None

    try:
        conn = conectar()          
        cursor = conn.cursor()

        mostrar_gastos()

        id = int(input("ingrese el id del gasto que desea eliminar: "))

        cursor.execute(f"delete from tipo_gasto where id = {id};")
        conn.commit()

        print("gasto eliminado correctamente")



    except Exception as e:
        print("Error al eliminar: ",e)

    
    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def menu():
    print("1. añadir un gasto")
    print("2. mostrar gastos añadidios")
    print("3. eliminar gasto")
    opc = int(input("eliga una opcion: "))

    if opc == 1:
        insertar_gasto()
    elif opc == 2:
        mostrar_gastos()
    elif opc == 3:
        eliminar_gasto()
    else:
        print("eliga una opcion valida")

if __name__ == "__main__":
    menu()

