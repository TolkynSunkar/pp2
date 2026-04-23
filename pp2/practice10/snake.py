import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

# Snake settings
BLOCK_SIZE = 20

clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
big_font = pygame.font.Font(None, 60)


def reset_game():
    """Reset all game variables"""
    snake = [(100,100)]
    direction = "RIGHT"
    score = 0
    level = 1
    speed = 10
    food = generate_food(snake)
    return snake, direction, score, level, speed, food


def generate_food(snake):
    """Generate food not on snake"""
    while True:
        x = random.randrange(0, WIDTH, BLOCK_SIZE)
        y = random.randrange(0, HEIGHT, BLOCK_SIZE)
        if (x, y) not in snake:
            return (x, y)


def draw_game(snake, food, score, level):
    """Draw all game elements"""
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

    # Draw score & level
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))


def game_over_screen(score, level):
    """Display Game Over screen"""
    screen.fill(BLACK)

    # Title
    game_over_text = big_font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (80, 120))

    # Score info
    info_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(info_text, (100, 200))

    # Restart instruction
    restart_text = font.render("Press c to Restart or ESC to Quit", True, WHITE)
    screen.blit(restart_text, (30, 250))

    pygame.display.update()


# Initialize game
snake, direction, score, level, speed, food = reset_game()
game_over = False

running = True
while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                # Movement control
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
            else:
                # Restart or quit
                if event.key == pygame.K_c:
                    snake, direction, score, level, speed, food = reset_game()
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

    if not game_over:
        # Move snake
        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= BLOCK_SIZE
        elif direction == "DOWN":
            head_y += BLOCK_SIZE
        elif direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif direction == "RIGHT":
            head_x += BLOCK_SIZE

        new_head = (head_x, head_y)

        # Wall collision
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over = True

        # Self collision
        if new_head in snake:
            game_over = True

        snake.insert(0, new_head)

        # Food collision
        if new_head == food:
            score += 1
            food = generate_food(snake)

            # Level system
            if score % 3 == 0:
                level += 1
                speed += 2
        else:
            snake.pop()

        draw_game(snake, food, score, level)

    else:
        game_over_screen(score, level)

    pygame.display.update()
    clock.tick(speed)

pygame.quit()