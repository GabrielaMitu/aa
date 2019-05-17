import pygame

class Shoot(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, startPosition, yspeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = startPosition
        self.yspeed = yspeed

    def move(self):
        self.rect.y += self.yspeed
