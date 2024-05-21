lista = [-1] * 5  #solo determina los espacios de la lista

respuesta = "Si"
largo_lista = len(lista)  #lee todos los espacios

while respuesta == "Si":

    posicion = int(input("Ingrese la posicion del numero a cargar: "))
    while posicion < 1 or posicion > largo_lista:   #largo_lista para que se pueda modificar amplitud de la lista
        posicion = int(input("Error, ingrese una posicion valida: "))

    numero = int(input("Ingrese el numero que desea cargar: "))

    lista[posicion -1] = numero   #asigna el indice de la lista por el nuevo numero ingresado, se pone -1 ya que el usuario ingresa 1, no 9

    respuesta = input("Desea continuar? Si/No: ")
    while respuesta != "Si" and respuesta != "No":
        respuesta = input("Desea continuar? Si/No: ")

for i in range(len(lista)):
    print(lista[i])    