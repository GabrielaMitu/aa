import pygame
import os
import clock
import random
from ClassPlayer import *
from ClassSubmarine import *

pygame.init()
pygame.display.set_caption("Jogo Beluga")
os.environ['SDL_VIDEO_CENTERED'] = '1'

clock = pygame.time.Clock()


red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
black = [0,0,0]

#display specs
display_specs = pygame.display.Info()

#game sets
width_screen = display_specs.current_w
height_screen = display_specs.current_h + 23
screen = pygame.display.set_mode((width_screen,height_screen))
FPS = 100

lifes = 3

player = Player('apple.png', max_vel=15, screenDimensions=(width_screen, height_screen))
player_group = pygame.sprite.Group()
player_group.add(player)

subs_group = pygame.sprite.Group()

for a in range(5):
    for y in range(10):
        x = random.randint(50, width_screen-50)
        sub = Submarine("submarine.png", [x,y*30+40], 3)
        subs_group.add(sub)

balls_group = pygame.sprite.Group()
shoot_group = pygame.sprite.Group()

while lifes > 0:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            lifes = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                lifes = 0

    for sub in subs_group:
        if sub.rect.right >= width_screen or sub.rect.left <= 0:
            sub.flip()
        sub.move()
        shoot = sub.shoot()
        if shoot != None:
            shoot_group.add(shoot)

    for shoot in shoot_group:
        shoot.move()

    colisions = pygame.sprite.spritecollide(player, shoot_group, True)
    for colision in colisions:
        lifes -= 1

    for ball in balls_group:
        colisions = pygame.sprite.spritecollide(ball, player_group, False)
        for colision in colisions:
            ball.rect.bottom = player.rect.top - 5
            ball.vertical_bounce()

        colisions = pygame.sprite.spritecollide(ball, subs_group, True)
        for colision in colisions:
            ball.vertical_bounce()

    ball = player.shoot()
    if ball != None:
        balls_group.add(ball)

    for ball in balls_group:
        ball.update()
        if ball.rect.right >= width_screen or ball.rect.left <= 0:
            ball.lateral_bounce()
        if ball.rect.top <= 0:
            ball.vertical_bounce()
        if ball.rect.top > height_screen + 30:
            lifes -= 1
            player.n_balls -= 1
            ball.kill()

    player.update()
    screen.fill(black)
    subs_group.draw(screen)
    shoot_group.draw(screen)
    player_group.draw(screen)
    balls_group.draw(screen)
    pygame.display.update()
