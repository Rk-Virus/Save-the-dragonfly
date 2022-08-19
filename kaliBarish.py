import math
import pygame
import random
pygame.init()

#game variables
game_exit = False
scrnWidth = 800
scrnHeight = 600
score = 0

villainX = random.randint(100, 700)
villainY = 0
villainSpeed = 0.4
playerX = 400
playerY = 300

screen = pygame.display.set_mode((scrnWidth, scrnHeight))
pygame.display.set_caption("Kaali Nagin")
pygame.display.update()

# game loop
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX = playerX + 10
            if event.key == pygame.K_LEFT:
                playerX -= 10
            if event.key == pygame.K_DOWN:
                playerY += 10
            if event.key == pygame.K_UP:
                playerY -= 10
            

    screen.fill((0,0,200))

    pygame.draw.rect(screen,(0,0,0), (villainX, villainY, 40, 40))
    pygame.draw.rect(screen,(255, 192, 203), (playerX, playerY, 40, 40))

    dist = math.sqrt((villainX - playerX)**2 + (villainY - playerY)**2)

    # game over collision detection 
    if dist <= 40:
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

    if villainY >= scrnHeight:
        villainY = 0
        villainX = random.randint(100, 700)
        villainSpeed += 0.01

    pygame.display.update()
    score += 1
    villainY += villainSpeed


pygame.quit()
quit()