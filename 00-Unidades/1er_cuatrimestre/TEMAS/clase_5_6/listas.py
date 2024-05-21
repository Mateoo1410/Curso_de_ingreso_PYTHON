#mi_lista = [23, 5, 45, 30, 14]
#mi_lista = list()


#for i in range(len(mi_lista)):  #de esta forma se muestran todos los indices de la lista
    #print(mi_lista[i])          #muestra todos los numeros/str que aparecen en la lista



#carga secuencial
mi_lista2 = [-1] * 5  #para asignarle los indices a la lista

for i in range(len(mi_lista2)):  
    print(mi_lista2[i])
    numero = int(input(f"Ingrese un numero para colocar la posicion {i+1}: ")) #se le suma 1 para iniciar el conteo desde 1
    mi_lista2[i] = numero  #se reemplaza el indice de la lista al numero nuevo ingresado

for i in range(len(mi_lista2)):
    print(mi_lista2[i])  #esto para poder mostrar los nuevos numeros ingresados en el indice