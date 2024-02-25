import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mateo
apellido: Santiago
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
            EJERCICIOS EXTRA:
    G. Minimo numero y que sea positivo
    H. Maximo numero y que sea negativo
    I. Promedio de los negativos y Promedio de los positivos
    J. Cantidad de numeros ingresados

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0   #va acumulando todos los numeros ingresados para luego sumarlos
        cantidad_de_ceros = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        minimo_positivo = 0
        maximo_negativo = 0

        bandera = True    #control de estado, verdadero o falso

        while bandera:
            numero = prompt("Numero", "Ingrese numero")
            if numero == None:
                bandera = False
            else:
                
                numero = int(numero)

                if numero > 0:
                    suma_positivos += numero
                    cantidad_positivos += 1   #para hacer un conteo de todos los numeros positivos ingresados
                    if numero < minimo_positivo or bandera == True: #EXTRA
                        minimo_positivo = numero 
                elif numero < 0:
                    suma_negativos += numero
                    cantidad_negativos += 1
                    if numero > maximo_negativo or bandera == True:  # EXTRA
                        maximo_negativo = numero
                else:
                    cantidad_de_ceros += 1
                    bandera = False

            #promedio_numeros = (suma_positivos + suma_negativos) /numero
            
            diferencia_de_numeros = cantidad_positivos - cantidad_negativos
        
        mensaje = f"Resultado \n la suma acumulada de los negativos es: {suma_negativos} \n La suma acumulada de los positivos es: {suma_positivos} \n la canitdad de ceros es: {cantidad_de_ceros} \n la diferencia de numeros es: {diferencia_de_numeros} \n cantidad de negativos: {cantidad_negativos} \n cantidad de positivos: {cantidad_positivos} \n El numero minimo positivo es: {minimo_positivo} \n El numero maximo negativo es: {maximo_negativo}"

        alert("Ejercicio 10", mensaje) 

#\n es para dar un salto de linea cuando se muestra el alert
#la variable "bandera" se usa para para remplazar al break, ademas puede llevarse un conteo de las repeticiones
#maximos y minimos no se inicializan, contadores si
#el or es para que solo se cumpla una  sola condicion  y de verdadero, la variable "bandera" es True pero se pone para que se cumpla el primer ingreso (agregar la variable "minimo_positivo") y se pueda comparar con los otros ingresos de numeros
#la bandera agregada cumple su funcion solo por un ingreso y luego no se repite gracias al "False"
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
