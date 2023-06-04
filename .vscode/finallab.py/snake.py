import pygame
import time
import random

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Snake segment size
SEGMENT_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Font for displaying the score
font_style = pygame.font.SysFont(None, 50)


def display_score(score):
    """Display the current score on the screen."""
    score_text = font_style.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, [0, 0])


def draw_snake(snake_body):
    """Draw the snake on the game window."""
    for segment in snake_body:
        pygame.draw.rect(window, WHITE, [segment[0], segment[1], SEGMENT_SIZE, SEGMENT_SIZE])


def game_loop():
    """Main game loop."""
    game_over = False
    game_exit = False

    # Initial position of the snake
    x = WIDTH // 2
    y = HEIGHT // 2

    # Initial movement direction of the snake
    dx = 0
    dy = 0

    # Snake body
    snake_body = []
    snake_length = 1

    # Initial position of the food
    food_x = round(random.randrange(0, WIDTH - SEGMENT_SIZE) / SEGMENT_SIZE) * SEGMENT_SIZE
    food_y = round(random.randrange(0, HEIGHT - SEGMENT_SIZE) / SEGMENT_SIZE) * SEGMENT_SIZE

    # Main game loop
    while not game_exit:

        while game_over:
            window.fill(BLACK)
            game_over_text = font_style.render("Game Over!", True, WHITE)
            window.blit(game_over_text, [WIDTH // 2 - 100, HEIGHT // 2])
            display_score(snake_length - 1)
            pygame.display.update()

            # Wait for user input to restart or quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_r:
                        game_loop()

        # Handle user input for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != SEGMENT_SIZE:
                    dx = -SEGMENT_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx != -SEGMENT_SIZE:
                    dx = SEGMENT_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy != SEGMENT_SIZE:
                    dx = 0
                    dy = -SEGMENT_SIZE
                elif event.key == pygame.K_DOWN and dy != -SEGMENT_SIZE:
                    dx = 0
                    dy = SEGMENT_SIZE

        # Move the snake
        x += dx
        y += dy

        # Check for collision with the boundaries
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        window.fill(BLACK)

        # Draw the food
        pygame.draw.rect(window, RED, [food_x, food_y, SEGMENT_SIZE, SEGMENT_SIZE])

        # Update the snake body
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for collision with the snake's body
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True

        # Draw the snake
        draw_snake(snake_body)

        # Check if the snake has eaten the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SEGMENT_SIZE) / SEGMENT_SIZE) * SEGMENT_SIZE
            food_y = round(random.randrange(0, HEIGHT - SEGMENT_SIZE) / SEGMENT_SIZE) * SEGMENT_SIZE
            snake_length += 1

        # Update the score
        display_score(snake_length - 1)

        pygame.display.update()

        # Set the game's frame rate
        clock.tick(15)

    # Quit the game
    pygame.quit()
    quit()


# Start the game loop
game_loop()