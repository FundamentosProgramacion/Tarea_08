def sumarAcumulados(lista):
    b = 0
    c = []
    for i in (lista):
        a = i + b
        b = b + i
        c.append(a)
    return c

def recortarLista(lista):
    return(lista[1:-1])

def estanOrdenados(lista):
    a = 0
    b = 0
    for numero in lista:
        if numero >=  b:
            a += 1
            b = numero
    if a == len(lista):
            return "True"
    else:
            return "False"


def sonAnagramas(cadena1, cadena2):
    cadenaM1 = cadena1.lower()
    cadenaM2 = cadena2.lower()
    lista1 = list(cadenaM1)
    lista2 = list(cadenaM2)
    lista2.sort()
    lista1.sort()
    if lista1 == lista2:
        return "True"
    else:
        return "False"


def hayDuplicado(lista):
    a = []
    i = 1
    for numero in lista:
        if not numero in a:
            if i == len(lista):
                return False
            else:
                i = i + 1
                a.append(numero)

        else:
            return True

def borrarDuplicados(lista):
    a = 0
    for i in lista:
        if i in lista:
            if i in lista[i::]:
                lista.pop(i)
                a += 1
            else:
                a += 1
    return lista

def main():
    lista = [1,2,3,4,5]
    cadena1 = "Roma"
    cadena2 = "Amor"
    print(hayDuplicado(lista))
    print(recortarLista(lista))
    print(sumarAcumulados(lista))
    print(estanOrdenados(lista))
    print(sonAnagramas(cadena1,cadena2))
    print(borrarDuplicados(lista))
main()



