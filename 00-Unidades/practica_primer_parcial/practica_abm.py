# La empresa “Recursos Inhumanos S.A.” nos ha pedido que desarrollemos un software de gestión de empleados para poder llevar a cabo un control más exhaustivo de ellos.

# Nuestro programa debe contar con un menú de las siguientes características:

# Dar de alta.
# Modificar.
# Eliminar.
# Mostrar todos.
# Mostrar gerentes.
# Calcular salario promedio.
# Salir.

# Datos correspondientes a cada empleado: PARTE DE DAR DE ALTA

# ID,
# Nombre, 
# Apellido, 
# Puesto, 
# Salario

# A tener en cuenta:
# El programa deberá contar con una lista de empleados. Cada empleado deberá ser representado con el tipo de dato diccionario.
# Al dar de alta un empleado el id debe ser autoincremental, comenzando en 1. Cada empleado tendrá un ID único. (El primer empleado dado de alta tendrá ID 1, el segundo ID 2, etc)
# El resto de datos deben ser pedidos por consola. También deberán ser validados (Los nombres y los apellidos no pueden contener números o caracteres especiales ni exceder el tamaño de 15 caracteres. El puesto deberá ser “Gerente” / “Supervisor” / “Analista” / “Encargado” / “Asistente”. El salario no podrá ser menor a 234315.
# En la opción modificar podrá modificarse cualquier información del empleado excepto su id, la cual será pedida pedida por consola para identificar al empleado a modificar. Deberá mostrarse un sub-menú donde el usuario seleccione qué dato/s desea modificar. Deberá mostrarse un mensaje indicando si se realizaron modificaciones o no.
# La opción eliminar deberá eliminar permanentemente a un empleado de la lista original. Deberá pedirse la id del empleado a eliminar por consola.
# La opción mostrar todos deberá imprimir por consola la información de todos los empleados de la empresa con el siguiente formato:
# ********************************************************************************************
# 	Nombre: 
# 	Apellido:	
# 	Puesto:
# 	Salario:
# ********************************************************************************************
# La opción mostrar gerentes deberá imprimir por consola la información de todos los empleados cuyo puesto sea gerente con el mismo formato de la opción mostrar todos.
# La opción calcular salario promedio deberá realizar un cálculo e imprimir por consola el resultado del promedio entre los salarios de todos los empleados. 
# El programa deberá estar correctamente modularizado, programado de manera eficiente y en funciones, respetando las reglas de estilo de la cátedra y las buenas prácticas.

lista_empleados = []

def dar_de_alta(lista_empleados:list)-> None:
    id = int
    if len(lista_empleados) == 0:
        id = 1
    else:
        indice_ultimo_empleado = len(lista_empleados)-1  #se consigue el indice del ultimo empleado
        id_ultimo_empleado = lista_empleados[indice_ultimo_empleado]["id"]
        id = id_ultimo_empleado +1  #evita que se repita la id sumandole 1
    nombre = validar_nombre_apellido(mensaje="Ingrese nombre")
    apellido = validar_nombre_apellido(mensaje="Ingrese apellido")
    puesto = validar_puesto()
    salario = validar_salario()
    empleado = {"id": id,
                "nombre": nombre,
                "apellido": apellido,
            	"puesto": puesto,
                "salario": salario}
    lista_empleados.append(empleado)     #para agregar el empleado a la lista
    


def validar_nombre_apellido(mensaje:str)->str:
    while True:
        empleado = input(mensaje)
        if empleado.isalpha() and len(empleado) <= 15:  #comprueba que no haya ni numeros ni caracteres
            return empleado  #si esta bien devuelve empleado
        else:
            print("Error, El nombre y el apellido no puede conter caracteres especiales y tiene que ser menor a 15: ")

def validar_puesto()->str:
    lista_puestos = ["Gerente","Supervisor","Analista","Encargado","Asistente"]
    while True:
        puesto = input("Ingrese puesto de trabajo: ")
        puesto = puesto.lower()  	  #pone todo en minuscula
        puesto = puesto.capitalize()  #pone la primera en mayuscula, esto es para hacerlo mas estetico
        for i in range(len(lista_puestos)):
            if puesto == lista_puestos[i]:
                return puesto
        print("Error, ingrese un puesto valido: ")
        
