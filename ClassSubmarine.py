import pygame
import random
from ClassShoot import *

class Submarine(pygame.sprite.Sprite):
    def __init__(self, img, startPosition, xspeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = startPosition[0]
        self.rect.bottom = startPosition[1]
        self.xspeed = xspeed

    def shoot(self):
        chance = random.randint(0,1000)
        if chance <= 1:
            shoot = Shoot("Red_laser.png" ,self.rect.center, 5)
            return shoot
        return None

    def move(self):
        self.rect.x += self.xspeed

    def flip(self):
        self.xspeed = -self.xspeed
        self.image = pygame.transform.flip(self.image, True, False)
