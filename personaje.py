import pygame
import constantes

class Personaje():
    
    def __init__(self, x, y, animaciones):
        # Guardamos posición en floats para movimiento suave
        self.x = float(x)
        self.y = float(y)
        self.animaciones = animaciones  # Lista de imágenes ya escaladas
        self.frame = 0
        self.image = self.animaciones[self.frame]
        self.rect = self.image.get_rect(topleft=(int(self.x), int(self.y)))
        self.contador_anim = 0           # Controla la velocidad de animación

    def movimiento(self, dx, dy):
        # Actualizamos posición en float y luego el rect (para evitar pérdida por truncado)
        self.x += dx
        self.y += dy
        self.rect.topleft = (int(self.x), int(self.y))

    def update(self):
        # Actualizar animación
        self.contador_anim += 1
        if self.contador_anim >= 10:  # Cambia de frame cada 10 ticks
            self.contador_anim = 0
            self.frame += 1
            if self.frame >= len(self.animaciones):
                self.frame = 0
            self.image = self.animaciones[self.frame]
            # Si la imagen cambió de tamaño, recalculamos el rect usando la
            # posición actual (self.x, self.y) para mantener la ubicación.
            self.rect = self.image.get_rect(topleft=(int(self.x), int(self.y)))

    def dibujar(self, superficie, direccion_derecha=True):
        # Solo volteamos la imagen si es necesario
        imagen = pygame.transform.flip(self.image, not direccion_derecha, False)
        superficie.blit(imagen, self.rect)
