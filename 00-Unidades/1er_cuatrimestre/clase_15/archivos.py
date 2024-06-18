from informacion import *
import json

# ESCRITURA #
#for heroe in lista_personajes:  #guarda la lista en la variable heroe
    #print(f"{heroe['nombre']}") #tiene que ser con '' xq sino no escribe

# .WRITE() #
# archivo = open("archivo.txt", "w") #archivo se convierte en objeto
# for heroe in lista_personajes:
#     texto = f"{heroe['nombre']} \n"
#     archivo.write(texto)
# archivo.close()

#se utiliza para escribir datos en un archivo, permite escribir una cadena de texto en el archivo abierto


# .WRITELINES() #
# lista_nombres = []
# for heroe in lista_personajes:
#     lista_nombres.append(f"{heroe['nombre']} \n")

# archivo = open("archivo.txt", "w")
# archivo.writelines(lista_nombres)
# archivo.close()

#se utiliza para escribir una lista de cadenas en un archivo. A diferencia de .write(), que escribe una única 
#cadena de texto, .writelines() puede escribir múltiples líneas de texto a partir de una lista de cadenas.


# .read(bytes) #
# archivo = open("archivo.txt", "r") # se abre el archivo leyendolo
# texto_1 = archivo.read()
# archivo.close()
# print(texto_1, end="")

#lee todo el archivo, tambien se puede marcar hasta donde leer


# .READLINE(bytes) #
# archivo = open("archivo.txt", "r")
# texto_1 = archivo.readline()
# texto_2 = archivo.readline(5)
# archivo.close()
# print(texto_1, end="")
# print(texto_2, end="")

#lee las lines, se puede indicar cuantos caracteres puede leer por linea, lee lista de str


# .READLINES() #
# archivo = open("archivo.txt", "r")
# contenido = archivo.readlines()
# archivo.close()

# print(contenido)
# for i in range(len(contenido)):
#     print(contenido[i])

#imprime todas las lineas una abajo de la otra




# "a"/append #
# archivo = open("archivo.txt", "a")
# archivo.write("Hola como estan")
# archivo.close()

#funciona como el append, crea una cadena de caracteres al final de la lista, con la "w" sobrepone lo que se escribe en el texto

# with open("archivo.txt", "a") as archivo:
#     archivo.write("\nChau nos vemos")
#cierra solo el archivo con el with


# .seek()  .tell(bytes)
with open("archivo.txt", "r") as archivo:
    archivo = open("archivo.txt", "r")
    print(archivo.tell())  #muestra el indice
    archivo.seek(3)        #lo que hace es que empieza a leer desde el el 3° caracter
    print(archivo.read())

#el r+ sobre escribe los caracteres que ya estan en la biblioteca

def guardar_csv_personas(lista_personas:list, path:str):
    
    archivo = open(path, "w")
    archivo.write("nombre,apellido,edad,dni\n")
    
    for i in range(len(lista_personas)):
        persona = lista_personas[i]
        nombre = persona["nombre"]
        apellido = persona["apellido"]
        edad = persona["edad"]
        dni = persona["dni"]

        archivo.write(f"{nombre},{apellido},{edad},{dni}\n")

    archivo.close()

#guardar_csv_personas(lista_personas "archivo.txt.csv")


def cargar_personas_desde_csv(path:str,)->list[dict]:

    archivo = open(path, "r")
    lineas = archivo.readlines()
    archivo.close()

    lista_personas = []
    for i in range(1, len(lineas)):
        persona = dict()
        datos = lineas[i]
        datos = datos.split(",")
        nombre = datos[0]
        apellido = datos[1]
        edad = datos[2]
        dni = datos[3]

        persona = {"nombre": nombre,
                    "apellido": apellido,
                    "edad": edad,
                    "dni": dni}

        lista_personas.append(persona)
    
    return lista_personas

lista_aux = cargar_personas_desde_csv("archivo.txt.csv")
print(lista_aux)


# JSON #
def crear_json(path:str, lista_personas:list):
    data = {}
    data["personas"] = lista_personas

    archivo = open(path, "w")

    json.dump(data,archivo,indent=4,ensure_ascii=False) 
    archivo.close()

#indent para que no quede todo junto
#ensure_ascii para que no se vean raros los tildes
#crear_json("archivo.txt.json", lista_personas)

#crea un diccionario gigante

def cargar_desde_json(path:str)->list[dict]:

    archivo = open(path, "r")
    retorno = json.load(archivo)
    archivo.close()

    return retorno["personas"] #se aclara que solo quiere la lista

lista = cargar_desde_json("archivo.txt.json")
print(lista)