#encoding: UTF-8
# Sebastian Morales Martin
# Tarea_08

#listas usadas en las funciones:
lista1 = [1,2,3,4,5]
lista2 =[1,2,2,3,4,3,5,6,6,7,1,3,4,8,3,4,6,3,9]
lista3 = []
lista4 = [1]

#Palabras usadas en la función de los anagramas:
anagrama1 = 'hola'
anagrama2 = "amor"
anagrama3 = 'roma'
anagrama4 = 'hello'

def sumarAcumulado(lista):

    nuevaLista = []
    acumulador = 0
    for numero in lista:
        acumulador += numero
        nuevaLista.append(acumulador)
    return nuevaLista

def recortarLista(lista):
    listaRecortada = []
    for k in range(0, len(lista), 1):
        if k != (len(lista)-len(lista)) and k != len(lista)-1:
            listaRecortada.append(lista[k])
    return listaRecortada

def estanOrdenados(lista):          #compara paquetes de 2 numeros en la lista a la vez, si la lista es completamente
    contador1 = 0
    contador2 = 1
    valor = True
    for numero in range(len(lista)-2):
         if lista[contador2] > lista[contador1]:
            contador1 += 1
            contador2 += 1
         else:
            valor = False
    return valor

def sonAnagramas(palabra1, palabra2):           #recibe dos cadenas, las diviede y sortea, al final las compara y si la lista es exactamente igual, regresa True, en otro caso False

    lista1 = list(palabra1)
    lista2 = list(palabra2)
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    return False

def hayDuplicados(lista):

    for x in range(len(lista)):
        for y in range(len(lista)):
            if x != y:
                if lista[x] == lista[y]:
                    return True
    return False


    return valor

def borrarDuplicados(lista):
    listaDuplicados = []            #lista generada para tener los indices de los valores repetidos

    for numero in lista:
        if numero not in listaDuplicados:
            listaDuplicados.append(numero)
    return listaDuplicados



def main():
    print('Ejercicio 1:')
    print('La lista ', lista1, ' regresa la lista acumulada ', sumarAcumulado(lista1))
    print('La lista ', lista2, ' regresa la lista acumulada ', sumarAcumulado(lista2))
    print('La lista ', lista3, ' regresa la lista acumulada ', sumarAcumulado(lista3))
    print('La lista ', lista4, ' regresa la lista acumulada ', sumarAcumulado(lista4))
    print('\n')
    print('Ejercicio 2:')
    print('La lista ', lista1, ' regresa ', recortarLista(lista1))
    print('La lista ', lista2, ' regresa ', recortarLista(lista2))
    print('La lista ', lista3, ' regresa ', recortarLista(lista3))
    print('La lista ', lista4, ' regresa ', recortarLista(lista4))
    print('\n')
    print('Ejercicio 3:')
    print('La lista ', lista1, ' regresa ', estanOrdenados(lista1))
    print('La lista ', lista2, ' regresa ', estanOrdenados(lista2))
    print('La lista ', lista3, ' regresa ', estanOrdenados(lista3))
    print('La lista ', lista4, ' regresa ', estanOrdenados(lista4))
    print('\n')
    print('Ejercicio 4:')
    print('las palabras', anagrama1, 'y ', anagrama2, 'regresan ', sonAnagramas(anagrama1, anagrama2))
    print('las palabras', anagrama2, 'y ', anagrama3, 'regresan ', sonAnagramas(anagrama2, anagrama3))
    print('las palabras', anagrama1, 'y ', anagrama4, 'regresan ', sonAnagramas(anagrama1, anagrama4))
    print('\n')
    print('Ejercicio 5:')
    print('La lista ', lista1, ' regresa ', hayDuplicados(lista1))
    print('La lista ', lista2, ' regresa ', hayDuplicados(lista2))
    print('La lista ', lista3, ' regresa ', hayDuplicados(lista3))
    print('La lista ', lista4, ' regresa ', hayDuplicados(lista4))
    print('\n')

    print('Ejercicio 6:')
    print('La lista ', lista1, ' regresa ', borrarDuplicados(lista1))
    print('La lista ', lista2, ' regresa ', borrarDuplicados(lista2))
    print('La lista ', lista3, ' regresa ', borrarDuplicados(lista3))
    print('La lista ', lista4, ' regresa ', borrarDuplicados(lista4))

main()
