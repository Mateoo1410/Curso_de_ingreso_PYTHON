# DESAFIO B: cuadrado magico
from Package_input.input import get_int

def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]: 4}", end=" ")
        print("")


filas_cuadrado = get_int("ingrese la cantidad de filas de la matriz: ", "Error,ingrese una cantidad de filas valida", 1, 10, 3)

columnas_cuadrado = get_int("ingrese la cantidad de columnas de la matriz: ", "Error,ingrese una cantidad de columndas valida", 1, 10, 3)

if filas_cuadrado == columnas_cuadrado:
    cuadrado_magico = [[0]*columnas_cuadrado for _ in range(filas_cuadrado)]

# Recorre la matriz y guarda los numeros ingresados por el usuario en sus respectivos lugares
    for i in range(len(cuadrado_magico)):
        for j in range(len(cuadrado_magico[i])):
            cuadrado_magico[i][j] = int(input(f"Ingrese un numero para la fila {i+1} y la columna {j}: "))
            mostrar_matriz(cuadrado_magico)

# Suma de filas
    for i in range(len(cuadrado_magico)):     #recorre filas
        suma_filas = 0
        for j in range(len(cuadrado_magico[i])): #recorre elementos
            suma_filas += cuadrado_magico[i][j]  #los va sumando


# Suma de columnas
    for j in range(len(cuadrado_magico[0])):  #lo mismo que en las filas pero con las columnas, empieza del indice 0
        suma_columnas = 0
        for i in range(len(cuadrado_magico)): #elementos de la columna
            suma_columnas += cuadrado_magico[i][j]


# Suma diagonal principal
    suma_diagonal_principal = 0
    for i in range(len(cuadrado_magico)):
        suma_diagonal_principal += cuadrado_magico[i][i] #al poner los 2 indices iguales va salteando filas y columnas de uno en uno, osea: 0,0


# Suma diagonal menor
    suma_diagonal_menor = 0
    fila = len(cuadrado_magico) - 1   #esto para que recorra las filas a la inversa, osea empieza desde la esquina inferior izquierda
    for i in range(len(cuadrado_magico)):
        suma_diagonal_menor += cuadrado_magico[fila][i]
        fila += -1   # resta para que vaya subiendo de filas y la i va recorriendo las columnas

# M = n*(n**2 +1)/2
    formula = filas_cuadrado*(filas_cuadrado**2 +1)/2
#esta formula sirve unicamente para matrices 3x3 un solo digito o para matrices  4x4 uno/dos digitos

    if suma_filas and suma_columnas and suma_diagonal_principal and suma_diagonal_menor == formula:
        print("Esta matriz es un cuadrado magico")

    else:
        print("Esta matriz no es un cuadrado magico")

else:
    print("No se puede realizar la matriz, ya que no cumple con la condicion para ser cuadrada")