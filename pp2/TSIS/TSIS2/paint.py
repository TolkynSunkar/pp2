import pygame
import sys
from datetime import datetime
from tools import *

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)

color = BLACK
tool = "pencil"
brush_size = 2

drawing = False
start_pos = None
last_pos = None

# TEXT
font = pygame.font.Font(None, 24)
typing = False
text = ""
text_pos = (0,0)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # -------- KEY --------
        if event.type == pygame.KEYDOWN:

            # BRUSH SIZE
            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            # TOOLS
            if event.key == pygame.K_z:
                tool = "pencil"
            if event.key == pygame.K_x:
                tool = "line"
            if event.key == pygame.K_c:
                tool = "fill"
            if event.key == pygame.K_v:
                tool = "text"
            if event.key == pygame.K_b:
                tool = "eraser"

            # SAVE
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # TEXT INPUT
            if typing:
                if event.key == pygame.K_RETURN:
                    img = font.render(text, True, color)
                    canvas.blit(img, text_pos)
                    typing = False
                    text = ""
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # -------- MOUSE --------
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

            if tool == "fill":
                flood_fill(canvas, event.pos[0], event.pos[1], color)

            if tool == "text":
                typing = True
                text_pos = event.pos
                text = ""

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if tool == "line":
                draw_line(canvas, color, start_pos, event.pos, brush_size)

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                draw_pencil(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    # -------- DRAW --------
    screen.fill(WHITE)
    screen.blit(canvas, (0,0))

    # LINE PREVIEW
    if drawing:
     if tool == "pencil":
        draw_pencil(canvas, color, last_pos, event.pos, brush_size)
        last_pos = event.pos

     elif tool == "eraser":
        draw_pencil(canvas, (255,255,255), last_pos, event.pos, brush_size)
        last_pos = event.pos

    # TEXT PREVIEW
    if typing:
        img = font.render(text, True, color)
        screen.blit(img, text_pos)

    pygame.display.flip()
    clock.tick(60)