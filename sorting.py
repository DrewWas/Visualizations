import pygame
from random import sample

pygame.init()
FPS = 60
HEIGHT, WIDTH = 600,1228
COLOR = (0,147,255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sorting algos")

def drawRects():
    WIN.fill((0,0,0))
    x = 2
    j = 0
    height = sample(range(590), 175)
    height.sort()
    for i in range(175):
        pygame.draw.rect(WIN, COLOR, pygame.Rect(x, 600 - height[j], 5, height[j]))
        top = height[j]
        j += 1
        x += 7
    pygame.display.update()


def main():
    run = True
    run1 = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if run1 == True:
            drawRects()
            run1 = False
    pygame.quit()



if __name__ == "__main__":
    main()