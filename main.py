from datetime import datetime #Libreria para darle un formato adecuado a las fechas

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
            opcion = int(input("Ingresa la opción (1-6): ")) #Se ingresa el número de la opción
            print("------------------------------------------------------------------")
            if 1 <= opcion <= 6: #verifica que la opción se encuentre dentro de las que se tiene
                return opcion
            print("Por favor ingresa un número entre 1 y 6")
        except ValueError:
            print("Por favor ingresa un valor válido")

def ingresoDeAlimento(): #Función para ingresar alimentos
    while True: #Ciclo while para ingresar el nombre hasta que sea correcto (sin espacio)
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
                print("La cantidad NO puede ser menor a 0")
                continue #Se reinicia el ciclo
            break

        except ValueError:
            print("Por favor ingresa un número válido para la cantidad") #Para que solo se ingresen números
            continue

    while True: #Ciclo while para ingresar la fecha de caducidad en formato adeacuado
        try:
            print(f"Alimento: {nombreAlimento}")
            print(f"Cantidad: {cantidad}")
            fechaStr = input("Ingresa la fecha de caducidad (DD/MM/YYYY): ")
            fechaCaducidad = datetime.strptime(fechaStr, "%d/%m/%Y") #Transforma el str al formato de la lireria datetime
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

    alimentos.append(nuevoAlimento) #El nuevo alimento se anida en la lista de alimentos
    print("------------------------------------------------------------------")
    print(f"¡Alimento agregado exitosamente!") #muestra los datos del nuevo alimento agregado
    print(f"Nombre: {nombreAlimento}")
    print(f"Cantidad: {cantidad}")
    print(f"Fecha de caducidad: {fechaCaducidad.strftime('%d/%m/%Y')}")
    print("------------------------------------------------------------------")

def eliminarAlimento(): #Función para eliminar un alimento
    if not alimentos:
        print("No hay alimentos en la lista")
        print("------------------------------------------------------------------")
        return

    print("Alimentos disponibles:")
    alimentosOrdenados = sorted(alimentos, key=lambda x: x['Nombre']) #ordena alimentos por orden alfabético
    for i, alimento in enumerate(alimentosOrdenados, 1): #Por cada alimento en la lista de los alimentos ordenados se enumera empezando con 1
        print(f"Lote {i}. {alimento['Nombre']} - Cantidad: {alimento['Cantidad']} - "
              f"Fecha de caducidad: {alimento['FechaCaducidad'].strftime('%d/%m/%Y')}")
    print(f"{len(alimentosOrdenados) + 1}. Cancelar eliminar") #Suma uno a la longitud de alimentos ordenados para mostrar la opción de cancelar

    while True:  # Bucle para volver a pedir la selección si hay error
        try:
            seleccionado = int(input(
                "Ingresa el número del alimento a eliminar: ")) - 1  # Se resta menos uno porque en python se enumera desde 0

            if seleccionado == len(alimentosOrdenados):
                print("No se eliminó ningún alimento")
                print("------------------------------------------------------------------")
                return

            if 0 <= seleccionado < len(alimentosOrdenados):  # Sí está dentro de 0 a la lista de alimentos
                alimentoAEliminar = alimentosOrdenados[seleccionado]  # El número del alimento que se va a eliminar

                while True:  # Ingresa la cantidad a eliminar
                    try:
                        cantidadAEliminar = int(input(
                            f"¿Cuántas unidades de {alimentoAEliminar['Nombre']} deseas eliminar? (disponibles: {alimentoAEliminar['Cantidad']}): "))  # Te pide la cantidad de alimentos que se va a eliminar
                        print("------------------------------------------------------------------")

                        if cantidadAEliminar <= 0:  # Que la cantidad no sea menor a 0
                            print("La cantidad debe ser mayor a 0")
                            continue

                        if cantidadAEliminar > alimentoAEliminar['Cantidad']:  # Que la cantidad no sea mayor a las unidades que se tiene
                            print(f"No hay suficientes unidades. Solo hay {alimentoAEliminar['Cantidad']} disponibles")
                            continue

                        if cantidadAEliminar == alimentoAEliminar['Cantidad']:  # se elimina por completo el alimento
                            alimentos.remove(alimentoAEliminar)
                            print(f"Alimento '{alimentoAEliminar['Nombre']}' eliminado completamente!")
                            print("------------------------------------------------------------------")
                        else:
                            alimentoAEliminar['Cantidad'] -= cantidadAEliminar  # Se eliminan las unidades pedidas
                            print(f"Se eliminaron {cantidadAEliminar} unidades de '{alimentoAEliminar['Nombre']}'")
                            print(f"Quedan {alimentoAEliminar['Cantidad']} unidades")
                            print("------------------------------------------------------------------")

                        return  # Sale de la función después de una eliminación exitosa

                    except ValueError:
                        print("Por favor ingresa un número válido")

            else:
                print("Número de alimento inválido")
                continue

        except ValueError:
            print("Por favor ingresa un valor válido")
            continue

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
    alimentosProximos = [] #Proximos a caducar
    alimentosCaducados = [] #Ya caducados

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
        for alimento, dias in alimentosProximos:  #Por cada alimento en días próximos
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
                  f"Lleva caducado {abs(dias)} días")  # abs() para mostrar días en positivos
    else:
        print("No hay alimentos caducados")
    print("------------------------------------------------------------------")

def ReporteCompleto(): #Reporte general d etodos los alimentos
    if not alimentos:
        print("No hay alimentos en la lista")
        return

    print("=== Reporte Completo de Alimentos ===")
    print(f"Total de alimentos diferentes: {len(alimentos)}") #Muestra que tanta variedad hay de alimentos
    print("------------------------------------------------------------------")
    print("--Detalle de alimentos--") #Muestra el reporte de cantidad y estado
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
        opcion = Menu()
        if opcion == 1:
            ingresoDeAlimento()
        elif opcion == 2:
            eliminarAlimento()
        elif opcion == 3:
            mostrarAlimentos()
        elif opcion == 4:
            alimentosPorCaducar()
        elif opcion == 5:
            ReporteCompleto()
        elif opcion == 6:
            print("¡Gracias por usar WasteSaver!")
            print("Espero vernos pronto.")
            break

    except ValueError:
        print("Ingresa una opción válida.")
