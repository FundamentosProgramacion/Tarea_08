#encoding: UTF-8
# Sebastian Morales Martin
# Tarea_08

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
    valor = True
    for x in lista:
        for y in lista:
            if x == y:
                valor = True
            else:
                valor = False
    return valor


    return valor

lista = [1,2,3,4,5]
print(hayDuplicados(lista))



