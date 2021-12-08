import random
import time


def busqueda_ingenua(lista, target):
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1


# Solo sirve para listas ordenadas:
def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior= None):
    if limite_inferior is None:
        limite_inferior = 0
    if limite_superior is None:
        limite_superior = len(lista) - 1
    
    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_inferior + limite_superior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio +1, limite_superior)


if __name__=='__main__':
    #Crear una lista ordenada con 10000 numeros aleatorios
    tamanio = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamanio:
        conjunto_inicial.add(random.randint(-3*tamanio, 3*tamanio))
    
    lista_ordenada = sorted(list(conjunto_inicial))

    # Medicion tiempo de busqueda ingenua:
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Busqueda Ingenua: {fin - inicio} segundos.")

    # Medicion tiempo de busqueda binaria:
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Busqueda Binaria: {fin - inicio} segundos.")