def calcular_altura(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int | None:
    iteraciones = 0

    mensaje = input(mensaje)
    mensaje = int(mensaje)   #se muestra el mensaje y se parcea el mensaje ya que tienen que ingresar un entero
    while mensaje < minimo or mensaje > maximo:
        iteraciones += 1
        if iteraciones == reintentos:  #si iteraciones llega a 3 se rompe el while
            return None
        mensaje = input(mensaje_error)
        mensaje = int(mensaje)

    return mensaje

print(calcular_altura("Ingrese su altura: ", "Error, reingrese su altura: ", 1, 250, 3))

#en el print se muestra todo en orden, mensaje, mensaje_error, minimo, maximo, reintentos.