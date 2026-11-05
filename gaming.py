import pygame

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (118, 238, 0)
ORANGE = (255, 127, 36)
PINK = (255, 20, 147)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Four Red Squares")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Make the backgroundcolour of choice
    screen.fill(BLUE)

    # Draw square 1
    pygame.draw.rect(screen, RED, (500, 275, 50, 50))

    # Draw square 2
    pygame.draw.rect(screen, RED, (675, 275, 25, 25))

    # Draw square 3
    pygame.draw.rect(screen, RED, (575, 275, 75, 75))

    # Draw square 4
    pygame.draw.rect(screen, RED, (375, 275, 100, 100))

    pygame.display.flip()

pygame.quit()