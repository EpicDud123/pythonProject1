import pygame
import random
import numpy as np

# Constants
EMPTY = 0
FOOD = 1
SNAKE_BODY = 2
SNAKE_HEAD = 3

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Function to display the board using Pygame
def display_board(board, screen):
    screen.fill(BLACK)
    cell_size = 20

    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == FOOD:
                pygame.draw.rect(screen, RED, (col_idx * cell_size, row_idx * cell_size, cell_size, cell_size))
            elif cell == SNAKE_BODY:
                pygame.draw.rect(screen, WHITE, (col_idx * cell_size, row_idx * cell_size, cell_size, cell_size))
            elif cell == SNAKE_HEAD:
                pygame.draw.rect(screen, GREEN, (col_idx * cell_size, row_idx * cell_size, cell_size, cell_size))

    pygame.display.update()

# Initialize Pygame
pygame.init()
rows = 20
cols = 30
screen = pygame.display.set_mode((cols * 20, rows * 20))
pygame.display.set_caption("Snake Game")

# Initialize the board
board = np.full((rows, cols), EMPTY)

# ... (rest of your code remains the same)

# Game loop
game_over = False
lastgun = 0
timeintevalyipeeeeeeeeeeeeeeeee = 0.3

clock = pygame.time.Clock()

while not game_over:
    # ... (your game logic remains the same)

    # Display the board using Pygame
    display_board(board, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    clock.tick(10)  # Adjust the speed of the game by changing the argument here

# Clean up and quit Pygame
pygame.quit()
print("The game is over! Present your skills!")
