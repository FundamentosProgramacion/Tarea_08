#autor: Diana patricia aguilar Martínez
#descripcion: tarea 8
import random as r
def sumarAcumulado(lista):
    suma= 0 #dato acumulado
    acumulada=[] #nueva lista

    for k in lista: #para que recorrra todos los datos de la lista
        suma=k+suma
        acumulada.append(suma)
    return acumulada


def recortarLista(lista):
    a= lista[1:len(lista)-1]
    return a


def listaOrdenada(lista):
    for k in range(0, len(lista)-1):
        if lista[k] >= lista[k+1]:
            return False
    return True


def borrarDuplicados(lista):
    lista= list(set(lista))
    return lista


def hayDuplicados(lista):
    list.sort(lista)
    for k in range(0, len(lista) - 1):
        if lista[k] == lista[k + 1]:
                return True
    return False


def esAnorama(palabra1, palabra2):
    estado= False
    p1= palabra1.upper()
    p2=palabra2.upper()
    a = list(p1)
    b = list(p2)
    list.sort(a)
    list.sort(b)
    stra=""
    strb=""
    fa= stra.join(a)
    fb= strb.join(b)

    if fa==fb:
       return True
    return estado

def main():
    lista2 = []
    n=int(input("Inserte un dato[-1 para salir]: "))

    while n != -1:
        lista2.append(n)
        n = int(input("Inserte un dato[-1 para salir]: "))

    print ("lista original: ", lista2)
    print ("lista acumulada: ", sumarAcumulado(lista2 ))
    print("lista recortada: ", recortarLista(lista2))
    print ("¿la lista esta ordenada?: ", listaOrdenada(lista2))

    palabra1=str(input("inserte la primera palabra: "))
    palabra2=str(input("inserte la segunda palabra: "))
    print("¿es un anorama?: ", esAnorama(palabra1, palabra2))

    print ("Hay duplicados: ", hayDuplicados(lista2))
    print("Lista sin duplicados: ", borrarDuplicados(lista2))
    '''for k in lista2:
        print(k)'''


main()