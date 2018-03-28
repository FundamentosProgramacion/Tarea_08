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




def estanOrdenador(lista):
    for k in range(0, len(lista) - 1):
        if lista[k] < lista[k + 1]:
            x = True
            continue
        else:
            x = False
        print(x)
        break


def sonAnagramas(a,b):







def hayDuplicados():


    pass



def borrarDuplicados():

    pass



def main():
    "lista=[1,2,3]
    #sumarAcumulado(lista)
    #recortarLista(lista)


    #sonAnagramas("AMOR","ROMA")
    sonAnagramas(list[""])

main()