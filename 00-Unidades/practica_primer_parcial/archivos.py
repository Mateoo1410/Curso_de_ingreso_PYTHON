# La empresa “Recursos Inhumanos S.A.” nos ha pedido que desarrollemos un software de gestión de empleados para poder llevar a cabo un control más exhaustivo de ellos.
# Nuevo: La empresa nos ha solicitado implementar la permanencia de datos en el sistema, para ellos debemos actualizar algunas opciones de menú para adecuarlo a los nuevos requerimientos.

# Nuestro programa debe contar con un menú de las siguientes características:

# Leer desde CSV / JSON
# Dar de alta.
# Modificar.
# Eliminar.
# Mostrar todos.
# Mostrar gerentes.
# Mostrar Analistas con sueldo mayor a $500000.
# Calcular salario promedio.
# Ordenar empleados.
# Salir.

# Datos correspondientes a cada empleado:
# ID,
# Nombre, 
# Apellido, 
# Puesto, 
# Salario

# A tener en cuenta:

# Nuevo: En la opción leer el programa deberá darle la opción al usuario de elegir si cargar los datos a partir de un archivo JSON o a partir de un archivo CSV. Los archivos deberán llamarse “empleados.csv” y “empleados.json” respectivamente.

# El programa deberá contar con una lista de empleados. Cada empleado deberá ser representado con el tipo de dato diccionario.

# Al dar de alta un empleado el id debe ser autoincremental, comenzando en 1. Cada empleado tendrá un ID único. (El primer empleado dado de alta tendrá ID 1, el segundo ID 2, etc)

# El resto de datos deben ser pedidos por consola. También deberán ser validados (Los nombres y los apellidos no pueden contener números o caracteres especiales ni tener exceder el tamaño de 20 caracteres. El puesto deberá ser “Gerente” / “Supervisor” / “Analista” / “Encargado” / “Asistente”. El salario no podrá ser menor a 234315.

# En la opción modificar podrá modificarse cualquier información del empleado excepto su id, la cual será pedida pedida por consola para identificar al empleado a modificar. Deberá mostrarse un sub-menú donde el usuario seleccione qué dato/s desea modificar. Deberá mostrarse un mensaje indicando si se realizaron modificaciones o no.

# La opción eliminar deberá eliminar permanentemente a un empleado de la lista original. Deberá pedirse la id del empleado a eliminar por consola.

# La opción mostrar todos deberá imprimir por consola la información de todos los empleados de la empresa con el siguiente formato:
# ********************************************************************************************
# 	Nombre: 
# 	Apellido:	
# 	Puesto:
# 	Salario:
# ********************************************************************************************
# Nuevo: Además de imprimir todos los empleados en la consola, deberá generar un archivo CSV y un archivo JSON con los datos de los empleados, llamados “empleados.csv” y “empleados.json” respectivamente.
# En caso de que los archivos ya existan, los mismos deberán sobreescribirse.

# La opción mostrar gerentes deberá imprimir por consola la información de todos los empleados cuyo puesto sea gerente con el mismo formato de la opción mostrar todos. Si no hay ningún gerente debe mostrar “No hay ningún empleado que sea gerente”.
# Nuevo: Además de imprimir todos los gerentes en la consola, deberá generar un archivo CSV y un archivo JSON con los datos de los empleados, llamados “gerentes.csv” y “gerentes.json” respectivamente.
# En caso de que los archivos ya existan, los mismos deberán sobreescribirse.

# La opción calcular salario promedio deberá realizar un cálculo e imprimir por consola el resultado del promedio entre los salarios de todos los empleados. 
# Nuevo: Además de calcular y mostrar el promedio, la opción deberá generar un archivo llamado “salario_promedio.txt” y guardar el valor calculado.
# En caso de que el archivo ya exista deberá sobreescribirse.

# En todos los casos (excepto en el alta) debe verificarse que la lista no esté vacía, caso contrario debe mostrarse un mensaje indicando lo sucedido.

# El programa deberá estar correctamente modularizado, programado de manera eficiente y en funciones, respetando las reglas de estilo de la cátedra y las buenas prácticas.

