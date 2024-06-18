# PYGAME:  es una herramienta que se usa para hacer juegos dentro de python(comunicandose con los perifericos de la pc o joystick)
import pygame

pygame.init()  #le da el permiso para acceder a los perifericos

ventana = pygame.display.set_mode((1000,500))  #crea la ventana, primero el ancho y luego el largo (el dato con parentesis es una "tupla"), x1000 y500
pygame.display.set_caption("God Of War III")  #asigna el nombre de la ventana

logo = pygame.image.load("C:\\Users\\Mateo\\Desktop\\python\\Curso_de_ingreso_PYTHON\\00-Unidades\\1er_cuatrimestre\\pygame\\God-of-War-III-2-icon.png") #para cargar una imagen descargada
pygame.display.set_icon(logo) 

DORADO = (255, 215, 0)
ROJO = (255, 0, 0)  #en forma de rgb(inensidad del red,gren,blue), se puede crear un modulo aparte solo de colores e importarlos al codigo
ventana.fill(ROJO)  #pinta la ventana de rojo (fuera del while para que no se pinte todo el tiempo)

fuente = pygame.font.SysFont("Arial", 40, True)  #determina que tipo de fuente se va a utilizar, tamaño de la letra, True/False si se quiere la letra en negrita o no

texto = fuente.render("Bienvenido", False, DORADO)   #crea el texto a partir de esta fuente, False(no se ve bien a fondo), y el color de la letra, el ultimo parametro es el color de la caja de txt

lista_nombres = ["Mateo", "Nicolas", "Santiago"]


x = 400
y = 250
for nombre in lista_nombres:
    texto = fuente.render(nombre, False, DORADO)
    ventana.blit(texto, (x,y))
    y += 40  #cada vez que se va iterando va sumando pixeles asi no se sobreponen los nombres de la lista

#ventana.blit(texto, (400,250))  #pega el texto encima, destino de la ventana donde se pega el texto
ventana.blit(logo, (0,0))

ejecutar = True
while ejecutar:  #bucle para permanecer la ventana abierta
    lista_eventos = pygame.event.get()  #eventos: algo que ocurre a lo largo del programa y que necesitamos saber
    for evento in lista_eventos:  #recorre elemento por elemento de la lista
        if evento.type == pygame.QUIT:
            ejecutar = False  #si el evento es del tipo "QUIT" cierra la ventana
    
    pygame.display.update() #actualiza la ventana con todos los cambios que se hayan realizado