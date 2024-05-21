#los str son inmutables

# STRIP #

cadena = "   Hola Mundo   "
cadena = cadena.strip()
print(cadena)
#borra los espacios en blanco al principio y al final de la cadena, tmb borra ###

# UPPER #

cadena = "Hola Mundo"
cadena = cadena.upper()
print(cadena)
#transforma las minusculas en mayusculas

# CAPITALIZE #
cadena = "Hola Mundo"
cadena = cadena.capitalize()
print(cadena)
#transforma la primera letra en mayuscula y las demas en minusculas

# REPLACE #

cadena = "Hola Mundo"
cadena = cadena.replace("Hola", "Chau")
print(cadena)
#reemplaza una palabla por otra

# SPLIT #
cadena = "Python,Java,C"
lista = cadena.split(",")
print(lista)
#divide la cadenas en subcadenas, depende del caracter que tome de referencia

# JOIN #
cadena = " "
cadena = cadena.join(["Python", "Java", "C"])
print(cadena)
#concatena cadena separadas, con caracteres

# ZFILL #
cadena = "3"
print(cadena.zfill(6))
#rellena con 0 hasta que se cumpla la cantidad de caracteres pasadas como parametro

# ISALPHA #

cadena = "Hola Mundo"
print(cadena.isalpha()) 
# False -> por el espacio

cadena = "HolaMundo"
print(cadena.isalpha()) 
# True
#devuelve un False si tiene un espacio en blanco, y si no tiene ninguno devuelve True

# COUNT #

cadena = "Hola Mundo Hola"
print(cadena.count("la"))
#cuenta cuantas veces se ingresa una cadena en especifico, con "" se cuentan todos los caracteres

# FORMAT #
nombre_usuario = "JUAN"
edad_usuario = 35
cadena = "Nombre: {1}, Edad: {0}"
print(cadena.format(edad_usuario, nombre_usuario))
#sirve para lo mismo que el f" " pero es menos efectiva 