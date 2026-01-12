from app.services.gastos_service import (crear_gasto, mostrar_gastos, eliminar_gasto, obtener_gastos_por_categoria, actualizar_gasto)


def menu():

    print("1. crear gasto \n"
    "2. mostrar gasto \n"
    "3. eliminar gasto \n"
    "4. obtener gasto por categoria \n"
    "5. actualizar gasto")

    opc = int(input("ingrese una opcion: "))

    if opc == 1:
        categoria = input("ingrese una categoria: ")
        cantidad = int(input("ingrese la cantidad gastada: "))
        descrpcion = input("ingrese la descripcion: ")
        date = input("ingrese la fecha: YYYY-MM-DD: ")

        print(crear_gasto(categoria, cantidad, descrpcion, date))

    elif opc == 2:
        print(mostrar_gastos())



print(menu())


