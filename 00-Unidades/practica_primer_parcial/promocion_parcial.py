# El programa debe contar con un menú de las siguientes características:
# 1. Dar de alta. Pedirá los datos necesarios y dará de alta a una nueva película, asignando
# un ID único autoincremental.
# 2. Modificar. Permitirá alterar cualquier dato de la película excepto su ID. Se usará el título
# para identificar la película a modificar. Se mostrará un submenú para seleccionar qué
# datos modificar. Se indicará si se realizaron modificaciones (y cuales) o no.
# 3. Eliminar. Eliminará permanentemente a una película del listado original. Se pedirá el
# título de la película a eliminar.
# 4. Mostrar películas. Ofrecer la opción de mostrar las películas en base a determinados
# filtros.
# a. Todas las películas.
# b. De determinado género.
# c. De determinado año.
# d. Todas las ATP
# e. Todas las No ATP.
# Imprimirá por consola la información de las películas en formato de tabla:
# 5. Ordenar películas. Ofrecer la opción de ordenar y mostrar la lista de películas de forma
# ascendente o descendente por:
# a. Título.
# b. Género.
# c. Año de lanzamiento.
# d. Duración.
# 6. Buscar película por título: Permitir al usuario buscar y mostrar la información de una
# película específica ingresando su título.
# 7. Calcular promedio: Mostrar un submenú que permita calcular y mostrar el promedio
# de:
# a. Año de lanzamiento.
# b. Duración de películas.
# 8. Calcular porcentaje:
# a. Porcentaje por género.
# b. Porcentaje por ATP.
# 9. Salir. Terminará la ejecución del programa.

import math


lista_peliculas = []
### DAR EL ALTA ###
def dar_de_alta(lista_peliculas:list)-> None:
    """Le pide al usuario ingresar una serie de datos para poder crear y agregar una nueva pelicula a la lista

    Args:
        lista_peliculas (list): variable donde se guarda la pelicula agregada
    """
    lista_plataformas = []
    id = int
    if len(lista_peliculas) == 0:
        id = 1
    else:
        indice_ultima_pelicula = len(lista_peliculas)-1  #se consigue el indice de la ultima pelicula
        id_ultima_pelicula = lista_peliculas[indice_ultima_pelicula]["Id"]
        id = id_ultima_pelicula +1  #evita que se repita la id sumandole 1
    titulo = validar_titulo("Ingrese titulo de la pelicula: ", False)
    Genero = validar_genero()
    fecha_lanzamiento = validar_fecha_lanzamiento()
    duracion = validar_duracion()
    atp = validar_ATP()
    plataforma = validar_plataformas()
    lista_plataformas.append(plataforma)
    pelicula = {"Id": id,
                "Titulo": titulo,
            	"Genero": Genero,
                "Fecha lanzamiento": fecha_lanzamiento,
                "Duracion": duracion,
                "ATP": atp,
                "Plataformas": lista_plataformas}
    lista_peliculas.append(pelicula)


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
### DAR EL ALTA ###


### MODIFICAR ###
def modificar_pelicula(lista_peliculas:list, titulo:str)->None:
    """Esta funcion busca las peliculas por titulo, si se encuentra esa pelicula se accede a ella para poder modificar sus datos

    Args:
        lista_peliculas (list): lista con todas las peliculas
        titulo (str): el titulo para buscar la pelicula dependiendo de su titulo
    """
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]["Titulo"] == titulo:   #busca un titulo que sea igual
            modificar_menu(lista_peliculas, i)       #encuentra el titulo y accede al menu para modificarlo
            return    #corta la funcion una vez encontrada la igualdad
    print("No existe esa pelicula.")
    
