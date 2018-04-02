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
    lista_acumulada.append(list[0])
    for n in range(1, leng):
        dato = lista[n]
        dato2 = lista_acumulada[n-1]
        sum = dato + dato2
        lista_acumulada.append(sum)
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
    listaordenada = []
    for n in range(1, leng):
        dato1 = list[n]
        dato2 = list[n-1]
        if dato1 > dato2:
            listaordenada.append("0")
    leng2 = len(listaordenada) + 1
    if leng == leng2:
        resultado = True
    return resultado

def main():
    print("Tarea 8: Listas\n")
    lista1 = generarLista() #funcion para generar listas al azar usando randint
    lista2 = generarLista()
    lista3 = generarLista()
    #Ejercicio 1
    print('Ejercicio1: Sumar Acumulado', '\nPara la lista', lista1, 'el programa regresa', sumarAcumulado(lista1),
          '\nPara la lista', lista2, 'el programa regresa', sumarAcumulado(lista2),
          '\nPara la lista', lista3, 'el programa regresa', sumarAcumulado(lista3))
    #ejercicio 2
    print('Ejercicio2: Recortar Lista', '\nPara la lista', lista1, 'el programa regresa', recortarLista(lista1),
          '\nPara la lista', lista2, 'el programa regresa', recortarLista(lista2),
          '\nPara la lista', lista3, 'el programa regresa', recortarLista(lista3))
    #Ejercicio 3
    print('Ejercicio3: Estan Ordenados', '\nPara la lista', lista1, 'el programa regresa', estanOrdenados(lista1),
          '\nPara la lista', lista2, 'el programa regresa', estanOrdenados(lista2),
          '\nPara la lista', lista3, 'el programa regresa', estanOrdenados(lista3))
    #Ejercicio4
    print('Ejercicio4: sonAnagramas'


main()