from Package_input.input import get_int

def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]: 4}", end=" ")
        print("")

filas_a = get_int("Ingrese la cantidad de filas que quiera tener en su matriz a: ", "Numero invalido", 1,100,3)
columnas_a = get_int("Ingrese la cantidad de columnas que quiera tener en su matriz a: ", "Numero invalido", 1,100,3)

matriz_vacia_a = [[0]* columnas_a for _ in range (filas_a)]   #esto va a hacer que se genere una matriz depende de lo que ingresa el usuario

filas_b = get_int("Ingrese la cantidad de filas que quiera tener en su matriz b: ", "Numero invalido", 1,100,3)
columnas_b = get_int("Ingrese la cantidad de columnas que quiera tener en su matriz b: ", "Numero invalido", 1,100,3)

matriz_vacia_b = [[0]* columnas_b for _ in range (filas_b)]

if columnas_a == filas_b:   #si se cumple esta regla se crea una matriz resultado y se multiplican
    matriz_resultado = [[0]* filas_a for _ in range(columnas_b)]

    for i in range(len(matriz_vacia_a)):
        for j in range(len(matriz_vacia_a[i])):

            matriz_vacia_a[i][j] = int(input(f"Ingrese un numero para la matriz A en la fila {i+1} y en la columna {j+1}: "))
            mostrar_matriz(matriz_vacia_a)

    for i in range(len(matriz_vacia_b)):
        for j in range(len(matriz_vacia_b[i])):

            matriz_vacia_b[i][j] = int(input(f"Ingrese un numero para la matriz B en la fila {i+1} y en la columna {j+1}: "))
            mostrar_matriz(matriz_vacia_b)

for i in range(len(matriz_vacia_a)):          #esta i para que cuando se multiplique la primera fila pase a la siguiente
    for j in range(len(matriz_vacia_b[0])):   #agarra la columna de la segunda matriz para multiplicarla
        for k in range(len(matriz_vacia_a)):  #agarra el siguiente valor de la fila para multiplicarla
            matriz_resultado[i][j] += matriz_vacia_a[i][k] * matriz_vacia_b[k][j]   #multiplicacion de matrices

#parara multiplicar las matrices se tienen que ir cambiando de fila en fila y de columna en columna

    print("RESULTADO: ")
    mostrar_matriz(matriz_resultado)

else:
    print("Esta multiplicacion no se puede realizar, intente nuevamente: ")

#nose xq me salta un error cuando quiero ingresar el segundo numero
#cuando ingreso el primer numero lo ingresa pero pone numero invalido