import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5
paddle1 = pygame.Rect(50, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up ball
BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
ball = pygame.Rect(WIDTH/2 - BALL_WIDTH/2, HEIGHT/2 - BALL_HEIGHT/2, BALL_WIDTH, BALL_HEIGHT)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Set up game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.y < HEIGHT - PADDLE_HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.y > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.y < HEIGHT - PADDLE_HEIGHT:
        paddle2.y += PADDLE_SPEED

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Ball collision with walls
    if ball.y > HEIGHT - BALL_HEIGHT or ball.y < 0:
        ball_speed_y *= -1

    # Draw game objects
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, paddle1)
    pygame.draw.rect(win, WHITE, paddle2)
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.draw.aaline(win, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))

    # Update display
    pygame.display.flip()

    # Set game FPS
    clock.tick(60)

# Quit the game
pygame.quit()
"""

This code sets up a basic Pong game using Pygame. The paddles are controlled using the W and S keys for the left paddle, and the Up and Down arrow keys for the right paddle. The ball bounces off the paddles and the walls, and the game runs at 60 frames per second.
"""
