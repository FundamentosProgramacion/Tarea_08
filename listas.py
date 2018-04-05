#encoding: UTF-8
#Jean Paul Esquivel Lobato
#A01376152
#Listas

def sumarAcumulado(lista):
    suma = 0
    acumulada = []
    for dato in lista:
        suma += dato
        acumulada.append(suma)

    return acumulada

def recortaLista(lista):
    nuevalista = lista[1:len(lista)-1]
    return nuevalista

def estanOrdenados(lista):
    for k in range (0,len(lista)-1):
        if lista[k]>lista[k+1]:
            return False

    return True

def sonAnagramas(palabra1, palabra2):
    sonAnagrama = "No son Anagrama"
    p1 = palabra1.upper()
    p2 = palabra2.upper()
    list_p1 = list(p1)
    list_p2 = list(p2)
    list_p2.sort()
    list_p1.sort()
    str1 = ""
    str2 = ""
    a1 = str1.join(list_p1)
    a2 = str2.join(list_p2)
    if a1 == a2:
        sonAnagrama = "Son Anagrama"

    return sonAnagrama

def hayDuplicados(lista):
    acum = 1
    for dato in lista:
        vecesD = lista.count(dato)
        if vecesD > 1:
            acum +=1

    if acum > 1:
        return True

    else:
        return False

def borrarDuplicados(lista):
    lista.sort()
    ac = 1
    for dato in lista:
        ac = lista.count(dato)
        if ac > 1:
            lista.remove(dato)

        else:
            lista = lista
    return lista

def main():
    #EJERCICIO 1
    print("Probando el ejercicio 1")
    x =[0,1,2,3,4,5,6,7,8,9]
    l = sumarAcumulado(x)
    print("La lista",x, "regresa el acumulado de la lista",l)
    y = []
    m = sumarAcumulado(y)
    print("La lista", y, "regresa el acumulado de la lista", m)
    z = [1]
    n = sumarAcumulado(z)
    print("La lista", z, "regresa el acumulado de la lista", n)

    # EJERCICIO 2
    print("Probando el ejercicio 2")
    x1 = [0,2,4,5,6,7,8,9]
    l1 = recortaLista(x1)
    print("La lista", x1, "regresa la lista recortada a", l1)
    y1 = []
    m1 = recortaLista(y1)
    print("La lista", y, "regresa la lista recortada a", m1)
    z1 = [1,4,5]
    n1 = recortaLista(z1)
    print("La lista", z1, "regresa la lista recortada a", n1)

 # EJERCICIO 3
    print("Probando el ejercicio 3")
    x2 = [1,3,6,7,9,12,56,89,667]
    l2 = estanOrdenados(x2)
    print("La lista", x2, "es", l2)
    y2 = []
    m2 = estanOrdenados(y2)
    print("La lista", y2, "es", m2)
    z2 = [3,4,5,6,8,9,10,1]
    n2 = estanOrdenados(z2)
    print("La lista", z2, "es", n2)

 # EJERCICIO 4
    print("Probando el ejercicio 4")
    x3 = 'casa'
    nuevaX = 'saca'
    l3 = sonAnagramas(x3,nuevaX)
    print("La lista", x3, "y",nuevaX , l3)
    y3 = 'hana'
    nuevaY = 'nava'
    m3 = sonAnagramas(y3,nuevaY)
    print("La lista", y3,"y",nuevaY, m3)
    z3 = 'mira'
    nuevaZ = 'rima'
    n3 = sonAnagramas(z3,nuevaZ)
    print("La lista", z3,"y",nuevaZ, n3)

# EJERCICIO 5
    print("Probando el ejercicio 5")
    x4 = [3,4,5,4,6,87,8,9,5,323]
    l4 = hayDuplicados(x4)
    print("La lista", x4, "es", l4)
    y4 = [1,2,3,4,5,6,7,8]
    m4 = hayDuplicados(y4)
    print("La lista", y4, "es", m4)
    z4 = [67,5,6,78,7,2,1,1]
    n4 = hayDuplicados(z4)
    print("La lista", z4, "es", n4)

    # EJERCICIO 6
    print("Probando el ejercicio 6")
    x5 = [4,2,4,2,5,9,9,2,1]
    l5 = borrarDuplicados(x5)
    print("La lista", x5, "regresa la lista", l5)
    y5 = [1,2,3,4,5,1]
    m5 = borrarDuplicados(y5)
    print("La lista", y5, "regresa la lista", m5)
    z5 = [2,3,4,5,6]
    n5 = borrarDuplicados(z5)
    print("La lista", z5, "regresa la lista", n5)

main()