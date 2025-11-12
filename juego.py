import pygame
import constantes
from personaje import Personaje

pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Gato con pulso al caminar")

# Función para escalar imágenes
def escalar_img(image, scale_or_size):
    """
    Escala una imagen.

    Parámetros:
    - scale_or_size: float (factor de escala) o tuple (ancho, alto) en píxeles.
    """
    # Si pasaron un tamaño objetivo (w, h)
    if isinstance(scale_or_size, (tuple, list)):
        target_w, target_h = scale_or_size
        return pygame.transform.scale(image, (int(target_w), int(target_h)))

    # Si pasaron un factor de escala
    scale = float(scale_or_size)
    w, h = image.get_size()
    return pygame.transform.scale(image, (int(w * scale), int(h * scale)))

# Cargar animaciones
animaciones = []
for i in range(2):
    img = pygame.image.load(f"assets/images/characters/player/Derecha{i}.png").convert_alpha()
    # Escalamos cada frame al tamaño definido por las constantes
    img = escalar_img(img, (constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE))
    animaciones.append(img)

jugador = Personaje(50, 50, animaciones)

reloj = pygame.time.Clock()
run = True
direccion_derecha = True

while run:
    dt = reloj.tick(constantes.FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movimiento
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_a]:
        dx -= 1
        direccion_derecha = False
    if keys[pygame.K_d]:
        dx += 1
        direccion_derecha = True
    if keys[pygame.K_w]:
        dy -= 1
    if keys[pygame.K_s]:
        dy += 1

    # Normalizar diagonal
    if dx != 0 or dy != 0:
        longitud = (dx**2 + dy**2) ** 0.5
        dx /= longitud
        dy /= longitud

    # Mover jugador
    jugador.movimiento(dx * constantes.VELOCIDAD_JUGADOR * dt * 60,
                       dy * constantes.VELOCIDAD_JUGADOR * dt * 60)
    jugador.update()

    # Dibujar
    ventana.fill(constantes.COLOR_FONDO)
    jugador.dibujar(ventana, direccion_derecha)
    pygame.display.flip()

pygame.quit()