'''
Funciones Parte I

1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
2. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
3. Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
4. Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables (que reciban el mensaje de pedido de datos por parámetro). Agregar validaciones.
5. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
6. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
7. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
8. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
'''


#1
def ingreso_numero_entero()-> int:
    numero = input("Ingrese un numero entero: ")
    numero = int(numero)
    return numero

print(ingreso_numero_entero())  #esto es en el caso de que me pida mostrarlo

#2
def ingreso_numero_float()-> float:
    numero = input("ingrese un numero float: ")
    return numero

#3
def solicitar_cadena()-> str:
    cadena = input("Ingrese una cadena de caracteres: ")
    return cadena

#4
def solicitar_entero(mensaje:str, rango_1=int, rango_2=int)-> int:
    numero = input(mensaje)
    numero = int(numero)
    while numero < rango_1 or numero > rango_2:   #VALIDACIONES
        numero = input(mensaje)
        numero = int(numero)
    return numero

mensaje = "Ingrese su edad: "
edad = solicitar_entero(mensaje, 1, 115) #se ejecuta el mensaje y si la altura es mas de 250 o menos que 1 entra en bucle
print(edad)
#EL 4 ES REUTILIZABLE YA QUE EL MENSAJE ESTA DENTRO DE LA FUNCION Y SE PUEDE CAMBIAR COMO QUIERAS

# 5
def area_circulo(radio)-> float:
    """esta funcion calcula el area de un circulo
    parametros: 
            radio: resive el radio del circulo
    retorna:
            area: devuelve el area del circulo"""
    pi = 3.14
    area = pi * radio**2
    return area

radio = input("Ingresar el radio: ")  #no pide el ejercicio un input, solo pide que reciba un numero
radio = int(radio)

area_del_circulo = (area_circulo(radio))
print(area_del_circulo)

#6
def indicar_pariedad(numero)-> None:  #no devuelve nada, el ejercicio pide que imprima el resultado (print)
    if numero % 2 == 0:
        mensaje= "es par"
    else:
        mensaje= "es impar"
    return mensaje
numero = input("Ingrese un numero: ") #se pone afuera de la funcion para despues tener el valor ingresado al parametro
numero = int(numero)
    
print(indicar_pariedad(numero))

#7
def IndicarMaximo(numero1, numero2, numero3):
    numeroMaximo = numero1  #podria ser cualquier numero

    if numeroMaximo < numero2:
        numeroMaximo = numero2
    if numeroMaximo < numero3:
        numeroMaximo = numero3   #de esta forma se saca el numero maximo
    return numeroMaximo

numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el segundo numero:")) 
numero3 = int(input("Ingrese el tercer numero:")) 

print(IndicarMaximo(numero1,numero2,numero3))

#8
def  CalcularPotencia(base, exponente):
    return base ** exponente  #** es potencia

base = int(input("Ingrese una base: "))
exponente = int(input("Ingrese el exponente: "))

print(CalcularPotencia(base, exponente))