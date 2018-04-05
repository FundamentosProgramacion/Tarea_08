    #Autor Karla Fabiola Ramirez Martines - A01746769

    #Palabras de prueba
lista0=[1,2,3,4,5,6,7,8,9]
lista2=[]
lista3=[8,3,8,1,9,5,3,1,4,342,3,434,]
lista4=[2,4,6,7,8,23,45]
lista1=[5,5,3,1,4,55,5,55,5,5,33,1,23]
listaA=["h","o","l","a"]
listaB=["c","a","m","a","r","a"]
listaC=["m","o","r","a"]
listaD=["a","m","o","r"]
listaE=["a","z","u","l"]
listaF=["v","e","r","d","e"]
listaG=["z","a","l","u"]

    #Primera funcion/La acabo de probar en pythontutor y funciona!
def sumarAcumulado(lista):
    if lista == []:
        return []
    suma=0
    nuevaLista=[]
    for dato in lista:
        suma+=dato
        nuevaLista.append(suma)
    return nuevaLista


    #Segunda funcion/ Probada en pythontutor ! funciona perfectamente
def recortarLista(lista):
    nuevaLista = []
    acumulador = 0
    for k in lista:
        acumulador += 1
        if acumulador != 1 and acumulador != len(lista):
            nuevaLista.append(k)

    return nuevaLista


    #Tercera función <3/la probe dos casos pero necesito probarla mas(por ahora funciona)
def estanOrdenados(lista):
    suma = 0
    primerValor = 0
    for dato in lista:
        if dato > primerValor:
            suma += 1
            primerValor = dato
    if suma == len(lista):
        return "True"
    else:
        return "False"

    #Cuarta funcion/Por ahora ni puta idea de como hacerla, ok se podria usar in pero aun no se como utilizarla
def sonAnagramas(lista1,lista2):
    a1=lista1.sort()
    a2=lista2.sort()
    if a1 == a2:
        return True
    return False



    #Quinta funcion/Tiene bastant eproblemas el mayor es como arreglar lo de la suma y hacerlo eficiente
    #Nenesita arreglarse
def hayDuplicados(lista):
    contador = 0
    for datoprimero in lista:
        for dato in lista:
            if dato == datoprimero:
                contador += 1
            if contador == 2:
                return "True"

    return "False"


    #Sexta funcion/no regresa una nueva lista asi que habria que utilizar remove :)
def borrarDuplicados(lista):
    for datoprimero in lista:
        lvacia=[]
        if lista==[]:
            return lvacia
        contador = 0
        for dato in lista:
            if dato == datoprimero:
                contador += 1
            if contador == 2:
                lista.remove(dato)
        return lista
    #Aqui probaremos varios ejemplos
def main():
        #Primer print
    print("Primera función Sumar Acumulado")
    print(lista0,"<-------Lista original y el resultado es:",sumarAcumulado(lista0))
    print(lista1,"<-------Lista original y el resultado es:",sumarAcumulado(lista1))
    print(lista2,"<-------Lista original y el resultado es:",sumarAcumulado(lista2))
    print(lista3,"<-------Lista original y el resultado es:",sumarAcumulado(lista3))

        #Segundo print
    print("Segunda función Recortar Lista")
    print(lista0, "<-------Lista original y el resultado es:", recortarLista(lista0))
    print(lista1, "<-------Lista original y el resultado es:", recortarLista(lista1))
    print(lista2, "<-------Lista original y el resultado es:", recortarLista(lista2))
    print(lista3, "<-------Lista original y el resultado es:", recortarLista(lista3))

        #Tercer print
    print("Tercera función Estan Ordenados")
    print(lista0, "<-------Lista original y el resultado es:", estanOrdenados(lista0))
    print(lista1, "<-------Lista original y el resultado es:", estanOrdenados(lista1))
    print(lista2, "<-------Lista original y el resultado es:", estanOrdenados(lista2))
    print(lista3, "<-------Lista original y el resultado es:", estanOrdenados(lista3))

        #Cuarto print
    print("Cuarta función sonAnagramas")
    print(listaC,listaD, "<-------Lista original y el resultado es:", sonAnagramas(listaC,listaD))
    print(listaG,listaE, "<-------Lista original y el resultado es:", sonAnagramas(listaG, listaE))
    print(listaB, listaF, "<-------Lista original y el resultado es:", sonAnagramas(listaB, listaF))
    print(listaE, listaA, "<-------Lista original y el resultado es:", sonAnagramas(listaE, listaA))


        #Quinto print
    print("Quinta función hay Duplicados")
    print(lista0, "<-------Lista original y el resultado es:", hayDuplicados(lista0))
    print(lista1, "<-------Lista original y el resultado es:", hayDuplicados(lista1))
    print(lista2, "<-------Lista original y el resultado es:", hayDuplicados(lista2))
    print(lista3, "<-------Lista original y el resultado es:", hayDuplicados(lista3))

        #Sexto print
    print("Sexta función borrarDuplicados")
    print(lista0, "<-------Lista original y el resultado es:", borrarDuplicados(lista0))
    print(lista1,"<-------Lista original y el resultado es:", borrarDuplicados((lista1))
    print(lista4, "<-------Lista original y el resultado es:", borrarDuplicados(lista4))
    print(lista3, "<-------Lista original y el resultado es:", borrarDuplicados(lista3))








main()
