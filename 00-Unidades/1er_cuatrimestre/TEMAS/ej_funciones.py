def get_int(numero:int, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int | None:
    iteraciones = 0

    numero = input(numero)
    numero = int(numero)   #se muestra el mensaje y se parcea el mensaje ya que tienen que ingresar un entero
    while numero < minimo or numero > maximo:
        iteraciones += 1
        if iteraciones == reintentos:  #si iteraciones llega a 3 se rompe el while
            return None
        numero = input(mensaje_error)
        numero = int(numero)

    return numero

print(get_int("Ingrese su altura: ", "Error, reingrese su altura: ", 1, 250, 3))

#en el print se muestra todo en orden, mensaje, mensaje_error, minimo, maximo, reintentos.