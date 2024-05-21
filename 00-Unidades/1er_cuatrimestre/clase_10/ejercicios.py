#1) Crear una función que reciba por parámetro una cadena y un caracter.
#La función deberá contar cuántas veces aparece dicho caracter en la cadena y retornar ese valor.


# def contar_caracteres(cadena:str, caracter:str):
#     "esta funcion va contando la cantidad de veces que aparece un caracter"
#     contador = 0
#     for i in range(len(cadena)):
#         if cadena[i] == caracter:
#             contador += 1
#     return contador

# cadena = "Hooola"
# print(contar_caracteres(cadena,"o"))


#2) Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.

# cadena = "Hola como estan"
# def retornar_indice(cadena: str, caracter: str)->int:

#     indice = -1
#     for i in range(len(cadena)):
#         if cadena[i] == caracter:
#             indice = i
#             break
        
#     return indice


# print(retornar_indice(cadena, "o"))


#3) Crear una función que reciba una cadena y retorne la misma pero al reverso.
# Ej: Si recibe la cadena “hola”, deberá retornar “aloh”.

cadena = "Hola"
def cadena_reverso(cadena: str)->str:

    cadena_reverso = ""
    for i in range(len(cadena) -1, -1, -1):
#-1 para empezar del ultimo indice -1 para recorrer a la inversa -1 para recorrer de 1 en 1
        cadena_reverso += cadena[i]
    
    return cadena_reverso

print(cadena_reverso(cadena))


#4) Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
cadena = "Hooola commmo essstan"
def suprimir_repetidos(cadena: str) -> str:
    "esta funcion lo que hace es borrar todos los caracteres que se repiten uno al lado del otro "
    cadena_sin_repetir = ""

    for i in range(len(cadena) - 1):
        if cadena[i] != cadena[i + 1]:
            cadena_sin_repetir += cadena[i]
    
    cadena_sin_repetir += cadena[i + 1]

    return cadena_sin_repetir



#5) Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
# Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.



#6) Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2
