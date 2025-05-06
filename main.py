from datetime import datetime #Libreria para darle un formato adecuado a las fecehas

alimentos = [] #Lista que ingresara cada nuevoAlimento ingresado

def Menu(): #función de menú
    print("--- WasteSaver Menu ---")
    print("1. Ingresar alimento")
    print("2. Eliminar alimento")
    print("3. Revisar lista de alimentos")
    print("4. Alimentos a caducar")
    print("5. Reporte completo de alimentos")
    print("6. Salir")

    while True:
        try:
            Opcion = int(input("Ingresa la opción (1-6): ")) #Verifica que se encuentre dentro del rango de respuesta
            print("------------------------------------------------------------------")
            if 1 <= Opcion <= 6:
                return Opcion
            print("Por favor ingresa un número entre 1 y 6")
        except ValueError:
            print("Por favor ingresa un valor válido")

def ingresoDeAlimento():
    while True: #Ciclo while para ingresar el nombre hasta que este correcto
        nombreAlimento = input("Ingresa el alimento: ").strip().upper()
        if nombreAlimento == "":
            print("No puedes dejar un espacio en blanco")
            continue
        break

    while True: #Ciclo while para ingresar la cantidad en formato correcto (no letras)
        try:
            print(f"Alimento: {nombreAlimento}")
            cantidad = int(input("Ingresa la cantidad de alimentos: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido para la cantidad")
            continue

    while True: #Ciclo while para ingresar la fecha de caducidad en formato adeacuado
        try:
            print(f"Alimento: {nombreAlimento}")
            print(f"Cantidad: {cantidad}")
            fechaStr = input("Ingresa la fecha de caducidad (DD/MM/YYYY): ")
            fechaCaducidad = datetime.strptime(fechaStr, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha inválido. Usa DD/MM/YYYY")
            continue

    # Creamos un diccionario para agregar el alimento y sus características
    nuevoAlimento = {
        'Nombre': nombreAlimento,
        'Cantidad': cantidad,
        'FechaCaducidad': fechaCaducidad
    }

    alimentos.append(nuevoAlimento) #El nuevoalimento se anida en la lista de alimentos
    print("------------------------------------------------------------------")
    print(f"¡Alimento agregado exitosamente!")
    print(f"Nombre: {nombreAlimento}")
    print(f"Cantidad: {cantidad}")
    print(f"Fecha de caducidad: {fechaCaducidad.strftime('%d/%m/%Y')}")
    print("------------------------------------------------------------------")


def eliminarAlimento():
    if not alimentos:
        print("No hay alimentos en la lista")
        return
        print("------------------------------------------------------------------")

    print("Alimentos disponibles:")
    alimentosOrdenados = sorted(alimentos, key=lambda x: x['Nombre']) #ordena alimentos por orden alfabético
    for i, alimento in enumerate(alimentosOrdenados, 1): #Por cada alimento en la lista de los alimentos ordenados se enumera empezando con 1
        print(f"Lote {i}. {alimento['Nombre']} - Cantidad: {alimento['Cantidad']} - "
              f"Fecha de caducidad: {alimento['FechaCaducidad'].strftime('%d/%m/%Y')}")

    try:
        seleccionado = int(input("Ingresa el número del alimento a eliminar: ")) - 1
        if 0 <= seleccionado < len(alimentosOrdenados):
            alimentoAEliminar = alimentosOrdenados[seleccionado]

            while True: #Ingresa la cantidad a eliminar
                try:
                    cantidadAEliminar = int(input(f"¿Cuántas unidades de {alimentoAEliminar['Nombre']} deseas eliminar? (disponibles: {alimentoAEliminar['Cantidad']}): "))
                    print("------------------------------------------------------------------")

                    if cantidadAEliminar <= 0: #Que la cantidad no sea menor a 0
                        print("La cantidad debe ser mayor a 0")
                        continue

                    if cantidadAEliminar > alimentoAEliminar['Cantidad']: #Que la cantidad no sea mayor a las unidades que se tiene
                        print(f"No hay suficientes unidades. Solo hay {alimentoAEliminar['Cantidad']} disponibles")
                        continue

                    if cantidadAEliminar == alimentoAEliminar['Cantidad']: #se elimina
                        alimentos.remove(alimentoAEliminar)
                        print(f"Alimento '{alimentoAEliminar['Nombre']}' eliminado completamente!")

                    else:
                        alimentoAEliminar['Cantidad'] -= cantidadAEliminar #Se eliminan las unidades pedidas
                        print(f"Se eliminaron {cantidadAEliminar} unidades de '{alimentoAEliminar['Nombre']}'")
                        print(f"Quedan {alimentoAEliminar['Cantidad']} unidades")
                    break

                except ValueError:
                    print("Por favor ingresa un número válido")

        else:
            print("Número de alimento inválido")
    except ValueError:
        print("Por favor ingresa un número válido")
    print("------------------------------------------------------------------")


def mostrarAlimentos(): #muestra la lista de alimentos
    if not alimentos:
        print("No hay alimentos en la lista")
        return
        print("------------------------------------------------------------------")

    print("Lista de alimentos:")
    alimentosOrdenados = sorted(alimentos, key=lambda x: x['Nombre'])
    for i, Alimento in enumerate(alimentosOrdenados, 1):
        print(f"Lote {i}. {Alimento['Nombre']} - Cantidad: {Alimento['Cantidad']} - "
              f"Caducidad: {Alimento['FechaCaducidad'].strftime('%d/%m/%Y')}")
    print("------------------------------------------------------------------")

def alimentosPorCaducar():
    if not alimentos:
        print("No hay alimentos en la lista")
        print("------------------------------------------------------------------")
        return

    hoy = datetime.now() #Obtiene la fecha de hoy
    alimentosProximos = []
    alimentosCaducados = []

    for alimento in alimentos: #por cada alimento se obtiene los días restantes
        diasRestantes = (alimento['FechaCaducidad'] - hoy).days #Se busca la diferencia de días
        if diasRestantes <= 7 and diasRestantes >= 0: #Si esta a 7 días de caducarse
            alimentosProximos.append((alimento, diasRestantes))  # Guardamos el alimento y sus días
        elif diasRestantes < 0:
            alimentosCaducados.append((alimento, diasRestantes))  # Guardamos el alimento y sus días

    if alimentosProximos: #Muestra alimentos que están próximos a caducar
        print("Alimentos próximos a caducar (7 días o menos):")
        # Ordenar por nombre del alimento (que está en la posición 0 de la tupla)
        alimentosProximos.sort(key=lambda x: x[0]['Nombre'])
        for alimento, dias in alimentosProximos:
            print(f"- {alimento['Nombre']} - Cantidad: {alimento['Cantidad']} - "
                  f"Caduca en {dias} días")
    else:
        print("No hay alimentos próximos a caducar")
    print("------------------------------------------------------------------")

    if alimentosCaducados: #Muestra los alimentos que ya caducaron
        print("Alimentos caducados:")
        # Ordenar por nombre del alimento (que está en la posición 0 de la tupla)
        alimentosCaducados.sort(key=lambda x: x[0]['Nombre'])
        for alimento, dias in alimentosCaducados:
            print(f"- {alimento['Nombre']} - Cantidad: {alimento['Cantidad']} - "
                  f"Lleva caducado {abs(dias)} días")  # abs() para mostrar días positivos
    else:
        print("No hay alimentos caducados")
    print("------------------------------------------------------------------")

def ReporteCompleto(): #Reporte general d etodos los alimentos
    if not alimentos:
        print("\nNo hay alimentos en la lista")
        return

    print("=== Reporte Completo de Alimentos ===")
    print(f"Total de alimentos diferentes: {len(alimentos)}") #Muestra que tanta variedad hay
    print("------------------------------------------------------------------")
    print("Detalle de alimentos:") #Muestra el reporte de cantidad y estado
    alimentosOrdenados = sorted(alimentos, key=lambda x: x['Nombre'])
    for Alimento in alimentosOrdenados:
        diasRestantes = (Alimento['FechaCaducidad'] - datetime.now()).days
        # Da el estado en el que se encuentra la comida
        if 0 <= diasRestantes <= 7:
            estado  = "Próximo a caducar"
        elif diasRestantes < 0:
            estado = "Caducado"
        else:
            estado = "Normal"

        print(f"Nombre: {Alimento['Nombre']}")
        print(f"Cantidad: {Alimento['Cantidad']}")
        print(f"Fecha de caducidad: {Alimento['FechaCaducidad'].strftime('%d/%m/%Y')}")
        print(f"Días restantes: {diasRestantes}")
        print(f"estado: {estado}")
        print("------------------------------------------------------------------")

# Loop principal
while True:
    try:
        Opcion = Menu()
        if Opcion == 1:
            ingresoDeAlimento()
        elif Opcion == 2:
            eliminarAlimento()
        elif Opcion == 3:
            mostrarAlimentos()
        elif Opcion == 4:
            alimentosPorCaducar()
        elif Opcion == 5:
            ReporteCompleto()
        elif Opcion == 6:
            print("¡Gracias por usar WasteSaver!")
            print("Espero vernos pronto.")
            break
    except ValueError:
        print("Ingresa una opción válida.")
