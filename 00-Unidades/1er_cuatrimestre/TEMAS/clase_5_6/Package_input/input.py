from .validate import validate_number   #.validate el punto es para indicar que esta en la misma carpeta

def get_int(numero:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int | None:

    numero = int(input(numero))
    numero = validate_number(mensaje_error, numero, minimo, maximo, type, reintentos)

    if numero == None:
        print(mensaje_error)
        return None
    else:
        return numero

#print(get_int("Ingrese altura: ", "Error, reingrese su altura", 1, 220, 3))

    #falta utilizar la función len.

#.validate el punto es para indicar que esta el archivo en la misma carpeta
#..validate el doble punto para indicar que esta fuera de la carpeta el archivo