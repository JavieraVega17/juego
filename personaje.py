import pygame
import constantes

class Personaje():
    
     def __init__(self, x, y, animaciones):
        self.x = x
        self.y = y
        self.animaciones = animaciones  # Lista de imágenes ya escaladas
        self.frame = 0                   # <-- Aquí defines 'frame'
        self.image = self.animaciones[self.frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.contador_anim = 0           # Controla la velocidad de animación

     def movimiento(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

     def update(self):
        # Actualizar animación
        self.contador_anim += 1
        if self.contador_anim >= 10:  # Cambia de frame cada 10 ticks
            self.contador_anim = 0
            self.frame += 1
            if self.frame >= len(self.animaciones):
                self.frame = 0
            self.image = self.animaciones[self.frame]

     def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)

    