from datetime import datetime
alimento = ()
cantidad = ()
fechaDeCaducidad =()
alimentos = [(alimento),(cantidad),(fechaDeCaducidad)]

def menu(): #Función de despliegue del menú
    print("\n--- WasteSaver Menu ---")
    print("1. Ingresar alimento")
    print("2. Eliminar alimento")
    print("3. Revisar lista de alimentos")
    print("4. Alimentos a caducar")
    print("5. Reporte completo de alimentos")
    print("6. Salir")

    while True:
        try:
            opcion = int(input("Ingresa la opción (1-6): ")).strip()
            if 1 <= opcion <= 6:
                return opcion
            print("Por favor ingresa un número entre 1 y 6")
        except ValueError:
            print("Por favor ingresa un número válido")

def ingreso_de_alimento(): # Función para ingresar un alimento
    while True:
        alimento = input("Ingresa el alimento: ").strip().upper()
        if alimento == "":
            print("No puedes dejar un espacio en blanco")
            continue
        try:
            cantidad = int(input("Ingresa la cantidad de alimentos: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                continue

            try:
                fecha_str = input("Ingresa la fecha de caducidad (DD/MM/YYYY): ")
                fecha_caducidad = datetime.strptime(fecha_str, "%d/%m/%Y")

                alimentos.append({alimento})

                alimentos.append(nuevo_alimento)
                print(f"\nAlimento '{alimento}' agregado exitosamente!")
                break

            except ValueError:
                print("Formato de fecha inválido. Use DD/MM/YYYY")
                continue

        except ValueError:
            print("Por favor ingresa un número válido para la cantidad")
            continue

def eliminar_alimento():
    if not alimentos:
        print("\nNo hay alimentos en la lista")
        return

    print("\nAlimentos disponibles:")
    for i, alimento in enumerate(alimentos, 1):
        print(f"{i}. {alimento['nombre']} - Cantidad: {alimento['cantidad']}")

    try:
        indice = int(input("\nIngresa el número del alimento a eliminar: ")) - 1
        if 0 <= indice < len(alimentos):
            alimento_eliminado = alimentos.pop(indice)
            print(f"\limento '{alimento_eliminado['nombre']}' eliminado exitosamente!")
        else:
            print("Número de alimento inválido")
    except ValueError:
        print("Por favor ingresa un número válido")

def mostrar_alimentos():
    if not alimentos:
        print("\nNo hay alimentos en la lista")
        return

    print("\nLista de alimentos:")
    for i, alimento in enumerate(alimentos, 1):
        print(f"{i}. {alimento['nombre']} - Cantidad: {alimento['cantidad']} - "
              f"Caducidad: {alimento['fecha_caducidad'].strftime('%d/%m/%Y')}")

def alimentos_por_caducar():
    if not alimentos:
        print("\nNo hay alimentos en la lista")
        return

    hoy = datetime.now()
    alimentos_proximos = []

    for alimento in alimentos:
        diasRestantes = (alimento['fecha_caducidad'] - hoy).days
        if diasRestantes <= 7 and diasRestantes >= 0:
            alimentos_proximos.append((alimento, diasRestantes))

    if alimentos_proximos:
        print("Alimentos próximos a caducar (7 días o menos):")
        for alimento, dias in alimentos_proximos:
            print(f"- {alimento['nombre']} - Caduca en {diasRestantes} días")
    else:
        print("\nNo hay alimentos próximos a caducar")

def reporte_completo():
    print("x")
while True:
    try:
        opcion = menu()
        if opcion == 1:
            ingreso_de_alimento()
        elif opcion == 2:
            eliminar_alimento()
        elif opcion == 3:
            mostrar_alimentos()
        elif opcion == 4:
            alimentos_por_caducar()
        elif opcion == 5:
            reporte_completo()
        elif opcion == 6:
            print("¡Gracias por usar WasteSaver!")
            print("Espero vernos pronto.")
            break
    except ValueError:
        print("Ingresa una opción válida.")
