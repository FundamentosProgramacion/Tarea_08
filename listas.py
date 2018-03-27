#Jossian Abimelec García Quijano

def sumarAcumulado(lista):
    nuevaLista=[]
    i=0
    for dato in lista:
        i += dato
        nuevaLista.append(i)
    print (nuevaLista)

    return nuevaLista


def recortarLista(lista):
    nuevaLista=[]
    for k in range(1,len(lista)-1):
        nuevaLista.append(lista[k])
        print(nuevaLista)




def estanOrdenador():

    pass


def sonAnagramas():
    pass





def hayDuplicados():


    pass



def borrarDuplicados():

    pass



def main():
    lista=[1,2,3]
    #sumarAcumulado(lista)

    recortarLista(lista)

main()