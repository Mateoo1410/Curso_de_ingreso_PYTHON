################# FUNCIONES ENCARGADAS DE VALIDAR #################
from peliculas import *
def validar_titulo(mensaje:str,saltar:bool)->str:
    """Esta funcion sirve para validar que el titulo de la pelicula no exceda los 30 caracteres y que no se agregue otra pelicula con un nombre existente

    Args:
        mensaje (str): Mensaje para interactuar con el usuario y que este ingrese el titulo de la pelicula

    Returns:
        str: Retorna el titulo una vez que ya fue validado  
    """
    bandera = True
    while bandera:
        titulo = input(mensaje)
        if len(titulo) <= 30:
            bandera_2 = False
            for i in range(len(lista_peliculas)):
                if lista_peliculas[i]["Titulo"] == titulo and saltar == False: #si es False entra al if e indica que la pelicula ya existe
                    bandera_2 = True   #si se encuentra una igualdad la bandera pasa a True
                    break
            if bandera_2:  #si la bandera es True entonces sale un msj de error
                print("Error, ya existe esa pelicula. ")
            else:
                bandera = False
                return titulo  #si esta bien devuelve titulo
        else:
            print("Error, El nombre de la pelicula tiene que ser menor a 30 caracteres: ")
            bandera = False


def validar_genero()->str:
    """imprime la lista de generos, pregunta que genero quier ingresar el usuario, atomaticamente pone todo en minuscula menos la primera letra que va en mayuscula y verifica que el genero ingresado sea el correcto y este dentro de la lista

    Returns:
        str: Retorna genero una vez que se verifica
    """
    lista_genero = ["Acción", "Aventura", "Animación", "Biográfico", "Comedia", "Comedia" "romántica", "Comedia" "dramática",
"Crimen", "Documental", "Drama", "Fantasía", "Histórico", "Infantil", "Musical", "Misterio", "Policíaco", "Romance",
"Ciencia ficción", "Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental", "Familiar",
"Superhéroes", "Espionaje", "Artes marciales", "Fantástico", "Catástrofe", "Melodrama", "Erótico", "Cine independiente", 
"Zombies", "Vampiros", "Cyberpunk", "Steampunk", "Distopía", "Utopía", "Road Movie",
"Docuficción", "Mockumentary", "Gótico", "Slasher", "Adolescente", "Culto", "Maravilloso"]
    
    while True:
        print("El genero puede ser cualquiera de los siguientes: ")
        for i in range(len(lista_genero)):
            print(lista_genero[i],end=", ")
        genero = input("Ingrese genero de la pelicula: ")
        genero = genero.lower()  	  #pone todo en minuscula
        genero = genero.capitalize()  #pone la primera en mayuscula, esto es para hacerlo mas estetico
        for i in range(len(lista_genero)):
            if genero == lista_genero[i]:
                return genero
        print("Error, ingrese un genero valido: ")


def validar_fecha_lanzamiento()->int:
    """Esta funcion valida que lo que se ingresa sea un numero y que no sea menor que 1888 ni mayor que 2024

    Returns:
        int: Una vez que se valida la fecha de lanzamiento la retorna
    """
    while True:
        fecha_lanzamiento = input("Ingresar fecha de lanzamiento entre 1888 y el presente: ")
        if fecha_lanzamiento.isdigit():     #Comprueba que sea un numero
            fecha_lanzamiento = int(fecha_lanzamiento)
            if fecha_lanzamiento >= 1888 and fecha_lanzamiento <= 2024:
                return fecha_lanzamiento
        print("Error. ingrese una fecha valida: ")

def validar_duracion()->int:
    """Esta funcion comprueba que lo que se ingrese sea un numero y que ese numero no sea menor que 1

    Returns:
        int: Una vez validado el numero lo retorna, y ese numero es la duracion de la pelicula en minutos
    """
    while True:
        duracion = input("Ingresar duracion de la pelicula a partir de 1 minuto: ")
        if duracion.isdigit():     #Comprueba que sea un numero
            duracion = int(duracion)
            if duracion >= 1:
                return duracion
        print("Error, la pelicula no puede durar menos de 1 minuto: ")

def validar_ATP()->bool:
    """Esta funcion se encarga de preguntar si la pelicula es ATP, el True pasa a verse como Si y el False pasa a verse como No

    Returns:
        bool: Retorna Si(True) o No(False)
    """
    booleano = None
    while type(booleano) != bool:   #devuelve el tipo de la varieble, para confirmar que se trata de un bool y poder verificar el dato
        booleano = input("Ingrese si la pelicula es ATP o no: ")
        booleano = booleano.lower() 
        booleano = booleano.capitalize()
        if booleano == "Si":
            booleano = True
        elif booleano == "No":
            booleano = False
    return booleano


def validar_plataforma_modificada()->str:
    """Esta funcion valida que la plataforma que se ingrese no debe contener números y no debe exceder los 20 caracteres de longitud

    Returns:
        str: retorna el nombre de la plataforma ingresado por el usuario una vez que es válido
    """
    bandera = True
    while bandera:
        ingresar_plataformas = input("Ingrese la nueva plataforma de la pelicula: ")
        if len(ingresar_plataformas) <= 20 and ingresar_plataformas.isnumeric() == False:
            bandera = False
        else:
            print("Error, ingrese una plataforma valida(sin numero, sin exceder 20 caracteres): ")
    return ingresar_plataformas

def validar_plataformas(lista_peliculas:str,claves:str)->str:
    """Esta funcion se encarga de validar la entrada del usuario para una o más plataformas de una película. Esta misma no debe contener números y no debe exceder los 20 caracteres de longitud

    Returns:
        str: retorna el nombre de la plataforma ingresado por el usuario una vez que es válido
    """
    bandera = True
    while bandera:
        ingresar_plataformas = input("Ingrese la/s plataforma/s de la pelicula: ")
        if len(ingresar_plataformas) <= 20 and ingresar_plataformas.isnumeric() == False:
            print("Plataforma validada.")
            bandera = False
        else:
            print("Error, ingrese una plataforma valida(sin numero, sin exceder 20 caracteres): ")
    return ingresar_plataformas