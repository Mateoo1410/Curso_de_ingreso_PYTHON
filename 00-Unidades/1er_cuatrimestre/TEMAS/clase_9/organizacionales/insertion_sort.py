def insertion_sort(lista):
    for i in range(1, len(lista)):  #recorre el 1 del indice que comienza en 0
        intercambio = lista[i]
        rastreador = i - 1
        while rastreador >= 0 and lista[rastreador] > intercambio:
            lista[rastreador + 1] = lista[rastreador]
            rastreador -= 1
        lista[rastreador +1] = intercambio

lista = [12, 11, 13, 5, 6]
insertion_sort(lista)
print("La insersion es: ", lista)