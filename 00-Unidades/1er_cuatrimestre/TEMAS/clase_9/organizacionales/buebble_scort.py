def mostrar_lista(lista:list)-> None:
    for i in range(len(lista)):
        print(lista[i], end='')

def bubble_sort(lista:list):
    for j in range(len(lista)):        #para que le de vueltas a la lista completa
        intercambio = False
        for i in range(len(lista)-1 -j):
            if lista[i] > lista[i+1]:  #esto para que se compare con el de al lado, osea de a pares
                auxiliar = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxiliar
                intercambio = True
        if intercambio == True:
            break 

#-1 para que no se vaya de rango y se compare con un num inexistente
#-j para que cuando el numero final queda bien ordenado, no lo siga comparando

numeros = [34, 25, 12, 64, 22, 11, 90]

mostrar_lista(numeros)
print("---------------")
bubble_sort(numeros)
mostrar_lista(numeros)