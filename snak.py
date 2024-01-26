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

display_translation = {
    EMPTY: ' ',
    FOOD: 'O',
    SNAKE_BODY: '#',
    SNAKE_HEAD: '@',
}


# Function to display the board
def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H\033[J", end="")
    for row in board:
        print(' '.join(display_translation[cell] for cell in row))
    print('-' * (board.shape[1] * 2))

# Initialize the board
rows = 20
cols = 30
board = np.full((rows, cols), EMPTY)

# Initialize the snake
snake = np.array([(random.randint(0, rows), random.randint(0, cols))])  # Snake starts at the top left corner
head = snake[0]
directons=['UP','DOWN','LEFT','RIGHT']
direction = np.random.choice(directons)  # Initial direction
last_direction=direction

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
lastgun=0
timeintevalyipeeeeeeeeeeeeeeeee=0.3
while not game_over:

    user_input = get_input()

    if user_input:
        if (user_input == 'UP' and direction != 'DOWN') or \
           (user_input == 'DOWN' and direction != 'UP') or \
           (user_input == 'LEFT' and direction != 'RIGHT') or \
           (user_input == 'RIGHT' and direction != 'LEFT'):
            direction = user_input
    if time.time()-lastgun>timeintevalyipeeeeeeeeeeeeeeeee:
        # Update the board
        board = np.full((rows, cols), EMPTY)
        for segment in snake:
            board[segment[0], segment[1]] = SNAKE_BODY
        board[snake[0, 0], snake[0, 1]] = SNAKE_HEAD
        board[food[0], food[1]] = FOOD

        # Display the board
        display_board(board)

        # Example logic for moving the snake based on direction
        if direction == 'UP':
            if last_direction != 'DOWN':
                head = (head[0] - 1, head[1])
                last_direction = direction
            else:
                direction = last_direction
                head = (head[0] + 1, head[1])
        elif direction == 'DOWN':
            if last_direction != 'UP':
                head = (head[0] + 1, head[1])
                last_direction = direction
            else:
                direction = last_direction
                head = (head[0] - 1, head[1])
        elif direction == 'LEFT':
            if last_direction != 'RIGHT':
                head = (head[0], head[1] - 1)
                last_direction = direction
            else:
                direction = last_direction
                head = (head[0], head[1] + 1)
        elif direction == 'RIGHT':
            if last_direction != 'LEFT':
                head = (head[0], head[1] + 1)
                last_direction = direction
            else:
                direction = last_direction
                head = (head[0], head[1] - 1)
        # Check for collision with itself
        # if tuple(head) in [tuple(segment) for segment in snake[1:]]:
        #     print(f"head: {head}, snake: {snake}")
        #     game_over = True

        snake = np.insert(snake, 0, head, axis=0)

        # Check for collision with food
        if tuple(head) == food:
            # Generate new food
            food = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        else:
            # Remove the tail (snake grows only when it eats the food)
            snake = snake[:-1]

        # Example game over condition (hitting the wall)
        if head[0] >= rows or head[1] >= cols or head[0] < 0 or head[1] < 0:
            game_over = True
        lastgun=time.time()
print("The game is over! present")
print("skill issue")