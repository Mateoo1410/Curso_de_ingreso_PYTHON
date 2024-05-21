


#1) Escribir una funcion que reciba una lista de enteros, la misma calculara y devolvera el promedio de todos los numeros.
#CUANDO DICE DEVOLVERA TIENE QUE HABER UN RETURN

#lista = [2,2,2]
# def calcular_promedio(lista:list)->int | float:
#     suma_entros = 0
#     promedio = 0
#     for i in range(len(lista)):
#         suma_entros += lista[i]

#     promedio = suma_entros / len(lista)  #esto para que sepa la cantidad de n° de la lista y lo divida para sacar el promedio
    
#     return promedio

#promedio = calcular_promedio(lista)
#print(promedio)

#2) Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

# lista = [2,2,2]
# def calcular_promedio_positivos(lista: list)->int | float:
#     suma_positivos = 0
#     contador_positivos = 0
#     promedio = 0
#     for i in range(len(lista)):
#         if lista[i] > 0:
#             suma_positivos += lista[i]
#             contador_positivos += 1
    
#     if contador_positivos > 0:
#         promedio = suma_positivos / contador_positivos
#     return promedio

# print(calcular_promedio_positivos(lista))

#3) Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
# lista = [5,-2,2]

# def calcular_producto(lista:list)->int:
#     producto = 1
#     for i in range(len(lista)):
#         producto *= lista[i]
#     return producto

# print(calcular_producto(lista))


#4) Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
# lista = [2,5,10]

# def buscar_maximo(lista:list)->int:
#     for i in range(len(lista)):
#         if i == 0 or lista[i] > numero_maximo:
#             numero_maximo = lista[i]
#             posicion_maximo = i + 1   #esto ya que pide la posicion, no el indice
#     return posicion_maximo

# print(buscar_maximo(lista))


#5) Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

# lista = [2,5,10]

# def buscar_maximo_entero(lista:list)->None:
#     for i in range(len(lista)):
#         if i == 0 or lista[i] > numero_maximo:
#             numero_maximo = lista[i]
    
#     for i in range(len(lista)):
#         if numero_maximo == lista[i]:
#             posicion = i + 1
            
#             print(f"El numero maximo es {numero_maximo} y se encuentra en la posicion {posicion}")
# buscar_maximo_entero(lista)



#6) Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.

lista_nombres = ["Mateo", "Santiago", "Carlos", "Jose"]

def reemplazar_nombres(lista_nombres:list, buscar:str, reemplazar:str)->int:
    cambios = 0

    for i in range(len(lista_nombres)):
        if lista_nombres == buscar:
            lista_nombres = reemplazar
            cambios += 1
    return cambios

print(reemplazar_nombres(lista_nombres, "Jose", "Mateo"))

# NO SE PORQUE ME IMPRIME 0, TENDRIA QUE INGRESAR LA CANTIDAD DE CAMBIOS QUE ES 1