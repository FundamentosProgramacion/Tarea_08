# Autor: José Francisco Murillo Lozano A01374561
# Tarea 8 Fundamentos de Programación

from itertools import permutations

def sumarAcumulado(lista):
    listaAcum = []
    if len(lista) > 0:
        listaAcum.append(lista[0])
        for val in range(1, len(lista)):
            acum = lista[val] + listaAcum[val-1]
            listaAcum.append(acum)
    return listaAcum


def recortarLista(lista):
    listaCrop = []
    if len(lista) >= 3:
        for val in range(1, len(lista)-1):
            listaCrop.append(lista[val])

    return listaCrop


def estanOrdenados(lista):
    contar = 1
    for val in range(1, len(lista)):
        if lista[val] >= lista[val-1]:
            contar += 1

    if contar == len(lista):
        return True
    return False


def sonAnagramas(cadena1, cadena2):
    cadena1 = list(cadena1.upper())
    cadena2 = list(cadena2.upper())
    compcadena2 = str(cadena2)

    if len(cadena1) == len(cadena2):
        for perm in permutations(cadena1, len(cadena1)):
            perm1 = str(list(perm))
            if perm1 == compcadena2:
                return True
    return False


def hayDuplicados(lista):
    for val1 in range(len(lista)):
        for val2 in range(len(lista)):
            if lista[val1] == lista[val2] and val1 != val2:
                return True
    return False


def borrarDuplicados(lista):
    lista.sort()
    val1 = 0
    val2 = 1
    if hayDuplicados(lista):
        while val2 < len(lista):
            if lista[val1] == lista[val2]:
                lista.remove(lista[val2])
                lista.insert(val2, "")
                val2 += 1
            elif val2-1 > val1:
                val1 += 1
            else:
                val1 += 1
                val2 += 1
        for x in range(len(lista)):
            if "" in lista:
                lista.remove("")
    return lista


def main():

    lista1 = [2, 3, 4, 5, 3, 3, 2, 4]
    lista2 = [6, 3, 9, 4, 1, 0, 9]
    lista3 = []#1, 2, 6, 7, 9]
    lista = [lista1, lista2, lista3]
    cadena1 = "Love"
    cadena2 = "Velo"


    print("\nEjercicio 1:")
    for elegida in lista:
        print("La lista", elegida, "regresa la lista acumulada:", sumarAcumulado(elegida))

    print("\nEjercicio 2:")
    for elegida in lista:
        print("Lista Original", elegida, "regresa:", recortarLista(elegida))

    print("\nEjercicio 3:")
    for elegida in lista:
        print("La lista", elegida, "está ordenada:", estanOrdenados(elegida))

    print("\nEjercicio 4:")
    anagrama = sonAnagramas(cadena1, cadena2)
    print(cadena1, "es anagrama de", cadena2+":", anagrama)

    print("\nEjercicio 5:")
    for elegida in lista:
        print("La lista", elegida, "contiene duplicados:", hayDuplicados(elegida))

    print("\nEjercicio 6:")
    for elegida in lista:
        conDuplicados = elegida[:]
        print("La lista", conDuplicados, "sin duplicados:", borrarDuplicados(elegida))


main()