def modificar_menu(lista_peliculas:list, indice:int)->None:
    """Esta funcion arma un menu interactivo para que el usuario pueda modificar el titulo, genero, fecha de lanzamiento, duracion y ATP de la pelicula. Luego se guardan los cambios hechos en la lista y se informan los cambios realizados.

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
        indice (int): el indice es para poder dividir las peliculas segun sus distintos datos(titulo, genero, fecha de lanzamiento, duracion y ATP)
    """
    bandera = True
    while bandera:
        print("1: Titulo.")
        print("2: Genero.")
        print("3: Fecha lanzamiento.")
        print("4: Duracion.")
        print("5: ATP.")
        print("6: Modificar plataformas.")
        seleccion = input("Ingrese opcion para modificar: ")
        match (seleccion):
            case "1":
                titulo = validar_titulo("Ingrese nombre nuevo para la pelicula: ", True)
                titulo_anterior = lista_peliculas[indice]["Titulo"]  #guarda el titulo anterior para mostrarlo en el print
                lista_peliculas[indice]["Titulo"] = titulo
                print(f"Se modifico el titulo de {titulo_anterior} a: {titulo}")
                bandera = False
            case "2":
                genero = validar_genero()
                genero_anterior = lista_peliculas[indice]["Genero"]
                lista_peliculas[indice]["Genero"] = genero
                print(f"Se modifico el genero de {genero_anterior} a: {genero}")
            case "3":
                fecha_lanzamiento = validar_fecha_lanzamiento()
                fecha_anterior = lista_peliculas[indice]["Fecha lanzamiento"]
                lista_peliculas[indice]["Fecha lanzamiento"] = fecha_lanzamiento
                print(f"Se modifico la fecha de lanzamiento de {fecha_anterior} a: {fecha_lanzamiento}")
                bandera = False
            case "4":
                duracion = validar_duracion()
                duracion_anterior = lista_peliculas[indice]["Duracion"]
                lista_peliculas[indice]["Duracion"] = duracion
                print(f"Se modifico la duracion de {duracion_anterior} a: {duracion}")
                bandera = False
            case "5":
                atp = validar_ATP()
                atp_anterior = lista_peliculas[indice]["ATP"]
                lista_peliculas[indice]["ATP"] = atp
                print(f"Se modifico el ATP anterior {atp_anterior} a: {atp}")
                bandera = False
            case "6":
                submenu_modificar_plataforma(lista_peliculas,indice)
                bandera = False
            case _:
                print("Error, ingrese una opcion valida: ")

### MODIFICAR ###

### ELIMINAR ###

def eliminar_pelicula(lista_peliculas: list)->None:
    """Esta funcion se encarga de eliminar una pelicula segun su titulo

    Args:
        lista_peliculas (list): lista con todas las peliculas
    """
    titulo = validar_titulo("Ingrese nombre de la pelicula que desea eliminar: ", True)
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]["Titulo"] == titulo:
            lista_peliculas.pop(i)    #elimina el indice que mandas
            break

### ELIMINAR ###

### MOSTRAR ###

def mostrar_peliculas(lista_peliculas:list)->None:
    """Esta funcion muestra todas las peliculas de la lista con todos sus datos

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
    """
    if lista_peliculas == []:
        print("No se encontraron peliculas")
        return
    encabezado = ["Título", "Género", "Año de lanzamiento", "Duración", "ATP","Plataforma"]
    separador = "*" * 160
    print(separador)
    print(f"| {' | '.join(encabezado)} |")
    for i in range(len(lista_peliculas)):
        id = lista_peliculas[i]["Id"]
        titulo = lista_peliculas[i]["Titulo"]
        genero = lista_peliculas[i]["Genero"]
        fecha_lanzamiento = lista_peliculas[i]["Fecha lanzamiento"]
        duracion = lista_peliculas[i]["Duracion"]
        atp = lista_peliculas[i]["ATP"]
        plataformas = lista_peliculas[i]["Plataformas"]
        plataformas_txt = ""
        for j in range(len(plataformas)):
            plataformas_txt += plataformas[j] + "-"

        if atp == True:
            atp = "Si"
        else:
            atp = "No"
        print(f"| {titulo:<50} | {genero:<30} | {fecha_lanzamiento:<5} | {duracion:<5} | {atp:<3} | {plataformas_txt:<35} |")
        print(separador)
        

def buscar_peliculas(lista_peliculas:list, clave:str, valor_buscado:str)->list:
    """Esta funcion busca la pelicula por titulo, la clave(ej:duracion) y el valor buscado(ej:30 si es de duracion). Todo esto para despues utilizar la funcion en un menu y buscar peliculas con distintas claves

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
        clave (str): se refiere al los distintos datos de las peliculas (titulo, genero, fecha de lanzamiento, duracion y ATP)
        valor_buscado (str): se refiere al dato final buscado a partir de la clave (bambi, maravilloso, 1999, 120, si)

    Returns:
        list: Retorna lista con los datos buscados
    """
    peliculas_buscadas = []
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i][clave] == valor_buscado:
            peliculas_buscadas.append(lista_peliculas[i])
    return peliculas_buscadas


