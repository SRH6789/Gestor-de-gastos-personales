# Gestor de gastos personales (versión con match/case)

gastos = []  # Lista para guardar los gastos


def mostrar_menu():
    print("\n=== GESTOR DE GASTOS PERSONALES ===")
    print("1. Agregar gasto")
    print("2. Ver lista de gastos")
    print("3. Eliminar gasto")
    print("4. Ver total gastado")
    print("5. Salir")


def agregar_gasto():
    descripcion = input("Descripción del gasto: ")
    try:
        monto = float(input("Monto ($): "))
    except ValueError:
        print("El monto debe ser un número.")
        return
    gastos.append({"descripcion": descripcion, "monto": monto})
    print("Gasto agregado correctamente.")


def ver_gastos():
    if not gastos:
        print("No hay gastos registrados.")
        return
    print("\n--- Lista de gastos ---")
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. {gasto['descripcion']} - ${gasto['monto']:.2f}")


def eliminar_gasto():
    ver_gastos()
    if not gastos:
        return
    try:
        indice = int(input("Número del gasto a eliminar: "))
        if 1 <= indice <= len(gastos):
            eliminado = gastos.pop(indice - 1)
            print(f"Gasto eliminado: {eliminado['descripcion']}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Ingresa un número válido.")


def total_gastos():
    total = sum(gasto['monto'] for gasto in gastos)
    print(f"Total gastado: ${total:.2f}")


# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")

    match opcion:
        case "1":
            agregar_gasto()
        case "2":
            ver_gastos()
        case "3":
            eliminar_gasto()
        case "4":
            total_gastos()
        case "5":
            print("Saliendo del gestor. Hasta luego.")
            break
        case _:
            print("Opción inválida. Intenta de nuevo.")
