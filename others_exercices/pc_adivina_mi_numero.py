import random


def pc_adivina_mi_numero(limite):
    print("===================")
    print("Bienvenido al juego!")
    print("===================")
    print(f"Selecciona un numero entre 1 y {limite} para que la computadora intente adivinar")

    limite_inferior = 1
    limite_superior = limite

    respuesta = ""
    while respuesta != "c":
        #Generar una prediccion:
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        # Obtener una respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}. Si es mayor ingrese 'A'. Si es menor ingrese 'B'. Si es correcta, ingrese 'C'. ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"La computadora adivino tu numero {prediccion} correctamente!")


pc_adivina_mi_numero(50)

        