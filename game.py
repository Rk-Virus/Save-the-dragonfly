import os
import sys
import time
import math
import pygame
import random
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

#to create .exe file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# initialize pygame
pygame.init()

#game variables
scrnWidth = 800
scrnHeight = 600

villain1X = random.randint(100, 700)
villain1Y = 0
villain2X = random.randint(100, 700)
villain2Y = scrnHeight
villain3X = 0
villain3Y = random.randint(100, 500)
villain4X = scrnWidth
villain4Y = random.randint(100, 500)

villainSpeed = 0.4
playerX = 400
playerY = 300
playerSpeed = 0.4
dir = 1

screen = pygame.display.set_mode((scrnWidth, scrnHeight))
pygame.display.set_caption("Save the Dragonfly")
player = pygame.image.load(resource_path("chidda.png")).convert()
bg = pygame.image.load(resource_path("background.png")).convert()
pygame.display.update()

play_button = Button(screen, "Play")
stats = GameStats()
sb = Scoreboard(screen, stats)

# game loop
while True:
    # keyboard inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dir = 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dir = -1
            if event.key == pygame.K_DOWN and playerY <= scrnHeight-50 or event.key == pygame.K_s:
                playerY += 20
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY -= 20
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if play_button.rect.collidepoint(mouse_pos):
                stats.game_active = True

    # backgroud 
    screen.blit(bg, (0,0))
    # villains 
    pygame.draw.rect(screen,(0,0,0), (villain1X, villain1Y, 40, 40))
    pygame.draw.rect(screen,(0,0,0), (villain2X, villain2Y, 40, 40))
    pygame.draw.rect(screen,(0,0,0), (villain3X, villain3Y, 40, 40))
    pygame.draw.rect(screen,(0,0,0), (villain4X, villain4Y, 40, 40))
    # player
    screen.blit(player, (playerX,playerY))

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    sb.show_score()

    # Make the most recently drawn screen visible
    pygame.display.flip()

    if stats.game_active:
        # distance btw player and villain 
        dist1 = math.sqrt((villain1X - playerX)**2 + (villain1Y - playerY)**2)
        dist2 = math.sqrt((villain2X - playerX)**2 + (villain2Y - playerY)**2)
        dist3 = math.sqrt((villain3X - playerX)**2 + (villain3Y - playerY)**2)
        dist4 = math.sqrt((villain4X - playerX)**2 + (villain4Y - playerY)**2)

        # game over - collision detection 
        if dist1 <= 35 or dist2 <= 35 or dist3 <= 35 or dist4 <= 35:
            print("Game Over!")
            print("Your Score : ",stats.score)
            # saving highscore 
            f = open(resource_path("highscore.txt"),"r")
            hs = int(f.read())
            f.close()
            if stats.score > hs:
                f = open(resource_path("highscore.txt"),"w")
                f.write(str(stats.score))
                f.close()
            time.sleep(10)
            sys.exit()

        if villain1Y >= scrnHeight or villain2Y <= 0:
            villain1Y = 0
            villain1X = random.randint(100, 700)
            villain2Y = scrnHeight
            villain2X = random.randint(100, 700)
            villainSpeed += 0.02

        if villain3X >= scrnWidth:
            villain3X = 0
            villain3Y = random.randint(100, 500)

        if villain4X <= 0:
            villain4X = scrnWidth
            villain4Y = random.randint(100, 500)

        if playerX <= 0:
            dir = 1
        if playerX >= scrnWidth - 50:
            dir = -1


        pygame.display.update()
        #update score
        stats.score += 1
        sb.prep_score()
        #update speed
        villain1Y += villainSpeed*1.1
        villain2Y -= villainSpeed
        playerX += playerSpeed*dir
        villain3X += villainSpeed
        villain4X -= villainSpeed


# pygame.quit()
# input()
# quit()
