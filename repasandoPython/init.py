mi_Diccionario = {}
while True:
    print("Diccionario Personal")
    print("1 Agregar palabra")
    print("2 Buscar palabra")
    print("3 Salir")

    opcion = input("Selecciona una opcion: ")


    if opcion == '1':
        print("seleccionaste la opcion 1")

    elif opcion == '2':
        print("seleccionaste la opcion 2")

    elif opcion == '3': 
        print("Hasta luego!")
        break

















"""mi_diccionario = {}

while True:
    print("\nDiccionario Personal")
    print("1. Agregar palabra")
    print("2. Buscar palabra")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        palabra = input("Ingresa la palabra: ").lower()
        definicion = input("Ingresa la definición: ")
        mi_diccionario[palabra] = definicion
        print(f"'{palabra}' ha sido agregada al diccionario.")
    elif opcion == '2':
        palabra_buscar = input("Ingresa la palabra que deseas buscar: ").lower()
        if palabra_buscar in mi_diccionario:
            print(f"La definición de '{palabra_buscar}' es: {mi_diccionario[palabra_buscar]}")
        else:
            print(f"La palabra '{palabra_buscar}' no se encontró en el diccionario.")
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")"""