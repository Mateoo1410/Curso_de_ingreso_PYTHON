import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Mateo
apellido: Santiago
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_interaciones = 0  #variable para finalizar el bucle
        contador_pares = 0        #se crean variables para luego sumarlas entre si
        
        while contador_interaciones <= 10:
            
            if contador_interaciones % 2 == 0: 
                
                contador_pares = contador_pares + contador_interaciones   #se hace la suma
            
            contador_interaciones += 1
            #print(contador_interaciones)
            
        alert("Fin", contador_pares)
        
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()