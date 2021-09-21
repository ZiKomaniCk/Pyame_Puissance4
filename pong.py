import pygame, sys

#Classes#
class Ball:
    #initialisation des paramètres de la balle
    def __init__(self, screen,  color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.show()
        
    def show(self):
        pygame.draw.circle( self.screen, self.color, (self.posX, self.posY), self.radius )

#class Paddle:
    #def __init__

pygame.init()
### TAILLE ECRAN
WIDTH = 900
HEIGHT = 500
### RGB COULEURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')

#### Couleur background + ligne milieu
def paint_back():
    screen.fill( BLACK )
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)

paint_back()

#Objets#
ball = Ball( screen, WHITE, WIDTH//2, HEIGHT//2, 12 )

### Boucle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
