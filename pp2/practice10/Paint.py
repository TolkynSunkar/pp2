import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fill background
screen.fill(WHITE)

# Default settings
color = BLACK          # Current drawing color
mode = "draw"          # Modes: draw / rect / circle / erase

# Variables for shapes
start_pos = None       # Starting point for rectangle/circle

running = True
while running:

    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:

            # Color selection
            if event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

            # Mode selection
            elif event.key == pygame.K_z:
                mode = "draw"      # Free draw
            elif event.key == pygame.K_x:
                mode = "rect"      # Draw rectangle
            elif event.key == pygame.K_c:
                mode = "circle"    # Draw circle
            elif event.key == pygame.K_v:
                mode = "erase"     # Eraser

        # Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos  # Save starting position

        # Mouse button released → draw shapes
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos

            if mode == "rect":
                # Draw rectangle from start to end
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(start_pos[0] - end_pos[0])
                h = abs(start_pos[1] - end_pos[1])
                pygame.draw.rect(screen, color, (x, y, w, h), 2)

            elif mode == "circle":
                # Draw circle based on distance
                radius = int(((start_pos[0] - end_pos[0]) ** 2 +
                              (start_pos[1] - end_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

    # Continuous drawing (for draw and erase)
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()

        if mode == "draw":
            # Free drawing (pen)
            pygame.draw.circle(screen, color, (x, y), 4)

        elif mode == "erase":
            # Eraser (draw white color)
            pygame.draw.circle(screen, WHITE, (x, y), 10)

    pygame.display.update()

pygame.quit()