#ayuda a organizar las carpetas de codigos grandes depende de lo que hace cada cosa, trae codigos de una pestaña a otra

import funciones #se llama a todas la funciones, es el mas practico (depende no siempre)
funciones.solicitar_entero() 

from funciones import solicitar_entero  #llama solo a la funcion solicitar_entero
solicitar_entero()

from funciones import * #importa todas las funciones y no hay necesidad de poner funciones. para llamar a la funcion
solicitar_entero()

#paquetes se usan para organizar los modulos