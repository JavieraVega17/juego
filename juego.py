import pygame
import constantes
from personaje import Personaje

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("Juego 0.0")

player_image = pygame.image.load("assets/images/characters/player/Derecha1.png")

jugador = Personaje(x=50, y=50, image = player_image)

#variables del movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()

run = True
while run == True: 

    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_FONDO)

    #calcular movimiento jugador 
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD_JUGADOR
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD_JUGADOR
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD_JUGADOR
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD_JUGADOR

    #mover jugador
    jugador.movimiento(delta_x, delta_y)

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        #cuando se aprete la tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True

            if event.key == pygame.K_d:
                mover_derecha = True

            if event.key == pygame.K_w:
                mover_arriba = True

            if event.key == pygame.K_s:
                mover_abajo = True


        #cuando se suelte la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                        mover_izquierda = False

            if event.key == pygame.K_d:
                        mover_derecha = False

            if event.key == pygame.K_w:
                        mover_arriba = False

            if event.key == pygame.K_s:
                        mover_abajo = False


    pygame.display.update()

pygame.quit()
