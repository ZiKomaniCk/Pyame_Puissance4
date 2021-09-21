import pygame, sys

#Classes#
class Ball:
    ###Initialisation des paramètres de la balle
    def __init__(self, screen,  color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.show()
        
    def show(self):
        pygame.draw.circle( self.screen, self.color, (self.posX, self.posY), self.radius )

class Paddle:
    ###Initialisation du Paddle
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.show()

    def show(self):
        pygame.draw.rect( self.screen, self.color, (self.posX, self.posY, self.width, self.height) )

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
paddleL = Paddle( screen, WHITE, 15, HEIGHT//2 - 60, 20, 120 )
paddleR = Paddle( screen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120 )

### Boucle main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()
