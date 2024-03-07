import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_edad = 0
        edad = 0
        suma_edad = 0
        contador_votos = 0
        promedio_edades = 0
        cantidad_votos = 0
        minimo = 0
        maximo = 0
        candidato_mas_votos = ""
        candidato_menos_votos = ""
        #bandera = True
        flag = True
        
        while True:#bandera == True:
            nombre_candidato = ("Nombre", "Ingrese nombre del candidato")  
            if nombre_candidato == None:
                break#bandera = False   #inicializo el bucle
            
                
            cantidad_votos = prompt("Voto", "ingrese cantidad de votos")
            cantidad_votos = int(cantidad_votos)    
            if cantidad_votos > 0:
                contador_votos += cantidad_votos   #esto para poder llevar un conteo de los votos
            if flag == True:
                minimo = cantidad_votos
                maximo = cantidad_votos
                candidato_mas_votos = cantidad_votos
                candidato_menos_votos = cantidad_votos
                flag = False
            else:
                if cantidad_votos < minimo:
                    minimo = cantidad_votos
                    candidato_menos_votos = nombre_candidato
                elif cantidad_votos > maximo:
                    maximo = cantidad_votos
                    candidato_mas_votos = nombre_candidato
                
            
            if edad != None or edad >= 25:
                edad = prompt("Edad", "Ingrese edad")
                edad = int(edad)
                if edad == None or edad < 25:
                    edad = prompt("ERROR", "Reingrese edad")  #esto para poner la condicion y que sea mayor a 25
                
                edad = int(edad)
                suma_edad += edad
            contador_edad += 1
            promedio_edades = suma_edad / contador_edad

            #bandera = question("Mensaje", "Desea continuar?")

        mensaje = f"{candidato_mas_votos} es el candidato con mas votos, ({maximo}) .\n {candidato_menos_votos}, ({edad}) años es el candidato con menos votos ({minimo}) \n {promedio_edades} es el promedio de edades \n {cantidad_votos} es la cantidad de votos emitidos"

        alert("Votaciones", mensaje)




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
