import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False 
        self.animaciones = animaciones
        #imagen de la animación que se muestra
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones [self.frame_index]
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)

        self.forma.center = (x, y)

    def movimiento(self, delta_x, delta_y):
            
            if delta_x < 0:
                 self.flip = True
            elif delta_x > 0:
                 self.flip = False

            self.forma.x += delta_x
            self.forma.y += delta_y


    def update(self):
         cooldown_animacion = 500
         self.image = self.animaciones[self.frame_index]
         if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
              self.frame_index += 1
              self.update_time = pygame.time.get_ticks()

              if self.frame_index >= len(self.animaciones):
                   self.frame_index = 0

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, flip_y= False)
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma, width=1)

    