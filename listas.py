# FERNANDO SEBASTAIAN SILVA MIRAMONTES


# EJERCICIO 1
def sumarAcomulado(lista):
    if lista == [] :
        return []

    else:
        listaSumar = [lista[0]]
        resultado = list(listaSumar)
        for posicion in range(1, len(lista)):
            listaSumar.append(lista[posicion])
            acomulado = sum(listaSumar)
            resultado.append(acomulado)
        return resultado


# EJERCICIO 2
def recortarLista(lista):
    if len(lista) < 2:
        return []

    listaAlfa = list(lista)
    listaAlfa.remove(lista[0])
    listaAlfa.remove(lista[-1])
    return(listaAlfa)



#EJERCICIO 3
def estanOrdenados(lista):
    for k in range(0,len(lista)-1):
        if lista[k] > lista[k+1]:
            return False

    return True

#EJERCICIO 4
def sonAnagramas(a,b):
    prueba = True
    for dato in range(0,len(b)):
        prueba = a[dato] in b
        if prueba == False:
            return False
    return True





def main():
    listaMagna = [[x for x in range(1,11)], [1,2], [5], [], [1,2,3],"ERROR", [1,9,9,6] ]
    print("Ejercicio 1:")
    for dato in range(0,4):
        print ("Para la lista %s regresa el acumulado %s " %(listaMagna[dato],  sumarAcomulado(listaMagna[dato])))

    print("\nEjercicio 2:")
    for dato in range(0,len(listaMagna)):
        if dato != 5:
            print ("Para la lista %s regresa %s " %(listaMagna[dato],  recortarLista(listaMagna[dato])))
        else:
            pass

    print("\nEjercicio 3:")
    for dato in range(0, len(listaMagna),3):
        print("Para la lista %s regresa %s " % (listaMagna[dato], estanOrdenados(listaMagna[dato])))


main()

