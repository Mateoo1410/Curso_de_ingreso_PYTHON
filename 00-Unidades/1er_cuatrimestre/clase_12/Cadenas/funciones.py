from class_video import *

def ordenar_temas(lista_videos:list[Video])-> list:
    for i in range(len(lista_videos)): 
        for j in range(len(lista_videos)-1 - i):

            if lista_videos[j].sesion > lista_videos [j + 1].sesion:  

                auxiliar = lista_videos[j]
                lista_videos[j] = lista_videos[j + 1]
                lista_videos[j + 1] = auxiliar
    return lista_videos

def promedio_visitas(lista_videos:list[Video])-> None:

    visitas_totales = 0

    for i in range(len(lista_videos)): 
        visitas_totales += lista_videos[i].vistas

    promedio = visitas_totales / len(lista_videos)
    promedio_visitas_k = promedio / 1000
    promedio_visitas_k = int(promedio_visitas_k)
    print(f"El promedio de visitas es de {promedio_visitas_k}k")

def mostrar_max_visitas(lista_videos:list[Video])-> None:
    bandera = False
    for i in range(len(lista_videos)):
        if bandera == False or lista_videos[i].vistas > num_max:
            num_max = lista_videos[i].vistas
            bandera = True
            colaborador = lista_videos[i].titulo
    print(f"Con {num_max} de visitas el que mas tiene es {colaborador}")

def buscar_codigo(lista_videos:list[Video], colaborador:str)-> None:
    for i in range(len(lista_videos)):
        buscar = lista_videos[i].url_youtube
        buscar = buscar.count(colaborador)
        if buscar >= 1:
            lista_videos[i].mostrar_tema()