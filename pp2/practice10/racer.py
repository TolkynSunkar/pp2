import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)

# Player setup
player = pygame.Rect(180, 500, 40, 40)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create coin surface
        self.image = pygame.Surface((20, 20))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        # Random starting position (top of screen)
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = -20

    def update(self):
        # Move coin downward
        self.rect.y += 5
        # Remove coin if it goes off screen
        if self.rect.y > HEIGHT:
            self.kill()

# Group to store coins
coins = pygame.sprite.Group()

# Score variable
coin_count = 0

# Clock
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Randomly spawn coins
    if random.randint(1, 30) == 1:
        coins.add(Coin())

    # Update and draw coins
    coins.update()
    coins.draw(screen)

    # Collision detection
    for coin in coins:
        if player.colliderect(coin.rect):
            coin.kill()
            coin_count += 1

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Display score (top right)
    font = pygame.font.Font(None, 30)
    text = font.render(f"Coins: {coin_count}", True, (0, 0, 0))
    screen.blit(text, (250, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()