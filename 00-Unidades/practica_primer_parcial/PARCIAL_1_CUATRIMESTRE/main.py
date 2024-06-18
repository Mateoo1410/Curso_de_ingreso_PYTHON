####################################################### MENU PRINCIPAL #######################################################
from validaciones import *
from peliculas import *
def menu_principal()->None:
    """Esta funcion se encarga de todo el menu principal, encargado de llevarte por las distintas opciones y entrar a los demas submenus
    """
    usuario = None
    while usuario != "10":
        print("1: Dar de alta.")
        print("2: Modificar.")
        print("3: Eliminar.")
        print("4: Mostrar películas.")
        print("5: Ordenar películas.")
        print("6: Buscar película por título.")
        print("7: Calcular promedio.")
        print("8: Calcular porcentaje.")
        print("9: Mostrar por genero.")
        print("10: Guardar y salir.")
        usuario = input("Ingrese una opcion: ")
        match(usuario):
            case "1":
                dar_de_alta(lista_peliculas)
            case "2":
                titulo = validar_titulo("Ingrese titulo de la pelicula que desea modificar: ", True)
                modificar_pelicula(lista_peliculas, titulo)  #uso el validar titulo de la funcion anterior para encontrarlo
            case "3":
                eliminar_pelicula(lista_peliculas)
            case "4":
                menu_peliculas_buscadas(lista_peliculas)
            case "5":
                menu_ordenamiento(lista_peliculas)
            case "6":
                titulo_buscado = validar_titulo("Ingrese titulo de la pelicula que desea buscar: ",True)
                titulo = buscar_peliculas(lista_peliculas, "Titulo", titulo_buscado)
                mostrar_peliculas(titulo)   ### BUSCAR POR TITULO ###
            case "7":
                menu_promedios(lista_peliculas)
            case "8":
                menu_porcentajes(lista_peliculas)
            case "9":
                mostrar_por_genero(lista_peliculas, "Western")
            case "10":
                guardar_datos_csv(lista_peliculas)
                print("Guardado, gracias por usar el programa!")
            case _:
                print("Error, ingrese una opcion valida: ")


leer_peliculas_csv(lista_peliculas)
convertir_claves(lista_peliculas)
menu_principal()
