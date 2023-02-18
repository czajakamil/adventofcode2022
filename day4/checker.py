"""
1. First, you'll need to decide on the structure of your game. This could include deciding on the layout of the board, how the pieces will move, and any other rules or features you want to include.

2. Next, you'll need to design your board. You can do this using a grid of squares, with each square representing a location on the board. You can use a two-dimensional list to represent the board, where each element in the list represents a square on the board.

3. Next, you'll need to create the checker pieces. You can do this by creating a class for each type of piece (e.g. red checker, black checker, etc.), and giving each piece properties such as its color, position on the board, and whether it is a king (able to move in any direction).

4. Once you have the basic structure of your game in place, you'll need to write the code to handle user input and move the pieces on the board. You can do this by using a loop to continually prompt the user for their next move, and then updating the board and the pieces accordingly.

5. You'll also need to add code to check for the end of the game, such as when a player has captured all of their opponent's pieces or when a player has no legal moves left.

6. Finally, you can add any additional features or functionality that you want, such as the ability for a player to "jump" over an opponent's piece to capture it, or a graphical user interface to make the game more visually appealing.
"""

# Import libraries for GUI
import pygame
import sys
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 100

# This sets the margin between each cell
MARGIN = 0

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(8):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(8):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and column numbers start at zero)
grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Checkerboard")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(8):
        for column in range(8):
            color = WHITE
            if row % 2 == column % 2:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Create the pieces
    

    # Handle user input
    # TODO

    # Update the board
    # TODO

    # Check for end of game
    # TODO

    # Close the window and quit.

# Be IDLE friendly
pygame.quit()

