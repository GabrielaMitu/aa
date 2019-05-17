import pygame
import math

class Ball(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, vel, angle, startPosition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = startPosition[0]
        self.rect.bottom = startPosition[1] -20
        self.vel = vel
        self.angle = angle
        self.xspeed = vel*math.cos(angle)
        self.yspeed = vel*math.sin(angle)

    def move(self):
        self.rect.x += self.xspeed
        self.rect.y -= self.yspeed

    def lateral_bounce(self):
        self.xspeed = -self.xspeed

    def vertical_bounce(self):
        self.yspeed = -self.yspeed

    def update(self):
        self.move()
