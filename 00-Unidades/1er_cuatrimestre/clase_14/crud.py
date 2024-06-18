#Facilita la gestión y manipulación de datos.
#Es fundamental en aplicaciones web, de escritorio y móviles.
#Es una parte esencial del desarrollo de software orientado a datos.

# CREATE #
lista_personas =[]

def crear_persona()->dict: #crea una persona con todos sus datos, devuelve un diccionario

    nombre = input("Ingrese el nombre: ")

    apellido = input("Ingrese el apellido: ")

    edad = input("Ingrese la edad: ")

    dni = input("Ingrese el DNI: ")  
#se tienen que validar todos los datos, ej que no se pongan n° en el nombre, que la edad no sea 0 o 200, que sea n° entero

    
    nueva_persona = {"nombre": nombre, "apellido": apellido, "edad": edad, "dni": dni}
    
    return nueva_persona

def agregar_persona(persona:dict, lista_personas:list):  #agrega la persona creada a la lista
    
    retorno = ""
    bandera_existe = False
    for i in range(len(lista_personas)):
        persona_actual = lista_personas[i]
        if persona_actual["dni"] == persona["dni"]:
            retorno = "Error, ya existe una persona con ese DNI"
            bandera_existe = True
            break # si ya se encontro un dni igual tiene que dejar de iterar, ya que seria inutil que lo siga haciendo
    
    if bandera_existe == False:
        lista_personas.append(persona) #agrega un indice al final de la lista
        retorno = f"La persona con el DNI: {persona['dni']} fue agregada exitosamente"
    return retorno



def modificar_personas(dni:int, lista_personas:list)->str:
    
    for i in range(len(lista_personas)):
        if dni == lista_personas[i]["dni"]:
            while True:
                opcion = input("Que dato desea modificar?\n a)Nombre \n b)Apellido \n c)Edad \n d)DNI \n e)Salir")

                match opcion:
                    case "a":
                        nombre = input("Ingrese nuevo nombre: ")
                        lista_personas[i]["nombre"] = nombre
                        retorno += "Se modifico el nombre. \n"
                    case "b":
                        apellido = input("Ingrese nuevo apellido: ")
                        lista_personas[i]["apellido"] = apellido
                        retorno += "Se modifico el apellido. \n"
                    case "c":
                        edad = input("Ingrese nueva edad: ")
                        lista_personas[i]["edad"] = edad
                        retorno += "Se modifico la edad. \n"
                    case "d":
                        dni = input("Ingrese nuevo DNI: ")
                        lista_personas[i]["dni"] = dni
                        retorno += "Se modifico el DNI. \n"
                    case "e":
                        break
                    case _:
                        print("Ingrese una opcion valida")
            break
        else:
            return retorno


def eliminar_persona(dni:str, lista_personas:list[dict])->str:

    for i in range(len(lista_personas)):
        if dni == lista_personas[i]["dni"]:
            persona_eliminada = lista_personas.pop(i)
            retorno = f"se ha eliminado correctamente a {persona_eliminada["nombre"]} {persona_eliminada['apellido']}"
    
    if retorno == "":
        retorno = "Error. No existe una persona con ese DNI."



def retornar_datos_personales(persona:dict):
    mensaje = f"""
    El nombre es: {persona["nombre"]}
    El apellido es: {persona["apellido"]}
    La edad es: {persona["edad"]}
    El dni es: {persona["edad"]}"""
    
    return mensaje


def mostrar_personas(lista_personas:list)->None:
    for i in range(len(lista_personas)):
        informacion = retornar_datos_personales(lista_personas[i])
        print(informacion)





def mostrar_menu():
    print("""\nSeleccione una opcion:
        1. Dar de alta.
        2. Modificar.
        3. Eliminar.
        4. Mostrar todos.
        5. Salir.
        """)
while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion")