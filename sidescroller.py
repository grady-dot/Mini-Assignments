import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Side Scroller")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)          
RED = (255, 0, 0)           



running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (375, 275, 50, 50))

    pygame.display.flip()



pygame.quit()