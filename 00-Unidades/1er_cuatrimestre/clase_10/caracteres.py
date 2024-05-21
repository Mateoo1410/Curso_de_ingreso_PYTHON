# DECLARACION E INDEXACION #

# cadena = "Hola como estan"
# print(id(cadena))

# cadena[0] = "H"
# print(id(cadena))
#las cadenas de caracteres son inmutables, lo que quiere decir que una vez creada no puede modificarse


# SLICING #

# cadena = "Hola Mundo"
# print(cadena[5:10]) # Mundo
# print(cadena[5:])   # Mundo
# print(cadena[:5])   # Hola
# print(cadena[0:])   # Hola Mundo
#cada espacio y cada caracter representa un indice


# USO DE LEN #

# cadena = "Hola"
# cadena_2 = "Hola como estan\n"

# print(cadena_2)
# print(len(cadena_2))
#lee toda la cadena e informa su cantidad de caracteres en ella


# CONCATENACION #

# cadena = "Hola"
# cadena_2 = "Mateo"

# # resultado = cadena + " " + cadena_2
# # resultado = f"{cadena} {cadena_2}"
# # print(resultado)

# cadena_2 += "2"
# print(cadena_2)
#varias formas de concatenar cadena de caracteres


# INMUTABILIDAD #

# cadena = "Hola"
# cadena[0] = "J"

# print(id(cadena))
# cadena = "J" + cadena[1:]
# print(id(cadena))
# print(cadena)
#como se marco en un principio, no se puede mutar una cadena de caracteres ya creada

# REPETICION #

# cadena = "Pedro"
# print(cadena *4 + cadena[0:2])

# COMPARACION #

# cadena = "ag"
# cadena_2 = "af"

# if cadena == cadena_2:
#     print("Se cumple")
# else:
#     print("No se cumple")
# #en la comparacion no se compara el valor ascci, sino caracter por caracter

# cadena = "hola"
# print(cadena == "hola")
# print(cadena != "hola")
# print(cadena == "Hola")
# print(cadena > "hola")  #False xq son iguales
# print(cadena < "azul")  #False xq la h(104) tiene un peso mayor que la a(97)
# print(cadena > "azul")  #True xq la h(104) tiene un peso mayor que la a(97)
# print(cadena > "Perro") #False xq las mayusculas son mas chicas que las minusculas

# char = "m"

# valor_ascci = ord(char)
# #la funcion ord sirve para saber el valor ascci del caracter
# valor_mayuscula = valor_ascci - 32
# #entre los valores de las minusculas y las mayusculas en la tabla ascci hay 32 caracteres de diferencia
# caracter = chr(valor_mayuscula)
# #la funcion chr convierte el valor ascci en un caracter
# print(caracter)


# EJERCICIO #

# cadena = "Hola como estan"

# for i in range(len(cadena)):
#     print(cadena[i], end="")

def reemplazar_caracteres(cadena: str, caracter:str, reemplazo: str):
    "esta funcion sirve para reemplazar un caracter en especifico"
    cadena_modificada = ""
    for i in range(len(cadena)):
        if cadena[i] != caracter:
            cadena_modificada += cadena[i]
        else:
            cadena_modificada += reemplazo
    
    return cadena_modificada


cadena = "Hola como estan"

print(reemplazar_caracteres(cadena, "o", "*"))
