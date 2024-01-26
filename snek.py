import random
import time
import os
import numpy as np
import msvcrt


# Constants
EMPTY = 0
FOOD = 1
SNAKE_BODY = 2
SNAKE_HEAD = 3

# Function to display the board
def display_board(board):
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # ANSI escape code to clear the screen
    print("\033[H\033[J", end="")
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print('-' * (len(board[0]) * 2))

# Initialize the board
rows = 20
cols = 30
board = [[EMPTY for _ in range(cols)] for _ in range(rows)]

# Initialize the snake
snake = [(0, 0)]  # Snake starts at the top left corner
head = snake[0]
direction = 'RIGHT'  # Initial direction

# Place initial food
food = (random.randint(0, rows - 1), random.randint(0, cols - 1))
board[food[0]][food[1]] = FOOD

# Function to get user input
def get_input():
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'w':
            return 'UP'
        elif key == b's':
            return 'DOWN'
        elif key == b'a':
            return 'LEFT'
        elif key == b'd':
            return 'RIGHT'
    return None

# Game loop
game_over = False
while not game_over:
    user_input = get_input()

    if user_input:
        if (user_input == 'UP' and direction != 'DOWN') or \
           (user_input == 'DOWN' and direction != 'UP') or \
           (user_input == 'LEFT' and direction != 'RIGHT') or \
           (user_input == 'RIGHT' and direction != 'LEFT'):
            direction = user_input

    # Update the board
    board = [[EMPTY for _ in range(cols)] for _ in range(rows)]
    for segment in snake:
        board[segment[0]][segment[1]] = SNAKE_BODY
    board[snake[0][0]][snake[0][1]] = SNAKE_HEAD
    board[food[0]][food[1]] = FOOD

    # Display the board
    display_board(board)

    # Example logic for moving the snake based on direction
    if direction == 'UP':
        head = (head[0] - 1, head[1])
    elif direction == 'DOWN':
        head = (head[0] + 1, head[1])
    elif direction == 'LEFT':
        head = (head[0], head[1] - 1)
    elif direction == 'RIGHT':
        head = (head[0], head[1] + 1)

    snake.insert(0, head)

    # Check for collision with food
    if head == food:
        # Generate new food
        food = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    else:
        # Remove the tail (snake grows only when it eats the food)
        snake.pop()

    # Example game over condition (hitting the wall)
    if head[0] >= rows or head[1] >= cols or head[0] < 0 or head[1] < 0:
        game_over = True

    # Delay for better visualization (optional)
    time.sleep(0.2)