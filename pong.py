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
    
    def paddle_collision(self):
        self.dx = -self.dx

    def wall_collision(self):
        self.dy = -self.dy

    def restart_pos(self):
        self.posX = WIDTH//2
        self.posY = HEIGHT//2
        self.dx = 0
        self.dy = 0
        self.show()

class Paddle:
    ###Initialisation du Paddle
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = 'stopped'
        self.show()

    def show(self):
        pygame.draw.rect( self.screen, self.color, (self.posX, self.posY, self.width, self.height) )

    # mouvement des paddles
    def move(self):
        if self.state == 'up':
            self.posY -= 1
        
        elif self.state == 'down':
            self.posY += 1

    #empecher les barres de sortir de l'écran
    def bloq(self):
        if self.posY <= 0:
            self.posY = 0
        
        if self.posY + self.height >= HEIGHT:
            self.posY = HEIGHT - self.height

class CollisionManag:

    #calcul de colision entre la balle et le paddle gauche
    def between_ball_and_paddleL(self, ball, paddleL):
        if ball.posY + ball.radius > paddleL.posY and ball.posY - ball.radius < paddleL.posY + paddleL.height:
            if ball.posX - ball.radius <= paddleL.posX + paddleL.width:
                return True
        
        return False        
    
    #calcul de colision entre la balle et le paddle droit
    def between_ball_and_paddleR(self, ball, paddleR):
        if ball.posY + ball.radius > paddleR.posY and ball.posY - ball.radius < paddleR.posY + paddleR.height:
            if ball.posX - ball.radius >= paddleR.posX:
               return True

        return False

    def between_ball_and_walls(self, ball):
        
        #top
        if ball.posY - ball.radius <= 0:
            return True
        
        #bot
        if ball.posY - ball.radius >= HEIGHT:
            return True
        
        return False
        
         
    #Check balle pos pour score
    def check_goal_player1(self, ball):
        return ball.posX - ball.radius >= WIDTH

    def check_goal_player2(self, ball):
        return ball.posX + ball.radius <= 0

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
    
    ### fonction pour ajout des points
    def increase(self):
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.render(self.points,0 , WHITE)

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
paddleL = Paddle( screen, WHITE, 15, HEIGHT//2 - 60, 20, 120 )
paddleR = Paddle( screen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120 )
ball = Ball( screen, WHITE, WIDTH//2, HEIGHT//2, 12 )
collision = CollisionManag()

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
            
            if event.key == pygame.K_z:
                paddleL.state = 'up'
            
            if event.key == pygame.K_s:
                paddleL.state = 'down'
            
            if event.key == pygame.K_UP:
                paddleR.state = 'up'

            if event.key == pygame.K_DOWN:
                paddleR.state = 'down'
        
        if event.type == pygame.KEYUP:
            paddleR.state = 'stopped'
            paddleL.state = 'stopped'

    
    
    if playing:
        paint_back()
        
        #mouvement de la balle + affichage
        ball.move()
        ball.show()

        #paddle gauche
        paddleL.move()
        paddleL.bloq()
        paddleL.show()

        #paddle droit
        paddleR.move()
        paddleR.bloq()
        paddleR.show()

        #verif collision
        if collision.between_ball_and_paddleL(ball, paddleL):
            ball.paddle_collision()
        
        if collision.between_ball_and_paddleR(ball, paddleR):
            ball.paddle_collision()

        if collision.between_ball_and_walls(ball):
            ball.wall_collision()

        ### Ajout des points avec check collision
        if collision.check_goal_player1(ball):
            score1.increase()
            ball.restart_pos()

        if collision.check_goal_player1(ball):
            score2.increase()
            ball.restart_pos()

    #score
    score1.show()
    score2.show()

    pygame.display.update()
