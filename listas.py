# Autor: Carlos Martínez Rodríguez
# Tarea 8 - Listas

def sumarAcumulado(lista): #Función que acumula y suma los valores de una lista
    result = []
    for data in range(0, len(lista), 1):
        suma = 0
        for x in range(data + 1):
            suma += lista[x]
        result.append(suma)
    return result

def recortarLista(lista): #Función que elimina el primero y último elementon de una lista
    result = []
    for x in range(1, len(lista) - 1, 1):
        result.append(lista[x])
    return result

def estanOrdenados(lista): #Función que determina si una lista está en orden
    resp = 0
    for x in range(1, len(lista)):
        if lista[x] < lista[x -1]:
            resp += 1
    if resp > 0:
        return False
    else:
        return True

def hayDuplicados(lista): #Función que determina si hay uno o más elementos iguales en una lista
    resp = False
    for x in range(len(lista)):
        count = 0
        for data in lista:
            if lista[x] == data:
                count += 1
        if count >= 2:
            resp = True
    return resp


def sonAnagramas(cadenaA, cadenaB): #Función que determina si dos palabras son anagramas
    cadenaA = cadenaA.lower()
    cadenaB = cadenaB.lower()
    cadenaA = list(cadenaA)
    cadenaB = list(cadenaB)
    cadenaA.sort()
    cadenaB.sort()
    if cadenaA == cadenaB:
        return True
    else:
        return False


def borrarDuplicados(lista): #Función que elimina todos los duplicados de un lista
    index = []
    for x in range(len(lista)):
        num = lista[x]
        numIndex = x
        for y in range(len(lista)):
            if num == lista[y] and numIndex != y and numIndex not in index:
                index.append(y)
    index.sort()
    for data in range(len(index), 0, -1):
        del lista[(index[data -1])]
    return lista

#Función Main
def main():

    #Listas y palabras con las que se probaran las funciones
    listaA = [1, 2, 3, 4, 5]
    listaB = []
    listaC = [6, 1, 3, 6, 34, 7, 3, 5, 5, 54, 2, 2, 4, 2, 5, 2, 1]

    palabra1 = "Roma"
    palabra2 = "Amor"
    palabra3 = "Poder"
    palabra4 = "Pedro"
    palabra5 = "Hola"
    palabra6 = "Hello"
    
    print('Ejercicio 1:')
    print('La lista', listaA, 'regresa la lista acumulada', sumarAcumulado(listaA))
    print('La lista', listaB, 'regresa la lista acumulada', sumarAcumulado(listaB))
    print('La lista', listaC, 'regresa la lista acumulada', sumarAcumulado(listaC))
    print('\n')
    print('Ejercicio 2:')
    print('La lista', listaA, 'regresa la lista recortada', recortarLista(listaA))
    print('La lista', listaB, 'regresa la lista recortada', recortarLista(listaB))
    print('La lista', listaC, 'regresa la lista recortada', recortarLista(listaC))
    print('\n')
    print('Ejercicio 3:')
    print('La lista', listaA, 'está ordenada:', estanOrdenados(listaA))
    print('La lista', listaB, 'está ordenada:', estanOrdenados(listaB))
    print('La lista', listaC, 'está ordenada:', estanOrdenados(listaC))
    print('\n')
    print('Ejercicio 4:')
    print('Las palabras', palabra1, 'y', palabra2, 'son anagramas', sonAnagramas(palabra1, palabra2))
    print('Las palabras', palabra3, 'y', palabra4, 'son anagramas', sonAnagramas(palabra3, palabra4))
    print('Las palabras', palabra5, 'y', palabra6, 'son anagramas', sonAnagramas(palabra5, palabra6))
    print('\n')
    print('Ejercicio 5:')
    print('La lista', listaA, 'regresa hay duplicados', hayDuplicados(listaA))
    print('La lista', listaB, 'regresa hay duplicados', hayDuplicados(listaB))
    print('La lista', listaC, 'regresa hay duplicados', hayDuplicados(listaC))
    print('\n')
    print('Ejercicio 6:')
    print('La lista', listaA, 'regresa', borrarDuplicados(listaA))
    print('La lista', listaB, 'regresa', borrarDuplicados(listaB))
    print('La lista', listaC, 'regresa', borrarDuplicados(listaC))
main()