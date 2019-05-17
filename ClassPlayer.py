import pygame
from ClassBall import *

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0    , 255)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, max_vel, screenDimensions, playerNumber, startX):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(player_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = startX
        self.rect.bottom = screenDimensions[1] -50
        self.max_vel = max_vel
        self.screenX = screenDimensions[0]
        self.n_balls = 0
        self.lifes = 10
        self.playerNumber = playerNumber
        self.shootAngle = 45
        self.score = 0

    def move(self):
        key = pygame.key.get_pressed()
        self.xspeed = 0
        if self.playerNumber==1:
            if self.rect.left >= 0:
                if key[pygame.K_d]:
                    self.xspeed = self.max_vel
                    self.shootAngle = 45
            else:
                self.rect.left = 1
            if self.rect.right <= self.screenX:
                if key[pygame.K_a]:
                    self.xspeed = -self.max_vel
                    self.shootAngle = 45+45
            else:
                self.rect.left = self.screenX-28

        if self.playerNumber==2:
            if self.rect.left >= 0:
                if key[pygame.K_RIGHT]:
                    self.xspeed = self.max_vel
                    self.shootAngle = 45
            else:
                self.rect.left = 1
            if self.rect.right <= self.screenX:
                if key[pygame.K_LEFT]:
                    self.xspeed = -self.max_vel
                    self.shootAngle = 45+45
            else:
                self.rect.left = self.screenX-28


        self.rect.x += self.xspeed

    def shoot(self):
        key = pygame.key.get_pressed()
        if self.playerNumber==1:
            if key[pygame.K_w] and self.n_balls < 1:
                self.n_balls += 1
                ball = Ball(img="golden_apple.png", vel=10, angle=self.shootAngle, startPosition=self.rect.center, playerNumber=self.playerNumber)
                return ball
        if self.playerNumber==2:
            if key[pygame.K_UP] and self.n_balls < 1:
                self.n_balls += 1
                ball = Ball(img="blue_apple.png", vel=10, angle=self.shootAngle, startPosition=self.rect.center, playerNumber=self.playerNumber)
                return ball
        return None

    def update(self):
        self.move()
