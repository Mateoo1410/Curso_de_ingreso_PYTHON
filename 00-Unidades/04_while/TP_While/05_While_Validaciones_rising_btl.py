import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mateo
apellido: Santiago
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido     
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        edad = 0
        legajo = 0
        Estado_civil = self.combobox_tipo.get()
        
        bandera = True

        while bandera == True:
            apellido = prompt("ERROR", "Reingrese datos")
            if apellido == None:
                bandera = False
                break
            
            else:
                
                edad = int(edad)
                edad = prompt("Edad", "Ingrese edad")
                if not (edad  >= 18 and edad <= 90):
                    prompt("ERROR", "Reingrese edad")
                else:
                    legajo = int(legajo)
                    legajo = prompt("Legajo", "Ingrese legajo")
                    if  legajo < 1000 and legajo > 9999:
                        prompt("ERROR", "Reingrese numero de legajo")
                bandera = False
        
        self.txt_apellido.delete(0, "end")
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, "end")
        self.txt_edad.insert(0, edad)
        self.txt_legajo.delete(0, "end")
        self.txt_legajo.insert(0, legajo)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
