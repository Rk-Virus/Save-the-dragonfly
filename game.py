import math
import pygame
import random
pygame.init()

#game variables
game_exit = False
scrnWidth = 800
scrnHeight = 600
score = 0

villain1X = random.randint(100, 700)
villain1Y = 0
villain2X = random.randint(100, 700)
villain2Y = scrnHeight
villainSpeed = 0.4
playerX = 400
playerY = 300
playerSpeed = 0.4
dir = 1

screen = pygame.display.set_mode((scrnWidth, scrnHeight))
pygame.display.set_caption("Save the Dragonfly")
player = pygame.image.load("chidda.png").convert()
bg = pygame.image.load("background.png").convert()
pygame.display.update()

# game loop
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dir = 1
            if event.key == pygame.K_LEFT:
                dir = -1
            if event.key == pygame.K_DOWN and playerY <= scrnHeight-50:
                playerY += 20
            if event.key == pygame.K_UP:
                playerY -= 20
    
    # backgroud 
    screen.blit(bg, (0,0))
    # villains 
    pygame.draw.rect(screen,(0,0,0), (villain1X, villain1Y, 40, 40))
    pygame.draw.rect(screen,(0,0,0), (villain2X, villain2Y, 40, 40))
    # player
    screen.blit(player, (playerX,playerY))
    pygame.display.flip()

    # distance btw player and villain 
    dist1 = math.sqrt((villain1X - playerX)**2 + (villain1Y - playerY)**2)
    dist2 = math.sqrt((villain2X - playerX)**2 + (villain2Y - playerY)**2)

    # game over - collision detection 
    if dist1 <= 40 or dist2 <= 40:
        print("Game Over!")
        print("Your Score : ",score)

        # saving highscore 
        f = open("highscore.txt","r")
        hs = int(f.read())
        f.close()
        if score > hs:
            f = open("highscore.txt","w")
            f.write(str(score))
            f.close()
        game_exit = True

    if villain1Y >= scrnHeight or villain2Y <= 0:
        villain1Y = 0
        villain1X = random.randint(100, 700)
        villain2Y = scrnHeight
        villain2X = random.randint(100, 700)
        villainSpeed += 0.02
    if playerX <= 0:
        dir = 1
    if playerX >= scrnWidth - 50:
        dir = -1


    pygame.display.update()
    score += 1
    villain1Y += villainSpeed*1.1
    villain2Y -= villainSpeed
    playerX += playerSpeed*dir


pygame.quit()
input()
quit()
