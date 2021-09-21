import pygame, sys

### RGB COULEURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

    #initialisation des paramètres de la balle
class Ball:
    def __init__(self, screen,  color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.show()
        
    def show(self):
        pygame.draw.circle( self.screen, self.color, (self.posX, self.posY), self.radius )

pygame.init()

screen = pong.pygame

#### Couleur background + ligne milieu
def paint_back():
    screen.fill( BLACK )
    pygame.draw.line(screen, WHITE.)


