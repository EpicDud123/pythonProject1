import pygame
import time
import random

pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake RPG Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake characteristics
snake_block = 10
snake_speed = 15

# Snake initial position
snake_pos = [100, 50]
snake_body = [snake_pos[:]]

# Fruit initial position
fruit_pos = [[random.randrange(1, (width//snake_block)) * snake_block,
              random.randrange(1, (height//snake_block)) * snake_block]]

# RPG elements
powers = ['speed_boost', 'extra_fruit']
power_cooldown = 5  # Cooldown in seconds for using the power
current_power = None
power_end_time = 0

# Initial direction
direction = 'RIGHT'
change_to = direction

# Function to draw the snake
def draw_snake(snake_block, snake_body):
    for segment in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(segment[0], segment[1], snake_block, snake_block))

# Function to draw the fruit
def draw_fruit(fruit_positions):
    for pos in fruit_positions:
        pygame.draw.rect(window, red, pygame.Rect(pos[0], pos[1], snake_block, snake_block))

# Function to handle power activation
def activate_power():
    global current_power, power_end_time

    if current_power == 'speed_boost':
        snake_speed_boost = 2
        snake_speed_temp = snake_speed
        snake_speed += snake_speed_boost
        time.sleep(power_cooldown)
        snake_speed = snake_speed_temp
    elif current_power == 'extra_fruit':
        for _ in range(3):
            spawn_extra_fruit()

    current_power = None
    power_end_time = 0

# Function to spawn extra fruit
def spawn_extra_fruit():
    global fruit_pos
    fruit_pos.append([random.randrange(1, (width//snake_block)) * snake_block,
                      random.randrange(1, (height//snake_block)) * snake_block])

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not direction == 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and not direction == 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and not direction == 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and not direction == 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_q and current_power is not None and time.time() < power_end_time:
                activate_power()

    # Update the direction of the snake
    direction = change_to

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= snake_block
    elif direction == 'DOWN':
        snake_pos[1] += snake_block
    elif direction == 'LEFT':
        snake_pos[0] -= snake_block
    elif direction == 'RIGHT':
        snake_pos[0] += snake_block

    # Check for collisions with walls or itself
    if snake_pos[0] >= width or snake_pos[0] < 0 or snake_pos[1] >= height or snake_pos[1] < 0:
        game_over = True

    for segment in snake_body[1:]:
        if snake_pos == segment:
            game_over = True

    # Check if the snake eats the fruit
    if snake_pos == fruit_pos[0]:
        fruit_pos.pop(0)
        snake_body.append(list(snake_pos))
        if len(fruit_pos) % 5 == 0:
            current_power = random.choice(powers)
            power_end_time = time.time() + power_cooldown
    else:
        # Remove the last segment of the snake body if it exists
        if snake_body:
            snake_body.pop()

    # Draw the background
    window.fill(black)

    # Draw the snake and fruit
    draw_snake(snake_block, snake_body)
    draw_fruit(fruit_pos)

    # Update the display
    pygame.display.flip()

    # Control the game speed
    pygame.time.Clock().tick(snake_speed)

# Quit the game
pygame.quit()
