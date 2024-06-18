lista_personas = []

def dar_alta_nombre_apellido(clave:str):

    opcion = input(f"Ingrese el {clave} del empleado: ")

    while opcion.isalpha() == False or len(opcion) <= 15: # False -> por el espacio
        opcion = input(f"{clave} inválido. Ingrese nuevamente el {clave} del empleado: ")

    return opcion

def validar_puesto():

    puesto = input("Ingrese el puesto del empleado (Gerente/Supervisor/Analista/Encargado/Asistente): ").capitalize() #transforma la primera letra en mayuscula y las demas en minusculas
    while (puesto != "Gerente" and 
        puesto != "Supervisor" and 
        puesto != "Analista" and 
        puesto != "Encargado" and 
        puesto != "Asistente"):
        puesto = input("Puesto inválido. Ingrese nuevamente el puesto del empleado (gerente/supervisor/analista/encargado/asistente): ").capitalize()

    return puesto

def validar_salario()-> int:

    salario = input("Ingrese el salario del empleado: ")
    
    while salario.isnumeric() != True or int(salario) < 234315:
        salario = input("Salario inválido. Ingrese nuevamente el salario del empleado (mayor a $234315): ")

    return salario

def crear_personas()->dict:
#crea un usuario para luego añadirlo a un diccionario
    
    identificacion = len(lista_personas) + 1

    nombre = dar_alta_nombre_apellido("nombre")

    apellido = dar_alta_nombre_apellido("apellido")

    puesto = validar_puesto()

    salario = validar_salario()

    persona_nueva = {"id": identificacion,  # diccionario
                    "nombre": nombre,
                    "apellido": apellido,
                    "puesto": puesto,
                    "salario": salario}
    
    return persona_nueva

def agregar_empleado(empleado: dict, lista_empleados: list[dict])-> str:
# se agrega el usuario creado a la lista
    
    lista_empleados.append(empleado) #agrega un indice al final de la lista

    mensaje = f"El empleado con el ID: {empleado['id']} fue agregado exitosamente"

    return mensaje

# MENU PARA INTERACTUAR CON EL USUARIO #
while True:
    print("""
            1- Dar de alta.
            2- Modificar.
            3- Eliminar.
            4- Mostrar todos.
            5- Mostrar gerentes.
            6- Calcular salario promedio.
            7- Salir.
            """)
    opciones = input("Ingrese una de las siguientes opciones: ")

    match opciones:

        case "1":
            agregar_empleado(crear_personas(), lista_personas) #se crea y se añade el usuario a la lista--

        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("¡Gracias por usar nuesto sistema!")
            break