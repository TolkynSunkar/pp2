import pygame
from collections import deque

WIDTH, HEIGHT = 900, 600

# -------- FLOOD FILL --------
def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x,y))
    if target_color == new_color:
        return

    q = deque()
    q.append((x,y))

    while q:
        px, py = q.popleft()

        if px < 0 or px >= WIDTH or py < 0 or py >= HEIGHT:
            continue

        if surface.get_at((px,py)) != target_color:
            continue

        surface.set_at((px,py), new_color)

        q.append((px+1, py))
        q.append((px-1, py))
        q.append((px, py+1))
        q.append((px, py-1))


# -------- PENCIL --------
def draw_pencil(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)


# -------- LINE --------
def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)