import pygame

pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Square")

# Set up our colours
SKY_BLUE = (135, 206, 235)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Store the player's and enemy starting position
player_x = 375
player_y = 275
enemy_one_x = 100
enemy_one_y = 200
enemy_two_x = 700
enemy_two_y = 200

# Control how many pixels the square moves each frame
speed = 2
enemy_speed_1 = 0.25
enemy_speed_2 = 0.15

# Keep the game running
running = True
clock = pygame.time.Clock()
while running:

    # Check for events, including closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keyboard keys are being pressed
    keys = pygame.key.get_pressed()

    # Move left by decreasing the X position
    if keys[pygame.K_LEFT]:
        player_x = player_x - speed

    # Move right by increasing the X position
    if keys[pygame.K_RIGHT]:
        player_x = player_x + speed

    # Move up by decreasing the Y position
    if keys[pygame.K_UP]:
        player_y = player_y - speed

    # Move down by increasing the Y position
    if keys[pygame.K_DOWN]:
        player_y = player_y + speed

    if enemy_one_x < player_x:
        enemy_one_x += enemy_speed_1
    elif enemy_one_x > player_x:
        enemy_one_x -= enemy_speed_1
    if enemy_one_y < player_y:
        enemy_one_y += enemy_speed_1
    elif enemy_one_y > player_y:
        enemy_one_y -= enemy_speed_1

    if enemy_two_x < player_x:
        enemy_two_x += enemy_speed_2
    elif enemy_two_x > player_x:
        enemy_two_x -= enemy_speed_2
    if enemy_two_y < player_y:
        enemy_two_y += enemy_speed_2
    elif enemy_two_y > player_y:
        enemy_two_y -= enemy_speed_2
        

    # Paint the background to clear the previous frame
        screen.fill(SKY_BLUE)

    # Draw the square at its current position
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))
    pygame.draw.rect(screen, RED, (enemy_one_x, enemy_one_y, 30, 30))
    pygame.draw.rect(screen, GREEN, (enemy_two_x, enemy_two_y, 30, 30))
    # Show the updated screen
    pygame.display.flip()
    clock.tick(120)

pygame.quit()