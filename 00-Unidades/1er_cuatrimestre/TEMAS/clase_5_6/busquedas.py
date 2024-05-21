lista = [9,45,3,-3,10,-2,3,45]

#numero_buscado = 10

#def buscar_numero(lista: list, numero_buscado: int)->int:
#     retorno = -1       #-1 ya que un indice nunca va a empezar por -1
#     for i in range(len(lista)):
#         if numero_buscado == lista[i]:
#             retorno = i
#     return retorno
    
# numero_posicion = buscar_numero(lista, 10)
# print(f"El {numero_buscado} se encuentra en la posicion {numero_posicion+1}")
        
        #print(f"El numero se encuentra en el indice: {i}")  

#muestra la posicion del numero_buscado en el indice de listas


##### SUMA DE POSITIVOS ######

# def sumar_positivos(lista: list)->int:
#     acumulador_de_sumas = 0
#     for i in range(len(lista)):
#         if lista[i] > 0:
#             acumulador_de_sumas += lista[i]  #si el numero es positivo en la lista, se suma junto a los ortos
#     return acumulador_de_sumas

# suma_final = sumar_positivos(lista)
# print(f"La suma de todos los numeros positivos es = {suma_final}")


#print(acumulador_de_sumas)

########## MAXIMO #############

# def buscar_maximo(lista: list, numero_mayor: int)->int:
#     for i in range(len(lista)):
#         if i == 0 or lista[i] > numero_mayor:
#             numero_mayor = lista[i]   #numero dentro del indice
#             #indice_maximo = i         #indice
#     return numero_mayor

# numero_final = buscar_maximo(lista, 1)
# print("El mayor numero de la lista es: {numero_final}")     #FALTA COMO PASARLO A FUNCIONES

#print(f"El numero maximo es {numero_mayor} se encuentra en la posicion {indice_maximo+1}")

#para mostrar el maximo no pongo bandera, se guarda el primer numero ya que la lista siempre va a iniciar en el indice 0


####### BUSCAR Y REEMPLAZAR ###########



def busca_remplazar(lista: list, numero_buscado: int, reemplazo: int)->list:
    
    for i in range(len(lista)):
        if lista[i] == numero_buscado:
            lista[i] = reemplazo    #si el indice es == 3 entoces el indice reemplaza el numero por el 11
    return lista

def mostrar_lista(lista:list)->None:   #funcion para imprimir la lista del retorno
    for i in range(len(lista)):
        print(lista[i])


mostrar_lista(busca_remplazar(lista, 3, 11))

# for i in range(len(lista)):
#     print(lista[i])