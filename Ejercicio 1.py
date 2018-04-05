# encoding UTF-8
# Autor: Genaro Ortiz Durán
# programa que realiza varios ejercicios con listas.


def sumarAcumulado(lista):
    lista1 = []
    acumulador = 0
    for i in (lista):
        acumulador += i
        lista1.append ( acumulador )

    return lista1


def recortarLista(lista):
    Lista1 = []
    for i in range ( 1, (len ( lista ) - 1) ):
        Lista1.append ( lista[i] )

    return Lista1

def hacerOrdenados(lista):
    parejasOrdenadas=0
    for i in range(0,len(lista)-1):
        if lista[i]<=lista[i+1]:
            parejasOrdenadas+=1
    if parejasOrdenadas==len(lista)-1:
        return True
    return False


def revisarAnagramas(cadena,cadena1):
    lista=list(cadena.lower())
    lista1=list(cadena1.lower())
    lista.sort ()
    lista1.sort ()

    if lista == lista1:
        respuesta = True

    else:
        respuesta = False

    return respuesta
def checarDuplicados(lista):
    for i in lista:
        if lista.count(1)>=1:
            return True
        else:
            return False
def borrarDuplicados(lista):
    for i in range(len(lista)):
        while lista.count(i)>1:
            lista.remove(i)
            lista.sort()
    return lista


def main():
    # Ejercicio 1
    listaEj1 = [1, 2, 3]
    lista1Ej1 = [1, 2, 3, 4]
    lista2Ej1 = [1, 2, 3, 4, 5]
    print ("Ejercicio 1:")
    print ("la lista",listaEj1,"regresa la lista acumulada",sumarAcumulado(listaEj1))
    print ("la lista",lista1Ej1,"regresa la lista acumulada",sumarAcumulado(lista1Ej1))
    print ("la lista",lista2Ej1,"regresa la lista acumulada",sumarAcumulado(lista2Ej1))
    s = [x for x in range ( 1, 11 )]
    print ( sumarAcumulado(s))
    # Ejercicio 2
    listaEj2 = [1, 2]
    lista1Ej2 = [1, 2, 3]
    lista2Ej2 = [1, 2, 3, 4]
    print ("Ejercicio 2:")
    print ("La lista",listaEj2,"regresa ", recortarLista(listaEj2))
    print ("La lista",lista1Ej2,"regresa",recortarLista (lista1Ej2))
    print ("La lista",lista2Ej2,"regresa",recortarLista (lista2Ej2))
    # Ejercicio 3
    print("Ejercicio 3: ")
    listaEj3 = [1, 2, 3]
    lista1Ej3 = [7, 3, 15]
    lista2Ej3 = [3, 9, 2, 7, 3, 9]
    print("La lista",listaEj3,"regresa ",hacerOrdenados(listaEj3))
    print("La lista",lista1Ej3,"regresa",hacerOrdenados(lista1Ej3))
    print("La lista",lista2Ej3,"regresa",hacerOrdenados(lista2Ej3))


    #Ejercicio 4
    print("Ejercicio 4:")
    cadena="Roma"
    cadena1="Mora"
    cadena2="Hola"
    cadena3="Hello"
    print("La cadena regresa",revisarAnagramas(cadena,cadena1))
    print ( "La cadena regresa",revisarAnagramas(cadena2,cadena3))
    #Ejercicio 5
    print("Ejercicio 5:")
    listaEj5=[1,2,3,1,4,5]
    lista1Ej5=[5,7,4,6,10]
    lista2Ej5=[1,2,2,3,3,4,5]
    print("La lista",listaEj5,"regresa ",checarDuplicados(listaEj5))
    print("La lista",lista1Ej5,"regresa",checarDuplicados(lista1Ej5))
    print("La lista",lista2Ej5,"regresa",checarDuplicados(lista2Ej5))
    #Ejercicio 6
    print("Ejercicio 6:")
    listaEj6= [1,8,3,4,3,1,8,2,7,8]
    lista1Ej6=  [1,8,3,4,2,7]
    lista2Ej6= [1,2,2,3,3,4,5]
    print("La lista",listaEj6,"regresa",borrarDuplicados(listaEj6))
    print("La lista",lista1Ej6,"regresa",borrarDuplicados(lista1Ej6))
    print("La lista",lista1Ej6,"regresa",borrarDuplicados(lista2Ej6))
    






main ()
