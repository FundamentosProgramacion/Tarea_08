# FERNANDO SEBASTAIAN SILVA MIRAMONTES
# EJERCICIOS CON LISTAS.

# EJERCICIO 1
def sumarAcumulado(lista):
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
    a = a.upper()
    b = b.upper()
    listaA = list(a)
    listaB = list(b)
    prueba = True
    if len(listaB) != len(listaA):
        return False
    for dato in range(0,len(b)):
        prueba = listaA[dato] in listaB
    return prueba


#EJERCICIO 5
def hayDuplicados(lista):
    for dato1 in lista:
        contador = 0
        for dato in lista:
            if dato == dato1:
                 contador += 1
            if contador == 2:
                return True
    return False


#EJERCICIO 6
def borrarDuplicados(lista):
    for dato1 in lista:
        contador = 0
        for dato in lista:
            if dato == dato1:
                 contador += 1
            if contador == 2:
                lista.remove(dato)
    return lista





def main():

    listaMagna = [[x for x in range(1,11)], [1,2], [5], [], [1,2,3],"ERROR", [1,9,9,6] ]
    print("Ejercicio 1:")
    for dato in range(0,4):
        print ("Para la lista %s regresa el acumulado %s " %(listaMagna[dato],  sumarAcumulado(listaMagna[dato])))

    print("\nEjercicio 2:")
    for dato in range(0,5):
        if dato != 5:
            print ("Para la lista %s regresa %s " %(listaMagna[dato],  recortarLista(listaMagna[dato])))
        else:
            pass

    print("\nEjercicio 3:")
    for dato in range(0, len(listaMagna),3):
        print("Para la lista %s regresa %s " % (listaMagna[dato], estanOrdenados(listaMagna[dato])))

    print("\nEjercicio 4:")
    print("FRENANDO es Anagrama de FERNANDO?: ", sonAnagramas("fernando","frenando"))
    print("SILVA es Anagrama de SILVIA?: ", sonAnagramas("SILVA", "silvia"))
    print("SI es Anagrama de SOL?: ", sonAnagramas("sI", "sOl"))

    print("\nEjercicio 5:")
    for dato in range(0, len(listaMagna), 3):
        print("Para la lista %s regresa %s " % (listaMagna[dato], hayDuplicados(listaMagna[dato])))

    print("\nEjercicio 6:")
    print("Para la lista %s reresa %s " % (listaMagna[0], borrarDuplicados(listaMagna[0])))
    print("Para la lista %s reresa %s " % ([1,9,9,6], borrarDuplicados([1,9,9,6])))

main()

