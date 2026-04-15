import pygame
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

player = MusicPlayer()
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((200, 200, 200))

    text = font.render(f"Track: {player.index + 1}", True, (0, 0, 0))
    screen.blit(text, (120, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print("l", event.key)  

            if event.key == pygame.K_b:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_m:
                player.prev()

            elif event.key == pygame.K_a:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()