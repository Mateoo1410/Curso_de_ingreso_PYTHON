from .input import get_int
def contar_regresivamente(numero: int)-> None:
    if numero == 0:
        print(numero)
        return
    print(numero)
    contar_regresivamente(numero -1)

#print(contar_regresivamente(10))    #en esta funcion cuenta regresivamente desde el 10 al 0

def calcular_factorial(numero:int)-> int:
    
    if numero == 1:
        return 1      #esto xq el factorial de 1 es igual a 1
    
    return numero * calcular_factorial(numero -1) #calculo para sacar el factorial

#print(calcular_factorial(5))

#va restando y multiplicando de 1 en 1 para sacar el resultado factorial

#1) Realizar una función recursiva que calcule la suma de los primeros números naturales (todos los números anteriores al recibido por parámetro)

def sumar_naturales(numero: int)-> int:
    if numero <= 0:
        return 0
    else:
        return numero + sumar_naturales(numero - 1)
    
numero = get_int("Ingrese un numero natural: ", "Error reingrese numero natural: ", 1, 10000, 3)
resultado = sumar_naturales(numero)
print("La suma de los primeros", numero, "numeros naturales es: ", resultado)


#2) Realizar una función recursiva que calcule la potencia de un número

def calcular_potencia(base: int, exponente: int)-> int:  #esto lo da la consigna
    
    if exponente == 0:
        return 1  #si la potencia queda en 0 devuelve un 1
    return base * calcular_potencia(base, exponente - 1) #funcion recursiva de potencia

#va restando uno a uno los exponentes para multiplicarlos y poder conseguir el resultado final 

print(calcular_potencia(20, 5))

#3) Realizar una función recursiva que realice la suma de los dígitos de un número

def sumar_digitos(numero: int)-> int:
    pass