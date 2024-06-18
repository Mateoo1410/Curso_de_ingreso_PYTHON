from informacion import lista_personajes

def stark_normalizar_datos(lista_personajes: list):
    """esta funcion lo que hace es, si se ingresa un dato numerico de forma str lo parcea.

    argumentos: lista_personajes (list): recibe como parametro una lista llena de diccionarios
    
    retorna un bool: True o False"""
    
    valor_de_la_funcion = False
    for i in range(len(lista_personajes)):
#convertir al tipo de dato correcto las keys
        if type(lista_personajes[i]["altura"]) != str:
            lista_personajes[i]["altura"] = float(lista_personajes[i] ["altura"])
            valor_de_la_funcion = True
        
        if type(lista_personajes[i]["peso"]) != str:
            lista_personajes[i]["peso"] = float(lista_personajes[i] ["peso"])
            valor_de_la_funcion = True
        
        if type(lista_personajes[i]["fuerza"]) != str:
            lista_personajes[i]["fuerza"] = int(lista_personajes[i] ["fuerza"])
            valor_de_la_funcion = True
    
    return valor_de_la_funcion

def obtener_dato(diccionario:dict, clave:str):
#Validar siempre que el diccionario no esté vacío y que el mismo tenga la key recibida por parámetro
    retorno = diccionario[clave]

    if diccionario[clave] == "":
        retorno = False
    return retorno
