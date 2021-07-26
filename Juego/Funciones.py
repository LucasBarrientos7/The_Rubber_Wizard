from principal import *
from configuracion import *
import random
import math



def lectura(archivo, salida):

    palabraAux=""
    Aux=""
    logn=archivo.readlines()

    for palabraAux in logn:

        for letra in palabraAux:
           if letra!="\n":
            Aux=Aux+letra
        salida.append(Aux)
        Aux=""
    archivo.close()

def nuevaPalabra(silabas):
    palabra=0
    palabra=random.randrange(len(silabas))
    return silabas[palabra]

def silabasTOpalabra(silaba):
    palabra=""
    for i in silaba:
        if (i!="-"):
            palabra=palabra+i
    return palabra

#Opcional
def palabraTOsilaba(palabra):
    nueva=separador(palabra)
    return nueva


def dameUltimaSilaba(enSilabas):
    ultimaSilaba=""
    for letra in (enSilabas):
        if (letra=="-"):
            ultimaSilaba=""
        else:
            ultimaSilaba=ultimaSilaba+letra
    return ultimaSilaba

def damePrimeraSilaba(enSilabas):
    primeraSilaba=""
    for letra in (enSilabas):
            if (letra=="-"):
                return primeraSilaba
            else:
                primeraSilaba=primeraSilaba+letra

def esValida(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario):

    ultSilabaPalabra= dameUltimaSilaba(palabraEnSilabas)
    primSilabaUsuario=damePrimeraSilaba(palabraUsuarioEnSilabas)
    for elem in listaPalabrasDiccionario:
        if elem == palabraUsuario:
            if (ultSilabaPalabra==primSilabaUsuario):
                return True
            else:
                pygame.mixer.Sound("Shao.MP3")
                return False

    return False

def Puntos(palabraUsuario,Valido):
    if Valido:
        return 2**(len(dameUltimaSilaba(palabraUsuario)))
    else:
        return -1*(len(palabraUsuario))

def procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario):
    if esValida(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario):
        return Puntos(palabraUsuario,True)
    else:
        return Puntos(palabraUsuario,False)

#opcional
def buscarPalabraQueEmpieceCon(silaba,lemarioEnSilabas):
    for palabra in lemarioEnSilabas:
        if silaba==damePrimeraSilaba(palabra):
            return silabasTOpalabra(palabra)

    aleatoria=random.randint(0,len(lemarioEnSilabas)-1)
    azar=silabasTOpalabra(lemarioEnSilabas[aleatoria])
    Self.risa=pygame.mixer.Sound("Shao.MP3")
    return(azar)
