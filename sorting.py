import pygame
from random import sample

pygame.init()
WIDTH, HEIGHT = 1400,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting algorithms")
WIDTH = 5
height = sample(range(20,121), 100)
x = 14
run = True

def draw(height):
    for i in range(len(height)):
        pygame.draw.rect(WIN, (0,147,255), pygame.Rect(x * i, 600 - (height[i] * 5), WIDTH, height[i] * 5))


while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_SPACE]:
            execute = True

        if execute == False:
            WIN.fill((0,0,0))
            draw(height)
            pygame.display.update
        if execute == True:
            for i in range(len(height) - 1):
                for j in range(len(height) - i - 1):
                    if height[j] > height[j + 1]:
                        height[j], height[j + 1] = height[j + 1], height[j]
                    
                    WIN.fill((0,0,0))
                    draw(height)
                    pygame.time.delay(10)
                    pygame.display.update()

pygame.quit()


