#Autor: Eduardo Roberto Muller Romero, A01745219
#Tarea8
from random import randint

def generarLista():
    leng = randint(0, 10)
    lista = []
    if leng > 0:
        for n in range(leng):
            dato = randint(0, 9)
            lista.append(dato)
        return lista
    else:
        return lista

def sumarAcumulado(lista):
    lista_acumulada = []
    leng = len(lista)
    if leng > 1:
        primerdato = lista[0]
        lista_acumulada.append(primerdato)
        for n in range(1, leng):
            dato = lista[n]
            dato2 = lista_acumulada[n-1]
            sum = dato + dato2
            lista_acumulada.append(sum)
        return lista_acumulada
    else:
        for n in range(leng):
            lista_acumulada.append(lista[n])
        return lista_acumulada

def recortarLista(list):
    leng = len(list)
    listaNueva = []
    for n in range(1, (leng -1)): #el rango abarca desde el indice 1 y termina 1 antes del ultimo indice
        listaNueva.append(list[n])
    return listaNueva

def estanOrdenados(list):
    leng = len(list)
    resultado = False
    ordenados = 0
    for n in range(1, leng):
        dato1 = list[n]
        dato2 = list[n-1]
        if dato1 >= dato2:
            ordenados += 1
    leng2 = ordenados + 1
    if leng == leng2:
        resultado = True
    return resultado

def sonAnagrama(a, b):
    sonAnagrama = False
    palabra1 = a.upper()
    palabra2 = b.upper()
    list_palabra1 = list(palabra1)
    list_palabra2 = list(palabra2)
    for x in list_palabra1:
        if x == ' ':
            list_palabra1.remove(x)
    for x in list_palabra2:
        if x == ' ':
            list_palabra2.remove(x)
    list_palabra2.reverse()
    str1 = ""
    str2 = ""
    word1 = str1.join(list_palabra1)
    word2 = str2.join(list_palabra2)
    if word1 == word2:
        sonAnagrama = True
    return sonAnagrama


def hayDuplicados(lista):
    hayDuplicados = False
    datos1 = len(lista)
    for n in range(datos1):
        x = lista[n]
        veces = lista.count(x)
        if veces > 1:
            hayDuplicados = True
            break
    return hayDuplicados

def borrarDuplicados(lista):
    duplicados = []
    datos1 = len(lista)
    for n in range(datos1):
        x = lista[n]
        veces = lista.count(x) #Cuantas veces esta 'x' en la lista
        if veces > 1:
            if x not in duplicados: #si esta repetido y si no lo habia registrado, asi la lista duplicados es [1, 2] y no [1,2,1,2]
                duplicados.append(x)
    lista.reverse() #Para que el repetido sea el eliminado y no el original
    for dato in duplicados:
        duplicado = dato
        lista.remove(duplicado) #borra el primer dato 'duplicado'
    lista.reverse() #La lista regresa a su orden original
    return lista


def main():
    print("Tarea 8: Listas\n")
    lista1 = generarLista() #funcion para generar listas al azar usando randint
    lista2 = generarLista()
    lista3 = []
    #Ejercicio 1
    print('\nEjercicio1: Sumar Acumulado', '\nPara la lista', lista1, 'el programa regresa', sumarAcumulado(lista1),
          '\nPara la lista', lista2, 'el programa regresa', sumarAcumulado(lista2),
          '\nPara la lista', lista3, 'el programa regresa', sumarAcumulado(lista3))
    #ejercicio 2
    print('\nEjercicio2: Recortar Lista', '\nPara la lista', lista1, 'el programa regresa', recortarLista(lista1),
          '\nPara la lista', lista2, 'el programa regresa', recortarLista(lista2),
          '\nPara la lista', lista3, 'el programa regresa', recortarLista(lista3))
    #Ejercicio 3
    print('\nEjercicio3: Estan Ordenados', '\nPara la lista', lista1, 'el programa regresa', estanOrdenados(lista1),
          '\nPara la lista', lista2, 'el programa regresa', estanOrdenados(lista2),
          '\nPara la lista', lista3, 'el programa regresa', estanOrdenados(lista3))
    #Ejercicio4
    palabra1 = 'RomA'
    anagrama1 = 'aMor' #La funcion convierte a mayusculas por lo que el uso de estas no lo afecta
    palabra2 = 'Anita lava la tina'
    anagrama2 = 'Anit al aval atinA' #La funcion borra los espacios para frases
    palabra3 = "linux"
    anagrama3 = 'LUNIX'
    palabra4 = ' '
    anagrama4 = ' '
    print('\nEjercicio4: sonAnagramas', '\nPara', palabra1, 'y', anagrama1, 'el programa regresa', sonAnagrama(palabra1, anagrama1),
          '\nPara', palabra2, 'y', anagrama2, 'el programa regresa', sonAnagrama(palabra2, anagrama2),
          '\nPara', palabra3, 'y', anagrama3, 'el programa regresa', sonAnagrama(palabra3, anagrama3),
          '\nPara', palabra4, 'y', anagrama4, 'el programa regresa', sonAnagrama(palabra4, anagrama4))
    #Ejercicio 5
    print('Ejercicio5: Hay Duplicados', '\nPara la lista', lista1, 'el programa regresa', hayDuplicados(lista1),
          '\nPara la lista', lista2, 'el programa regresa', hayDuplicados(lista2),
          '\nPara la lista', lista3, 'el programa regresa', hayDuplicados(lista3))
    #Ejercicio 6
    lista1_sd = lista1[:]
    lista2_sd = lista2[:]
    lista3_sd = lista3[:]
    print('\nEjercicio 6: Borrar Duplicados', '\nPara la lista', lista1_sd, 'el programa regresa', borrarDuplicados(lista1),
          '\nPara la lista', lista2_sd, 'el programa regresa', borrarDuplicados(lista2),
          '\nPara la lista', lista3_sd, 'el programa regresa', borrarDuplicados(lista3))



main()