import random
import string

from lemario import palabras
from diagrama import vidas_diagrama


def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()



def ahorcado():
    print("====================")
    print("Bienvenido al juego del Ahorcado!")
    print("====================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra) # serara las letras. ej: {'c', 'a', 's', 'i', 'n', 'o'}
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas >0:
        print (f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #Muestra el estado actual de la palabra:
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra] # List Comprehenision
        print(vidas_diagrama[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra {letra_usuario} no esta en la palabra.\n")
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Escoge una letra nueva.\n")
        else:
            print("\nEsta letra no es valida.")
    # El juego llega a esta linea cuando se adivinan las letras de la palabra o ya no tiene vidas
    if vidas == 0:
        print(vidas_diagrama[vidas])
        print(f"Ahorcado! Perdiste la palabra era {palabra}.\n")
    else:
        print(f"Ganaste! adivinaste la palabra {palabra}!.\n")
    

ahorcado()