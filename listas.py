##Autor: David Medina Medina A01653311
##Tarea 8 completa, listas.

from random import *

def sumarAcumulado(lista):
    a = 0
    listab = []
    for i in lista:
        a +=i
        listab.append(a)
    return listab


def recortarLista(lista):
    listaR = lista[1:len(lista)-1]
    return listaR


def estanOrdenados(lista):
    for k in range(0, len(lista) - 1):
        if lista[k]>lista[k+1]:
            return False
    return True


def sonAnagramas(lista1, lista2):
    if len(lista1) == len(lista2):
        a = 0
        for k in lista1:
            if k in lista2:
                a +=1
        if a == len(lista1):
            return True
        else:
            return False
    else:
        return False


def hayDuplicados(lista):
    a = 0
    for i in lista:
        lista.count(i)
        if lista.count(i)>1:
            a +=1

    if a == 0:
        return False
    else:
        return True


def borrarDuplicados(lista):
    for i in lista:
        lista.count(i)
        if lista.count(i)>1:
            lista.remove(i)
    return lista


def main():

    #1
    print("Ejercicio 1: Sumar Acumulado:")
    lista1 = [1, 2, 3, 4, 5]
    lista2s = []
    lista3s = [5]
    print("La lista:", lista1,"regresa la lista acumulada:", sumarAcumulado(lista1))
    print("La lista:", lista2s,"regresa la lista acumulada:", sumarAcumulado(lista2s))
    print("La lista:", lista3s,"regresa la lista acumulada:", sumarAcumulado(lista3s))


    #2
    print("\nEjercicio 2: Recortar listas:")
    lista = [1,2,3,4,5]
    lista2r = [3,4,5,6,7,8,9]
    lista3r = []
    print ("Lista original:", lista, "Lista recortadada:", recortarLista(lista))
    print("Lista original:", lista2r, "Lista recortadada:", recortarLista(lista2r))
    print("Lista original:", lista3r, "Lista recortadada:", recortarLista(lista3r))


    #3
    print("\nEjercicio 3: Orden de listas:")
    listaOrdenados1 = [randint(0,233),randint(0,233),randint(0,233)]
    listaOrdenados2 = [randint(0, 233), randint(0, 233), randint(0, 233)]
    listaOrdenados3 = [randint(0, 233), randint(0, 233), randint(0, 233)]
    print ("Lista original:",listaOrdenados1,"Lista ordenada:", estanOrdenados(listaOrdenados1))
    print("Lista original:", listaOrdenados2, "Lista ordenada:", estanOrdenados(listaOrdenados2))
    print("Lista original:", listaOrdenados3, "Lista ordenada:", estanOrdenados(listaOrdenados3))


    #4
    print("\nEjercicio 4: Anagramas:")
    lista1Anagramas = list("roma")
    lista2Anagramas =list("amor")
    lista1Anagramas1 = list("zapato")
    lista2Anagramas2 = list("bote")
    lista1Anagramas3 = list("oso")
    lista2Anagramas3 = list("oso")
    sonAnagramas(lista1Anagramas,lista2Anagramas)
    print("Cadenas :", lista1Anagramas, ",", lista2Anagramas,"Es anagrama:", sonAnagramas(lista1Anagramas,lista2Anagramas))
    print("Cadenas :", lista1Anagramas1, ",",lista2Anagramas2, "Es anagrama:", sonAnagramas(lista1Anagramas1,lista2Anagramas2))
    print("Cadenas :", lista1Anagramas3, ",", lista2Anagramas3, "Es anagrama:", sonAnagramas(lista1Anagramas3, lista2Anagramas3))

    #5
    print("\nEjercicio 5: Detectar repetidos:")
    lista1Dup = [1,2,3,4,5,6,2,3,4,5]
    lista2Dup = [1,2,3,4,5]
    lista3Dup = [2,2,2]
    hayDuplicados(lista1Dup)
    print("Lista:", lista1Dup, "Hay repetidos:", hayDuplicados(lista1Dup))
    print("Lista:", lista2Dup, "Hay repetidos:", hayDuplicados(lista2Dup))
    print("Lista:", lista3Dup, "Hay repetidos:", hayDuplicados(lista3Dup))

    #6
    print("\nEjercicio 6: Borrar repetidos:")
    lista1Bor = [1,8,3,4,3,1,8,2,7,8]
    lista2Bor = [1,1,2,2,3,3]
    lista3Bor = [2,3,5,4,2,4,4,7,8,8]
    print("Lista original con duplicados: ", lista1Bor,"=")
    print("Lista sin duplicados: ", borrarDuplicados(lista1Bor))
    print("Lista original con duplicados: ", lista2Bor,"=")
    print("Lista sin duplicados: ", borrarDuplicados(lista2Bor))
    print("Lista original con duplicados: ", lista3Bor,"=" )
    print("Lista sin duplicados: ", borrarDuplicados(lista3Bor))

main()


