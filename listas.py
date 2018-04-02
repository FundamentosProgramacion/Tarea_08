# FERNANDO SEBASTAIAN SILVA MIRAMONTES
#

def sumarAcomulado(lista):
    listaSumar = [lista[0]]
    resultado = list(listaSumar)
    for posicion in range(1, len(lista)):
        listaSumar.append(lista[posicion])
        acomulado = sum(listaSumar)
        resultado.append(acomulado)
    print(resultado)


def estanOrdenados(lista):
    for k in range(0,len(lista)-1):
        if lista[k] > lista[k+1]:
            return False

    return True







def main():
    s = [x for x in range(1,11)]
    print(s)
    sumarAcomulado(s)


main()