def menu_peliculas_buscadas(lista_peliculas:list)->None:
    """Esta funcion arma un menu de opciones para ordenar de distintas maneras las peliculas, esto lo hace a traves de la funcion de buscar_peliculas y agregando los parametros depende del tipo de orden que se desee.

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
    """
    bandera = True
    pelicula_buscada = None
    while bandera:
        print("A: Todas las películas.")
        print("B: De determinado género.")
        print("C: De determinado año.")
        print("D: Todas las ATP.")
        print("E: Todas las No ATP.")
        print("F: De determinada plataforma")
        pelicula_buscada = input("Ingrese una de las opciones para mostrar peliculas: ")
        match(pelicula_buscada):
            case "A":
                mostrar_peliculas(lista_peliculas)
                bandera = False
            case "B":
                genero = validar_genero()
                genero_pelicula = buscar_peliculas(lista_peliculas, "Genero", genero)
                mostrar_peliculas(genero_pelicula)
                bandera = False
            case "C":
                año = validar_fecha_lanzamiento()
                año_pelicula = buscar_peliculas(lista_peliculas, "Fecha lanzamiento", año)
                mostrar_peliculas(año_pelicula)
                bandera = False
            case "D":
                atp = buscar_peliculas(lista_peliculas, "ATP", True)   #solo muestra las peliculas que estan dentro del diccionario "ATP" True
                mostrar_peliculas(atp)
                bandera = False
            case "E":
                no_atp = buscar_peliculas(lista_peliculas, "ATP", False)
                mostrar_peliculas(no_atp)
                bandera = False
            case "F":
                plataforma_buscada = input("Ingrese plataforma buscada: ")
                plataforma = buscar_plataforma(lista_peliculas, plataforma_buscada)
                mostrar_peliculas(plataforma)
                bandera = False
            case _:
                print("Error, ingrese una opcion valida: ")

### MOSTRAR ###

### ORDENAR ###

def menu_ordenamiento(lista_peliculas:list)->None:
    """Esta funcion crea un menu interactivo el cual funciona para ordernar de forma ascendente y descendente el titulo, genero, fecha lanzamiento y duracion de las peliculas

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
    """
    bandera = True
    seleccion = None
    while bandera:
        print("1: Titulo ascendente")
        print("2: Titulo descendente")
        print("3: Genero ascendente")
        print("4: Genero descendente")
        print("5: Fecha lanzamiento ascendente")
        print("6: Fecha lanzamiento descendente")
        print("7: Duracion descendente")
        print("8: Duracion descendente")
        seleccion = input("Ingrese opcion para modificar: ")
        match (seleccion):
            case "1":
                bubble_sort_ascendente(lista_peliculas,"Titulo")
                bandera = False
            case "2":
                bubble_sort_descendente(lista_peliculas,"Titulo")
                bandera = False
            case "3":
                bubble_sort_ascendente(lista_peliculas,"Genero")
                bandera = False
            case "4":
                bubble_sort_descendente(lista_peliculas,"Genero")
                bandera = False
            case "5":
                bubble_sort_ascendente(lista_peliculas,"Fecha lanzamiento")
                bandera = False
            case "6":
                bubble_sort_descendente(lista_peliculas,"Fecha lanzamiento")
                bandera = False
            case "7":
                bubble_sort_descendente(lista_peliculas,"Duracion")
                bandera = False
            case "8":
                bubble_sort_descendente(lista_peliculas,"Duracion")
                bandera = False
            case _:
                print("Error, ingrese una opcion valida: ")

def bubble_sort_ascendente(lista:list,parametro:str)->None:
    """Esta funcion ordena de forma ascendente una lista.

    Args:
        lista (list): lista con todas las peliculas ingresadas
        parametro (str): dentro de este parametro se ingresa el (titulo, genero, fecha de lanzamiento, duracion y ATP)
    """
    for j in range(len(lista)):
        for i in range(len(lista)-1 -j):
            if lista[i][parametro] > lista[i+1][parametro]:
                auxiliar = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxiliar

def bubble_sort_descendente(lista:list,parametro:str)->None:
    """Esta funcion ordena de forma descendente una lista.

    Args:
        lista (list): lista con todas las peliculas ingresadas
        parametro (str): dentro de este parametro se ingresa el titulo, genero, fecha de lanzamiento, duracion y ATP
    """
    for j in range(len(lista)):
        for i in range(len(lista)-1 -j):
            if lista[i][parametro] < lista[i+1][parametro]:
                auxiliar = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxiliar

