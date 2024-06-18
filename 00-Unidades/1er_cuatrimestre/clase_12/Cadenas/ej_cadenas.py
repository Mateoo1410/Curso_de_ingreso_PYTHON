from class_video import *
from data import lista_videos
from funciones import *

"""
Consigna:

1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.

B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""
llave_acceso = False

while True:

    opcion = input("Ingrese una de las opciones: ").upper()
    while (opcion != "A" and 
            opcion != "B" and 
            opcion != "C" and 
            opcion != "D" and 
            opcion != "E" and 
            opcion != "F" and 
            opcion != "G" and 
            opcion != "H"):
        opcion = input("Ingrese una de las opciones: ").upper()
    
    match opcion:
        case "A":
            for i in range(len(lista_videos)):
                lista_videos[i].dividir_titulo()
                lista_videos[i].obtener_codigo_url()
                lista_videos[i].formatear_fecha()

            print("--YA-SE-NORMALIZO--")
            llave_acceso = True
            
        case "B":

            if llave_acceso == True:
                for i in range(len(lista_videos)):
                    lista_videos[i].mostrar_tema()
            else:
                print("No se ingreso la opcion A")

        case "C":

            if llave_acceso == True:
                lista_videos = ordenar_temas(lista_videos)

            else:
                print("No se ingreso la opcion A")

        case "D":

            if llave_acceso == True:
                promedio_visitas(lista_videos)

            else:
                print("No se ingreso la opcion A")

        case "E":

            if llave_acceso == True:
                mostrar_max_visitas(lista_videos)
                
            else:
                print("No se ingreso la opcion A")  
        
        case "F":

            if llave_acceso == True:
                buscar_codigo(lista_videos, "nick")
            else:
                print("No se ingreso la opcion A")
                
        case "G":

            if llave_acceso == True:
                colaborador = input("Ingrese el nombre de un colaborador: ")
                buscar_codigo(lista_videos, colaborador)
            else:
                print("No se ingreso la opcion A")

        case "H":

            print("¡Gracias por usar nuestro sistema!")
            break