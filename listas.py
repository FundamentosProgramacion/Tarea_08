#Autor: Andrés Reyes Rangel

def sumarAcumulado(lista):
    suma = 0
    acumulada = []
    for dato in lista:
        suma += int(dato)
        acumulada.append(suma)
    return acumulada


def quitarEspacios(lista):
    sinEspacios = []

    for dato in lista:  # dato pasa por cada cadena en la lista
        if dato != " ":  # Evalua si en la lista hay un espacio
            sinEspacios.append(dato)  # Agrega el dato a la lista

    return sinEspacios


def recortarLista(lista):
    recortar = lista[1:len(lista)-1]
    return recortar


def estanOrdenados(lista):
    for k in range(0,len(lista)-1):
        if lista[k]>lista[k+1]:
            return False
    return True


def sonAnagramas(palabra1, palabra2):
    lista1 = list(palabra1)
    lista2 = list(palabra2)
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    return False


def hayDuplicados(lista):
    duplicados = False
    veces = 0
    for n in range(len(lista)):
        veces += 1
        if veces > 1:
            duplicados = True
            break
    return duplicados


def borrarDuplicados(lista):
    duplicados = []
    datos1 = len(lista)
    for n in range(datos1):
        x = lista[n]
        veces = lista.count(x)
        if veces > 1:
            if x not in duplicados:
                duplicados.append(x)
    lista.reverse()
    for dato in duplicados:
        duplicado = dato
        lista.remove(duplicado)
    lista.reverse()
    return lista


def main():
    lista1 = [1, 2, 3]
    lista2 = [1, 2, 3, 4, 5]
    lista3 = [1, 2]
    lista4 = [7, 3, 15]
    lista5 = [1]
    lista6 = []
    lista7 = [1,2,3,1,4,5]
    lista8 = [4,5,8,9,3,4,8,7,2]
    lista9 = [1,8,4,5,9,8,1,5,2]
    lista = lista9[:]
    palabra1 = "roma"
    palabra2 = "mora"
    palabra3 = "hola"
    palabra4 = "hello"
    palabra5 = "amor"

    print("Ejercicio 1:")
    suma1 = sumarAcumulado(lista1)
    suma2 = sumarAcumulado(lista2)
    suma3 = sumarAcumulado(lista3)
    suma4 = sumarAcumulado(lista4)
    suma5 = sumarAcumulado(lista5)
    suma6 = sumarAcumulado(lista6)
    print("La lista", lista1,"regresa la lista acumulada", suma1)
    print("La lista", lista2, "regresa la lista acumulada", suma2)
    print("La lista", lista3, "regresa la lista acumulada", suma3)
    print("La lista", lista4, "regresa la lista acumulada", suma4)
    print("La lista", lista5, "regresa la lista acumulada", suma5)
    print("La lista", lista6, "regresa la lista acumulada", suma6)
    print("")

    print("Ejercicio 2:")
    recortar1 = recortarLista(lista1)
    recortar2 = recortarLista(lista2)
    recortar3 = recortarLista(lista3)
    recortar4 = recortarLista(lista4)
    recortar5 = recortarLista(lista5)
    recortar6 = recortarLista(lista6)
    print("La lista original", lista1, "regresa", recortar1)
    print("La lista original", lista2, "regresa", recortar2)
    print("La lista original", lista3, "regresa", recortar3)
    print("La lista original", lista4, "regresa", recortar4)
    print("La lista original", lista5, "regresa", recortar5)
    print("La lista original", lista6, "regresa", recortar6)
    print("")

    print("Ejercicio 3:")
    ordenado1 = estanOrdenados(lista1)
    ordenado2 = estanOrdenados(lista2)
    ordenado3 = estanOrdenados(lista3)
    ordenado4 = estanOrdenados(lista4)
    ordenado5 = estanOrdenados(lista5)
    ordenado6 = estanOrdenados(lista6)
    print("La lista original", lista1, "regresa", ordenado1)
    print("La lista original", lista2, "regresa", ordenado2)
    print("La lista original", lista3, "regresa", ordenado3)
    print("La lista original", lista4, "regresa", ordenado4)
    print("La lista original", lista5, "regresa", ordenado5)
    print("La lista original", lista6, "regresa", ordenado6)
    print("")

    print("Ejercicio 4:")
    anagrama1 = sonAnagramas(palabra1,palabra2)
    anagrama2 = sonAnagramas(palabra3, palabra4)
    anagrama3 = sonAnagramas(palabra1, palabra4)
    anagrama4 = sonAnagramas(palabra2, palabra3)
    anagrama5 = sonAnagramas(palabra1, palabra5)
    print("las palabras", palabra1, "y ", palabra2, "¿son anagramas?", anagrama1)
    print("las palabras", palabra3, "y ", palabra4, "¿son anagramas?", anagrama2)
    print("las palabras", palabra1, "y ", palabra4, "¿son anagramas?", anagrama3)
    print("las palabras", palabra3, "y ", palabra2, "¿son anagramas?", anagrama4)
    print("las palabras", palabra1, "y ", palabra5,"¿son anagramas?", anagrama5)
    print("")

    print("Ejercicio 5:")
    duplicado1 = hayDuplicados(lista1)
    duplicado2 = hayDuplicados(lista2)
    duplicado3 = hayDuplicados(lista7)
    duplicado4 = hayDuplicados(lista8)
    duplicado5 = hayDuplicados(lista5)
    duplicado6 = hayDuplicados(lista6)
    print("La lista ", lista1, "¿tiene duplicados?", duplicado1)
    print("La lista ", lista2, "¿tiene duplicados?", duplicado2)
    print("La lista ", lista7, "¿tiene duplicados?", duplicado3)
    print("La lista ", lista8, "¿tiene duplicados?", duplicado4)
    print("La lista ", lista5, "¿tiene duplicados?", duplicado5)
    print("La lista ", lista6, "¿tiene duplicados?", duplicado6)
    print("")

    print("Ejercicio 6:")
    print("La lista ", lista, "regresa", borrarDuplicados(lista9))
main()