### ORDENAR ###

### PROMEDIO ###

def menu_promedios(lista_peliculas:list)->None:
    """Esta funcion crea un submenu en el cual se muestra el promedio de las fechas de lanzamiento y la duracion de las peliculas.Calculandolo con la funcion calcular_promedio.

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
    """
    bandera = True
    pelicula_promedio = None
    while bandera:
        print("1: Año de lanzamiento.")
        print("2: Duración de peliculas.")
        pelicula_promedio = input("Que promedio desea ver?: ")
        match(pelicula_promedio):
            case "1":
                promedio_lanzamiento = calcular_promedio(lista_peliculas, "Fecha lanzamiento")
                print(f"El promedio de la fecha de lanzamiento es: {promedio_lanzamiento}")
                bandera = False
            case "2":
                promedio_duracion = calcular_promedio(lista_peliculas, "Duracion")
                print(f"El promedio de duracion de las peliculas es de: {promedio_duracion}")
                bandera = False
            case _:
                print("Error, ingrese una opcion valida: ")



def	calcular_promedio(lista_peliculas:list, clave:str)->int:
    """Esta funcio se encarga de calcular promedios y de redondearlos para abajo para que no den con decimal

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
        clave (str): en la clave se ingresa el titulo, genero, fecha de lanzamiento, duracion y ATP de la pelicula

    Returns:
        int: retorna el promedio en forma de numero entero
    """
    acumulador = 0
    for i in range(len(lista_peliculas)):
        acumulador += lista_peliculas[i][clave]
    promedio = acumulador/len(lista_peliculas)
    promedio = math.floor(promedio)              #esto para que no de con decimales, redondea para abajo
    return promedio

### PROMEDIO ###

### PORCENTAJE ###

def calcular_porcentaje_atp(lista_peliculas:list)->None:
    """Esta funcion se encarga de calcular el porcentaje de las peliculas que son ATP y las que no

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas

    Returns:
        int: Retorna el porcentaje en forma de numero entero
    """
    contador_atp = 0
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]["ATP"] == True:  #cuenta el True como parte del si
            contador_atp += 1
    porcentaje = (contador_atp *100) / len(lista_peliculas)
    porcentaje_final = 100 - porcentaje
    print(f"El porcentaje de las peliculas ATP es de: %{porcentaje}")  
    print(f"El porcentaje de no ATP es de: %{porcentaje_final}")


def calcular_porcentaje_genero(lista_peliculas:list,genero:str)->None:
    """Esta funcion se encarga de calcular exclusivamente el porcentaje de cada genero que haya en la lista

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
        genero (str): dentro de este parametro se ingresa el tipo de genero el cual se busca el porcentaje
    """
    contador_genero = 0
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]["Genero"] == genero:  #cuenta el True como parte del si
            contador_genero += 1
    porcentaje = (contador_genero *100) / len(lista_peliculas)
    print(f"El genero {genero} es un %{porcentaje} de todas las peliculas ingresadas")


def menu_porcentajes(lista_peliculas:list)->None:
    """Esta funcion se encarga de mostrar un submenu interactivo para mostrar los % de "ATP" y de "Genero"

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
    """
    bandera = True
    pelicula_porcentaje = None
    while bandera:
        print("1: Porcentaje por ATP.")
        print("2: Porcentaje por genero.")
        pelicula_porcentaje = input("Que porcentaje desea ver?: ")
        match(pelicula_porcentaje):
            case "1":
                calcular_porcentaje_atp(lista_peliculas)
                bandera = False
            case "2":
                genero_buscado = validar_genero()
                calcular_porcentaje_genero(lista_peliculas, genero_buscado)
                bandera = False
            case _:
                print("Error, ingrese una opcion valida: ")
### PORCENTAJE ###

