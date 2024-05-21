from Package_input.input import get_int


"""Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
a. Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
b. Mostrar la cantidad de números positivos y negativos.
c. Mostrar la sumatoria de los números pares.
d. Informar el mayor de los números impares.
e. Imprimir todos los números ingresados.
f. Imprimir todos los números pares.
g. Imprimir los números de los índices impares.  
h. Salir

Notas:
Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario haya ingresado los datos solicitados.

Todas las opciones deberán ser programadas en funciones: habrá funciones específicas (por ejemplo para determinar si un número es positivo o negativo) y funciones de nivel general (por ejemplo una función que liste los números pares). Tener en cuenta las características de la programación funcional.

Las funciones específicas deberán estar en el módulo “Especificas.py”, mientras que las generales en el módulo “Array_Generales.py”. Todos estos módulos deben estar integrados en el paquete Package_Arrays.

Utilizar las funciones input del paquete Package_Input.
"""
##### A #####
lista = [-1] *10
validar = False

def seleccionar_a(lista:list)->None:
    for i in range(10):
        lista[i] = get_int("Ingrese 10 numeros: ", "Reingrese numero: ", -1000, 1000, 3)
    # for i in range(len(lista)):
    #     print(lista[i])

##### B #####
#se necesita validar la positividad (descompongo funciones)
def determinar_positividad(numero:int)->bool:  #bool es True y False
    retorno = None
    if numero > 0:
        retorno = True
    elif numero < 0:
        retorno = False
    return retorno


def contador_positivos_negativos(lista:list)->int:
    contador_positivos = 0
    contador_negativos = 0
    for i in range(len(lista)):
        if determinar_positividad(lista[i]) == True:
            contador_positivos += 1
        elif determinar_positividad(lista[i]) == False:
            contador_negativos += 1
    print(f"La cantidad de positivos es: {contador_positivos}, la cantidad de negativos es: {contador_negativos}")

##### C #####
def validar_pariedad(numero: int)->bool:
    par = False
    if numero % 2 == 0:
        par = True
    return par

def sumar_pares(lista:list)->None:
    acumulador_pares = 0
    for i in range(len(lista)):
        if validar_pariedad(lista[i]) == True:
            acumulador_pares += lista[i]
    
    print(acumulador_pares)



while True:
    print("""Elija una de las siguientes opciones:
            A. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
            B. Mostrar la cantidad de números positivos y negativos.
            C. Mostrar la sumatoria de los números pares.
            D. Informar el mayor de los números impares.
            E. Imprimir todos los números ingresados.
            F. Imprimir todos los números pares.
            G. Imprimir los números de los índices impares.
            H. Salir. """)
    
    opcion = input("")

    match(opcion):
        case "A":
            seleccionar_a(lista)
            validar = True
        case "B":
            if validar == True:
                contador_positivos_negativos(lista)
            else:
                print("No se ingresaron los datos en el punto A")
        case "C":
            if validar == True:
                sumar_pares(lista)
            else:
                print("No se ingresaron los datos en el punto A")
        case "D":
            pass
        case "E":
            pass
        case "F":
            pass
        case "G":
            pass
        case "H":
            break
        case _:   #en caso que no sea nada de eso
            opcion = print("Ingrese una opcion valida: ")