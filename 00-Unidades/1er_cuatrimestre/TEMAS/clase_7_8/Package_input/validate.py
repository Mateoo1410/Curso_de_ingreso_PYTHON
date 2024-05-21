def validate_number(mensaje_error:str, numero: int,minimo:int | float, maximo:int | float, type , reintentos:int)-> int | None:


    for _ in range(reintentos):
        if numero < minimo or numero > maximo:
            numero = int(input(mensaje_error))

    if type == "int":
        numero = int(numero)
        return numero
    else:
        if type == "float":
            numero = float(numero)
            return numero
        
def validate_legth(texto, mensaje_error, minimo, maximo, reintentos):
    longitud = len(texto)

    for _ in range(reintentos):
        if longitud < minimo or longitud > maximo:
            texto = input(mensaje_error)
            longitud = len(texto)
        else:
            return texto