#COLUMNAS

# matriz =[[1,2,3,10],
#         [4,5,6,11],
#         [7,6,9,12]]

# for j in range(len(matriz[0])):   #con eso ya se sabe el numero de columnas
#     print(f"Columna: {j+1}")
#     for i in range(len(matriz)):  #con esto recorre la contidad de filas 
#         print(f"{matriz[i][j]: 4}")



#MULTIPLICACION ESCALADA
def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]: 4}", end=" ")
        print("")


# ESCALAR = 5

# matriz =[[1,2,3],
#         [4,5,6],
#         [7,6,9]]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         matriz[i][j] = matriz[i][j] * ESCALAR

# mostrar_matriz(matriz)

#SUMA DE MATRICES



#SUMA MATRICES

matriz =[[1,2,3],
        [4,5,6],
        [7,6,9]]

matriz_auxiliar=[[10,20,30],
                [40,50,60],
                [70,60,90]]

matriz_resultado = [[0]*3 for _ in range(3)]  #se crea esta variable para guardar el resultado de la suma de matrices

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz_resultado = matriz[i][j] + matriz_auxiliar[i][j]

mostrar_matriz(matriz_resultado)