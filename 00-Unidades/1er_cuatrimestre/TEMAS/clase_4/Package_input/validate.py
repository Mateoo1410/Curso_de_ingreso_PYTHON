def validate_number(numero:str | float, mensaje_error:str, minimo:int | float, maximo:int | float, reintentos:int, tipo_de_dato:str)-> int | None:
    iteraciones = 0


    while numero < minimo or numero > maximo:
        iteraciones += 1
        if iteraciones == reintentos:  #si iteraciones llega a 3 se rompe el while
            return None
        numero = input(mensaje_error)
        if tipo_de_dato == "int":
            numero = int(numero)
        else:
            numero = float(numero)   

    return numero