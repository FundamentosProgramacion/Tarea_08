#Mirna Fernanda Zertuche Calvillo A01373852
#Tarea 8, programa que prueba varias funciones que alteran o buscan ordenes en  listas
def estanOrdenados(lista):

    for k in range(0, len(lista) - 1):
        if lista[k] > lista[k + 1]:
            return False
    return True


def recortarLista(lista):
    if len(lista) == 0:
        return ("[]")
    else:
        a = lista[1:len(lista) - 1]
        return (a)
    #first= lista[0]
        #list.pop(lista)
        #lista.remove(first)
        #return lista



def sumarAcomulado(lista):
    i= 0
    lista2=[]
    for dato in lista:
        dato = dato+i
        i = dato
        lista2.append(dato)
    return (lista2)


def hayDuplicados(lista):
    ndupli= 1
    for dato in lista:
        vecesDato= lista.count(dato)
        if vecesDato> 1:
            ndupli= vecesDato

    if ndupli> 1:
        return True
    else:
        return False


def borrarDuplicados(lista):
    ndupli= 1
    for dato in lista:
        ndupli= lista.count(dato)
        if ndupli > 1:
            lista.remove(dato)

        else:
            lista = lista
    return lista

def sonAnagramas(lista,listab):
    cuenta = 0
    listaa = []

    for dato in lista:
        if dato in listab:
            cuenta += 1
            listaa.append(cuenta)

    if len(listaa) == len(lista) == len(listab):
        return ("true")
    else:
        return ("false")

def main():
    listaA= [1,2,3,4,5,6]
    listab=[2,4,6,8,10]
    listac=[30,31,3]
    listad=[1,3,7,8,9,11]
    listae=[1,3,7]
    listaf=[1,3]
    listag=[]
    listah=[1,2,3,4,5]
    listai = [1,3,2,4,5]
    listaj = [1,5,6,8]
    listak = [1, 2, 1]
    listal = [-10, -5, -4]
    listam = [-1,0,5]
    listan = [1, 2, 3, 3, 2,1]
    listao = [1, 2, 3, 4]
    listap = [1, 2, 33, 4, 3]
    listaq = [1,4,6,4,3 ,2,2,5,25,2]
    listar = [1]

    listaAna=['J', 'A', 'P', 'O', 'N', 'E', 'S']
    listaAna2=['E', 'S', 'P', 'O', 'N', 'J', 'A']
    listaAna3=['R', 'O', 'M', 'A']
    listaAna4=['A', 'M', 'O', 'R']
    listaAna5=['H', 'O', 'L', 'A']
    listaAna6=['H', 'E', 'L', 'L', 'O']
    listaAna7 = ['P', 'A', 'Y', 'A', 'S', 'O']
    listaAna8 = ['E', 'P', 'A', 'Y', 'A', 'S', 'O']

    #EJERCICIO 1
    print("Ejercicio 1:")
    print("La lista original", listaA," regresa como acomulado:", sumarAcomulado(listaA))
    print("La lista original", listab, " regresa como acomulado:", sumarAcomulado(listab))
    print("La lista original", listac, " regresa como acomulado:", sumarAcomulado(listac))
    print("La lista original", listag, " regresa como acomulado:", sumarAcomulado(listag))
    print("La lista original", listar, " regresa como acomulado:", sumarAcomulado(listar))

    # EJERCICIO 2
    print("Ejercicio 2:")
    print("La lista original", listad, " regresa reducida:", recortarLista(listad))
    print("La lista original", listae, " regresa reducida:", recortarLista(listae))
    print("La lista original", listaf, " regresa reducida:", recortarLista(listaf))
    print("La lista original", listag, " regresa reducida:", recortarLista(listag))

    # EJERCICIO 3
    print("Ejercicio 3:")
    print("La lista original", listah, " ¿esta ordenada?:", estanOrdenados(listah))
    print("La lista original", listai, " ¿esta ordenada?:", estanOrdenados(listai))
    print("La lista original", listaj, " ¿esta ordenada?:", estanOrdenados(listaj))
    print("La lista original", listak, " ¿esta ordenada?:", estanOrdenados(listak))
    print("La lista original", listal, " ¿esta ordenada?:", estanOrdenados(listal))
    print("La lista original", listam, " ¿esta ordenada?:", estanOrdenados(listam))


    # EJERCICIO 4
    print("Ejercicio 4:")
    print("La lista original", listaAna, "¿es angrama de",listaAna2,"?:", sonAnagramas(listaAna,listaAna2))
    print("La lista original", listaAna3, "¿es angrama de",listaAna4,"?:", sonAnagramas(listaAna3, listaAna4))
    print("La lista original", listaAna5, "¿es angrama de",listaAna6,"?:", sonAnagramas(listaAna5, listaAna6))
    print("La lista original", listaAna7, "¿es angrama de", listaAna8, "?:", sonAnagramas(listaAna7, listaAna8))

    # EJERCICIO 5
    print("Ejercicio 5:")
    print("La lista original", listan, "¿tiene duplicados?:", hayDuplicados(listan))
    print("La lista original", listao, "¿tiene duplicados?:", hayDuplicados(listao))
    print("La lista original", listap, "¿tiene duplicados?:", hayDuplicados(listap))
    print("La lista original", listaq, "¿tiene duplicados?:", hayDuplicados(listaq))

    # EJERCICIO 6
    print("Ejercicio 6:")
    print("La lista original", listan, "sin duplicados es:", borrarDuplicados(listan))
    print("La lista original", listao, "sin duplicados es:", borrarDuplicados(listao))
    print("La lista original", listap, "sin duplicados es:", borrarDuplicados(listap))
    print("La lista original", listaq, "sin duplicados es:", borrarDuplicados(listaq))





main()