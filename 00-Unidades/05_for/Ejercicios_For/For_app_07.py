import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mateo
apellido: Santiago
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        bandera = True
        numero = int(prompt("Mensaje", "Ingrese numero"))
        
        for i in range(2,numero): #empieza del 2 ya que solo se busca numeros que no sean divisibles por 1 o por si mismos
            if numero % i == 0:
                bandera = False #si consigue un divisor quiere decir que no es primo y se rompe la bandera
                break

        if bandera == True:
            alert("mensaje", f"{numero} ES un numero primo")
        else:
            alert("mensaje", f"{numero} NO es un numero primo")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()