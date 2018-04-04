#Autor: Ricardo Cornejo Lozano
#Ejercicios con listas con ejemplos


def sumarAcumulado(lista):
    suma = 0    #acumular
    acumulada = []
    for dato in lista:
        suma += dato
        acumulada.append(suma)

    return acumulada

def recortarLista(lista):
    if len(lista) == 0:
        return []
    else:
        del lista[0]
        del lista[-1]
    return lista
def estanOrdenados(lista):
    logic = (lista[0]+1) - (lista[1])
    if logic == 0:
        return True
    else:
        return False

def sonAnagramas(palabra,palabra2):
    palabra = list("allergy")
    palabra.sort()
    palabra2 = list("gallery")
    palabra2.sort()
    if palabra == palabra2:
        return True
    else:
        return False

def hayDuplicados(lista):
    if len(lista) != len(set(lista)):
        return True
    else:
        return False

def borrarDuplicados(lista):
    erase = list(set(lista))
    return erase

def main():
    lista1 = [1,2,3,4,5]
    listaorden = [1,2,3,4,5]
    listadesorden = [1,2,3,5,2,5]
    listadesorden2 = [1,2,3,3,3,3,3,4,5,99,7]
    listaorden2 = [1,2,3]
    listaorden3 = [1,7]
    lista2 = []
    lista3 = [5]
    lista4 = [1,2,3]
    palabraOriginal = ("Allergy")
    palabraOriginal2 = ("Gallery")
    palabraOriginal3 = ("Hello")
    palabraOriginal4 = ("Hi")
    palabra = list("Allergy")
    palabra.sort()
    palabra2 = list("Gallery")
    palabra2.sort()
    palabra3 = list("Hello")
    palabra3.sort()
    palabra4 = list("Hi")
    palabra4.sort()
    print("Ejercicio 1: ")
    print ("La lista: "+ str(lista1),"Regresa la lista acumulada: "+ str(sumarAcumulado(lista1)))
    print("La lista: " + str(lista2), "Regresa la lista acumulada: " + str(sumarAcumulado(lista2)))
    print("La lista: " + str(lista3), "Regresa la lista acumulada: " + str(sumarAcumulado(lista3)))

    print ("\nEjercicio 2: ")
    print("Lista Original: " + str(lista1), "Regresa: " + str(recortarLista(lista1)))
    print("Lista Original: " + str(lista4), "Regresa: " + str(recortarLista(lista4)))
    print("Lista Original: " + str(lista2), "Regresa: " + str(recortarLista(lista2)))

    print("\nEjercicio 3: ")
    print("Lista: "+ str(listaorden), "Estan Ordenados? " +str(estanOrdenados(listaorden)))
    print("Lista: " + str(listaorden2), "Estan Ordenados? " + str(estanOrdenados(listaorden2)))
    print("Lista: " + str(listaorden3), "Estan Ordenados? " + str(estanOrdenados(listaorden3)))

    print("\nEjercicio 4: ")
    print ("Palabra 1: " +str(palabraOriginal), "Palabra 2: " +str(palabraOriginal2), "\nSon Anagrama? " +str(sonAnagramas(palabra,palabra2)))

    print("\nEjercicio 5: ")
    print("Lista: " +str(listaorden), "Hay duplicados? " +str(hayDuplicados(listaorden)))
    print("Lista: " + str(listadesorden), "Hay duplicados? " + str(hayDuplicados(listadesorden)))
    print("Lista: " + str(listaorden3), "Hay duplicados? " + str(hayDuplicados(listaorden3)))

    print("\nEjercicio 6: ")
    print("Lista: " +str(listadesorden), "Sin Duplicados: " +str(borrarDuplicados(listadesorden)))
    print("Lista: " + str(listaorden2), "Sin Duplicados: " + str(borrarDuplicados(listaorden2)))
    print("Lista: " + str(listadesorden2), "Sin Duplicados: " + str(borrarDuplicados(listadesorden2)))
main()