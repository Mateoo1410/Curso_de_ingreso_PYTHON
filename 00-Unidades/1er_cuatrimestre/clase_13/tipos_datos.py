# TUPLA #
lista = [1,2,3,4,5]

tupla = (5,4,3,2,1)

print(type(tupla)) #imprime que tipo es la variable
print(tupla)
#son iguales a las listas pero son inmutables

# SET #

lista = [1,2,3,4,5,1,2,3,4]
set_datos = {43,65,23,65,7}

print(lista)
set_datos = set(lista)
print(set_datos)
#no tienen elementos duplicados, no representan un orden, son inmutables

# METODO ADD #

set_datos = {1,2,3}
set_datos.add(5)
print(set_datos)
#agrega un elemento

# METODO DISCARD #

set_datos = {1,2,3}
set_datos.discard(3)
print(set_datos)
#se borra un elemento si es que existe, si no existe no hace nada

# METODO DICT #

diccionario = {'nombre': 'Juan', 
                'edad': 21, 
                'ciudad': 'Buenos Aires',
                "DNI": 9000000}
diccionario['nombre'] = "Mateo"
diccionario['edad']  = 20
diccionario["ciudad"] = "Mar del plata"
diccionario['DNI'] = 5000000
print(diccionario)
#las keys son: nombre, edad, ciudad, etc. lo demas son los datos
#el diccionario es como una lista con distintas funciones

# METODO GET #

diccionario = {'a': 1, 'b': 2}

print(diccionario.get('a')) #1
print(diccionario.get('c')) #None
#devuelve el valor asociado a una clave, si existe devuelve None

# METODO KEYS #

diccionario = {'a': 1, 'b': 2}
print(diccionario.keys()) #dict_keys(['a', 'b'])
print(list(diccionario.keys())) #['a', 'b']
#devuelve un objeto de tipo  dict_keys de todas las claves del diccionario

# VALUES #

diccionario = {'a': 1, 'b': 2}
print(diccionario.values()) #dict_values([1, 2])
print(list(diccionario.values())) #[1, 2]
#devuelve un objeto de tipo  dict_values de todos los valores del diccionario

# POP #

diccionario = {'a': 1, 'b': 2}
print(diccionario.pop('a')) #1
print(diccionario) #{'b': 2}
#elimina un indice y devuelve el elemento del indice eliminado