import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre: Mateo
apellido: Santiago
---
Ejercicio: if_09
---
Simulacro Turno Mañana

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

Nombre del votante
Edad del votante (debe ser mayor a 13)
Género del votante (Masculino, Femenino, Otro)
El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:
El promedio de edad de las votantes de género Femenino 
Del votante más viejo, su nombre.
Nombre del votante más joven qué votó a Gianni.
Nombre de cada participante y porcentaje de los votos qué recibió.
El nombre del participante que debe dejar la casa (El que tiene más votos)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_femenino = 0    #para el promedio se necesita un contador y un acumulador que van dentro del bucle
        acumulador_femenino_edad = 0
        contador_giovanni = 0
        contador_gianni = 0                         #% porcentaje_femenino = (contador_femenino + acumulador_femenino) /100
        contador_esteban = 0
        votante_mayor_edad = 0  # se pone con comillas para no inicializar maximos ni minimos
        nombre_mayor_edad = ""
        votante_menor_edad = 0
        nombre_menor_edad = ""
        bandera_primer_ingreso = True

        seguir = True
        while seguir == True:
            nombre = prompt("Mensaje", "Ingrese su nombre") #NOMBRE
            
            #while nombre == None or nombre == "":
            #nombre = prompt("Mensaje", "Reingrese su nombre")esto es un extra, no es necesario
            
            #EDAD
            edad = prompt("Mensaje", "Ingrese su edad")
            edad = int(edad)

            while edad < 13:
                edad = prompt("Mensaje", "Usted debe ser mayor de 13 años")
                edad = int(edad)

            #GENERO
            genero = prompt("Mensaje", "Ingrese su genero")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Error", "Reingrese genero")

            #PARTICIPANTE
            nombre_participante = prompt("Mensaje", "Ingrese el nombre para dar el voto")
            while nombre_participante != "Giovanni" and nombre_participante != "Gianni" and nombre_participante != "Esteban":
                nombre_participante = prompt("Error", "Reingrese nombre del participante")

            #PROMEDIO FEMENINO
            if genero == "Femenino":
                contador_femenino += 1
                acumulador_femenino_edad += edad

            #VOTANTE MAS VIEJO
            if edad > votante_mayor_edad or bandera_primer_ingreso == True:  #se cumple solo la bandera y luego de eso se ingresa el pirmer numero 
                votante_mayor_edad = edad
                nombre_mayor_edad = nombre
                bandera_primer_ingreso = False


            #CONTADOR DE TODOS LOS VOTOS
            match nombre_participante:
                case "Giovanni":
                    contador_giovanni += 1
                case "Gianni":
                    contador_gianni += 1
                    if edad < votante_menor_edad or contador_gianni == 1:
                        votante_menor_edad = edad   #se remplaza la bandera por contador_gianni == 1
                        nombre_menor_edad = nombre
                case "Esteban":
                    contador_esteban += 1


        
            seguir = question("mensaje", "desea continuar?") #va dentro del while
            

        #CONTINUACION DEL PROMEDIO FEMENINO
        if contador_femenino  != 0:
            promedio_femenino = acumulador_femenino_edad / contador_femenino

        total_votos = contador_esteban + contador_gianni + contador_giovanni
        
        #PORCENTAJE DE TODOS LOS PARTICIPANTES
        porcentaje_giovanni = (contador_giovanni * 100) /total_votos
        porcentaje_gianni = (contador_gianni * 100) /total_votos
        porcentaje_esteban = (contador_esteban * 100) /total_votos

        #PARTICIPANTE CON MAS VOTOS
        if contador_giovanni > contador_gianni and contador_giovanni > contador_esteban:
            participante_mas_votado = "Giovanni"
        elif contador_gianni > contador_esteban:
            participante_mas_votado = "Gianni"
        else:
            participante_mas_votado = "Esteban"

        mensaje = f"El promedio de edad de las votantes femenina es de: {promedio_femenino} \n El votante mas viejo se llama: {nombre_mayor_edad} \n El votante mas joven que voto a gianni es: {nombre_menor_edad} \n porcentaje de todos los participantes: \n Giovanni: {porcentaje_giovanni} \n Gianni: {porcentaje_gianni} \n Esteban: {porcentaje_esteban} \n El participante que debe dejar la casa es: {participante_mas_votado}"

        alert("Gran hermano", mensaje)

    # El promedio de edad de las votantes de género Femenino 
    # Del votante más viejo, su nombre.
    # Nombre del votante más joven qué votó a Gianni.
    # Nombre de cada participante y porcentaje de los votos qué recibió.
    # El nombre del participante que debe dejar la casa (El que tiene más votos)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()