def validar_salario()->int:
    while True:
        salario = input("Ingresar salario: ")
        if salario.isdigit():     #Comprueba que sea un numero
            salario = int(salario)
            if salario >= 234315:
                return salario
        print("Ingrese un salario valido: ")
        
#### MODIFICAR ###
def modificar_empleado(lista_empleados:list):
    id = validar_id()
    for i in range(len(lista_empleados)):
        if lista_empleados[i]["id"] == id:   #busca un empleado
            modificar_menu(lista_empleados, i)   #recorre la lista buscando id del usuario
            break

def modificar_menu(lista_empleados:list, indice:int)->None:
    seleccion = None
    while True:
        print("1: Nombre")
        print("2: Apellido")
        print("3: Puesto")
        print("4: Salario")
        seleccion = input("Ingrese opcion para modificar: ")
        match (seleccion):
            case "1":
                nombre = validar_nombre_apellido(mensaje="Ingrese nuevo nombre: ")
                lista_empleados[indice]["nombre"] = nombre
                break
            case "2":
                apellido = validar_nombre_apellido(mensaje="Ingrese nuevo apellido: ")
                lista_empleados[indice]["apellido"] = apellido
                break
            case "3":
                puesto = validar_puesto()
                lista_empleados[indice]["puesto"] = puesto
                break
            case "4":
                salario = validar_salario()
                lista_empleados[indice]["salario"] = salario
                break

def validar_id():
    while True:
        id = input("Ingresar id: ")
        if id.isdigit():
            id = int(id)
            if id > 0:
                return id
        print("Error, reingrese id")
        
def eliminar_empleado(lista_empleados: list)->None:
    id = validar_id()
    for i in range(len(lista_empleados)):
        if lista_empleados[i]["id"] == id:
            lista_empleados.pop(i)    #elimina el indice que mandas
            break

def mostrar_empleados(lista_empleados:list)->None:
    for i in range(len(lista_empleados)):
        id = lista_empleados[i]["id"]
        nombre = lista_empleados[i]["nombre"]
        apellido = lista_empleados[i]["apellido"]
        puesto = lista_empleados[i]["puesto"]
        salario = lista_empleados[i]["salario"]
        print("********************************************************************************************")
        print(f"id: {id}")
        print(f"nombre: {nombre}")
        print(f"apellido: {apellido}")
        print(f"puesto: {puesto}")
        print(f"salario: {salario}")
        print("********************************************************************************************")


def buscar_puesto(lista_empleados:list, puesto:str)->list:
    lista_puesto = []
    for i in range(len(lista_empleados)):
        if lista_empleados[i]["puesto"] == puesto:
            lista_puesto.append(lista_empleados[i])  #busca el puesto que se manda y se agrega a lista puesto
    return lista_puesto

def	calcular_salario_promedio(lista_empleados):
    acumulador = 0
    for i in range(len(lista_empleados)):
        acumulador += lista_empleados[i]["salario"]
    promedio = acumulador/len(lista_empleados)
    return promedio


def menu_principal():
    usuario = None
    while usuario != "7":
        print("1: Dar de alta")
        print("2: Modificar")
        print("3: Eliminar")
        print("4: Mostrar todo")
        print("5: Mostrar gerentes")
        print("6: Calcular salario promedio")
        print("7: Salir")
        usuario = input("Ingrese una opcion: ")
        match(usuario):
            case "1":
                dar_de_alta(lista_empleados)
                #print(lista_empleados) #para saber si se agrego el empleado a la lista
            case "2":
                modificar_empleado(lista_empleados)
            case "3":
                eliminar_empleado(lista_empleados)
            case "4":
                mostrar_empleados(lista_empleados)
            case "5":
                puesto = buscar_puesto(lista_empleados, "Gerente")
                mostrar_empleados(puesto)
            case "6":
                print(f"El salario promedio es de: {calcular_salario_promedio(lista_empleados)}")
            case "7":
                print("gracias por usar el programa")

menu_principal()