# Nuevo: La opción ordenar empleados debe permitir ordenar el listado de empleados ofreciéndole al usuario ordenar en base al nombre, apellido, o salario de forma ascendente o descendente.

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

def	calcular_salario_promedio(lista_empleados)->float:
    acumulador = 0
    for i in range(len(lista_empleados)):
        acumulador += lista_empleados[i]["salario"]
    promedio = acumulador/len(lista_empleados)
    return promedio

def analista_mayor_sueldo(lista_empleados:list)->None:
    lista_analistas = []
    for i in range(len(lista_empleados)):
        if lista_empleados[i]["salario"] > 500000:
            lista_analistas.append(lista_empleados[i])
    return lista_analistas



def menu_ordenamiento():
    seleccion = None
    while True:
        print("1: Nombre_ascendente")
        print("2: Nombre_descendente")
        print("3: Apellido_ascendente")
        print("4: Apellido_descendente")
        print("5: Salario_ascendente")
        print("6: Salario_descendente")
        seleccion = input("Ingrese opcion para modificar: ")
        match (seleccion):
            case "1":
                bubble_sort_ascendente(lista_empleados,"nombre")
                break
            case "2":
                bubble_sort_descendente(lista_empleados,"nombre")
                break
            case "3":
                bubble_sort_ascendente(lista_empleados,"apellido")
                break
            case "4":
                bubble_sort_descendente(lista_empleados,"apellido")
                break
            case "5":
                bubble_sort_ascendente(lista_empleados,"salario")
                break
            case "6":
                bubble_sort_descendente(lista_empleados,"salario")
                break

def bubble_sort_ascendente(lista:list,parametro:str)->None:
    for j in range(len(lista)):
        for i in range(len(lista)-1 -j):
            if lista[i][parametro] > lista[i+1][parametro]:
                auxiliar = lista[i][parametro]
                lista[i][parametro] = lista[i+1][parametro]
                lista[i+1][parametro] = auxiliar

def bubble_sort_descendente(lista:list,parametro:str)->None:
    for j in range(len(lista)):
        for i in range(len(lista)-1 -j):
            if lista[i][parametro] < lista[i+1][parametro]:
                auxiliar = lista[i][parametro]
                lista[i][parametro] = lista[i+1][parametro]
                lista[i+1][parametro] = auxiliar




def menu_principal():
    usuario = None
    while usuario != "7":
        print("1: Leer desde CSV / JSON")
        print("2: Dar de alta")
        print("3: Modificar")
        print("4: Eliminar")
        print("5: Mostrar todo")
        print("6: Mostrar gerentes")
        print("7: Mostrar Analistas con sueldo mayor a $500000")
        print("8: Calcular salario promedio")
        print("9: Ordenar empleados")
        print("10: Salir")
        usuario = input("Ingrese una opcion: ")
        match(usuario):
            case "1":
                pass
            case "2":
                dar_de_alta(lista_empleados)
                #print(lista_empleados) #para saber si se agrego el empleado a la lista
            case "3":
                modificar_empleado(lista_empleados)
            case "4":
                eliminar_empleado(lista_empleados)
            case "5":
                mostrar_empleados(lista_empleados)
            case "6":
                puesto = buscar_puesto(lista_empleados, "Gerente")
                mostrar_empleados(puesto)
            case "7":
                puesto_analista = buscar_puesto(lista_empleados, "Analista")
                puesto_analista = analista_mayor_sueldo(puesto_analista)
                mostrar_empleados(puesto_analista)
            case "8":
                print(f"El salario promedio es de: {calcular_salario_promedio(lista_empleados)}")
            case "9":
                menu_ordenamiento()
            case "10":
                print("gracias por usar el programa")

menu_principal()

# Leer desde CSV / JSON
# Dar de alta.
# Modificar.
# Eliminar.
# Mostrar todos.
# Mostrar gerentes.
# Mostrar Analistas con sueldo mayor a $500000.
# Calcular salario promedio.
# Ordenar empleados.
# Salir.