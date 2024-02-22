import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mateo
apellido: Santiago
---
Ejercicio: while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0   #siempre se usa esta variable para colocar el while
        suma_acumulada = 0   #numeros que ingresa el usuario
        
        while contador < 5:  #se va a ejecutar el while hasta que se pongan 5 numeros
            numero_str = prompt("suma","ingrese numero")
            numero = int(numero_str)
            
            suma_acumulada += numero   #sumo las dos variables
            
            contador += 1

            promedio = suma_acumulada /5  #/5 porque es el promedio entre 5 numeros

            self.txt_suma_acumulada.delete(0, "end")   
            self.txt_suma_acumulada.insert(0, suma_acumulada)

            self.txt_promedio.delete(0, "end")   
            self.txt_promedio.insert(0, promedio)

#el "end" para borrar todo el txt que hay en la caja para no sobre escribirlo
#insert para insertar el contenido en la caja de texto
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
