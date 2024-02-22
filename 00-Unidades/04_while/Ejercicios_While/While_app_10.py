import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
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
        suma_negativos = 0
        cantidad_de_ceros = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        minimo_positivo = 1000
        maximo_negativo = -1000

        bandera = True    #control de estado, verdadero o falso

        while bandera:
            numero = prompt("Numero", "Ingrese numero")
            if numero == None or numero == "":
                bandera = False
            else:
                
                numero = int(numero)

                if numero > 0:
                    suma_positivos += numero
                    cantidad_positivos += 1   #para hacer un conteo de todos los numeros positivos ingresados
                elif numero < 0:
                    suma_negativos += numero
                    cantidad_negativos += 1
                else:
                    cantidad_de_ceros += 1

            diferencia_de_numeros = suma_positivos - suma_negativos

        mensaje = f"Resultado \n la suma acumulada de los negativos es: {suma_negativos} \n La suma acumulada de los positivos es: {suma_positivos} \n la canitdad de ceros es: {cantidad_de_ceros} \n la diferencia de numeros es: {diferencia_de_numeros} \n cantidad de negativos: {cantidad_negativos} \n cantidad de positivos: {cantidad_positivos}"

        alert("Ejercicio 10", mensaje) 

#\n es para dar un salto de linea cuando se muestra el alert
#la variable "bandera" se usa para para remplazar al break, ademas puede llevarse un conteo de las repeticiones
#maximos y minimos no se inicializan, contadores si
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
