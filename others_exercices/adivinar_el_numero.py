import random

print("=============================================")
print(" Bienvenido al juego! ")
print("=============================================")
print("Tu meta es adivinar el numero generado por computadora.")
limite = int(input("Ingrese el numero limite: "))

def guess_my_number(limite): #entre el numero 0 y el numero "x"
 numero_aleatorio = random.randint(1, limite)
 prediccion = 0

 while prediccion != numero_aleatorio:
        # El usuario ingresa un numero:
        prediccion = int(input(f"Adivina un numero entre el valor 1 y el valor {limite}: "))
        if prediccion < numero_aleatorio:
            print("Intenta otra vez, el numero es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez, el numero es muy grande.")
 print(f"Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente!")

guess_my_number(limite)