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
        self.dx = 0
        self.dy = 0
        self.show()
        
    def show(self):
        pygame.draw.circle( self.screen, self.color, (self.posX, self.posY), self.radius )

    def start(self):
        self.dx = 0.5
        self.dy = 0.25
        
    def move(self):
        self.posX = self.posX + self.dx
        self.posY = self.posY + self.dy

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

### Score
class Score: 
    def __init__(self, screen, points, posX, posY):
        self.screen = screen
        self.points = points
        self.posX = posX
        self.posY = posY
        self.font = pygame.font.SysFont("monospace", 50, bold=True)
        self.label = self.font.render(self.points,0 , WHITE)
        self.show()
        
    def show(self):
        self.screen.blit(self.label, (self.posX - self.label.get_rect().width // 2, self.posY))


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

score1 = Score(screen,'0' , WIDTH//4,15)
score2 = Score(screen, '0', WIDTH - WIDTH//4,15)

#Variables
playing = False

### Boucle main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                ball.start()
                playing = True

    
    
    if playing:
        paint_back()
        
        #mouvement de la balle
        ball.move()
        ball.show()

        #paddle gauche
        paddleL.show()

        #paddle droit
        paddleR.show()

        score1.show()

        score2.show()

    pygame.display.update()
