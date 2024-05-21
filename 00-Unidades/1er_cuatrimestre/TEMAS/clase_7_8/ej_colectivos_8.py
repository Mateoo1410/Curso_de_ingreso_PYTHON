import random

def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]: 4}', end='')

        print("")

# Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado 
# aleatoriamente).
# Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
# Menú:
# Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe 
#cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. 
#Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
# Mostrar la recaudación de todos los coches y líneas.
# Calcular y mostrar recaudación por línea.
# Calcular y mostrar recaudación por coche.
# Calcular y mostrar la recaudación total.
# Salir
# Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.

matriz_colectivo = [[100, 1, 2, 3, 4, 5],
                    [23, 1, 2, 3, 4, 5],
                    [33, 1, 2, 3, 4, 5]]

matriz_choferes = [[0]* 5 for _ in range(3)]

def brindar_legajos (matriz_vacia:list) -> list:

    legajo = random.randint(0, 1000)

    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):

            legajo += 1

            matriz_vacia[i][j] = legajo


    return matriz_vacia
    
brindar_legajos(matriz_choferes)

print("legajos existentes")

mostrar_matriz(matriz_choferes)

def validar_legajo (legajo: int, matriz: list)-> bool:
    for i in range(len (matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == legajo:
                return True
    return False

def validar_linea (linea: int, matriz: int)-> bool:

    for i in range(len(matriz)):
        if matriz[i][0] == linea:
            return True
    return False

def validar_coche (coche: int, matriz: list)-> bool:

    for i in range (len(matriz)):
        for j in range (1, len(matriz[i])):
            if matriz[i][j] == coche:
                return True
    return False

def cargar_planilla(matriz: list):
    
    legajo = int(input("Por favor ingrese su legajo: "))

    validacion = validar_legajo(legajo, matriz)

    while validacion == False:
        legajo = int(input("Por favor ingrese un legajo válido: "))
        validacion = validar_legajo(legajo, matriz)

    continuar = "si"
    while True:
        linea = int(input("Ingrese la línea de colectivos: "))
        validacion_linea = validar_linea(linea,matriz)

        while validacion_linea == False:
            linea = int(input("Ingrese la línea de colectivos: "))
            validacion_linea = validar_linea(linea,matriz)

        coche = int(input("Ingrese el número de coche: "))
        validacion_coche = validar_coche(coche, matriz)

        while validacion_coche == False:
            coche = int(input("Ingrese el número de coche: "))
            validacion_coche = validar_coche(coche, matriz)

        recaudacion = int(input("Ingrese la recaudación: "))
        

        continuar = input("¿Desea continuar? si/no: ")

        if continuar != "si":
            break



   

menu = print("""
    A)Cargar planilla         
    B)Mostrar la recaudación de todos los coches y líneas.
    C)Calcular y mostrar recaudación por línea.
    D)Calcular y mostrar recaudación por coche.
    E)Calcular y mostrar la recaudación total.
    F)Salir""")

bandera_validar = False

while True:
    opcion = input("Elegir una de estas opciones: ")

    match opcion:
        case "A": 
            bandera_validar = True
            
        case "B":
            if bandera_validar == True :
                pass
            else:
                print("Ingrese opcion A")
            
        case "C":
            if bandera_validar == True :
                pass
            else:
                print("Ingrese opcion A")
            
        case "D":
            if bandera_validar == True :
                pass
            else:
                print("Ingrese opcion A")
            
        case "E":
            if bandera_validar == True :
                pass
            else:
                print("Ingrese opcion A")

        case "F":
            break
                    
                
                    
        case _:
            error = input("Error: ingrese una opción válida: ")
  
