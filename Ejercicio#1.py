def imprimir_nombre(usuario, repeticion):
    if repeticion <= 0:
        return
    print(usuario)
    imprimir_nombre(usuario, repeticion - 1)

nombre_usuario = input("Ingresa tu nombre: ")
numero_repeticion = int(input("Ingresa un número entero: "))

imprimir_nombre(nombre_usuario, numero_repeticion)