### LEER CSV ###
def leer_peliculas_csv(lista_peliculas:list):
    """Esta funcion se encarga de leer el archivo de "peliculas.csv"

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
    """
    leer = open("00-Unidades/practica_primer_parcial/peliculas.csv","r",encoding="utf-8")#encondig para que no salga ningun error al leer el archivo
    leer_peliculas = leer.readlines()
    claves_peliculas = leer_peliculas[0]
    claves_peliculas = claves_peliculas.split(",") #guarda la primera fila donde estan las claves
    ultimo_indice = len(claves_peliculas)-1
    claves_peliculas[ultimo_indice] = claves_peliculas[ultimo_indice].replace("\n","")
    for i in range(1, len(leer_peliculas)):  #empieza de la fila 2, ya que la primera fila no hay que leerla
        diccionario = {}
        lista_lectura = leer_peliculas[i].split(",")  #elimina las , a la hora de leer la lista y separa los elementos
        for j in range(len(lista_lectura)):
            diccionario[claves_peliculas[j]] = lista_lectura[j]
            if lista_lectura[j] == "Si":
                lista_lectura[j] = True
            elif lista_lectura[j] == "No":
                lista_lectura[j] = False
        lista_peliculas.append(diccionario)
    leer.close()
#con la i se recorre la linea y con la j los elementos de la linea

def convertir_claves(lista_peliculas:list):
    """Esta funcion se encarga de transformar

    Args:
        lista_peliculas (list): lista con todas las peliculas ingresadas
    """
    for i in range(len(lista_peliculas)):
        lista_peliculas[i]["Id"] = int(lista_peliculas[i]["Id"])
        lista_peliculas[i]["Fecha lanzamiento"] = int(lista_peliculas[i]["Fecha lanzamiento"])
        lista_peliculas[i]["ATP"] = bool(lista_peliculas[i]["ATP"]) #no muestra las no atp
        lista_peliculas[i]["Duracion"] = int(lista_peliculas[i]["Duracion"])
        lista_peliculas[i]["Plataformas"] = lista_peliculas[i]["Plataformas"].replace("\n","")
        lista_peliculas[i]["Plataformas"] = lista_peliculas[i]["Plataformas"].split("-")

#cerrar el archivo (archivo.close)

def guardar_datos_csv(lista_peliculas:list):
    guardar = open("00-Unidades/practica_primer_parcial/peliculas.csv", "w",encoding="utf-8")
    clave = "Id,Titulo,Genero,Fecha lanzamiento,Duracion,ATP,Plataformas\n"
    guardar.write(clave)                  #esto para ponerlo una sola vez, arriba de todo el archivo
    ultimo_indice = len(lista_peliculas)-1
    for i in range(len(lista_peliculas)):
        id = lista_peliculas[i]["Id"]
        titulo = lista_peliculas[i]["Titulo"]
        genero = lista_peliculas[i]["Genero"]
        fecha_lanzamiento = lista_peliculas[i]["Fecha lanzamiento"]
        duracion = lista_peliculas[i]["Duracion"]
        atp = lista_peliculas[i]["ATP"]
        if atp == True:
            atp = "Si"
        else:
            atp = "No"
        plataformas = lista_peliculas[i]["Plataformas"]
        plataformas_txt = ""
        
        for j in range(len(plataformas)):
            
            indice_ultima_pelicula = len(plataformas)-1
            if j == indice_ultima_pelicula:
                plataformas_txt += f"{plataformas[j]}"
            else:
                plataformas_txt += f"{plataformas[j]}-"


        escribir_datos = f"{id},{titulo},{genero},{fecha_lanzamiento},{duracion},{atp},{plataformas_txt}\n"
        if i == ultimo_indice:
            escribir_datos = escribir_datos.replace("\n","")
        guardar.write(escribir_datos)
    guardar.close()


def validar_plataformas():
    bandera = True
    while bandera:
        ingresar_plataformas = input("Ingrese nueva plataforma a la pelicula: ")
        if len(ingresar_plataformas) <= 20 and ingresar_plataformas.isnumeric() == False:
            print("Plataforma validada.")
            bandera = False
        else:
            print("Error, ingrese una plataforma valida(sin numero, sin exceder 20 caracteres): ")
    return ingresar_plataformas

def buscar_plataforma(lista_peliculas:list, valor_buscado:str):
    peliculas_buscadas = []
    for i in range(len(lista_peliculas)):
        for j in range(len(lista_peliculas[i]["Plataformas"])):
            if lista_peliculas[i]["Plataformas"][j] == valor_buscado:
                peliculas_buscadas.append(lista_peliculas[i])
    return peliculas_buscadas


