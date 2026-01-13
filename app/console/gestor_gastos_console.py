from app.services.gastos_service import (crear_gasto, mostrar_gastos, eliminar_gasto, obtener_gastos_por_categoria, actualizar_gasto)


def menu():
    
    while True:
        print("1. crear gasto \n"
        "2. mostrar gasto \n"
        "3. eliminar gasto \n"
        "4. obtener gasto por categoria \n"
        "5. actualizar gasto \n"
        "6. salir")

        opc = int(input("ingrese una opcion: "))

        if opc == 1:
            categoria = input("ingrese una categoria: ")
            cantidad = int(input("ingrese la cantidad gastada: "))
            descrpcion = input("ingrese la descripcion: ")
            date = input("ingrese la fecha: YYYY-MM-DD: ")

            crear_gasto(categoria, cantidad, descrpcion, date)

        elif opc == 2:
            print(mostrar_gastos())

        elif opc == 3:
            gasto_id = int(input("ingrese el id del gasto que desea eliminar: "))
            eliminar_gasto(gasto_id)

        elif opc == 4:
            categoria = input("ingrese la categoria que desea obtener: ")

            obtener_gastos_por_categoria(categoria)

        elif opc == 5:
            print("ingrese los datos del gasto que desea acualizar con el mismo ID:")
            gasto_id = int(input("ingrese el id del gasto: "))
            categoria = input("ingrese una categoria: ")
            cantidad = int(input("ingrese la cantidad gastada: "))
            descrpcion = input("ingrese la descripcion: ")
            fecha = input("ingrese la fecha: YYYY-MM-DD: ")

            actualizar_gasto(gasto_id, categoria, cantidad, descrpcion, fecha)
            print("gasto actualizado correctamente")

        elif opc == 6:
            break

        else:
            print("ingrese una opcion valida")



print(menu())


