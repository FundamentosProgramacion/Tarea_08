#Nataly Paulina Lopez Salazar
#Diferentes ejercicios con listas

def sumarAcumulado(lista): #Esta funcion suma los valores de la lista sin juntar todos
    suma = 0
    acumulada = []
    for dato in lista:
        suma += dato
        acumulada.append(suma)
    return acumulada


def recortarLista(lista): # Esta funcion quita el primero y el ultimo numero
    lista2= lista[1:len(lista)-1]
    return lista2


def estanOrdenados(lista): # Esta funcion checa que los valores esten ordenados
    ordenados = False
    for k in range(0, len(lista) - 1):
        if lista[k] <= lista[k + 1]:
           ordenados = True
        else:
            ordenados = False
            break

    return ordenados


def sonAnagramas(lista2, lista3): #Esta funcion verifica que las cadenas sean anagramas
    dato = lista2
    dato2 = lista3

    if len(dato)==len(dato2):
        for i in range (len(dato)):
            if dato[i] not in dato2:
                return "No"

        return "Si"
    return "No"



def hayDuplicados(lista): # Esta funcion detecta los duplicados
    list.sort(lista)
    for k in range(0,len(lista)-1):
        if lista[k]==lista[k+1]:
            return True
    return False


def borrarDuplicados(lista): #Esta funcion quita los duplicados
    lista = list(set(lista))

    return lista


def main():
    lista = []  # Lista Vacia
    dato = int(input("Teclea un valor [-1 Termina]: "))
    while dato != -1:  # no pide terminar
        lista.append(dato)
        dato = int(input("Reclea un valor [-1 Termina]: "))
    # Calcular datos
    print("Datos: ", lista)
    listaA = sumarAcumulado(lista)
    print("Ejercicio 1")
    print("La lista", lista, "regresa la lista acumulada", listaA, "\n")

    listaB = recortarLista(lista)
    print("Ejercicio 2")
    print("Lista original ", lista, "regresa", listaB, "\n")

    listaC = estanOrdenados(lista)
    print("Ejercicio 3")
    print("La lista", lista, "esta ordenada:", listaC, "\n")

    print("Ejercicio 4")
    cadena1 = input("Dame la primer palabra:")
    cadena1.upper()
    cadena2 = input("Dame la seguna palabra:")
    cadena2.upper()
    lista2 = list(cadena1)
    lista3 = list(cadena2)
    print(lista2)
    print(lista3)
    listaD = sonAnagramas(lista2, lista3)
    print("Tus cadenas son anagramas:",listaD,"\n")

    print("Ejercicio 5")
    listaE = hayDuplicados(lista)
    print("Tu lista",lista,"tiene duplicados:",listaE,"\n")

    print("Ejercicio 6")
    print("Quita los duplicados")
    listaF = borrarDuplicados(lista)
    print(listaF)

main()