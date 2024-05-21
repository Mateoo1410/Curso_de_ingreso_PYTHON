


matriz_ej =[[1,2,3],
            [4,5,6],
            [7,8,9]]

#lista = [1.2,3,4,5]

M = 3  #columnas
N = 4  #filas

matriz = [[0]*M for _ in range(N)]  #se crea una lista de 3*4, el _ ya que no es variable de control
#por cada iteracion del for in range se va creando una nueva lista

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:4}", end=" ")
    print("")

#CARGA SECUENCIAL
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        numero = int(input(f"Ingrese un numero a cargar en la fila {i+1} y en la columna {j+1}: "))
        matriz[i][j] = numero

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:4}", end=" ")
        print("")



#print matriz [i][j] para imprimir filas y columnas
#end para imprimir con espacios los numeros y se agrega un print vacio abajo para imprimir las matrices separadas
#f"{matriz[i][j]:4}" esto es para dejarles 4 espacios a cada numero asi se ordenan
