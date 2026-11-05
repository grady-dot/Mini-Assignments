# Import the Pygame library so we can use its tools to create a game
import pygame

# Start up Pygame and initialize the modules needed for our game
pygame.init()

# Create the game window
# The first number (800) is the width in pixels
# The second number (600) is the height in pixels
screen = pygame.display.set_mode((800, 600))

# Set the text that appears at the top of the game window
pygame.display.set_caption("My First Game")


# COLOURS
# Colours are created using RGB values: (Red, Green, Blue)
# Each value ranges from 0 to 255
# 0 means none of that colour, while 255 means the maximum amount

SKY_BLUE = (135, 206, 235)  # A light blue colour for our background
BLUE = (0, 0, 255)          # Blue for our player
RED = (255, 0, 0)           # Red, which we can use for other objects


# Create a variable to control whether our game keeps running
# True means the game should continue running
running = True


# THE GAME LOOP
# A while loop repeats the code inside it as long as running is True
# This allows our game window to stay open and update continuously
while running:

    # Check for events that happen while the game is running
    # Events include clicking the close button or pressing a key
    for event in pygame.event.get():

        # Check whether the current event is the user closing the window
        # pygame.QUIT represents the window's close event
        if event.type == pygame.QUIT:

            # Change running to False so the while loop will stop
            running = False

    # BACKGROUND
    # Fill the entire game window with our sky blue colour
    # This clears the previous frame before we draw the next one
    screen.fill(SKY_BLUE)

    # DRAW THE PLAYER
    # Draw a rectangle on the screen to represent our player
    # The four numbers below represent:
    # 375 = horizontal position (x), measured from the left
    # 275 = vertical position (y), measured from the top
    # 50  = width of the rectangle in pixels
    # 50  = height of the rectangle in pixels
    pygame.draw.rect(screen, BLUE, (375, 275, 50, 50))

    # DISPLAY THE FRAME
    # Show the background and rectangle on the game window
    # This makes our latest drawing visible to the player
    pygame.display.flip()


# SHUT DOWN PYGAME
# This line runs after the game loop ends
# It closes Pygame properly when the user exits the game
pygame.quit()