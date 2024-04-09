import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mateo
apellido: Santiago
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Numero", "ingrese un numero")
        numero = int(numero)
        contador = 0
        for i in range(1, numero +1):
            if numero % i == 0: #modulo de i ya que va de uno en uno encontrando divisores
                alert("mensaje", f"el numero {numero} es divisible por {i}")
                contador += 1
        alert("Mensaje", f"El numero {numero} es divisible por si mismo {contador} veces")

#en el range se usa el numero 1 para arrancar y que no divida por 0, hasta el numero ingresado, el +1 para que se divida por si mismo

# "if numero % i == 0:" esto es para que si el modulo (que es el resto) es igual a cero osea que se divide por si mismo muestra el mensaje

#se agrega un contador dentro del if y un alert fuera del if y del for para que cuente la cantidad de veces que se puede dividir el numero por si mismo


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()