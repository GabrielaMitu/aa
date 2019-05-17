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

player1 = Player('golden_apple.png', max_vel=15, screenDimensions=(width_screen, height_screen), playerNumber=1, startX=width_screen/4)

player2 = Player('blue_apple.png', max_vel=15, screenDimensions=(width_screen, height_screen), playerNumber=2, startX=3*width_screen/4)

player_group = pygame.sprite.Group()
player_group.add(player1)
player_group.add(player2)

subs_group = pygame.sprite.Group()
def create_subs():
    for a in range(5):
        for y in range(10):
            x = random.randint(50, width_screen-50)
            sub = Submarine("submarine.png", [x,y*30+40], 3)
            subs_group.add(sub)

balls_group = pygame.sprite.Group()
shoot_group = pygame.sprite.Group()
play_again = True
while play_again:
    while player1.lifes > 0 and player2.lifes > 0:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                player1.lifes = 0
                play_again = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player1.lifes = 0
                    play_again = False

        for sub in subs_group:
            if sub.rect.right >= width_screen or sub.rect.left <= 0:
                sub.flip()
            sub.move()
            shoot = sub.shoot()
            if shoot != None:
                shoot_group.add(shoot)

        for shoot in shoot_group:
            shoot.move()

        for player, ball in zip(player_group, balls_group):
            collided = pygame.sprite.collide_rect(ball, player)
            if collided:
                if ball.playerNumber==1:
                    ball.rect.bottom = player1.rect.top - 5
                if ball.playerNumber==2:
                    ball.rect.bottom = player2.rect.top - 5
                ball.vertical_bounce()

        for player in player_group:
            collisions = pygame.sprite.spritecollide(player, shoot_group, True)
            for collisions in collisions:
                player.lifes -= 1

            ball = player.shoot()
            if ball != None:
                balls_group.add(ball)

        for ball in balls_group:
            collisions = pygame.sprite.spritecollide(ball, subs_group, True)
            for collisions in collisions:
                ball.vertical_bounce()
                if ball.playerNumber == 1:
                    player1.score += 100
                if ball.playerNumber == 2:
                    player2.score += 100

        for ball in balls_group:
            ball.update()
            if ball.rect.right >= width_screen or ball.rect.left <= 0:
                ball.lateral_bounce()
            if ball.rect.top <= 0:
                ball.vertical_bounce()
            if ball.rect.top > height_screen + 30:
                if ball.playerNumber == 1:
                    player1.lifes -= 1
                    player1.n_balls -= 1
                if ball.playerNumber == 2:
                    player2.lifes -= 1
                    player2.n_balls -= 1

                ball.kill()

        if len(subs_group) == 0:
            create_subs()
        for player in player_group:
            player.update()
        screen.fill(black)
        subs_group.draw(screen)
        shoot_group.draw(screen)
        player_group.draw(screen)
        balls_group.draw(screen)
        pygame.display.update()

    if player1.score == player2.score:
        print("Empate, ambos com {0} pontos".format(player1.score))
    elif player1.score > player2.score:
        print("Player 1 Ganhou com {0} pontos, enquanto o Player 2 ficou com {1}".format(player1.score, player2.score))
    else:
        print("Player 2 Ganhou com {0} pontos, enquanto o Player 1 ficou com {1}".format(player2.score, player1.score))
    morto = True
    while morto:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                player1.lifes = 0
                play_again = False
                morto = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player1.lifes = 0
                    play_again = False
                    morto = False
                if event.key == pygame.K_SPACE:
                    create_subs()
                    for e in shoot_group:
                        e.kill()
                    for e in balls_group:
                        e.kill()
                    for e in subs_group:
                        e.kill()

                    player1.rect.centerx = width_screen/4
                    player1.lifes = 10
                    player1.score = 0

                    player2.rect.centerx = 3*width_screen/4
                    player2.lifes = 10
                    player2.score = 0
                    morto = False
