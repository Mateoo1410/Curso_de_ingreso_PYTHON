import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mateo
apellido: Santiago
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(prompt("mensaje", "ingrese un numero"))
        bandera = True
        contador = 0

        for i in range(2, numero): #comienza desde el dos, el uno no se tiene en cuenta aca
            if i>2:
                for j in range(2,i -1): #se pone el if mayor que 2 para que en el -1 del range no rompa el codigo
                    if i % j == 0:
                        bandera = False
                        break
            if bandera:
                contador += 1
                alert("este numero es primo", i)
            bandera = True
        alert("mensaje", f"hay una cantiadad de {contador} numeros primos")
#se pone bandera True ya que si la bandera queda establecida en False no toma ningun otro numero primo de los que quedan
    

#para este ej se necesita colocar un for dentro del for asi por cada numero que vaya iterando calcula si es un numero primo o no
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()