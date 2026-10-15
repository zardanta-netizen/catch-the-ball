"""
Simple Pygame Example: "Catch the Falling Box"
-----------------------------------------------------
The player moves a green box at the bottom to catch a
yellow box falling from the top. Each catch = +1 score.
If the yellow box falls to the bottom without being caught = game over.

How to run:
1. pip install pygame-ce
2. python main.py
"""

import pygame
import random

# ---------- 1. INITIALIZATION ----------
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Box")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Colors (R, G, B)
WHITE = (255, 255, 255)
RED= (0, 200 , 100)
YELLOW = (255, 210, 0)
BACKGROUND = (20, 20, 40)
RED = (255, 60, 60)

# ---------- 2. GAME VARIABLES ----------
player_width, player_height = 80, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 8

box_size = 30
box_x = random.randint(0, WIDTH - box_size)
box_y = 0
box_speed = 5

score = 0
game_over = False


def draw_text(text, font_size, color, pos):
    f = pygame.font.SysFont(None, font_size)
    render = f.render(text, True, color)
    rect = render.get_rect(center=pos)
    screen.blit(render, rect)


# ---------- 3. GAME LOOP ----------
running = True
while running:
    # --- Check events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:  # press R to restart
                score = 0
                box_y = 0
                box_x = random.randint(0, WIDTH - box_size)
                box_speed = 5
                game_over = False

    if not game_over:
        # --- Update player position ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # --- Update falling box position ---
        box_y += box_speed

        # --- Check collision ---
        player_box = pygame.Rect(player_x, player_y, player_width, player_height)
        falling_box = pygame.Rect(box_x, box_y, box_size, box_size)

        if player_box.colliderect(falling_box):
            score += 1
            box_y = 0
            box_x = random.randint(0, WIDTH - box_size)
            # slightly speed up the game as score increases
            box_speed = min(15, 5 + score // 5)

        # --- Check if the box fell to the bottom without being caught ---
        if box_y > HEIGHT:
            game_over = True

    # ---------- 4. REDRAW THE SCREEN ----------
    screen.fill(BACKGROUND)

    if not game_over:
        pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, YELLOW, (box_x, box_y, box_size, box_size))
        draw_text(f"Score: {score}", 36, WHITE, (70, 30))
    else:
        draw_text("GAME OVER", 64, RED, (WIDTH // 2, HEIGHT // 2 - 40))
        draw_text(f"Final score: {score}", 40, WHITE, (WIDTH // 2, HEIGHT // 2 + 20))
        draw_text("Press R to play again", 28, WHITE, (WIDTH // 2, HEIGHT // 2 + 70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
