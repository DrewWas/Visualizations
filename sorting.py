import pygame
from random import sample

pygame.init()
FPS = 60
HEIGHT, WIDTH = 600,1400
COLOR = (0,147,255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sorting algos")

print("\n\nEnter 1 for BubbleSort\nEnter 2 for Quicksort\n")
#inp = input("What algorithm would you like to use? ")
#inp.strip()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            bubblesort()
        

def bubblesort():
    height = sample(range(10,461), 450)
    n = len(height)
    x = 2
    j = 0
    
    for i in range(n):
        for i in range(n):
            WIN.fill((0,0,0))
            pygame.draw.rect(WIN, (0,147,255), pygame.Rect(x, 600 - height[j], 2, height[j]))
            pygame.display.update()
        x += 4
        j += 1
        for q in range(0, n - i - 1):
            if height[q] > height[q + 1]:
                height[q], height[q + 1] = height[q + 1], height[q]


    
            
    print(height)




    
    #Run bubblesort on the heights list

    #redraw the scene (win.fill and redraw all rects) after each step of bubble sort 

    


if __name__ == "__main__":
    main()