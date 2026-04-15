import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

ball = Ball()

running = True
while running:
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y), ball.radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move(0, -1, WIDTH, HEIGHT)
            elif event.key == pygame.K_DOWN:
                ball.move(0, 1, WIDTH, HEIGHT)
            elif event.key == pygame.K_LEFT:
                ball.move(-1, 0, WIDTH, HEIGHT)
            elif event.key == pygame.K_RIGHT:
                ball.move(1, 0, WIDTH, HEIGHT)

    pygame.display.flip()

pygame.quit()