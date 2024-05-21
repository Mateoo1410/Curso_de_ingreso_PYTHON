# APEND #

lista = [1,2,3,4]

lista.append(-3) 
print(lista)
#agrega un indice al final de la lista

# INSERT #

mi_lista = [1,2,3]
mi_lista.insert(1,-5) 
print(mi_lista)
#primer parametro el indice, segundo parametro elemento a agregar

# REMOVE #

mi_lista = [1,3,2,4,2]
mi_lista.remove(2) 
print(mi_lista)
#borra un elemento en especifico de la lista(el primero)

# POP #

mi_lista = [1,2,3]
elemento = mi_lista.pop(2) 
print(elemento)
print(mi_lista)
#saca un elemento de la lista fuera de ella(el 2 es el indice)

# INDEX #

mi_lista = [1,2,3,2]
indice = mi_lista.index(3) 
print(indice)
#devuelve el indice de un elemento en particular que se busca

# SORT #

mi_lista = [3,52,1,2,85]
mi_lista.sort() 
print(mi_lista)
#ordena la lista

# REVERSE #

mi_lista = [1,2,3,5]
mi_lista.reverse()
print(mi_lista)
#recorre la lista a la inversa

# CLEAR #

mi_lista = [1,2,3]
mi_lista.clear()
print(mi_lista)
#borra la lista

# COPY #

mi_lista = [1,2,[1,2,3]]

lista_copia = mi_lista.copy()

mi_lista[0] = 85
lista_copia[2][0] = 52   #modifica un elemento de una lista dentro de otra

print(mi_lista)
print(lista_copia)
#hace una copia de una lista ya creada