def modificar_plataforma(lista_peliculas:str,plataforma:str,nueva_plataforma,indice:int):
    #recibe la plataforma que le quiere cambiar el nombre, y el nombre de la plataforma cambiado
        for i in range(len(lista_peliculas[indice]["Plataformas"])):
            if lista_peliculas[indice]["Plataformas"][i] == plataforma:
                lista_peliculas[indice]["Plataformas"][i] = nueva_plataforma
                print(f"Se cambio la plataforma{plataforma}, por {nueva_plataforma}.")
                return
        print("Error. Pelicula no encontrada: ")

def eliminar_plataforma(lista_peliculas:str,plataforma:str,indice:int):
        #indice es la pelicula, plataforma elemento a eliminar
        lista_peliculas[indice]["Plataformas"].remove(plataforma)


def validar_plataforma_modificada():
    bandera = True
    while bandera:
        ingresar_plataformas = input("Ingrese la nueva plataforma de la pelicula: ")
        if len(ingresar_plataformas) <= 20 and ingresar_plataformas.isnumeric() == False:
            bandera = False
        else:
            print("Error, ingrese una plataforma valida(sin numero, sin exceder 20 caracteres): ")
    return ingresar_plataformas




def submenu_modificar_plataforma(lista_peliculas:str,indice:int):
    bandera = True
    while bandera:
        print("1: Modificar plataformas.")
        print("2: Eliminar plataformas.")
        print("3: Agregar nueva plataforma.")
        seleccion = input("Que cambio desea realizar?: ")
        match(seleccion):
            case "1":
                plataforma = input("Ingrese plataforma que desea cambiar: ")
                plataforma_modificada = validar_plataforma_modificada()
                modificar_plataforma(lista_peliculas,plataforma,plataforma_modificada,indice)
                bandera = False
            case "2":
                plataforma = input("Ingrese plataforma que desea eliminar: ")
                eliminar_plataforma(lista_peliculas,plataforma,indice)
                bandera = False
            case "3":
                plataforma = validar_plataformas()
                crear_plataforma(lista_peliculas,plataforma,indice)
                break
            case _:
                print("Error, ingrese una opcion valida: ")

def crear_plataforma(lista_peliculas:str,nueva_plataforma:str,indice:int):
    lista_peliculas[indice]["Plataformas"].append(nueva_plataforma)
    while True != "2":
        print("1: Ingresar nueva plataforma.")
        print("2: Salir.")
        seleccion = input("Desea ingresar una nueva plataforma o salir?: ")
        match(seleccion):
            case "1":
                plataforma = validar_plataformas()
                crear_plataforma(lista_peliculas,plataforma,indice)
                break
            case "2":
                print("Saliendo...")
                break
            case _:
                print("Error, ingrese una opcion valida. ")


























def menu_principal()->None:
    """Esta funcion se encarga de todo el menu principal, encargado de llevarte por las distintas opciones y entrar a los demas submenus
    """
    usuario = None
    while usuario != "9":
        print("1: Dar de alta.")
        print("2: Modificar.")
        print("3: Eliminar.")
        print("4: Mostrar películas.")
        print("5: Ordenar películas.")
        print("6: Buscar película por título.")
        print("7: Calcular promedio.")
        print("8: Calcular porcentaje.")
        print("9: Guardar y salir.")
        usuario = input("Ingrese una opcion: ")
        match(usuario):
            case "1":
                dar_de_alta(lista_peliculas)
            case "2":
                titulo = validar_titulo("Ingrese titulo de la pelicula que desea modificar: ", True)
                modificar_pelicula(lista_peliculas, titulo)  #uso el validar titulo de la funcion anterior para encontrarlo
            case "3":
                eliminar_pelicula(lista_peliculas)
            case "4":
                menu_peliculas_buscadas(lista_peliculas)
            case "5":
                menu_ordenamiento(lista_peliculas)
            case "6":
                titulo_buscado = validar_titulo("Ingrese titulo de la pelicula que desea buscar: ",True)
                titulo = buscar_peliculas(lista_peliculas, "Titulo", titulo_buscado)
                mostrar_peliculas(titulo)   ### BUSCAR POR TITULO ###
            case "7":
                menu_promedios(lista_peliculas)
            case "8":
                menu_porcentajes(lista_peliculas)
            case "9":
                guardar_datos_csv(lista_peliculas)
                print("Guardado, gracias por usar el programa!")
            case _:
                print("Error, ingrese una opcion valida: ")


leer_peliculas_csv(lista_peliculas)
convertir_claves(lista_peliculas)
menu_principal()